from telegram.ext import ContextTypes
from telegram import  ReplyKeyboardMarkup, WebAppInfo, KeyboardButton
from telegram import Update
from json import load
from dotenv import load_dotenv
from helpers import buttons
import os

load_dotenv()

image = os.getenv("start_image")

# Load text from json file
with open("helpers/button_text/text.json", "r+") as file:
    text = load(file)

async def start(
        update:Update, 
        context:ContextTypes.DEFAULT_TYPE):
    """
    Start command handler.
    """

    user_id = update.message.chat_id
    start_text = text.get("start")

    # Send start message
    await context.bot.send_photo(user_id, 
                                 image,
                                 caption=start_text, 
                                 parse_mode="MarkdownV2", 
                                 reply_markup=buttons.start)
