import re
import unicodedata
from datetime import datetime

_SLUG_STRIP = re.compile(r"[^a-z0-9]+")


def slugify(value: str, max_length: int = 80) -> str:
    """Lowercase, alphanumeric + hyphens, capped length. Deterministic."""
    if not value:
        return ""
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    lower = normalized.lower()
    hyphenated = _SLUG_STRIP.sub("-", lower).strip("-")
    if len(hyphenated) <= max_length:
        return hyphenated
    truncated = hyphenated[:max_length].rstrip("-")
    return truncated


def item_slug(published_at_iso: str, source_name: str, title: str) -> str:
    """{yyyy-mm-dd}-{source_slug}-{title_slug}, total ≤ 80 chars."""
    date_str = datetime.fromisoformat(published_at_iso.replace("Z", "+00:00")).strftime("%Y-%m-%d")
    source_part = slugify(source_name, max_length=20)
    title_part = slugify(title, max_length=80 - len(date_str) - len(source_part) - 2)
    parts = [date_str, source_part, title_part]
    return "-".join(p for p in parts if p)
