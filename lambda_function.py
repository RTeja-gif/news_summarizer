import json
import os
import requests
from bs4 import BeautifulSoup

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
HUGGINGFACE_API_TOKEN = os.getenv("HF_API_TOKEN")

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        url = body.get('url')
        if not url:
            return {"statusCode": 400, "body": json.dumps({"error": "Missing 'url' in request"})}

        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            return {"statusCode": 400, "body": json.dumps({"error": "Failed to fetch article"})}

        soup = BeautifulSoup(resp.text, "html.parser")
        paragraphs = soup.find_all('p')
        article_text = ' '.join([p.get_text() for p in paragraphs])[:4000]

        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
        response = requests.post(HUGGINGFACE_API_URL, headers=headers, json={"inputs": article_text})
        summary_result = response.json()

        summary_text = summary_result[0]['summary_text'] if isinstance(summary_result, list) else "Summary failed"

        return {"statusCode": 200, "body": json.dumps({"summary": summary_text})}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
