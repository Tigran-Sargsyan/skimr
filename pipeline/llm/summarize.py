from .client import parse_structured
from .schemas import SummaryOutput

SYSTEM_PROMPT = """You are summarizing a video transcript for a personal reading list. The user \
prefers depth over brevity but does not want padding. Adapt length to the \
substance of the source: a 4-minute video does not need 500 words of notes.

Your output is structured JSON. Do not include any prose outside the schema.
Do not editorialize. Do not add facts not in the source. Do not include \
filler like "the speaker discusses..." — extract claims and explain them."""


def build_messages(*, title: str, author: str, duration_seconds: int | None,
                   transcript: str) -> list[dict[str, str]]:
    duration_str = str(duration_seconds) if duration_seconds is not None else "unknown"
    user = (
        f"Source title: {title}\n"
        f"Source author: {author}\n"
        f"Source duration: {duration_str} seconds\n\n"
        f"Transcript:\n{transcript}"
    )
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user},
    ]


def summarize(*, model: str, reasoning_effort: str, title: str, author: str,
              duration_seconds: int | None, transcript: str) -> SummaryOutput:
    messages = build_messages(
        title=title,
        author=author,
        duration_seconds=duration_seconds,
        transcript=transcript,
    )
    return parse_structured(
        model=model,
        reasoning_effort=reasoning_effort,
        messages=messages,
        response_format=SummaryOutput,
        stage="summarize",
    )
