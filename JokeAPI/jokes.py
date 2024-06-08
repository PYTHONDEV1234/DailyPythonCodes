from data import load_jokes, save_jokes

def find_joke(joke_id):
    jokes = load_jokes()
    return next((joke for joke in jokes if joke["id"] == joke_id), None)

def get_all_jokes():
    return load_jokes()

def add_joke(new_joke):
    jokes = load_jokes()
    new_joke["id"] = jokes[-1]["id"] + 1 if jokes else 1
    jokes.append(new_joke)
    save_jokes(jokes)
    return new_joke

def update_joke(joke_id, updated_joke):
    jokes = load_jokes()
    joke = find_joke(joke_id)
    if joke:
        joke["joke"] = updated_joke.get("joke", joke["joke"])
        save_jokes(jokes)
    return joke

def delete_joke(joke_id):
    jokes = load_jokes()
    joke = find_joke(joke_id)
    if joke:
        jokes.remove(joke)
        save_jokes(jokes)
    return joke
