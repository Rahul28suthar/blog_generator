from dotenv import load_dotenv
import os
from openai import OpenAI

config = load_dotenv('.env')

openai.api_key = config['API_KEY']

def generate_blog(paragraph_topic):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful blog writer."},
            {"role": "user", "content": f"Write a blog about the following topic: {paragraph_topic}"}
        ],
        max_tokens=500,
        temperature=0.4,
    )
    return response.choices[0].message.content.strip()

print(generate_blog("BMW M4")) # can write any topic you like
