# Main.py

import streamlit as st
from youtube_api.youtube import extract_video_id, get_youtube_transcript
from youtube_api.ai import generate_summary
from youtube_api.ui import render_ui
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Load API key
API_KEY = os.getenv('GENAI_API_KEY')

if API_KEY is None:
    st.error("Please set the API key in the environment variable 'GENAI_API_KEY'")
else:
    import google.generativeai as genai
    genai.configure(api_key=API_KEY)

# Render UI
render_ui()

# Application Logic
def run_app():
    # Input for YouTube URL
    youtube_url = st.text_input("Enter YouTube Video URL:", "")

    # Options for user selection
    option_summary = st.checkbox("Do you want the summary of the video?", key="summary")
    option_mcq = st.checkbox("Do you want some MCQ questions related to the video?", key="mcq")
    option_notes = st.checkbox("Do you want the complete notes of the video?", key="notes")

    # Submit button
    submit = st.button("Submit")

    if submit:
        if youtube_url:
            video_id = extract_video_id(youtube_url)
            if video_id:
                transcript = get_youtube_transcript(video_id)

                if option_summary + option_mcq + option_notes > 1:
                    st.error("Please select only one option at a time.")
                elif option_summary + option_mcq + option_notes == 0:
                    st.info("Select an option to proceed.")
                else:
                    if option_summary:
                        prompt_summary = "Act as a summarizer and write the summary as a paragraph for the input with at least 500 words"
                        with st.spinner('Generating summary...'):
                            summary = generate_summary(prompt_summary, transcript)
                            st.subheader("Summary")
                            st.write(summary)

                    if option_mcq:
                        prompt_questions = "Act as a summarizer and write 20-25 MCQ questions based on the input given"
                        with st.spinner('Generating MCQ questions...'):
                            questions = generate_summary(prompt_questions, transcript)
                            st.subheader("MCQ Questions")
                            st.write(questions)

                    if option_notes:
                        prompt_notes = "Act as a summarizer and write detailed handwritten notes based on the input given."
                        with st.spinner('Generating notes...'):
                            notes = generate_summary(prompt_notes, transcript)
                            st.subheader("Complete Notes")
                            st.write(notes)
            else:
                st.warning("Invalid YouTube URL. Please enter a valid URL.")
        else:
            st.warning("Please enter a YouTube video URL.")

if __name__ == "__main__":
    run_app()
