from telethon.sync import TelegramClient, events
from settings import settings
import asyncio
import json
import os
import chat_bot


SESSION_NAME = "session"
DATA_PATH = 'data'
client = TelegramClient(SESSION_NAME, settings.api_id, settings.api_hash)
limit = 200


class ChatClient:

    def __init__(self):
        self.DATA_PATH = DATA_PATH

    async def get_dialog_history(self, entity):
        messages_data = []
        async for message in client.iter_messages(entity):
            message_data = {"sender_id": message.sender_id, "message": message.text}
            messages_data.insert(0, message_data)
            if len(messages_data) >= limit:
                break
        return messages_data

    def save_dialog_history(self, messages_data):
        os.makedirs('data', exist_ok=True)
        file_name = os.path.join(self.DATA_PATH, 'dialog.json')
        with open(file_name, 'w') as json_file:
            json.dump(messages_data, json_file, indent=4)


async def start_client():
    async with client:
        chat_client = ChatClient()
        user = await client.get_me()
        entity = await client.get_entity(input('Enter username:'))
        dialog = await chat_client.get_dialog_history(entity)

        if dialog:
            chat_client.save_dialog_history(dialog)

        @client.on(events.NewMessage())
        async def handle_message(event):

            response_id = event.message.from_id.user_id
            if response_id == entity.id:
                prompt = chat_bot.load_prompt_file(user.id)
                response = chat_bot.generate_response(event.message.text, prompt)
                print(response)
                await event.reply(response)

        await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(start_client())
