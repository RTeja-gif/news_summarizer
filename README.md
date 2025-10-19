# Serverless News Summarizer

## Objective
Build a serverless function that takes a news article URL and returns a short summary using Hugging Face NLP API and AWS Lambda.

## How to Use
1. Open `demo.html` in a browser (or use local server with `python -m http.server 8000`).
2. Paste a news URL, e.g., `https://www.bbc.com/news/world-asia-67149306`.
3. Click **Summarize**.
4. The summary will appear below the button.

## API Endpoint

### Example curl
```bash
curl -X POST "https://boayfb3y69.execute-api.ap-south-1.amazonaws.com/default/news-summarizer" ^
-H "Content-Type: application/json" ^
-d "{\"url\":\"https://www.bbc.com/news/world-asia-67149306\"}"
