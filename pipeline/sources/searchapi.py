"""SearchAPI.io adapter for YouTube transcripts.

Used when SEARCHAPI_KEY env var is set. SearchAPI handles the IP-block /
proxy plumbing so we don't have to. Free tier is 100 searches/month.

Endpoint: GET https://www.searchapi.io/api/v1/search?engine=youtube_transcripts&video_id=...
"""
from __future__ import annotations

import json
import logging
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

logger = logging.getLogger("skimr.searchapi")

_BASE_URL = "https://www.searchapi.io/api/v1/search"


def fetch_transcript(video_id: str, api_key: str, timeout: float = 30.0) -> str | None:
    """Return concatenated transcript text or None if unavailable."""
    params = {
        "engine": "youtube_transcripts",
        "video_id": video_id,
        "api_key": api_key,
    }
    url = f"{_BASE_URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8", errors="replace"))
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8", errors="replace")[:300]
        except Exception:
            pass
        if e.code in (402, 403, 429):
            logger.warning("SearchAPI quota/auth (%s) for %s: %s", e.code, video_id, body)
        else:
            logger.warning("SearchAPI HTTP %s for %s: %s", e.code, video_id, body)
        return None
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        logger.warning("SearchAPI request failed for %s: %s", video_id, e)
        return None

    return _extract_transcript_text(payload)


def _extract_transcript_text(payload: dict[str, Any]) -> str | None:
    """Pull text out of SearchAPI's response, defensive across schema variants."""
    segments = payload.get("transcripts")
    if not isinstance(segments, list) or not segments:
        # Some responses nest under different keys; check defensively.
        for key in ("captions", "transcript", "results"):
            candidate = payload.get(key)
            if isinstance(candidate, list) and candidate:
                segments = candidate
                break
    if not isinstance(segments, list) or not segments:
        return None
    parts: list[str] = []
    for seg in segments:
        if isinstance(seg, dict):
            text = seg.get("text") or seg.get("snippet") or seg.get("caption")
        elif isinstance(seg, str):
            text = seg
        else:
            text = None
        if text:
            parts.append(str(text).strip())
    joined = " ".join(p for p in parts if p)
    return joined or None
