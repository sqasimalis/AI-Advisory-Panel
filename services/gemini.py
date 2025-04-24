from os import getenv
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_response(prompt):
    client = OpenAI(
        api_key=getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        n=1,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ]
    )

    return response.choices[0].message.content