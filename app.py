from os import getenv
from services import gemini, deepseek

prompt = 'What do you know about python langugae?'

# response_1 = gemini.get_response(prompt)
response_2 = deepseek.get_response(prompt)
print(response_2)