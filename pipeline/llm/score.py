from .client import parse_structured
from .schemas import ScoreOutput

SYSTEM_PROMPT = """You are evaluating whether this item is worth the user's time. Use their \
profile, the item's content, and its theme classification to produce:

1. A relevance score from 1 to 10
2. A one-sentence pitch addressed directly to the user explaining why it's \
   worth their time, given who they are. Use "you" naturally.
3. A one-sentence caveat for what might make them skip it. Empty if none.

Be honest. A score below 5 means the user should probably skip it. A score \
of 9 or 10 should be rare — reserve those for items that strongly match \
the user's stated interests AND clearly meet their style preferences.

Do not flatter. Do not hedge. The user wants to be told when something \
isn't worth reading."""


def build_messages(*, profile_yaml: str, source_notes: str, title: str, author: str,
                   primary_theme: str, secondary_theme: str | None,
                   hook: str, tldr: str, key_points: list[str]) -> list[dict[str, str]]:
    bulleted = "\n".join(f"- {p}" for p in key_points)
    secondary = secondary_theme if secondary_theme else "none"
    user = (
        "=== USER PROFILE ===\n"
        f"{profile_yaml}\n\n"
        "=== SOURCE NOTES ===\n"
        f"{source_notes or '(none)'}\n\n"
        "=== ITEM ===\n"
        f"Title: {title}\n"
        f"Author: {author}\n"
        f"Primary theme: {primary_theme}\n"
        f"Secondary theme: {secondary}\n\n"
        f"Hook: {hook}\n"
        f"TL;DR: {tldr}\n"
        f"Key points:\n{bulleted}"
    )
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user},
    ]


def score(*, model: str, reasoning_effort: str, profile_yaml: str, source_notes: str,
          title: str, author: str, primary_theme: str, secondary_theme: str | None,
          hook: str, tldr: str, key_points: list[str]) -> ScoreOutput:
    messages = build_messages(
        profile_yaml=profile_yaml,
        source_notes=source_notes,
        title=title,
        author=author,
        primary_theme=primary_theme,
        secondary_theme=secondary_theme,
        hook=hook,
        tldr=tldr,
        key_points=key_points,
    )
    result = parse_structured(
        model=model,
        reasoning_effort=reasoning_effort,
        messages=messages,
        response_format=ScoreOutput,
        stage="score",
    )
    if result.caveats is not None and not result.caveats.strip():
        result.caveats = None
    return result
