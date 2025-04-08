from pydantic import BaseModel, EmailStr, NonNegativeInt, NonNegativeFloat, PositiveInt

'''

Útmutató a fájl használatához:

Az osztályokat a schema alapján ki kell dolgozni.

A schema.py az adatok küldésére és fogadására készített osztályokat tartalmazza.
Az osztályokban az adatok legyenek validálva.
 - az int adatok nem lehetnek negatívak.
 - az email mező csak e-mail formátumot fogadhat el.
 - Hiba esetén ValuErrort kell dobni, lehetőség szerint ezt a 
   kliens oldalon is jelezni kell.

'''

ShopName='Bolt'

class User(BaseModel):
    id: NonNegativeInt
    name: str
    email: EmailStr

class Item(BaseModel):
    item_id: NonNegativeInt
    name: str
    brand: str
    price: NonNegativeFloat
    quantity: PositiveInt

class Basket(BaseModel):
    id: NonNegativeInt
    user_id: NonNegativeInt
    items: list[Item]
