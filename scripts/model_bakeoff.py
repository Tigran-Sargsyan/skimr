"""Run the summarize step against multiple OpenAI models on one DB-stored item.

Usage:
    uv run python scripts/model_bakeoff.py [--item-id N] [--source "Nate B Jones"]

Picks the most recent item from the given source (default "Nate B Jones") that
has a transcript stored in the DB, then summarizes it with each model in
MODELS below. Writes per-model outputs to bakeoff/<model>.md and a side-by-side
summary to bakeoff/COMPARE.md.

No SearchAPI calls — uses transcripts already in data/digest.db.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

# ---- candidate models -------------------------------------------------------

# (model_id, reasoning_effort | None)
# - None = don't pass reasoning_effort (for non-reasoning models)
MODELS: list[tuple[str, str | None]] = [
    ("gpt-5.4-mini",    "none"),  # current pick (~$1.10/mo)
    ("gpt-5.1",         "none"),  # mid step, newer than gpt-5 at same price (~$2.00/mo)
    ("gpt-5.4",         "none"),  # one step up same family (~$3.60/mo)
]

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="Nate B Jones",
                        help="Source name to pick the latest item from")
    parser.add_argument("--item-id", type=int, default=None,
                        help="Override: use a specific item ID")
    parser.add_argument("--out", default="bakeoff",
                        help="Output directory")
    args = parser.parse_args()

    from pipeline import db
    from pipeline.llm.summarize import summarize
    from pipeline.llm.client import LLMError

    conn = db.connect()
    if args.item_id is not None:
        item = db.get_item(conn, args.item_id)
        if not item:
            print(f"No item with id {args.item_id}", file=sys.stderr)
            return 1
    else:
        row = conn.execute(
            "SELECT i.* FROM items i "
            "JOIN sources s ON s.id = i.source_id "
            "WHERE s.name = ? AND i.transcript IS NOT NULL AND i.transcript != '' "
            "ORDER BY i.published_at DESC LIMIT 1",
            (args.source,),
        ).fetchone()
        if not row:
            print(f"No item with transcript for source {args.source!r}", file=sys.stderr)
            return 1
        item = row

    transcript = item["transcript"] or ""
    print(f"Using item {item['id']}: {item['title']}")
    print(f"Source: {item['author']}  duration: {item['duration_seconds']}s  "
          f"transcript chars: {len(transcript)}")
    print()

    out_dir = REPO_ROOT / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    results: list[dict] = []
    for model, reasoning in MODELS:
        print(f"--- {model} (reasoning_effort={reasoning}) ---")
        t0 = time.monotonic()
        try:
            r = summarize(
                model=model,
                reasoning_effort=reasoning or "",
                title=item["title"],
                author=item["author"],
                duration_seconds=item["duration_seconds"],
                transcript=transcript,
            )
            elapsed = time.monotonic() - t0
            results.append({
                "model": model,
                "reasoning": reasoning,
                "elapsed_s": round(elapsed, 1),
                "hook": r.hook,
                "tldr": r.tldr,
                "key_points": r.key_points,
                "full_notes": r.full_notes,
                "ok": True,
            })
            print(f"  OK in {elapsed:.1f}s — hook: {r.hook[:80]}")
        except LLMError as e:
            elapsed = time.monotonic() - t0
            results.append({
                "model": model,
                "reasoning": reasoning,
                "elapsed_s": round(elapsed, 1),
                "error": str(e),
                "ok": False,
            })
            print(f"  FAIL in {elapsed:.1f}s — {e}")
        print()

    # Per-model markdown files
    for r in results:
        path = out_dir / f"{r['model'].replace('/', '_')}.md"
        if not r["ok"]:
            path.write_text(
                f"# {r['model']}\n\nFAILED in {r['elapsed_s']}s\n\n```\n{r['error']}\n```\n",
                encoding="utf-8",
            )
            continue
        body = (
            f"# {r['model']}  (reasoning_effort={r['reasoning']})\n\n"
            f"**elapsed:** {r['elapsed_s']}s\n\n"
            f"## Hook\n{r['hook']}\n\n"
            f"## TL;DR\n{r['tldr']}\n\n"
            f"## Key Points\n" + "\n".join(f"- {kp}" for kp in r["key_points"]) + "\n\n"
            f"## Full Notes\n{r['full_notes']}\n"
        )
        path.write_text(body, encoding="utf-8")

    # Side-by-side compare doc
    compare_lines: list[str] = [
        f"# Model Bake-Off: {item['title']}",
        "",
        f"- Item ID: {item['id']}",
        f"- Source: {item['author']}",
        f"- URL: {item['url']}",
        f"- Transcript chars: {len(transcript)}",
        "",
        "| Model | Reasoning | Elapsed | OK | Hook |",
        "|---|---|---|---|---|",
    ]
    for r in results:
        hook = r.get("hook", r.get("error", ""))[:60].replace("|", "\\|")
        compare_lines.append(
            f"| {r['model']} | {r['reasoning'] or '-'} | {r['elapsed_s']}s | "
            f"{'✓' if r['ok'] else '✗'} | {hook} |"
        )
    compare_lines += ["", "## TL;DRs side-by-side", ""]
    for r in results:
        if r["ok"]:
            compare_lines.append(f"### {r['model']}")
            compare_lines.append(r["tldr"])
            compare_lines.append("")
    compare_lines += ["## Full notes per model: see individual files in this directory.", ""]
    (out_dir / "COMPARE.md").write_text("\n".join(compare_lines), encoding="utf-8")

    print(f"Done. See {out_dir}/COMPARE.md and per-model files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
