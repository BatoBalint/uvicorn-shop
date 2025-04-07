from schemas.schema import User, Basket, Item
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi import FastAPI, HTTPException, Request, Response, Cookie
from fastapi import APIRouter
from pydantic import ValidationError

from typing import Dict, Any, List
from data.filehandler import load_json as lj
from data.filehandler import save_json as sj

from data.filereader import get_all_users, get_user_by_id

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
def user(userid: int) -> JSONResponse:
    u = get_user_by_id(userid)
    if "error" in u:
        raise HTTPException(status_code=404, detail=f"There was no user found with the given id ({userid})")
    else:
        return JSONResponse(content=u, status_code=200)


@routers.get('/users')
def users() -> JSONResponse:
    return JSONResponse(get_all_users(), status_code=200)

@routers.get('/shoppingbag')
def shoppingbag(userid: int) -> list[Item]:
    pass

@routers.get('/getusertotal')
def getusertotal(userid: int) -> float:
    pass

@routers.get('/test')
def getTestData() -> Dict[str, Any] | Any:
    return {"Message": "Haiii :3"}
    


