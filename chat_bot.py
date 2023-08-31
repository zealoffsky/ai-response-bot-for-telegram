import openai
from settings import settings
import json



class Chat_bot():

    def __int__(self):
        openai.api_key = settings.openai_key

    def load_prompt_file(self, response_id):
        with open("data/dialog.json", "r", encoding='utf-8') as json_file:
            json_parsed = json.load(json_file)
            formatted_messages = "\n".join(
                f"Sender ID: {message['sender_id']}, Message: {message['message']}"
                for message in json_parsed
            )

        with open("prompt.txt", "r", encoding="utf-8") as prompt_file:
            prompt = prompt_file.read() + "\n" + f"{formatted_messages}" + "\n" + f"all messages that have id {response_id} is mine, analyse them and write response messages like them "
        return prompt

    def generate_response(self, message, prompt):
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

chat_bot = Chat_bot()