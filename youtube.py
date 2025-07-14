from dotenv import load_dotenv
from googleapiclient.discovery import build
import os
from isodate import parse_duration
from datetime import datetime

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def fetchMetadata(videoID):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.videos().list(part="snippet, contentDetails, statistics", id=videoID)
    response = request.execute()

    video = response["items"][0]
    snippet = video["snippet"]
    details = video["contentDetails"]
    stats = video["statistics"]

    return {
        "title": snippet['title'],
        "channel": snippet['channelTitle'],
        "duration": int(parse_duration(details['duration']).total_seconds()),
        "thumbnail": snippet['thumbnails'].get("high", {}).get('url', ''),
        "created": datetime.fromisoformat(snippet['publishedAt'].replace("Z", "+00:00")),
        "likes": int(stats['likeCount']),
        "views": int(stats['viewCount']),
        "language": snippet['defaultAudioLanguage']
    }
