import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound  # Updated import
from langdetect import detect
from googletrans import Translator

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the Translator
translator = Translator()

# Summarization prompt template
prompt_template = """
You are a YouTube video summarizer. Summarize the following transcript within 500 words. Transcript: 
"""

# CSS for a professional look
st.markdown("""
    <style>
        /* General Styling */
        body {
            background-color: #f4f4f9;
            color: #333;
        }
        
        /* Header Styling */
        .header {
            font-size: 3em;
            color: #DAA520; /* Goldenrod color */
            text-align: center;
            padding: 1em;
            font-weight: bold;
            border-bottom: 2px solid #DAA520;
        }
        
        /* Button Styling */
        .stButton > button {
            background-color: #1abc9c;
            color: #ffffff;
            border: None;
            font-size: 1.2em;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background-color: #16a085;
        }

        /* Sidebar Styling */
        .sidebar .sidebar-content {
            background-color: #ecf0f1;
            padding: 10px;
        }

        /* Footer Styling */
        .footer {
            text-align: center;
            color: #7f8c8d;
            font-size: 0.9em;
            padding: 2em 0 1em;
        }

        /* Input Box Styling */
        .stTextInput > div > input {
            background-color: #ecf0f1;
            font-size: 1.1em;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# Function to extract transcript from YouTube with enhanced error handling
def extract_transcript_details(youtube_video_url):
    try:
        # Extract the video ID from different types of YouTube URLs
        if "youtube.com" in youtube_video_url:
            video_id = youtube_video_url.split("v=")[1].split("&")[0]
        elif "youtu.be" in youtube_video_url:
            video_id = youtube_video_url.split("/")[-1]
        else:
            st.error("Invalid YouTube link format.")
            return None
        
        # Attempt to get the transcript in Hindi first
        try:
            transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=['hi', 'en'])
        except NoTranscriptFound:
            st.error("No Hindi transcript found. Trying to get English transcript...")
            transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

        # Combine the transcript text
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Function to detect language
def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

# Function to generate summary
def generate_summary(content, language):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt_template + content)
    summary = response.text

    # Translate the summary if needed
    if language == "en":
        hindi_summary = translator.translate(summary, src='en', dest='hi').text
        return summary, hindi_summary
    elif language == "hi":
        english_summary = translator.translate(summary, src='hi', dest='en').text
        return english_summary, summary

# Layout and Instructions
st.markdown("<div class='header'>📜 YouTube QuickNotes </div>", unsafe_allow_html=True)
st.write("**Generate professional notes from YouTube videos in both English and Hindi**. Use this tool for quick summaries, insights, and more! 🎥")
st.sidebar.title("🚀 Getting Started")
st.sidebar.write("""
1. Copy the YouTube video link and paste it in the field below.
2. Hit **Generate Notes** for a dual-language summary.
3. VIEW, READ, and COPY your personalized notes instantly! 📋
""")


# Input for YouTube link
youtube_link = st.text_input("Enter YouTube Video Link:", placeholder="e.g., https://www.youtube.com/watch?v=abc123")

# Processing the video link
if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

    if st.button("📝 Generate Notes", help="Get your detailed notes in English and Hindi"):
        with st.spinner("Summarizing... Please wait"):
            transcript_text = extract_transcript_details(youtube_link)
            
            if transcript_text:
                detected_language = detect_language(transcript_text)
                
                # Generate summary based on the detected language
                if detected_language == "en":
                    english_summary, hindi_summary = generate_summary(transcript_text, "en")
                elif detected_language == "hi":
                    english_summary, hindi_summary = generate_summary(transcript_text, "hi")
                else:
                    st.error("Unable to detect transcript language or unsupported language.")
                    english_summary, hindi_summary = None, None
                
                # Display summaries
                if english_summary and hindi_summary:
                    st.markdown("### 📄 English Summary")
                    st.write(english_summary)
                    st.markdown("### 📄 Hindi Summary")
                    st.write(hindi_summary)

#Footer
st.markdown("<div class='footer'>© 2024 QuickNotes by Mayur Satpute - All Rights Reserved 🌐</div>", unsafe_allow_html=True)
