import requests
from config import TRELLO_KEY, TRELLO_TOKEN

def get_user_boards():
    url = "https://api.trello.com/1/members/me/boards"
    params = {
        "key": TRELLO_KEY,
        "token": TRELLO_TOKEN,
        "fields": "name"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def get_board_lists(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    params = {"key": TRELLO_KEY, "token": TRELLO_TOKEN}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def get_list_cards(list_id):
    url = f"https://api.trello.com/1/lists/{list_id}/cards"
    params = {"key": TRELLO_KEY, "token": TRELLO_TOKEN}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
