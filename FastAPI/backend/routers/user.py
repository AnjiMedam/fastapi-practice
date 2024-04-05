
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Usermodel
from schemas import ShowUser, ShowUserschema, Userschema

import database,hashing



router =APIRouter(
    tags=['Users']
)



@router.post('/user',response_model=ShowUserschema )
def create_user(req :Userschema,db:Session=Depends(database.get_db)):
    # hashPW=pwd_context.hash(req.password)
    add_user=Usermodel(name=req.name,email=req.email,password=hashing.Hash.bcrypt(req.password))
    db.add(add_user)
    db.commit()
    db.refresh(add_user)
    return add_user

@router.get('/user/{id}',response_model=ShowUserschema)
def read_user(id:int,db:Session=Depends(database.get_db)):
    user_data=db.query(Usermodel).filter(Usermodel.id==id).first()
    if user_data is None:
        raise HTTPException(status_code=404, detail='user not foudn')
    return user_data

@router.get('/user',response_model=List[ShowUser])
def read_all_users(db:Session=Depends(database.get_db)):
    # user_data=db.query(Usermodel).filter(Usermodel.id==id).first()
    user_data=db.query(Usermodel).all()
    if user_data is None:
        raise HTTPException(status_code=404, detail='user not foudn')
    return user_data















