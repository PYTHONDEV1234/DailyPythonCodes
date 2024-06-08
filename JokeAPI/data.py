import json

JOKE_FILE = 'jokes.txt'

def load_jokes():
    try:
        with open(JOKE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_jokes(jokes):
    with open(JOKE_FILE, 'w') as file:
        json.dump(jokes, file, indent=4)
