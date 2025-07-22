# Web-Summarizer

🧠 Webpage GPT Summarizer
This project is a Python-based tool that uses OpenAI's GPT-4o-mini model to scrape and summarize content from any website. It reads the main content of a web page (excluding navigation menus, scripts, styles, etc.), constructs a clean prompt, and sends it to GPT for summarization in natural language.

🚀 Features
✅ Scrapes any website using requests + BeautifulSoup

✅ Removes irrelevant elements like scripts, styles, and inputs

✅ Sends the content to OpenAI’s GPT-4o-mini model

✅ Returns a short and informative summary in markdown

✅ Easily extendable to support multiple URLs or models

✅ Can be executed directly from the command line

📦 Technologies Used
Python 3

OpenAI API

BeautifulSoup (for HTML parsing)

requests (for fetching web content)

python-dotenv (for securely loading API keys)

🛠️ How to Run
Clone the repo

git clone https://github.com/your-username/webpage-gpt-summarizer.git
cd webpage-gpt-summarizer
Install requirements


pip install -r requirements.txt
Add your OpenAI API Key to a .env file:


OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx
Run the summarizer


python webpage_gpt_summarizer.py
📌 Example Output
Website Title:
CNN - Breaking News, Latest News and Videos

GPT Summary of CNN:
CNN is a global news site featuring up-to-the-minute breaking news on politics, world affairs, health, tech, and more...
📂 Use Cases
Technical research summarization

News article digests

Competitive website monitoring

Educational summaries

