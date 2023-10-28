import os
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, MessageHandler, filters
from telegram.ext._applicationbuilder import InitApplicationBuilder
from dotenv import load_dotenv

# Import handlers that help handle incoming messages
from handlers.start import start
from handlers.info import info

load_dotenv()

bot_token = os.getenv("bot_token")

class Bot(ApplicationBuilder):
     """
     Main class for building the application and add handlers.
     Args: 
         bot_token: telegram bot token
     Return:
         None
     """  
    
     def __init__(self: InitApplicationBuilder, bot_token:str):
          self.bot_token = bot_token
          super().__init__()  
          
     def tokenize(self):
          """
          Add token.
          """
          super().token(self.bot_token) 

     def builder(self):
          """
          Build.
          """
          self.builder = super().build()     

     def add_handlers(self):
          """
          Add message handlers.
          """
          self.builder.add_handler(MessageHandler(filters.Regex("^/start$"), start))  
          self.builder.add_handler(MessageHandler(filters.Regex("word_"), info))

     def run(self):
          """
          Run the bot.
          """
          self.tokenize()
          self.builder()
          self.add_handlers()
          self.builder.run_polling()
     
# If the the script run from terminal
if __name__ == "__main__":
    Bot(bot_token).run()