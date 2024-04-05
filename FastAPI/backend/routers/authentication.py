from datetime import timedelta
from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session
from JWTtoken import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
import JWTtoken
from schemas import Loginschema
import database,models
from models import Usermodel
from hashing import Hash
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(
    tags=['Authentications']
)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/login')
def login(req:OAuth2PasswordRequestForm = Depends(), db:Session=Depends(database.get_db)):
    user_data = db.query(models.Usermodel).filter(models.Usermodel.email == req.username).first()

    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(Usermodel.password, req.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = JWTtoken.create_access_token(data={"sub": user_data.email} )
    return  {"access_token":access_token, "token_type":"bearer"} 





# if not user_data :
    #     raise HTTPException(status_code=404, detail="username Or password incorrect")
    # if not Hash.verify(req.password, Usermodel.password):
    #     raise HTTPException(status_code=404, detail=f"username Or password incorrect")

# from fastapi import APIRouter, Depends, status, HTTPException
# from fastapi.security import OAuth2PasswordRequestForm
# from .. import schemas, database, models, token
# from ..hashing import Hash
# from sqlalchemy.orm import Session
# router = APIRouter(tags=['Authentication'])

# @router.post('/login')
# def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.email == request.username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Invalid Credentials")
#     if not Hash.verify(user.password, request.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Incorrect password")

#     access_token = token.create_access_token(data={"sub": user.email})
#     return {"access_token": access_token, "token_type": "bearer"}