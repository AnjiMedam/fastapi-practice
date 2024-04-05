
# /routers/fruit.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from models import Fruitmodel,Usermodel
from schemas import Fruitschema, Showfruitschema
import database
from sqlalchemy.orm import Session
from repository import fruit
router = APIRouter(
 tags=["Fruits"]
)

@router.get('/fruit',response_model=List[Showfruitschema]) 
def get_all_fruits( db:Session = Depends(database.get_db)):
    # fruit=db.query(Fruitmodel).all()
    return fruit.reposit_all(db)
     
@router.post('/fruit')
def post_fruit(data: Fruitschema, db: Session = Depends(database.get_db)):
 
    add_fruit = Fruitmodel(name=data.name, price=data.price,user_id = data.user_id)
    db.add(add_fruit)
    db.commit()
    db.refresh(add_fruit) 
    return add_fruit



@router.get('/fruit/{id}',response_model=Showfruitschema )
def get_fruit(id:int, db:Session = Depends(database.get_db)):
    fruit = db.query(Fruitmodel).filter(Fruitmodel.id == id).first()
    if fruit is None:
        raise HTTPException(status_code=404, detail=f"fruit with {id} not found")
    return fruit


@router.put('/fruit/{id}')
def put_fruit(id:int, new_schema:Fruitschema, db:Session = Depends(database.get_db)):
    fruit = db.query(Fruitmodel).filter(Fruitmodel.id == id).first()
    if fruit is None:
        raise HTTPException(status_code=404, detail=f"fruit with {id} not found")
    else:
        fruit.name = new_schema.name
        fruit.price = new_schema.price
    db.add(fruit)
    db.commit()
    db.refresh(fruit)
    return fruit


@router.delete('/fruit/{id}')
def delete_fruit(id:int, db:Session = Depends(database.get_db)):
    fruit = db.query(Fruitmodel).filter(Fruitmodel.id == id).first()
    if fruit is None:
        raise HTTPException(status_code=404, detail=f"fruit with {id} not found")
    else:
        db.delete(fruit)
        db.commit()
    return fruit


