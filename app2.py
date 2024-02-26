#!/usr/bin/env python
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    api_key = os.getenv("MISTRAL_API_KEY")
    model1 = "mistral-medium-latest"

    client1 = MistralClient(api_key=api_key)

    #model2 = "mistral-large-latest"
    model2 = "open-mixtral-8x7b"
    client2 = MistralClient(api_key=api_key)

    list_models_response = client1.list_models()

    # Your initial message/query to the LLM
    '''initial_messages = [
        ChatMessage(role="user", content="Please provide information on....")
    ]
    
    
    # First request to get information
    initial_response = client.chat(
        model=model,
        messages=initial_messages,
    )
    initial_response_content = initial_response.choices[0].message.content
'''
    initial_response_content = list_models_response

    # Second request to format the response in Markdown
    markdown_messages = [
        ChatMessage(role="user", content=f"Format the following in Markdown: \n{initial_response_content}")
    ]

    markdown_response = client2.chat(
        model=model2,
        messages=markdown_messages,
    )

    # Print the Markdown formatted content
    print(markdown_response.choices[0].message.content)

if __name__ == "__main__":
    main()
