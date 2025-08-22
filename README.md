# ai-response-bot-for-telegram by zealoffsky [Deprecated]

Overview
This Python program creates a Telegram chat bot powered by the OpenAI API to automatically respond to messages in a Telegram chat. 
The bot uses the GPT-3 language model to generate responses based on the your prompts (For example, answer for incoming messages like user). 
This readme provides instructions on how to set up and use the chat bot.

Installation:
1. Clone this repository to your local machine:

  git clone https://github.com/zealoffsky/OpenAI_Response_bot_For_Telegram.git

2. Navigate to the project directory:

  cd OpenAI_Response_bot_For_Telegram

3. Install the required Python packages using pip:

  pip install -r requirements.txt

Configuration:

API Credentials:
  Create .env file and input your Telegram API credentials (api_id and api_hash) and your OpenAI API key.
  example:
          api_id=your_telegram_api_id
          api_hash=your_telegram_api_hash
          openai_key=your_openai_api_key

GPT-3 Prompt File(Optional):
  You can enter your own prompts for GPT-3

Usage:
1. Run the bot:
     python main.py
   
2. The bot will prompt you to enter a your phone number for connecting Telegram. Enter your phone number and enter received code from Telegram

3. The bot will prompt you to enter a username or chat name in the Telegram. Enter the username or chat name of the user or group you want the bot to interact with.

4. The bot will connect to Telegram, fetch the chat history, and start monitoring for incoming messages.

5. When a message is received, the bot will use GPT-3 to generate a response based on the received message and the prompts in the prompts.txt file. It will then send the response back to the chat.

6.The bot will continue running and responding to messages until you manually stop it.

 



