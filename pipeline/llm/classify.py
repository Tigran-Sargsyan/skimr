from .client import parse_structured
from .schemas import ClassificationOutput

SYSTEM_PROMPT = """Classify the item into one of five fixed themes. Do not invent new themes.
The themes are:

- tech: software, AI/ML, agents, distributed systems, infrastructure, programming
- business: startups, strategy, economics, markets, management
- science: physics, biology, neuroscience, research methodology, mathematics
- thinking: epistemics, decision-making, philosophy, learning, expertise
- culture: books, films, history, broader cultural ideas

Pick the single best fit as the primary theme. If — and only if — the item \
substantially spans two themes, add a secondary. Most items do not need a \
secondary."""


def build_messages(*, title: str, author: str, tldr: str, key_points: list[str]) -> list[dict[str, str]]:
    bulleted = "\n".join(f"- {p}" for p in key_points)
    user = (
        f"Title: {title}\n"
        f"Author: {author}\n\n"
        f"Summary:\n{tldr}\n\n"
        f"Key points:\n{bulleted}"
    )
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user},
    ]


def classify(*, model: str, reasoning_effort: str, title: str, author: str,
             tldr: str, key_points: list[str]) -> ClassificationOutput:
    messages = build_messages(title=title, author=author, tldr=tldr, key_points=key_points)
    result = parse_structured(
        model=model,
        reasoning_effort=reasoning_effort,
        messages=messages,
        response_format=ClassificationOutput,
        stage="classify",
    )
    if result.secondary_theme == result.primary_theme:
        result.secondary_theme = None
    return result
