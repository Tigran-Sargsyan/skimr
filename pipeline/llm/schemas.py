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
        description="Each is a complete claim, not a topic.",
    )
    full_notes: str = Field(
        ...,
        description=(
            "300-500 word structured prose with subheadings. For short videos under "
            "5 minutes, scale down to 100-200 words. Markdown formatting."
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
