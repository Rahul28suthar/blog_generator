from openai import OpenAI

client = OpenAI(api_key="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")

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

print(generate_blog("BMW M4"))
