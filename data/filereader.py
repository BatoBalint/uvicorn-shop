import json
from typing import Dict, Any, List

'''
Útmutató a féjl használatához:

Felhasználó adatainak lekérdezése:

user_id = 1
user = get_user_by_id(user_id)
print(f"Felhasználó adatai: {user}")

Felhasználó kosarának tartalmának lekérdezése:

user_id = 1
basket = get_basket_by_user_id(user_id)
print(f"Felhasználó kosarának tartalma: {basket}")

Összes felhasználó lekérdezése:

users = get_all_users()
print(f"Összes felhasználó: {users}")

Felhasználó kosarában lévő termékek összárának lekérdezése:

user_id = 1
total_price = get_total_price_of_basket(user_id)
print(f"A felhasználó kosarának összára: {total_price}")

Hogyan futtasd?

Importáld a függvényeket a filehandler.py modulból:

from filereader import (
    get_user_by_id,
    get_basket_by_user_id,
    get_all_users,
    get_total_price_of_basket
)

 - Hiba esetén ValuErrort kell dobni, lehetőség szerint ezt a 
   kliens oldalon is jelezni kell.

'''

# A JSON fájl elérési útja
JSON_FILE_PATH = "data/data.json"

def load_json() -> Dict[str, Any]:
    try:
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        return {}

def get_user_by_id(user_id: int) -> Dict[str, Any]:
    users = load_json().get("Users", [])
    for user in users:
        if user.get("id") == user_id:
            return user
    return {"error": "User not found"}

def get_basket_by_user_id(user_id: int) -> List[Dict[str, Any]]:
    baskets = load_json().get("Baskets", [])
    for basket in baskets:
        if basket.get("user_id") == user_id:
            return basket.get("items", [])
    return {"error": "Users basket not found"}

def get_all_users() -> List[Dict[str, Any]]:
    return load_json().get("Users", [])

def get_total_price_of_basket(user_id: int) -> float:
    basket = get_basket_by_user_id(user_id)
    if "error" in basket:
        return 0

    sum = 0
    for item in basket:
        sum += item.get("price", 0)
    return sum
