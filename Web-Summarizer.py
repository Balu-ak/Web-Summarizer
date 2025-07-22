import os
import requests
import json
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from openai import OpenAI

# ------------------------------
# Load environment variables
# ------------------------------

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

# ------------------------------
# Check API Key
# ------------------------------

if not api_key:
    print("No API key was found - please set OPENAI_API_KEY in your .env file.")
elif not api_key.startswith("sk-proj-"):
    print("The API key format looks incorrect.")
elif api_key.strip() != api_key:
    print("API key has leading/trailing whitespace.")
else:
    print("API key found and looks good.")

# ------------------------------
# Initialize OpenAI client
# ------------------------------

openai = OpenAI(api_key=api_key)

# ------------------------------
# Send a test message to GPT
# ------------------------------

message = "Hello, GPT! This is my first ever message to you! Hi!"
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": message}]
)
print("\nGPT Test Response:")
print(response.choices[0].message.content)

# ------------------------------
# Set headers for web scraping
# ------------------------------

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# ------------------------------
# Define Website class to scrape and clean HTML
# ------------------------------

class Website:
    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

# ------------------------------
# Create Website instance for CNN
# ------------------------------

cnn = Website("https://cnn.com")
print("\nWebsite Title:")
print(cnn.title)
print("\nWebsite Text Snippet:")
print(cnn.text[:500])  # Print only the first 500 chars for brevity

# ------------------------------
# Define prompt structure for GPT
# ------------------------------

system_prompt = (
    "You are an assistant that has over 20 years of experience in analyzing the contents of a website "
    "and provides a short summary, ignoring text that might be navigation related. "
    "Respond in markdown."
)

def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; "
    user_prompt += "please provide a short summary of this website in markdown. "
    user_prompt += "If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

# ------------------------------
# Test basic GPT interaction
# ------------------------------

messages = [
    {"role": "system", "content": "You are a snarky assistant"},
    {"role": "user", "content": "What is 2 + 2?"}
]
response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
print("\nSnarky GPT Response:")
print(response.choices[0].message.content)

# ------------------------------
# Format messages for GPT summary
# ------------------------------

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

# ------------------------------
# Summarize a given URL using GPT
# ------------------------------

def summarize(url):
    website = Website(url)
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages_for(website)
    )
    return response.choices[0].message.content

# Run summary for CNN
summary = summarize("https://cnn.com")
print("\nGPT Summary of CNN:")
print(summary)

# ------------------------------
# Display summary (Notebook-only feature)
# ------------------------------
# Note: Markdown display is not usable in plain .py scripts,
# so we just print it to terminal.
