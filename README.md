# Serverless News Summarizer

## Objective
Build a serverless function that takes a news article URL and returns a short summary using Hugging Face NLP API and AWS Lambda.

## Live Demo
Open this URL in a browser: [Live Demo](https://rteja-gif.github.io/news_summarizer/)  
Paste a news article URL, e.g., https://www.bbc.com/news/world-asia-67149306.  
Click **Summarize** → The summary will appear below the button.

## How to Use
1. Open the live demo link above.  
2. Paste any news article URL in the input box.  
3. Click **Summarize**.  
4. The summary will appear below the button instantly.

## API Endpoint

### Example curl
```bash
curl -X POST "https://boayfb3y69.execute-api.ap-south-1.amazonaws.com/default/news-summarizer" \
-H "Content-Type: application/json" \
-d '{"url":"https://www.bbc.com/news/world-asia-67149306"}'
