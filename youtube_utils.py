import re
from urllib.parse import urlparse, parse_qs

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import YOUTUBE_API_KEY

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def extract_playlist_id(playlist_url: str) -> str:
    """
    Extract the 'list' parameter (playlist ID) from a YouTube playlist URL.
    Raises ValueError if it cannot be found.
    """
    parsed = urlparse(playlist_url)
    query_params = parse_qs(parsed.query)
    if "list" in query_params and query_params["list"]:
        return query_params["list"][0]
    raise ValueError(f"Invalid YouTube playlist URL (no list param): {playlist_url}")


def get_playlist_videos(playlist_url: str) -> list[dict]:
    """
    Fetches all videos in the given YouTube playlist.
    Returns a list of dicts with keys: video_id, title, url.
    """
    playlist_id = extract_playlist_id(playlist_url)
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=YOUTUBE_API_KEY,
    )

    videos: list[dict] = []
    next_page_token = None

    while True:
        try:
            resp = (
                youtube.playlistItems()
                .list(
                    part="snippet",
                    playlistId=playlist_id,
                    maxResults=50,
                    pageToken=next_page_token,
                )
                .execute()
            )
        except HttpError as e:
            raise RuntimeError(f"Failed to fetch playlist items: {e}")

        for item in resp.get("items", []):
            snip = item["snippet"]
            vid_id = snip["resourceId"]["videoId"]
            title = snip.get("title", "")
            videos.append({
                "video_id": vid_id,
                "title": title,
                "url": f"https://www.youtube.com/watch?v={vid_id}"
            })

        next_page_token = resp.get("nextPageToken")
        if not next_page_token:
            break

    return videos
