import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

from .config import db_path

SCHEMA = """
CREATE TABLE IF NOT EXISTS sources (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT NOT NULL,
    type            TEXT NOT NULL CHECK (type IN ('youtube')),
    external_id     TEXT NOT NULL,
    active          INTEGER NOT NULL DEFAULT 1,
    notes           TEXT,
    last_checked_at TEXT,
    added_at        TEXT NOT NULL,
    UNIQUE(type, external_id)
);

CREATE TABLE IF NOT EXISTS items (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id       INTEGER NOT NULL REFERENCES sources(id),
    external_id     TEXT NOT NULL,
    title           TEXT NOT NULL,
    url             TEXT NOT NULL,
    author          TEXT NOT NULL,
    published_at    TEXT NOT NULL,
    duration_seconds INTEGER,
    discovered_at   TEXT NOT NULL,
    status          TEXT NOT NULL CHECK (status IN (
                        'discovered',
                        'no_transcript',
                        'transcript_fetched',
                        'summarized',
                        'classified',
                        'scored',
                        'rendered',
                        'failed'
                    )),
    failure_reason  TEXT,
    transcript      TEXT,
    UNIQUE(source_id, external_id)
);

CREATE INDEX IF NOT EXISTS idx_items_published_at ON items(published_at DESC);
CREATE INDEX IF NOT EXISTS idx_items_status ON items(status);
CREATE INDEX IF NOT EXISTS idx_items_source_id ON items(source_id);

CREATE TABLE IF NOT EXISTS summaries (
    item_id         INTEGER PRIMARY KEY REFERENCES items(id) ON DELETE CASCADE,
    hook            TEXT NOT NULL,
    tldr            TEXT NOT NULL,
    key_points      TEXT NOT NULL,
    full_notes      TEXT NOT NULL,
    model           TEXT NOT NULL,
    generated_at    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS classifications (
    item_id         INTEGER PRIMARY KEY REFERENCES items(id) ON DELETE CASCADE,
    primary_theme   TEXT NOT NULL CHECK (primary_theme IN (
                        'tech', 'business', 'science', 'thinking', 'culture'
                    )),
    secondary_theme TEXT CHECK (secondary_theme IN (
                        'tech', 'business', 'science', 'thinking', 'culture'
                    )),
    reasoning       TEXT NOT NULL,
    model           TEXT NOT NULL,
    generated_at    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS scores (
    item_id         INTEGER PRIMARY KEY REFERENCES items(id) ON DELETE CASCADE,
    relevance       INTEGER NOT NULL CHECK (relevance BETWEEN 1 AND 10),
    pitch           TEXT NOT NULL,
    caveats         TEXT,
    model           TEXT NOT NULL,
    generated_at    TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_scores_relevance ON scores(relevance DESC);

CREATE TABLE IF NOT EXISTS pipeline_runs (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at      TEXT NOT NULL,
    finished_at     TEXT,
    status          TEXT NOT NULL CHECK (status IN ('running', 'success', 'failed')),
    items_discovered INTEGER NOT NULL DEFAULT 0,
    items_processed INTEGER NOT NULL DEFAULT 0,
    items_failed    INTEGER NOT NULL DEFAULT 0,
    notes           TEXT
);
"""


def utcnow_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def connect(path: Path | None = None) -> sqlite3.Connection:
    target = path or db_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(target)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)
    conn.commit()


@contextmanager
def transaction(conn: sqlite3.Connection) -> Iterator[sqlite3.Connection]:
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise


# ---------- Sources ----------

def upsert_source(conn: sqlite3.Connection, name: str, type_: str, external_id: str,
                  active: bool, notes: str) -> int:
    row = conn.execute(
        "SELECT id FROM sources WHERE type = ? AND external_id = ?",
        (type_, external_id),
    ).fetchone()
    if row:
        conn.execute(
            "UPDATE sources SET name = ?, active = ?, notes = ? WHERE id = ?",
            (name, 1 if active else 0, notes, row["id"]),
        )
        conn.commit()
        return row["id"]
    cursor = conn.execute(
        "INSERT INTO sources (name, type, external_id, active, notes, added_at) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (name, type_, external_id, 1 if active else 0, notes, utcnow_iso()),
    )
    conn.commit()
    return cursor.lastrowid


