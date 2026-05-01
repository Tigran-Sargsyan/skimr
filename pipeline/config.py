import os
from pathlib import Path
from typing import Literal

import yaml
from dotenv import load_dotenv
from pydantic import BaseModel, Field, ValidationError

load_dotenv()

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"

ThemeKey = Literal["tech", "thinking", "culture", "business", "science"]
Weight = Literal["high", "medium", "low"]


class ThemeConfig(BaseModel):
    weight: Weight
    description: str


class ProfileConfig(BaseModel):
    identity: str
    themes: dict[ThemeKey, ThemeConfig]
    avoid: list[str] = Field(default_factory=list)
    style_preferences: str = ""


class SourceConfig(BaseModel):
    name: str
    type: Literal["youtube"]
    id: str
    active: bool = True
    notes: str = ""


def get_env(name: str, default: str | None = None) -> str:
    value = os.environ.get(name, default)
    if value is None:
        raise RuntimeError(f"Missing required env var: {name}")
    return value


def load_profile(path: Path | None = None) -> ProfileConfig:
    profile_path = path or DATA_DIR / "profile.yaml"
    if not profile_path.exists():
        raise FileNotFoundError(
            f"profile.yaml not found at {profile_path}. Copy data/profile.yaml.example "
            f"to data/profile.yaml and fill it in."
        )
    raw = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
    expected_themes = {"tech", "thinking", "culture", "business", "science"}
    actual_themes = set((raw or {}).get("themes", {}).keys())
    extra = actual_themes - expected_themes
    if extra:
        raise ValueError(
            f"profile.yaml contains unknown theme keys {sorted(extra)}. "
            f"Allowed: {sorted(expected_themes)}"
        )
    missing = expected_themes - actual_themes
    if missing:
        raise ValueError(
            f"profile.yaml is missing required theme keys {sorted(missing)}."
        )
    try:
        return ProfileConfig.model_validate(raw)
    except ValidationError as e:
        raise ValueError(f"profile.yaml is invalid:\n{e}") from e


def load_sources(path: Path | None = None) -> list[SourceConfig]:
    sources_path = path or DATA_DIR / "sources.yaml"
    if not sources_path.exists():
        raise FileNotFoundError(
            f"sources.yaml not found at {sources_path}. Copy data/sources.yaml.example "
            f"to data/sources.yaml and fill it in."
        )
    raw = yaml.safe_load(sources_path.read_text(encoding="utf-8")) or {}
    items = raw.get("sources", [])
    if not isinstance(items, list):
        raise ValueError("sources.yaml must have a top-level `sources:` list.")
    try:
        return [SourceConfig.model_validate(item) for item in items]
    except ValidationError as e:
        raise ValueError(f"sources.yaml is invalid:\n{e}") from e


def db_path() -> Path:
    return Path(os.environ.get("SKIMR_DB_PATH", str(DATA_DIR / "digest.db")))


def site_content_dir() -> Path:
    return REPO_ROOT / os.environ.get("SKIMR_SITE_CONTENT_DIR", "site/src/content/items")


def homepage_limit() -> int:
    return int(os.environ.get("SKIMR_HOMEPAGE_LIMIT", "10"))


def backfill_days() -> int:
    return int(os.environ.get("SKIMR_BACKFILL_DAYS", "3"))


def model_for(stage: Literal["summarize", "classify", "score"]) -> str:
    return os.environ.get(f"SKIMR_MODEL_{stage.upper()}", "gpt-5.4-mini")


def reasoning_for(stage: Literal["summarize", "classify", "score"]) -> str:
    defaults = {"summarize": "low", "classify": "minimal", "score": "medium"}
    return os.environ.get(f"SKIMR_REASONING_{stage.upper()}", defaults[stage])
