from schemas.schema import User, Basket, Item
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi import FastAPI, HTTPException, Request, Response, Cookie
from fastapi import APIRouter
from pydantic import ValidationError

from typing import Dict, Any, List
from data.filehandler import load_json as lj
from data.filehandler import save_json as sj

from data.filereader import get_all_users, get_user_by_id, get_basket_by_user_id, get_total_price_of_basket

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
    pass

@routers.post('/addshoppingbag')
def addshoppingbag(userid: int) -> str:
    pass

@routers.post('/additem', response_model=Basket)
def additem(userid: int, item: Item) -> Basket:
    pass

@routers.put('/updateitem')
def updateitem(userid: int, itemid: int, updateItem: Item) -> Basket:
    pass

@routers.delete('/deleteitem')
def deleteitem(userid: int, itemid: int) -> Basket:
    pass

@routers.get('/user')
def user(userid: int) -> User:
    try:
        return get_user_by_id(userid)
    except ValueError:
        raise HTTPException(status_code=404, detail=f"There is no user with the received id (id: {userid})")


@routers.get('/users')
def users() -> list[User]:
    return get_all_users()

@routers.get('/shoppingbag')
def shoppingbag(userid: int) -> list[Item]:
    try:
        return get_basket_by_user_id(userid)
    except ValueError:
        raise HTTPException(status_code=422, detail=f"Couldn't find a basket for this user (userid: {userid})")

@routers.get('/getusertotal')
def getusertotal(userid: int) -> float:
    try:
        return get_total_price_of_basket(userid)
    except ValueError:
        raise HTTPException(status_code=422, detail=f"Couldn't find a basket for this user (userid: {userid})")

    


