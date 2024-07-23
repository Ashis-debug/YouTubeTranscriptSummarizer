# youtube.py

import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
)

def extract_video_id(youtube_url):
    """
    Extract the video ID from a YouTube URL.
    """
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, youtube_url)
    if match:
        return match.group(1)
    return None

def get_youtube_transcript(video_id):
    """
    Get the transcript of a YouTube video using its video ID.
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        message = " ".join([text['text'] for text in transcript])
        return message
    except VideoUnavailable:
        return "The video is unavailable."
    except TranscriptsDisabled:
        return "Transcripts are disabled for this video."
    except NoTranscriptFound:
        return "No transcript is found for the given video."
    except Exception as e:
        return f"An error occurred: {str(e)}"
