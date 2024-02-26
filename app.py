from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv

import os

load_dotenv()


api_key = os.getenv("MISTRAL_API_KEY")
model = "open-mixtral-8x7b"

client = MistralClient(api_key=api_key)

messages = [
    ChatMessage(role="user", content="Daniel picks up the football. Daniel drops the newspaper. Daniel picks up the milk. John took the apple. What is Daniel holding?")
]

# No streaming
chat_response = client.chat(
    model=model,
    messages=messages,
)

print(chat_response.choices[0].message.content)