"""Skimr pipeline orchestrator. See spec §9."""
import logging
import traceback
from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import db
from .config import (
    DATA_DIR,
    backfill_days,
    db_path,
    load_profile,
    load_sources,
    model_for,
    reasoning_for,
)
from .llm.classify import classify
from .llm.client import LLMError
from .llm.score import score as score_call
from .llm.summarize import summarize
from .render.markdown import render_item
from .sources.youtube import YouTubeSource
from .utils.logging import setup_logging

logger = logging.getLogger("skimr.main")


def _profile_yaml_text() -> str:
    return (DATA_DIR / "profile.yaml").read_text(encoding="utf-8")


def _build_source(cfg) -> YouTubeSource:
    if cfg.type != "youtube":
        raise ValueError(f"Unsupported source type: {cfg.type}")
    return YouTubeSource(name=cfg.name, channel_handle=cfg.id, notes=cfg.notes)


def _since_from_row(row, default_days: int) -> datetime:
    last_checked = row["last_checked_at"]
    if last_checked:
        return datetime.fromisoformat(last_checked.replace("Z", "+00:00"))
    return datetime.now(timezone.utc) - timedelta(days=default_days)


def stage_discover_and_fetch(conn, source_configs) -> tuple[int, int]:
    """Returns (items_discovered, fetch_failures)."""
    discovered = 0
    fetch_failures = 0
    for cfg in source_configs:
        if not cfg.active:
            continue
        source = _build_source(cfg)
        source_id = db.upsert_source(
            conn, name=cfg.name, type_=cfg.type, external_id=cfg.id,
            active=cfg.active, notes=cfg.notes,
        )
        source_row = conn.execute(
            "SELECT * FROM sources WHERE id = ?", (source_id,)
        ).fetchone()
        since = _since_from_row(source_row, backfill_days())
        logger.info("[discover] %s — listing videos since %s", cfg.name, since.isoformat())
        try:
            videos = source.list_recent_videos(since=since)
        except Exception as e:
            logger.error("[discover] %s failed: %s", cfg.name, e)
            continue
        logger.info("[discover] %s — found %d videos", cfg.name, len(videos))
        for video in videos:
            item_id = db.insert_item(
                conn,
                source_id=source_id,
                external_id=video.external_id,
                title=video.title,
                url=video.url,
                author=cfg.name,
                published_at=video.published_at,
                duration_seconds=video.duration_seconds,
            )
            if item_id is None:
                continue
            discovered += 1
            logger.info("[discover] new item %d: %s", item_id, video.title)
            try:
                transcript = source.fetch_transcript(video.external_id)
            except Exception as e:
                logger.warning("[fetch] transcript error for %s: %s", video.external_id, e)
                db.set_item_status(conn, item_id, "no_transcript", failure_reason=str(e))
                fetch_failures += 1
                continue
            if not transcript:
                logger.info("[fetch] no transcript for %s", video.external_id)
                db.set_item_status(conn, item_id, "no_transcript")
                continue
            db.set_item_transcript(conn, item_id, transcript)
            logger.info("[fetch] transcript ok for item %d (%d chars)", item_id, len(transcript))
        db.update_source_last_checked(conn, source_id)
    return discovered, fetch_failures


def stage_summarize(conn) -> tuple[int, int]:
    items = db.items_in_status(conn, "transcript_fetched")
    ok = 0
    failed = 0
    model = model_for("summarize")
    reasoning = reasoning_for("summarize")
    for item in items:
        try:
            result = summarize(
                model=model,
                reasoning_effort=reasoning,
                title=item["title"],
                author=item["author"],
                duration_seconds=item["duration_seconds"],
                transcript=item["transcript"],
            )
            db.upsert_summary(
                conn, item["id"],
                hook=result.hook, tldr=result.tldr,
                key_points=result.key_points, full_notes=result.full_notes,
                model=model,
            )
            db.set_item_status(conn, item["id"], "summarized")
            ok += 1
            logger.info("[summarize] item %d ok", item["id"])
        except LLMError as e:
            logger.warning("[summarize] item %d failed: %s", item["id"], e)
            db.set_item_status(conn, item["id"], "failed", failure_reason=str(e))
            failed += 1
    return ok, failed


