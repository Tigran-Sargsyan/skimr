"""Initialize an empty SQLite database at SKIMR_DB_PATH (default data/digest.db)."""
from pipeline import db
from pipeline.config import db_path


def main() -> int:
    conn = db.connect()
    db.init_schema(conn)
    print(f"Initialized DB at {db_path()}")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
