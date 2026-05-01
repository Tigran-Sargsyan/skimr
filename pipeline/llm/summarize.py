import re

from .client import parse_structured
from .schemas import SummaryOutput

# Strip suspect characters that some long-output models occasionally trail
# with. Observed during bake-off: a gpt-5.1 key_point ended with hundreds of
# U+FFFC OBJECT REPLACEMENT CHARACTERs. Also strip U+FFFD (REPLACEMENT) and
# control chars except \n \t.
_DROP = re.compile(r"[￼�￾￿]")  # OBJECT REPLACEMENT, REPLACEMENT, etc.
_INLINE_WS = re.compile(r"[\s\x00-\x1F]+")  # any whitespace or control → collapse to one space
_BLOCK_CTRL = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F]")  # control chars except \t \n \r


def _clean_inline(text: str) -> str:
    """For one-line fields (hook, tldr, key_points): drop noise, collapse newlines to spaces."""
    return _INLINE_WS.sub(" ", _DROP.sub("", text)).strip()


def _clean_block(text: str) -> str:
    """For markdown bodies (full_notes): preserve newlines/tabs, drop only stray control chars."""
    return _BLOCK_CTRL.sub("", _DROP.sub("", text)).strip()


def _split_runaway(point: str, max_words: int = 35) -> list[str]:
    """If a key_point ran on (>max_words), split at sentence boundaries.

    Defends against the case where the model still ignores the prompt and
    crams multiple claims into one bullet. We never want a wall of text.
    """
    if len(point.split()) <= max_words:
        return [point]
    # Split on sentence-ending punctuation followed by a space + capital letter.
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(])", point)
    return [p.strip() for p in parts if p.strip()]


def _sanitize(result: SummaryOutput) -> SummaryOutput:
    result.hook = _clean_inline(result.hook)
    result.tldr = _clean_inline(result.tldr)

    cleaned_points: list[str] = []
    for raw in result.key_points:
        for piece in _split_runaway(_clean_inline(raw)):
            if len(piece) >= 5:
                cleaned_points.append(piece)
    # Re-cap to schema's max of 8 items so we don't blow the contract.
    result.key_points = cleaned_points[:8] if cleaned_points else result.key_points

    result.full_notes = _clean_block(result.full_notes)
    return result


SYSTEM_PROMPT = """You are summarizing a video transcript for a personal reading list. The user \
prefers depth over brevity but does not want padding. Adapt length to the \
substance of the source: a short video does not need 1000 words of notes; a \
long-form interview earns them.

Your output is structured JSON. Do not include any prose outside the schema.
Do not editorialize. Do not add facts not in the source. Do not include \
filler like "the speaker discusses..." — extract claims and explain them.

Field discipline:
- `hook`: one sentence, ≤15 words.
- `tldr`: exactly three sentences. No more, no fewer.
- `key_points`: 3–8 items. EACH item is ONE atomic claim in ONE sentence, \
≤30 words. Never stitch multiple claims into a single bullet. Never use \
internal newlines or run-on lists inside a key point.
- `full_notes`: this is where depth lives. Use `## Subheading` sections to \
organize. Scale length to substance: ~150 words for short videos, ~400 for \
medium, 800–1500 for long-form. If the transcript is rich, prefer expanding \
here over cramming into key_points."""


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
