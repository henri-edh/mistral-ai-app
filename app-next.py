import requests
from dotenv import load_dotenv

import os

load_dotenv()

# Define your Mistral API key
api_key = os.getenv("MISTRAL_API_KEY")

# Endpoint for chat completions
chat_endpoint = "https://api.mistral.ai/v1/chat/completions"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {api_key}'
}
data = {
    "model": "mistral-small-latest",
    "messages": [{"role": "user", "content": "Daniel picks up the football. Daniel drops the newspaper. Daniel picks up the milk. John took the apple. What is Daniel holding?"}]
}

# Make a POST request to get chat completions
response = requests.post(chat_endpoint, headers=headers, json=data)

# Process the response as needed
print(response.json())