def stage_classify(conn) -> tuple[int, int]:
    items = db.items_in_status(conn, "summarized")
    ok = 0
    failed = 0
    model = model_for("classify")
    reasoning = reasoning_for("classify")
    for item in items:
        summary = db.get_summary(conn, item["id"])
        try:
            result = classify(
                model=model,
                reasoning_effort=reasoning,
                title=item["title"],
                author=item["author"],
                tldr=summary["tldr"],
                key_points=summary["key_points"],
            )
            db.upsert_classification(
                conn, item["id"],
                primary_theme=result.primary_theme,
                secondary_theme=result.secondary_theme,
                reasoning=result.reasoning,
                model=model,
            )
            db.set_item_status(conn, item["id"], "classified")
            ok += 1
            logger.info("[classify] item %d ok (%s)", item["id"], result.primary_theme)
        except LLMError as e:
            logger.warning("[classify] item %d failed: %s", item["id"], e)
            db.set_item_status(conn, item["id"], "failed", failure_reason=str(e))
            failed += 1
    return ok, failed


def stage_score(conn, profile_yaml: str) -> tuple[int, int]:
    items = db.items_in_status(conn, "classified")
    ok = 0
    failed = 0
    model = model_for("score")
    reasoning = reasoning_for("score")
    for item in items:
        summary = db.get_summary(conn, item["id"])
        classification = db.get_classification(conn, item["id"])
        source_row = conn.execute(
            "SELECT notes FROM sources WHERE id = ?", (item["source_id"],)
        ).fetchone()
        source_notes = (source_row["notes"] if source_row else "") or ""
        try:
            result = score_call(
                model=model,
                reasoning_effort=reasoning,
                profile_yaml=profile_yaml,
                source_notes=source_notes,
                title=item["title"],
                author=item["author"],
                primary_theme=classification["primary_theme"],
                secondary_theme=classification["secondary_theme"],
                hook=summary["hook"],
                tldr=summary["tldr"],
                key_points=summary["key_points"],
            )
            db.upsert_score(
                conn, item["id"],
                relevance=result.relevance,
                pitch=result.pitch,
                caveats=result.caveats,
                model=model,
            )
            db.set_item_status(conn, item["id"], "scored")
            ok += 1
            logger.info("[score] item %d ok (relevance=%d)", item["id"], result.relevance)
        except LLMError as e:
            logger.warning("[score] item %d failed: %s", item["id"], e)
            db.set_item_status(conn, item["id"], "failed", failure_reason=str(e))
            failed += 1
    return ok, failed


def stage_render(conn) -> tuple[int, int]:
    items = db.items_in_status(conn, "scored")
    ok = 0
    failed = 0
    for item in items:
        source_row = conn.execute(
            "SELECT name FROM sources WHERE id = ?", (item["source_id"],)
        ).fetchone()
        source_name = source_row["name"] if source_row else item["author"]
        try:
            path = render_item(conn, item, source_name=source_name)
            db.set_item_status(conn, item["id"], "rendered")
            ok += 1
            logger.info("[render] item %d -> %s", item["id"], path)
        except Exception as e:
            logger.warning("[render] item %d failed: %s", item["id"], e)
            db.set_item_status(conn, item["id"], "failed", failure_reason=f"render: {e}")
            failed += 1
    return ok, failed


def run() -> int:
    setup_logging()
    logger.info("skimr pipeline starting")

    profile = load_profile()  # validates schema
    source_configs = load_sources()
    if not source_configs:
        logger.warning("no sources configured; exiting")
        return 0
    profile_yaml = _profile_yaml_text()
    _ = profile  # silence linter — we read the raw yaml directly for the prompt

    conn = db.connect()
    db.init_schema(conn)
    run_id = db.start_run(conn)

    discovered = 0
    processed = 0
    failed = 0
    final_status = "success"
    try:
        d, _fail_fetch = stage_discover_and_fetch(conn, source_configs)
        discovered += d

        ok, f = stage_summarize(conn)
        processed += ok
        failed += f

        ok, f = stage_classify(conn)
        failed += f

        ok, f = stage_score(conn, profile_yaml)
        failed += f

        ok, f = stage_render(conn)
        failed += f
    except Exception as e:
        logger.error("pipeline aborted: %s\n%s", e, traceback.format_exc())
        db.append_run_notes(conn, run_id, f"aborted: {e}")
        final_status = "failed"
    finally:
        db.finish_run(
            conn, run_id, status=final_status,
            items_discovered=discovered,
            items_processed=processed,
            items_failed=failed,
        )
        conn.close()
    logger.info("skimr pipeline finished: status=%s discovered=%d processed=%d failed=%d",
                final_status, discovered, processed, failed)
    return 0 if final_status == "success" else 1


if __name__ == "__main__":
    raise SystemExit(run())
