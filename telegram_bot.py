#Firstly, looking into cleaning up code by removing any unused or commented out lines

import telegram
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up the Telegram bot
bot = telegram.Bot('6088146021:AAHzfrDc53rGBsc9HOzNP0gxNUvzTmdSzEM')

# Set up the OpenAI API
openai.api_key = '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'

# Define a function to generate responses using ChatGPT
def generate_response(text):
    response = openai.Completion.create(
        engine='davinci',
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm your personal AI assistant. How can I help you today?")

def echo(update, context):
    user_input = update.message.text
    response = generate_response(user_input)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def main():
    updater = Updater('6088146021:AAHzfrDc53rGBsc9HOzNP0gxNUvzTmdSzEM', use_context=True)
    dispatcher = updater.dispatcher

    # Add handlers for start command and echo message
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

#Keep your own API Keys & tokens secure - don't hardcode them into your scripts; use env variables or a configuration file.
#As an example the 'os' module to read the keys from enviroment variables

import os
bot.token = os.environ['TELEGRAM_BOT_TOKEN']
openai_api_key = os.environ['OPENAI_API_KEY']