def get_active_sources(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    return conn.execute(
        "SELECT * FROM sources WHERE active = 1 ORDER BY id"
    ).fetchall()


def update_source_last_checked(conn: sqlite3.Connection, source_id: int) -> None:
    conn.execute(
        "UPDATE sources SET last_checked_at = ? WHERE id = ?",
        (utcnow_iso(), source_id),
    )
    conn.commit()


# ---------- Items ----------

def insert_item(conn: sqlite3.Connection, *, source_id: int, external_id: str,
                title: str, url: str, author: str, published_at: str,
                duration_seconds: int | None) -> int | None:
    """Insert a new item in `discovered` state. Returns item id, or None if it already exists."""
    existing = conn.execute(
        "SELECT id FROM items WHERE source_id = ? AND external_id = ?",
        (source_id, external_id),
    ).fetchone()
    if existing:
        return None
    cursor = conn.execute(
        "INSERT INTO items (source_id, external_id, title, url, author, published_at, "
        "duration_seconds, discovered_at, status) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'discovered')",
        (source_id, external_id, title, url, author, published_at, duration_seconds, utcnow_iso()),
    )
    conn.commit()
    return cursor.lastrowid


def set_item_status(conn: sqlite3.Connection, item_id: int, status: str,
                    failure_reason: str | None = None) -> None:
    conn.execute(
        "UPDATE items SET status = ?, failure_reason = ? WHERE id = ?",
        (status, failure_reason, item_id),
    )
    conn.commit()


def set_item_transcript(conn: sqlite3.Connection, item_id: int, transcript: str) -> None:
    conn.execute(
        "UPDATE items SET transcript = ?, status = 'transcript_fetched' WHERE id = ?",
        (transcript, item_id),
    )
    conn.commit()


def items_in_status(conn: sqlite3.Connection, status: str) -> list[sqlite3.Row]:
    return conn.execute(
        "SELECT * FROM items WHERE status = ? ORDER BY id",
        (status,),
    ).fetchall()


def get_item(conn: sqlite3.Connection, item_id: int) -> sqlite3.Row | None:
    return conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()


# ---------- Summaries / Classifications / Scores ----------

def upsert_summary(conn: sqlite3.Connection, item_id: int, *, hook: str, tldr: str,
                   key_points: list[str], full_notes: str, model: str) -> None:
    conn.execute(
        "INSERT OR REPLACE INTO summaries (item_id, hook, tldr, key_points, full_notes, model, generated_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        (item_id, hook, tldr, json.dumps(key_points), full_notes, model, utcnow_iso()),
    )
    conn.commit()


def get_summary(conn: sqlite3.Connection, item_id: int) -> dict[str, Any] | None:
    row = conn.execute("SELECT * FROM summaries WHERE item_id = ?", (item_id,)).fetchone()
    if not row:
        return None
    data = dict(row)
    data["key_points"] = json.loads(data["key_points"])
    return data


def upsert_classification(conn: sqlite3.Connection, item_id: int, *, primary_theme: str,
                          secondary_theme: str | None, reasoning: str, model: str) -> None:
    conn.execute(
        "INSERT OR REPLACE INTO classifications "
        "(item_id, primary_theme, secondary_theme, reasoning, model, generated_at) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (item_id, primary_theme, secondary_theme, reasoning, model, utcnow_iso()),
    )
    conn.commit()


def get_classification(conn: sqlite3.Connection, item_id: int) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM classifications WHERE item_id = ?", (item_id,)
    ).fetchone()


def upsert_score(conn: sqlite3.Connection, item_id: int, *, relevance: int, pitch: str,
                 caveats: str | None, model: str) -> None:
    conn.execute(
        "INSERT OR REPLACE INTO scores (item_id, relevance, pitch, caveats, model, generated_at) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (item_id, relevance, pitch, caveats, model, utcnow_iso()),
    )
    conn.commit()


def get_score(conn: sqlite3.Connection, item_id: int) -> sqlite3.Row | None:
    return conn.execute("SELECT * FROM scores WHERE item_id = ?", (item_id,)).fetchone()


# ---------- Pipeline runs ----------

def start_run(conn: sqlite3.Connection) -> int:
    cursor = conn.execute(
        "INSERT INTO pipeline_runs (started_at, status) VALUES (?, 'running')",
        (utcnow_iso(),),
    )
    conn.commit()
    return cursor.lastrowid


def finish_run(conn: sqlite3.Connection, run_id: int, *, status: str,
               items_discovered: int, items_processed: int, items_failed: int,
               notes: str | None = None) -> None:
    conn.execute(
        "UPDATE pipeline_runs SET finished_at = ?, status = ?, items_discovered = ?, "
        "items_processed = ?, items_failed = ?, notes = ? WHERE id = ?",
        (utcnow_iso(), status, items_discovered, items_processed, items_failed, notes, run_id),
    )
    conn.commit()


def append_run_notes(conn: sqlite3.Connection, run_id: int, line: str) -> None:
    row = conn.execute("SELECT notes FROM pipeline_runs WHERE id = ?", (run_id,)).fetchone()
    existing = (row["notes"] or "") if row else ""
    new_notes = (existing + "\n" + line).strip()
    conn.execute("UPDATE pipeline_runs SET notes = ? WHERE id = ?", (new_notes, run_id))
    conn.commit()
