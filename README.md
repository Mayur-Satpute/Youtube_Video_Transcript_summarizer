# YouTube QuickNotes

📜 **Generate professional notes from YouTube videos in both English and Hindi!** This tool helps you summarize YouTube video transcripts quickly and efficiently. 

---

## Features

- Extract transcripts from YouTube videos in Hindi and English.
- Summarize transcripts into easy-to-read notes.
- Dual-language summaries: English and Hindi.
- Simple and user-friendly Streamlit interface.

---

## Requirements

Make sure you have the following installed:

- **Python 3.7 or later**
- Required Python libraries (see `requirements.txt`):
  - `youtube_transcript_api`
  - `streamlit`
  - `google-generativeai`
  - `python-dotenv`
  - `pathlib`
  - `langdetect`
  - `googletrans==4.0.0-rc1`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your `.env` file:
   - Add your **Google API Key**:
     ```plaintext
     GOOGLE_API_KEY="your-google-api-key"
     ```

---

## How to Use

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the provided local URL in your browser.

3. Paste the YouTube video link in the input field.

4. Click **"Generate Notes"** to get summaries in English and Hindi.

---

## Screenshots
![image alt](https://github.com/Mayur-Satpute/Youtube_Video_Transcript_summarizer/blob/main/Screenshot%20(10).png?raw=true)
![image alt](https://github.com/Mayur-Satpute/Youtube_Video_Transcript_summarizer/blob/main/Screenshot%20(11).png?raw=true)
![image alt](https://github.com/Mayur-Satpute/Youtube_Video_Transcript_summarizer/blob/main/Screenshot%20(10).png?raw=true)
![image alt](https://github.com/Mayur-Satpute/Youtube_Video_Transcript_summarizer/blob/main/Screenshot%20(10).png?raw=true)
---

## Notes

- Make sure the YouTube video has available transcripts in English or Hindi.
- If the video has no transcript, the app will display an error message.

---

## License

© 2025 QuickNotes by Mayur Satpute - All Rights Reserved 🌐
