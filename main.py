from telethon.sync import TelegramClient, events
from settings import settings
import asyncio
import json
import os
from chat_bot import chat_bot

client = TelegramClient('session', settings.api_id, settings.api_hash)
limit = 200
data_folder = 'data'

async def main():
    async with client:
        global user
        user = await client.get_me()
        global entity
        entity = await client.get_entity(input('Enter username:'))

        dialog = await get_dialog_history(entity)

        if dialog:
            save_dialog_history(dialog)

        await client.run_until_disconnected()


async def get_dialog_history(entity):
    messages_data = []
    async for message in client.iter_messages(entity):
        message_data = {"sender_id": message.sender_id, "message": message.text}
        messages_data.append(message_data)
        if len(messages_data) >= limit:
            break
    return messages_data


def save_dialog_history(messages_data):
    os.makedirs('data', exist_ok=True)
    file_name = os.path.join(data_folder, 'dialog.json')
    with open(file_name, 'w') as json_file:
        json.dump(messages_data, json_file, indent=4)


@client.on(events.NewMessage())
async def handle_message(event):
    global entity
    global user
    response_id = event.message.from_id.user_id
    if response_id == entity.id:
        prompt = chat_bot.load_prompt_file(user.id)
        response = chat_bot.generate_response(event.message.text, prompt)
        print(response)
        await event.reply(response)


if __name__ == '__main__':
    asyncio.run(main())
