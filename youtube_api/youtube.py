# youtube.py
import re
import requests
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


def get_video_detail(videoID):
    # access the API
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details?"
    headers = {
        'x-rapidapi-key': "ce8371e650mshe45717dee95c8a8p1a0b57jsn195433104778",
        'x-rapidapi-host': "youtube-media-downloader.p.rapidapi.com"
    }
    # send a get request to the API
    querystring = {"videoId": videoID}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # conver the response to json format
    json_response = response.json()
    # obtain the subtitle url (in XML format)
    subtitleURL = json_response['subtitles']['items'][0]['url']

    return subtitleURL


def get_subtitle_text(subtitleUrl):
    # access the API
    url = "https://youtube-media-downloader.p.rapidapi.com//v2/video/subtitles?format=json&targetLang=en"
    headers = {
        'x-rapidapi-key': "ce8371e650mshe45717dee95c8a8p1a0b57jsn195433104778",
        'x-rapidapi-host': "youtube-media-downloader.p.rapidapi.com"
    }
    # send a get subtitle text request to the API
    querystring = {"subtitleUrl": subtitleUrl}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # return the text response
    try:
        transcript = response.json()
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
