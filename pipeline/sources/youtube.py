import logging
import re
import time
from datetime import datetime, timezone
from typing import Any

import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    CouldNotRetrieveTranscript,
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

from .base import Source, VideoMetadata

logger = logging.getLogger("skimr.youtube")

_WHITESPACE = re.compile(r"\s+")


class YouTubeSource(Source):
    def __init__(self, name: str, channel_handle: str, notes: str = ""):
        self.name = name
        self.notes = notes
        # Normalize: ensure handle starts with @
        self.handle = channel_handle if channel_handle.startswith("@") else f"@{channel_handle}"

    def _channel_videos_url(self) -> str:
        return f"https://www.youtube.com/{self.handle}/videos"

    def list_recent_videos(self, since: datetime | None) -> list[VideoMetadata]:
        url = self._channel_videos_url()
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "extract_flat": "in_playlist",
            "skip_download": True,
            "playlistend": 30,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=False)
            except Exception as e:
                logger.warning("yt-dlp failed listing %s: %s", self.handle, e)
                return []

        entries: list[dict[str, Any]] = []
        for entry in info.get("entries") or []:
            if not entry:
                continue
            # YouTube channels expose top-level tabs as nested entries on some yt-dlp versions.
            if entry.get("_type") == "playlist" and entry.get("entries"):
                entries.extend(e for e in entry["entries"] if e)
            else:
                entries.append(entry)

        results: list[VideoMetadata] = []
        detail_opts = {"quiet": True, "no_warnings": True, "skip_download": True}
        for entry in entries[:30]:
            video_id = entry.get("id")
            if not video_id:
                continue
            timestamp = entry.get("timestamp") or entry.get("release_timestamp")
            duration = entry.get("duration")
            title = entry.get("title") or ""
            if timestamp is None:
                # Fall back to per-video metadata fetch.
                try:
                    with yt_dlp.YoutubeDL(detail_opts) as ydl2:
                        detail = ydl2.extract_info(
                            f"https://www.youtube.com/watch?v={video_id}", download=False
                        )
                    timestamp = detail.get("timestamp") or detail.get("release_timestamp")
                    duration = detail.get("duration") or duration
                    title = detail.get("title") or title
                except Exception as e:
                    logger.warning("yt-dlp detail fetch failed for %s: %s", video_id, e)
                    continue
            if timestamp is None:
                logger.warning("no timestamp for %s, skipping", video_id)
                continue
            published_dt = datetime.fromtimestamp(int(timestamp), tz=timezone.utc)
            if since and published_dt < since:
                continue
            results.append(
                VideoMetadata(
                    external_id=video_id,
                    title=title,
                    url=f"https://www.youtube.com/watch?v={video_id}",
                    published_at=published_dt.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    duration_seconds=int(duration) if duration else None,
                )
            )
        return results

    def fetch_transcript(self, video_id: str) -> str | None:
        # Polite delay before each transcript fetch.
        time.sleep(2)
        api = YouTubeTranscriptApi()
        try:
            transcript_list = api.list(video_id)
        except (TranscriptsDisabled, VideoUnavailable, NoTranscriptFound):
            return None
        except CouldNotRetrieveTranscript as e:
            logger.warning("transcript list failed for %s: %s", video_id, e)
            return None
        except Exception as e:
            logger.warning("transcript list unexpected error for %s: %s", video_id, e)
            return None

        chosen = None
        try:
            chosen = transcript_list.find_manually_created_transcript(["en"])
        except NoTranscriptFound:
            try:
                chosen = transcript_list.find_generated_transcript(["en"])
            except NoTranscriptFound:
                return None
        if chosen is None:
            return None
        try:
            fetched = chosen.fetch()
        except Exception as e:
            logger.warning("transcript fetch failed for %s: %s", video_id, e)
            return None
        # FetchedTranscript exposes `snippets` (>=1.0) or yields dicts via to_raw_data().
        raw_segments = fetched.to_raw_data() if hasattr(fetched, "to_raw_data") else list(fetched)
        parts: list[str] = []
        for seg in raw_segments:
            text = seg.get("text") if isinstance(seg, dict) else getattr(seg, "text", None)
            if text:
                parts.append(text)
        joined = " ".join(parts)
        normalized = _WHITESPACE.sub(" ", joined).strip()
        return normalized or None
