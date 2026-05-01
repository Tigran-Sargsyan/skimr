from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class VideoMetadata:
    external_id: str
    title: str
    url: str
    published_at: str  # ISO 8601 UTC
    duration_seconds: int | None


class Source(ABC):
    name: str
    notes: str

    @abstractmethod
    def list_recent_videos(self, since: datetime | None) -> list[VideoMetadata]:
        ...

    @abstractmethod
    def fetch_transcript(self, video_id: str) -> str | None:
        ...
