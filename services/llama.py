from os import getenv
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def get_response(prompt):
    client = Groq(api_key=getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ]
    )

    return response.choices[0].message.content