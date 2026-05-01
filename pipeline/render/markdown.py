import re
import sqlite3
from pathlib import Path

import yaml

from ..config import site_content_dir
from ..db import get_classification, get_score, get_summary
from ..utils.slugs import item_slug, slugify

# Backfill fix: earlier sanitizer stripped \n without inserting a space, leaving
# strings like "burden.A healthy" or "project.You should". Insert a space when
# we see sentence-end punctuation immediately followed by a capital letter.
_CONCAT_FIX = re.compile(r"(?<=[.!?;])(?=[A-Z(])")


def _unmash(text: str) -> str:
    return _CONCAT_FIX.sub(" ", text or "")


_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(])")


def _explode_bullet(point: str, max_words: int = 35) -> list[str]:
    """Split a single 'bullet' that crammed multiple sentences into one.

    Used at render time to recover from the early-data case where the model
    wrote multi-claim paragraphs into key_points. New summaries (with the
    tightened prompt) shouldn't trigger this.
    """
    cleaned = _unmash(point or "").strip()
    if not cleaned:
        return []
    if len(cleaned.split()) <= max_words:
        return [cleaned]
    parts = [p.strip() for p in _SENTENCE_SPLIT.split(cleaned) if p.strip()]
    return parts or [cleaned]


def _frontmatter(data: dict) -> str:
    return "---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=10_000) + "---\n"


def render_item(conn: sqlite3.Connection, item: sqlite3.Row, source_name: str) -> Path:
    summary = get_summary(conn, item["id"])
    classification = get_classification(conn, item["id"])
    score_row = get_score(conn, item["id"])
    if not (summary and classification and score_row):
        raise RuntimeError(
            f"Cannot render item {item['id']}: missing summary/classification/score."
        )

    slug = item_slug(item["published_at"], source_name, item["title"])
    source_slug = slugify(source_name, max_length=40)

    frontmatter_data = {
        "title": item["title"],
        "author": item["author"],
        "source_id": item["source_id"],
        "source_slug": source_slug,
        "url": item["url"],
        "published_at": item["published_at"],
        "duration_seconds": item["duration_seconds"],
        "primary_theme": classification["primary_theme"],
        "secondary_theme": classification["secondary_theme"],
        "relevance": score_row["relevance"],
        "hook": _unmash(summary["hook"]),
        "tldr": _unmash(summary["tldr"]),
        "caveats": score_row["caveats"],
        "pitch": score_row["pitch"],
    }

    body_lines: list[str] = ["", "## Key Points", ""]
    for point in summary["key_points"]:
        for piece in _explode_bullet(point):
            body_lines.append(f"- {piece}")
    body_lines += ["", "## Notes", "", _unmash(summary["full_notes"]), ""]

    out_path = site_content_dir() / f"{slug}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(_frontmatter(frontmatter_data) + "\n".join(body_lines) + "\n", encoding="utf-8")
    return out_path
