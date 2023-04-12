'''This module is what handles all of the OpenAI integration. Responsible for communicating with the API and returning an appropiate response'''
import os
import openai

openai.api_key = os.getenv("OPENAI_KEY")
ai_temperature = 0.7
ai_max_tokens = 1024



def answer_question(prompt):
    '''This function generates a response in a QnA format'''
    response = openai.ChatCompletion.create(
        engine="gpt-3.5-turbo",
        prompt=f"Q: {prompt}\nA:",
        max_tokens = ai_max_tokens,
        temperature = ai_temperature,
    )
    return response.choices[0].text.strip()
