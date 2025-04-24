from os import getenv
from services import gemini

prompt = 'What do you know about python langugae?'

response_1 = gemini.get_response(prompt)
print(response_1)