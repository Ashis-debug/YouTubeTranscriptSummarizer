import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import re

# Configure Google Generative AI API
API_KEY = "AIzaSyDcLJiSbmkhZAmb2wfq4h5PPHU6lPCPysU"
genai.configure(api_key=API_KEY)


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
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    message = " ".join([text['text'] for text in transcript])
    return message


def generate_summary(prompt, message):
    """
    Generate summary or questions using Google Generative AI.
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt + "\n" + message)
    return response.text


st.set_page_config(page_title="YouTube Transcript Summarizer", layout="centered")

st.title("YouTube Transcript Summarizer and Question Generator Please Add 15-20 Minutes video URL for better results")
st.markdown("""
<style>
body {
    background-color: #f0f2f6;
    color: #333333;
}
.main {
    background-color: #ffffff;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
h1 {
    color: #4CAF50;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}
.stButton>button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)

youtube_url = st.text_input("Enter YouTube Video URL:", "")
if st.button("Generate Transcript and Questions"):
    if youtube_url:
        video_id = extract_video_id(youtube_url)
        if video_id:
            with st.spinner('Fetching transcript...'):
                try:
                    transcript = get_youtube_transcript(video_id)
                    st.success("Transcript fetched successfully!")

                    prompt_summary = "act as a summarizer and write the summary in points for the input with 250 words"
                    prompt_questions = "act as a summarizer and write some MCQ questions based on the input given"

                    with st.spinner('Generating summary...'):
                        summary = generate_summary(prompt_summary, transcript)
                        st.subheader("Summary")
                        st.write(summary)

                    with st.spinner('Generating questions...'):
                        questions = generate_summary(prompt_questions, transcript)
                        st.subheader("MCQ Questions")
                        st.write(questions)
                except Exception as e:
                    st.error(f"Error fetching transcript: {e}")
        else:
            st.warning("Invalid YouTube URL. Please enter a valid URL.")
    else:
        st.warning("Please enter a YouTube video URL.")
