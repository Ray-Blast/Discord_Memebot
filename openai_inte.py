import os
import openai

openai.api_key = os.getenv("OPENAI_KEY")
temperature = 0
max_tokens = 1024

def generate_response(prompt):

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f'Q: {prompt}\nA:',
        max_tokens=1024,
        temperature=0.7,
    )
    return response.choices[0].text.strip()