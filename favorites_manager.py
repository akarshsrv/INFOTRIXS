import json
import argparse

def load_favorites():
    try:
        with open("favorites.json", "r") as file:
            favorites = json.load(file)
    except FileNotFoundError:
        favorites = []
    return favorites

def save_favorites(favorites):
    with open("favorites.json", "w") as file:
        json.dump(favorites, file)

def add_favorite(city):
    favorites = load_favorites()
    if city not in favorites:
        favorites.append(city)
        save_favorites(favorites)
        print(f"{city} added to favorites.")
    else:
        print(f"{city} is already in your favorites list.")

def remove_favorite(city):
    favorites = load_favorites()
    if city in favorites:
        favorites.remove(city)
        save_favorites(favorites)
        print(f"{city} removed from favorites.")
    else:
        print(f"{city} is not in your favorites list.")

def list_favorites():
    favorites = load_favorites()
    if favorites:
        print("Your favorite cities:")
        for city in favorites:
            print(city)
    else:
        print("Your favorites list is empty.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Favorites Manager")
    parser.add_argument("action", choices=["add", "remove", "list"], help="Action to perform")

    if parser.parse_args().action == "list":
        list_favorites()
    else:
        city = input("Enter the city: ")
        if parser.parse_args().action == "add":
            add_favorite(city)
        elif parser.parse_args().action == "remove":
            remove_favorite(city)