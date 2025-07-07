from dotenv import load_dotenv
from googleapiclient.discovery import build
import os

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
        "duration": details['duration'],
        "thumbnail": snippet['thumbnails'],
        "created": snippet['publishedAt'],
        "likes": int(stats['likeCount']),
        "views": int(stats['viewCount']),
        "language": snippet['defaultAudioLanguage']
    }