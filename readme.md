# YouTube Transcript Summarizer

Welcome to the **YouTube Transcript Summarizer**, a Streamlit application that leverages AI to extract, summarize, and generate questions from YouTube video transcripts. This project is designed to provide users with summaries, multiple-choice questions (MCQs), and detailed notes from the transcripts of YouTube videos. The application is built with Python and utilizes Google Generative AI for natural language processing tasks.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **YouTube Transcript Extraction:** Extract transcripts from YouTube videos using the `YouTubeTranscriptApi`.
- **AI-Powered Summarization:** Generate concise summaries, MCQs, and detailed notes using Google Generative AI.
- **Intuitive UI:** A user-friendly interface powered by Streamlit.
- **Modular Codebase:** Organized into multiple Python modules for better maintainability and scalability.

## Project Structure

```
NewYoutubeAPiTranscript/
│
├── .venv/                # Virtual environment (don't modify manually)
├── .env                  # Environment variables
├── .gitignore            # Git ignore file
├── Main.py               # Main Streamlit application file
├── requirements.txt      # Python dependencies
├── README.md             # Project readme
│
├── youtube_api/          # Directory for Python modules
│   ├── __init__.py       # Initialize the package
│   ├── youtube.py        # YouTube-related functionalities
│   ├── ai.py             # AI-related functionalities
│   ├── ui.py             # UI-related functionalities
│   └── utils.py          # Utility functions
```

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.8+**: Ensure that Python is installed on your system.
- **pip**: The Python package installer should be available.
- **Git**: For cloning the repository.
- **Google Generative AI API Key**: Sign up for access to the API and get your API key from [Google Cloud Console](https://console.cloud.google.com/).

## Installation

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

Open a terminal and execute the following command to clone the repository:

```bash
git clone https://github.com/Ashis-debug/YouTubeTranscriptSummarizer.git
cd YouTubeTranscriptSummarizer
```

### 2. Set Up the Virtual Environment

Create a virtual environment to isolate your dependencies:

```bash
python -m venv .venv
```

Activate the virtual environment:

- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies

Install all the necessary Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your Google Generative AI API key:

```plaintext
GENAI_API_KEY=YOUR_ACTUAL_API_KEY_HERE
```

> **Note:** Make sure to replace `YOUR_ACTUAL_API_KEY_HERE` with your actual API key.

## Running the Application

Once you have completed the installation steps, you can run the Streamlit application using the following command:

```bash
streamlit run Main.py
```

After executing this command, your default web browser should open automatically, displaying the application interface. If it doesn't open automatically, you can manually navigate to `http://localhost:8501` in your web browser.

## Usage

1. **Enter a YouTube Video URL**: Paste the URL of the YouTube video you wish to analyze into the input field.
   
2. **Select an Option**:
   - **Summary**: Get a concise summary of the video transcript.
   - **MCQ Questions**: Generate multiple-choice questions based on the video content.
   - **Complete Notes**: Receive detailed notes from the video transcript.

3. **Submit**: Click the **Submit** button to process the video and receive the desired output.

4. **View Results**: The application will display the requested information, whether it's a summary, MCQs, or notes, depending on your selection.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request.

### Steps to Contribute:

1. **Fork the Repository**: Create a personal fork of the repository on GitHub.
   
2. **Clone the Fork**: Clone your forked repository to your local machine.

   ```bash
   git clone https://github.com/YOUR_USERNAME/YouTubeTranscriptSummarizer.git
   ```

3. **Create a New Branch**: Make sure you’re working in a new branch, specific to the feature or fix you're working on.

   ```bash
   git checkout -b feature-or-fix-name
   ```

4. **Make Changes**: Implement your changes or new features.

5. **Test Your Changes**: Run the application to make sure everything works as expected.

6. **Commit and Push**: Commit your changes and push them to your fork.

   ```bash
   git commit -m "Add brief description of your changes"
   git push origin feature-or-fix-name
   ```

7. **Submit a Pull Request**: Go to the original repository and submit a pull request from your fork.


## Contact

If you have any questions, feel free to reach out to me via [LinkedIn](https://www.linkedin.com/in/ashis-tripathy-337030218/) or open an issue on GitHub.
