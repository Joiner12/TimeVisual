# -*- coding:utf-8 -*-
from openai import OpenAI

api_key = "sk-MHsqURJak3XEGYiYv3PSWC5v1UqqwyJASf7dMWqyxGig2u1K"
base_url = "https://api.chatanywhere.tech"

client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key,
    base_url=base_url,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)
print(chat_completion.choices[0].message)
