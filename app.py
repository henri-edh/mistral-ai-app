from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv

import os

load_dotenv()


api_key = os.getenv("MISTRAL_API_KEY")
model = "mistral-small-latest"

client = MistralClient(api_key=api_key)

messages = [
    ChatMessage(role="user", content="What is Machine Learning?")
]

# No streaming
chat_response = client.chat(
    model=model,
    messages=messages,
)

print(chat_response.choices[0].message.content)