from schemas.schema import User, Basket, Item
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi import FastAPI, HTTPException, Request, Response, Cookie
from fastapi import APIRouter
from pydantic import ValidationError

from typing import Dict, Any, List

import data.filereader as reader
import data.filehandler as handler

'''

Útmutató a fájl használatához:

- Minden route esetén adjuk meg a response_modell értékét (típus)
- Ügyeljünk a típusok megadására
- A függvények visszatérési értéke JSONResponse() legyen
- Minden függvény tartalmazzon hibakezelést, hiba esetén dobjon egy HTTPException-t
- Az adatokat a data.json fájlba kell menteni.
- A HTTP válaszok minden esetben tartalmazzák a 
  megfelelő Státus Code-ot, pl 404 - Not found, vagy 200 - OK

'''

routers = APIRouter()

@routers.post('/adduser', response_model=User)
def adduser(user: User) -> User:
    try:
        handler.add_user(user.model_dump())
        return user
    except ValueError:
        raise HTTPException(status_code=422, detail="Could not add user")
    

@routers.post('/addshoppingbag')
def addshoppingbag(userid: int) -> str:
    b = Basket(id=0, user_id=userid, items=[])
    try:
        handler.add_basket(b)
        return "Sikeres kosár hozzárendelés."
    except ValueError:
        raise HTTPException(status_code=422, detail="Could not add basket")

@routers.post('/additem', response_model=Basket)
def additem(userid: int, item: Item) -> Basket:
    data = handler.load_json()                      # get baskets
    baskets = data.get("Baskets", [])
    basket = {}
    for b in baskets:                               # find users basket
        if b["user_id"] == userid:
            basket = b
            items = b.get("items", [])
            items.append(item.model_dump())
            b["items"] = items
    if "user_id" in basket.keys():                  # if basket was found it will have a user_id key
        handler.add_item_to_basket(userid, item)    # store the new basket in the file
        return basket
    raise HTTPException(status_code=422, detail="Could not add item to basket")
        
    

@routers.put('/updateitem')
def updateitem(userid: int, itemid: int, updateItem: Item) -> Basket:
    pass

@routers.delete('/deleteitem')
def deleteitem(userid: int, itemid: int) -> Basket:
    pass

@routers.get('/user')
def user(userid: int) -> User:
    try:
        return reader.get_user_by_id(userid)
    except ValueError:
        raise HTTPException(status_code=422, detail=f"There is no user with the received id (id: {userid})")


@routers.get('/users')
def users() -> list[User]:
    return reader.get_all_users()

@routers.get('/shoppingbag')
def shoppingbag(userid: int) -> list[Item]:
    try:
        return reader.get_basket_by_user_id(userid)
    except ValueError:
        raise HTTPException(status_code=422, detail=f"Couldn't find a basket for this user (userid: {userid})")

@routers.get('/getusertotal')
def getusertotal(userid: int) -> float:
    try:
        return reader.get_total_price_of_basket(userid)
    except ValueError:
        raise HTTPException(status_code=422, detail=f"Couldn't find a basket for this user (userid: {userid})")

    


