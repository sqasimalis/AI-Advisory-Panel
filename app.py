from os import getenv
from services import gemini, deepseek, llama

prompt = 'What do you know about python langugae?'

response_1 = gemini.get_response(prompt)
response_2 = deepseek.get_response(prompt)
response_3 = llama.get_response(prompt)

summary_prompt = 'Summarize the following response in 14 points: ' + response_1 + '\n\n' + response_2 + '\n\n' + response_3

final_response = gemini.get_response(summary_prompt)

print(final_response)