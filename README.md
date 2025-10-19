\# Serverless News Summarizer



\## Objective

AWS Lambda function to summarize news articles using Hugging Face free API.



\## Setup

1\. Create AWS Lambda function (Python 3.11)

2\. Add API Gateway (POST method)

3\. Paste code from lambda\_function.py

4\. Set Hugging Face API token

5\. Deploy and test



\## Usage

curl -X POST https://<your-api-endpoint> -H "Content-Type: application/json" -d '{"url":"<news\_url>"}'



\## Challenges

\- Extracting text cleanly from HTML required BeautifulSoup

\- Limited input size for API, trimmed to 4000 characters



\## AI Tool Usage

\- Hugging Face API used for summarization



