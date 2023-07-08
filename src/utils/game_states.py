from json import load as json_load, dump as json_dump, JSONDecodeError

SAVE_FILE_PATH = "./save.json"


def save_game(player_json):
    try:
        with open(SAVE_FILE_PATH, "w") as file:
            json_dump(player_json, file)
    except IOError:
        return False


def load_game():
    try:
        with open(SAVE_FILE_PATH, "r") as file:
            return json_load(file)
    except FileNotFoundError:
        return False
    except JSONDecodeError:
        return False
