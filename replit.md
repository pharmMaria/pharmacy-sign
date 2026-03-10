# 약국 매대 안내문 자동 생성기

A Streamlit web app that uses Google Gemini AI to generate pharmacy product label descriptions in Korean.

## Architecture

- **Framework**: Streamlit (Python)
- **AI**: Google Gemini (`gemini-2.5-flash`) via `google-generativeai`
- **Port**: 5000

## Project Structure

- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `.streamlit/config.toml` - Streamlit server config (port 5000, host 0.0.0.0)

## Environment Variables

- `GEMINI_API_KEY` - Google Gemini API key (required, stored as Replit secret)

## Running

The app runs via the "Start application" workflow:
```
streamlit run app.py
```

## Features

- Enter a pharmacy product name to generate a label
- Looks up average price from a mock database
- Uses Gemini AI to generate product category and recommendation text
