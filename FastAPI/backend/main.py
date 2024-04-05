#  main.py 
# from typing import List,Union
from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
# from database import engine, SessionLocal 
from fastapi.middleware.cors import CORSMiddleware
# from passlib.context import CryptContext

# from models import Base, EMPmodel, Fruitmodel, Usermodel
# from schemas import   EMPschema, Fruitschema, ShowUserschema, Showfruitschema, Userschema
import uvicorn 
import models, database,hashing
from routers import fruit,user,authentication,paymode
app = FastAPI()
router=APIRouter()
# Create all tables
models.Base.metadata.create_all(bind=database.engine)

app.include_router(fruit.router)
app.include_router(user.router)
app.include_router(paymode.router)
# app.include_router(authentication.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

 
import sys
sys.setrecursionlimit(10000)

""" #  adding data
@app.post('/fruit',tags=["Fruits"])
def post_fruit(data: Fruitschema, db: Session = Depends(database.get_db)):
    add_fruit = Fruitmodel(name=data.name, price=data.price)
    db.add(add_fruit)
    db.commit()
    db.refresh(add_fruit)
     
    return add_fruit
 
# Reading all data 
@app.get('/fruit',response_model=List[Showfruitschema],tags=["Fruits"])
def get_fruit(  db:Session = Depends(database.get_db)):
    fruit = db.query(Fruitmodel). all()
    if fruit is None:
        raise HTTPException(status_code=404, detail="fruit is  not found")
    return fruit

# Reading databy id
@app.get('/fruit/{id}',response_model=Fruitschema,tags=["Fruits"])
def get_fruit(id:int, db:Session = Depends(database.get_db)):
    fruit = db.query(Fruitmodel).filter(Fruitmodel.id == id).first()
    if fruit is None:
        raise HTTPException(status_code=404, detail=f"fruit with {id} not found")
    return fruit

# Updata operations
@app.put('/fruit/{id}',tags=["Fruits"])
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

# delete operations
@app.delete('/fruit/{id}',tags=["Fruits"])
def delete_fruit(id:int, db:Session = Depends(database.get_db)):
    fruit = db.query(Fruitmodel).filter(Fruitmodel.id == id).first()
    if fruit is None:
        raise HTTPException(status_code=404, detail=f"fruit with {id} not found")
    else:
        db.delete(fruit)
        db.commit()
    return fruit


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@app.post('/user',response_model=ShowUserschema,tags=["Users"])
def create_user(req :Userschema,db:Session=Depends(database.get_db)):
    # hashPW=pwd_context.hash(req.password)
    add_user=Usermodel(name=req.name,email=req.email,password=hashing.Hash.bcrypt(req.password))
    db.add(add_user)
    db.commit()
    db.refresh(add_user)
    return add_user
    
@app.get('/user/{id}',response_model=ShowUserschema,tags=["Users"])
def read_user(id:int,db:Session=Depends(database.get_db)):
    user_data=db.query(Usermodel).filter(Usermodel.id==id).first()
    if user_data is None:
        raise HTTPException(status_code=404, detail='user not foudn')
    return user_data




@app.post("/formdata")
def create_employee(reactdata: EMPschema, db: Session = Depends(get_db)):
    react_data = EMPmodel(name=reactdata.name, city=reactdata.city)
    db.add(react_data)
    db.commit()
    db.refresh(react_data)
    return react_data


@app.post("/employees/")
def create_employee(employee: EMPschema, db: Session = Depends(get_db)):
    db_employee = EMPmodel(name=employee.name, city=employee.city)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.get("/employees")
def get_employee( db: Session = Depends(get_db)):
    # employee = db.query(EMPmodel).filter(EMPmodel.id == employee_id).first()
    employee = db.query(EMPmodel).all()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee



@app.get("/employees/{emp_id}")
def get_employee(emp_id:int, db: Session = Depends(get_db)):
    employee = db.query(EMPmodel).filter(EMPmodel.id == emp_id).first()
    # employee = db.query(EMPmodel).all()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


# update Operation
@app.put("/employees/{emp_id}")
def put_employee(emp_id:int,new_emp:EMPschema, db: Session = Depends(get_db)):
    employee = db.query(EMPmodel).filter(EMPmodel.id == emp_id).first()
     
    # employee = db.query(EMPmodel).all()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    else:
        employee.name=new_emp.name
        employee.city = new_emp.city
        db.add(employee)
        db.commit()
        db.refresh(employee)
    return employee

# delete Operaion
@app.delete("/employees/{emp_id}")
def del_employee(emp_id:int,  db: Session = Depends(get_db)):
    employee = db.query(EMPmodel).filter(EMPmodel.id == emp_id).first()
    # employee = db.query(EMPmodel).all()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    else:
        db.delete(employee)
        db.commit()

    return employee


def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()    


@app.post('/empdata')
def post_emp(request: Detail, db:Session=Depends(get_db())):
     new_data= EMP(name=request.name, city=request.city)
     db.add(new_data)
     db.commit()
     db.refresh(new_data)
     return new_data

@app.get('/empdata')
def get_emp(db:Session=Depends(get_db())):
    get_data=db.query( EMP).all()
    return get_data

@app.get('/age/{id}')
def comments(id:int):
    return {'my age is': f'{id}'}

class Detail(BaseModel):
    name :str
    city :str


@app.post('/posting')
def post_method(info:Detail):
    return f"my name is : {info.name} ,living in {info.city}"    

 """
 

if __name__=='__main__':
    uvicorn.run(app,host="localhost",port=8000)



