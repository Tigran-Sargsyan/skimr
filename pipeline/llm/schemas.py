from typing import Literal

from pydantic import BaseModel, Field


class SummaryOutput(BaseModel):
    hook: str = Field(
        ...,
        description="One sentence, ≤15 words, that makes a busy reader want to engage.",
    )
    tldr: str = Field(..., description="Three sentences capturing the substance.")
    key_points: list[str] = Field(
        ...,
        min_length=3,
        max_length=8,
        description=(
            "Each item is ONE atomic claim, ≤30 words, written as a single sentence "
            "with no internal line breaks, no semicolons stitching multiple ideas, "
            "no lists embedded in the string. If you have more ideas than fit in 8 "
            "items, push the rest into full_notes — never cram multiple claims into "
            "one bullet."
        ),
    )
    full_notes: str = Field(
        ...,
        description=(
            "Markdown-formatted structured prose with `## Subheading` sections. "
            "Length should scale with the substance of the source: ~150 words for "
            "videos under 5 minutes, ~400 words for 10–20 minute videos, and "
            "800–1500 words for long-form (45+ minute) interviews and deep-dives. "
            "When the transcript is rich, prefer depth here over compression — the "
            "user reads this section as the primary takeaway, not the key_points list."
        ),
    )


Theme = Literal["tech", "business", "science", "thinking", "culture"]


class ClassificationOutput(BaseModel):
    primary_theme: Theme
    secondary_theme: Theme | None = Field(
        None,
        description=(
            "Only set if the item meaningfully spans two themes. Must differ from primary."
        ),
    )
    reasoning: str = Field(..., description="One sentence explaining the choice.")


class ScoreOutput(BaseModel):
    relevance: int = Field(..., ge=1, le=10, description="1-10 relevance to the user's interests.")
    pitch: str = Field(
        ...,
        description=(
            "One sentence addressed to the user, telling them why this is worth their "
            "time given who they are."
        ),
    )
    caveats: str | None = Field(
        None,
        description="One sentence on what would make them skip it. Empty string if none.",
    )
