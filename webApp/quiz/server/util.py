from random import choice, shuffle

MAX_CHOICE = 4
MAX_QUIZ = 10

def random_choices(words:list[str], correct_choice:str):
    """
    Choose random choices from a given choices list.

    Args:
        words: words that are being selected.
        correct_choice: correct choice
    """
    words_list = list(words)
    words_list.remove(correct_choice)

    choices = [correct_choice]

    for word in range(MAX_CHOICE-1):
        if not words_list:
            break

        # Choose a random word from the list.
        word = choice(words_list)
        choices.append(word)
        words_list.remove(word)

    shuffle(choices)
    return choices

def random_words(words):
    """
    Choose random words from a given choices list.

    Args:
        words: words that are being selected.
    """
    quizes = []

    for word in range(MAX_QUIZ):
        if not words:
            break

        # Choose a random word from the list.
        word = choice(words)
        quizes.append(word)
        words.remove(word)

    shuffle(quizes)
    return quizes