from telegram import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
import os
from dotenv import load_dotenv

load_dotenv()

web_app_url = os.getenv("web_app_url")

# start button
start  = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Take vocabulary Quiz", web_app=WebAppInfo(web_app_url)),
        ]
    ], resize_keyboard=True
)
