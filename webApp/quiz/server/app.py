from flask import Flask, request, jsonify
from flask_cors import CORS
from util import random_choices, random_words
from database import Database
from random import choice

app = Flask(__name__)

# Cors 
CORS(app)

@app.route("/quizes")
def quizes():
    # Generate random words
    words_list = random_words(list(Database.get_words()))

    title = "Vocabulary Quiz"
    
    # Empty list that generated quizes save later
    quizes = []

    for word in words_list:
        # Retrieve the meaning of a word from database
        word_meaning = str(Database.get_meaning(word)).split(".")[0]

        question = ((word_meaning.lower()).replace(word, f"{'_' * 5} ")).capitalize()

        # Generate random options for a specific question
        choices = random_choices(words_list, word)

        quiz = {"correct-option": word,
                "question-text": question, 
                "question-image": None,
                "options": choices,
                "description":word_meaning, 
                "time":30}
        quizes.append(quiz)

    
    return {"title": title, "questions": quizes}


if __name__ == "__main__":
    # Run flask app
    app.run()