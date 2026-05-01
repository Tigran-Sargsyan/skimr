import logging
import time
from typing import Any, Type, TypeVar

from openai import APITimeoutError, OpenAI, RateLimitError
from pydantic import BaseModel, ValidationError

from ..config import get_env

logger = logging.getLogger("skimr.llm")

_client: OpenAI | None = None

T = TypeVar("T", bound=BaseModel)


def get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(api_key=get_env("OPENAI_API_KEY"), timeout=60.0)
    return _client


class LLMError(Exception):
    """Raised when an LLM call fails after retries. Carries the failure reason."""


def parse_structured(
    *,
    model: str,
    reasoning_effort: str,
    messages: list[dict[str, Any]],
    response_format: Type[T],
    stage: str,
) -> T:
    """Call chat.completions.parse with retries and schema validation."""
    client = get_client()
    last_error: str = "unknown error"

    # 1) Rate-limit retries with exponential backoff: 1s, 4s, 16s.
    rate_limit_delays = [1, 4, 16]
    rate_limit_attempts = 0

    # 2) Schema validation: retry once.
    schema_retries_remaining = 1
    # 3) Timeout: retry once.
    timeout_retries_remaining = 1

    while True:
        try:
            kwargs: dict[str, Any] = {
                "model": model,
                "messages": messages,
                "response_format": response_format,
            }
            if reasoning_effort:
                kwargs["reasoning_effort"] = reasoning_effort
            completion = client.chat.completions.parse(**kwargs)
            parsed = completion.choices[0].message.parsed
            if parsed is None:
                raw = completion.choices[0].message.content or ""
                if schema_retries_remaining > 0:
                    schema_retries_remaining -= 1
                    last_error = f"empty parsed output: {raw[:200]}"
                    logger.warning("[%s] empty parsed output, retrying once", stage)
                    continue
                raise LLMError(f"schema validation failed in {stage}: {raw[:200]}")
            return parsed
        except RateLimitError as e:
            if rate_limit_attempts >= len(rate_limit_delays):
                raise LLMError(f"rate limited in {stage} after retries: {e}") from e
            delay = rate_limit_delays[rate_limit_attempts]
            rate_limit_attempts += 1
            logger.warning("[%s] rate limited, sleeping %ss", stage, delay)
            time.sleep(delay)
            continue
        except APITimeoutError as e:
            if timeout_retries_remaining > 0:
                timeout_retries_remaining -= 1
                logger.warning("[%s] timeout, retrying once", stage)
                continue
            raise LLMError(f"timeout in {stage}") from e
        except ValidationError as e:
            if schema_retries_remaining > 0:
                schema_retries_remaining -= 1
                last_error = f"schema validation: {e}"
                logger.warning("[%s] schema validation failed, retrying once", stage)
                continue
            raise LLMError(f"schema validation failed in {stage}: {e}") from e
        except LLMError:
            raise
        except Exception as e:
            raise LLMError(f"{stage} failed: {e}") from e
