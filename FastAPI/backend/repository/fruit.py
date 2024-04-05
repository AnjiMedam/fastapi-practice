
from sqlalchemy.orm import Session

from models import Fruitmodel


def reposit_all(db:Session):
    fruit=db.query(Fruitmodel).all()
    return fruit


    