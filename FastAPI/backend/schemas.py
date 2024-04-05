
# schemas.py
from typing import List, Optional
from pydantic import BaseModel

class EMPschema(BaseModel):
   
    name: str
    city: str
    class Config():
        orm_mode:True



class Fruit(BaseModel):
    name :str                  #Blog .table =blogs
    price:int

class Fruitschema(Fruit):
    user_id:int
    class Config():                   #Blog .table =blogs
        orm_mode:True

class Userschema(BaseModel):
    name:str                         #User  ,table=users
    email:str
    password:str
    
class ShowUserschema(BaseModel):
    name:str                              #User  ,table=users
    email:str
    Creator:List[Fruitschema]=[]
    class Config():
        orm_mode:True
    
class ShowUser(BaseModel):
    name:str
    email:str

class Showfruitschema(BaseModel):
    name:str
    price:int
    Buyer: ShowUser
    class Config():
        orm_mode:True

class Pay(BaseModel):
    pay_mode:str

class Payschema(Pay):
    fruit_id:int
    class Config():
        orm_mode:True  
        
class Showpay(Pay):
    Payer:Showfruitschema
    class Config():
        orm_mode:True    




# we have to put buyer in only fruitschemas
# we have to put Creator in only userschemas

class Loginschema(BaseModel):
    username:str    # you have to enter email
    password:str 


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

