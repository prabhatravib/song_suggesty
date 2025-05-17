# SongSuggest-YouTube

**SongSuggest** is a Flask web app that takes a **YouTube playlist** URL as input and returns an AI-generated song recommendation, complete with a link to the recommended video on YouTube.

## Features

- Accepts public YouTube playlist URLs  
- Retrieves playlist items via the YouTube Data API  
- Uses OpenAI’s ChatCompletion API to recommend a similar song  
- Returns a clickable link to the official video  
- Tracks usage analytics in a SQLite database  

## Setup

```bash
git clone https://github.com/yourusername/song_suggest_youtube.git
cd song_suggest_youtube
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
