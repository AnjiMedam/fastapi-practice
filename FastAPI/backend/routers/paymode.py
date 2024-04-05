
from typing import List
from fastapi import APIRouter, Depends
from  models import Fruitmodel, Paymodel
import database
from schemas import Payschema, Showpay
from sqlalchemy.orm import Session

router= APIRouter(
    tags=['Payment']
)


# paymode.py
@router.post('/pay')
def pay_method( data:Payschema ,db:Session=Depends(database.get_db)):
    add_pay = Paymodel(pay_mode=data.pay_mode,fruit_id=data.fruit_id)
    db.add(add_pay)
    db.commit()
    db.refresh(add_pay) 
    return add_pay

@router.get('/pay',response_model=List[Payschema]) 
def get_all_paymodes( db:Session = Depends(database.get_db)):
    paid=db.query(Paymodel).all()
    return paid

# @router.get('/pay{id}',response_model=List[Showpay]) 
# def get_all_fruits( id:int,db:Session = Depends(database.get_db)):
#     paid=db.query(Paymodel).filter(Paymodel.id==id).first()
#     return paid
