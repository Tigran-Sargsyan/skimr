import re

from .client import parse_structured
from .schemas import SummaryOutput

# Strip suspect characters that some long-output models occasionally trail
# with. Observed during bake-off: a gpt-5.1 key_point ended with hundreds of
# U+FFFC OBJECT REPLACEMENT CHARACTERs. Also strip U+FFFD (REPLACEMENT) and
# control chars except \n \t.
_BAD_INLINE = re.compile(r"[￼�￾￿\x00-\x1F]")
_BAD_BLOCK = re.compile(r"[￼�￾￿\x00-\x08\x0B\x0C\x0E-\x1F]")
_WS = re.compile(r"\s+")


def _clean_inline(text: str) -> str:
    return _WS.sub(" ", _BAD_INLINE.sub("", text)).strip()


def _clean_block(text: str) -> str:
    # Preserve newlines / tabs for markdown bodies.
    return _BAD_BLOCK.sub("", text).strip()


def _sanitize(result: SummaryOutput) -> SummaryOutput:
    result.hook = _clean_inline(result.hook)
    result.tldr = _clean_inline(result.tldr)
    result.key_points = [
        kp for kp in (_clean_inline(p) for p in result.key_points) if len(kp) >= 5
    ]
    result.full_notes = _clean_block(result.full_notes)
    return result


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
    result = parse_structured(
        model=model,
        reasoning_effort=reasoning_effort,
        messages=messages,
        response_format=SummaryOutput,
        stage="summarize",
    )
    return _sanitize(result)
