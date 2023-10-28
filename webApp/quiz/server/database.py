from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environmetal variables
load_dotenv()

mongo_key = os.getenv("mongo_key")

# To connecting to mongodb Database
client =  MongoClient(mongo_key)
word_db = client.wotd.words


class Database:
    @staticmethod
    def get_words() -> list[str]:
        """
        Get words from database.

        Return:
            list of words that sends to a channel.
        """

        crawled_data = word_db.find()
        return [word["word"] for word in crawled_data]    

    @staticmethod 
    def get_meaning(word: str) -> str:
        """
        Get meaning a word.
        
        Args:
            word: a word that is used.
        Return
            meaning of the word.
        """
        word_meaning = word_db.find_one({"word":word})
        return word_meaning["meaning"]
    