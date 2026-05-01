import logging
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

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
_CHANNEL_ID_RE = re.compile(r'"(?:channelId|externalId)":"(UC[\w-]{22})"')
_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
_ATOM_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
}


def _http_get(url: str, timeout: float = 30.0) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": _USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


class YouTubeSource(Source):
    def __init__(self, name: str, channel_handle: str, notes: str = ""):
        self.name = name
        self.notes = notes
        # Normalize: ensure handle starts with @ (or accept a bare UCxxx channel id).
        if channel_handle.startswith("UC") and len(channel_handle) == 24:
            self.handle = channel_handle
            self._channel_id_cached: str | None = channel_handle
        else:
            self.handle = channel_handle if channel_handle.startswith("@") else f"@{channel_handle}"
            self._channel_id_cached = None

    def _resolve_channel_id(self) -> str | None:
        if self._channel_id_cached:
            return self._channel_id_cached
        url = f"https://www.youtube.com/{self.handle}"
        try:
            html = _http_get(url)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            logger.warning("channel page fetch failed for %s: %s", self.handle, e)
            return None
        match = _CHANNEL_ID_RE.search(html)
        if not match:
            logger.warning("could not find channelId in %s", url)
            return None
        self._channel_id_cached = match.group(1)
        return self._channel_id_cached

    def list_recent_videos(self, since: datetime | None) -> list[VideoMetadata]:
        channel_id = self._resolve_channel_id()
        if not channel_id:
            return []
        feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
        try:
            xml_text = _http_get(feed_url)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            logger.warning("feed fetch failed for %s: %s", channel_id, e)
            return []
        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError as e:
            logger.warning("feed parse failed for %s: %s", channel_id, e)
            return []

        results: list[VideoMetadata] = []
        for entry in root.findall("atom:entry", _ATOM_NS):
            video_id_el = entry.find("yt:videoId", _ATOM_NS)
            title_el = entry.find("atom:title", _ATOM_NS)
            published_el = entry.find("atom:published", _ATOM_NS)
            if video_id_el is None or title_el is None or published_el is None:
                continue
            video_id = (video_id_el.text or "").strip()
            title = (title_el.text or "").strip()
            published_at_raw = (published_el.text or "").strip()
            if not (video_id and title and published_at_raw):
                continue
            try:
                published_dt = datetime.fromisoformat(published_at_raw.replace("Z", "+00:00"))
            except ValueError:
                continue
            if since and published_dt < since:
                continue
            results.append(
                VideoMetadata(
                    external_id=video_id,
                    title=title,
                    url=f"https://www.youtube.com/watch?v={video_id}",
                    published_at=published_dt.astimezone(timezone.utc).strftime(
                        "%Y-%m-%dT%H:%M:%SZ"
                    ),
                    duration_seconds=None,  # not exposed in the Atom feed
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
