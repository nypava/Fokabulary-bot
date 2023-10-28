from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load environmetal variables
load_dotenv()

mongo_key = os.getenv("mongo_key")

client =  MongoClient(mongo_key)
word_db = client.wotd.words

class Database:
    @staticmethod
    def get_info(word:str) -> list[str]:
        """
        Get detail info about a word.

        Return:
            list of detailed info about the word. 
        """
        return word_db.find_one({"word":word})
        