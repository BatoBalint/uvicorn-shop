import json
from typing import Dict, Any

'''
Útmutató a fájl függvényeinek a használatához

Új felhasználó hozzáadása:

new_user = {
    "id": 4,  # Egyedi felhasználó azonosító
    "name": "Szilvás Szabolcs",
    "email": "szabolcs@plumworld.com"
}

Felhasználó hozzáadása a JSON fájlhoz:

add_user(new_user)

Hozzáadunk egy új kosarat egy meglévő felhasználóhoz:

new_basket = {
    "id": 104,  # Egyedi kosár azonosító
    "user_id": 2,  # Az a felhasználó, akihez a kosár tartozik
    "items": []  # Kezdetben üres kosár
}

add_basket(new_basket)

Új termék hozzáadása egy felhasználó kosarához:

user_id = 2
new_item = {
    "item_id": 205,
    "name": "Szilva",
    "brand": "Stanley",
    "price": 7.99,
    "quantity": 3
}

Termék hozzáadása a kosárhoz:

add_item_to_basket(user_id, new_item)

Hogyan használd a fájlt?

Importáld a függvényeket a filehandler.py modulból:

from filehandler import (
    add_user,
    add_basket,
    add_item_to_basket,
)

 - Hiba esetén ValuErrort kell dobni, lehetőség szerint ezt a 
   kliens oldalon is jelezni kell.

'''

# A JSON fájl elérési útja
JSON_FILE_PATH = "data/data.json"

def load_json() -> Dict[str, Any]:
    d: Dict[str, Any] = {}
    try:
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
            d = json.load(file)
    except: 
        pass
    return d

def save_json(data: Dict[str, Any]) -> None:
    with open(JSON_FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def add_user(user: Dict[str, Any]) -> None:
    data: Dict[str, Any] = load_json()
    users: list[Dict[str, Any]] = data.get("Users", [])
    for u in users:
        if u.get("id", user.get("id")) == user.get("id"):
            raise ValueError()
    users.append(user)
    data["Users"] = users
    save_json(data)

def add_basket(basket: Dict[str, Any]) -> None:
    data: Dict[str, Any] = load_json()                      # get baskets
    baskets: list[Dict[str, Any]] = data.get("Baskets", [])
    maxind: int = 0                                         # find largest id
    for b in baskets:
        if int(b["id"]) > maxind:
            maxind = int(b["id"])
    basket.id = maxind + 1                                  # set new id for basket
    baskets.append(basket.model_dump())                     # save basket
    data["Baskets"] = baskets
    save_json(data)                                         # write new data to file

def add_item_to_basket(user_id: int, item: Dict[str, Any]) -> None:
    data: Dict[str, Any] = load_json()                      # get baskets
    baskets: list[Dict[str, Any]] = data.get("Baskets", [])
    for i in range(0, len(baskets)):                        # update users all baskets
        if baskets[i]["user_id"] == user_id:
            items = baskets[i].get("items", [])
            items.append(item.model_dump())
            baskets[i]["items"] = items
    data["Baskets"] = baskets
    save_json(data)                                         # write new data to file
    
