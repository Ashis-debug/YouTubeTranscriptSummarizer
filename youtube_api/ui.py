# ui.py

import streamlit as st

def render_ui():
    # UI setup and styles
    st.set_page_config(page_title="YouTube Transcript Summarizer", layout="centered")

    # Adding background image
    st.markdown("""
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0");
            background-size: cover;
            background-position: center;
        }
        body {
            color: #333333;
        }
        .main {
            background-color: rgba(255, 255, 255, 0.9);
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

    # Application title
    st.title("YouTube Transcript Summarizer and Question Generator")
