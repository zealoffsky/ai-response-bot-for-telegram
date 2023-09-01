"""GPT for generating responses"""
import json
import openai
from settings import settings

DIALOG_PATH = 'data/dialog.json'
PROMPT_PATH = 'prompt.txt'


def load_prompt_file(response_id):
    """Loads prompt file and insert messages into it"""
    with open(DIALOG_PATH, encoding="utf-8") as dialog_file:
        dialog_messages = json.load(dialog_file)

    with open(PROMPT_PATH, encoding="utf-8") as prompt_file:
        prompt = prompt_file.read()

    formatted_messages = "\n".join(
        f"Sender ID: {message['sender_id']}, Message: {message['message']}"
        for message in dialog_messages
    )

    result = f"{prompt}\n{formatted_messages}\nall messages that have id {response_id}" \
             f" is mine, analyse them and write response messages like them"

    return result


def generate_response(message, prompt):
    """Generating response using GPT"""
    openai.api_key = settings.openai_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt},
                  {"role": "user", "content": message}],
        temperature=0.8,
        max_tokens=400,
    )

    answer = response["choices"][0]["message"]["content"]
    return answer
