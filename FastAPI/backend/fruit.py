from typing import List
from fastapi import APIRouter, Depends
from backend.models import Fruitmodel
from backend.schemas import Showfruitschema
import database
from sqlalchemy.orm import Session
router = APIRouter()

@router.get('/fruit',response_model=List[Showfruitschema],tags=["Fruits"])
def all( db:Session = Depends(database.get_db)):
    fruit=db.query(Fruitmodel).all()
    return fruit
     