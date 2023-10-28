from telegram.ext import ContextTypes
from telegram import Update
from json import load
from dotenv import load_dotenv
from helpers import Database
import os

# Load text from json file
with open("helpers/button_text/text.json", "r+") as file:
    text = load(file)

async def info(
        update:Update, 
        context:ContextTypes.DEFAULT_TYPE):
    """
    More info message handler.
    """
    
    word = (update.message.text.split("_")[-1])

    # Retrieve word info from database
    word_info = Database.get_info(word)

    user_id = update.message.chat_id

    info_text = text.get("info").format(word_info.get("context"), word_info.get("facts"))

    # Send info message
    await context.bot.send_message(
        chat_id=user_id,
        text=info_text,
        parse_mode="Html"
    )

