# models.py

from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Relationship
Base = declarative_base()

class EMPmodel(Base):
    __tablename__ = 'forminfo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
    city = Column(String(100))


class Usermodel(Base):
    __tablename__ ='userinfo'           #User , tablename :users

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(90))
    email = Column(String(90))
    password=Column(String(90))
    Creator=Relationship('Fruitmodel',back_populates='Buyer')


class Fruitmodel(Base):
    __tablename__ ='fruitinfo'     #Blog tablename :blogs

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
    price = Column(Integer)
    user_id =Column(Integer, ForeignKey('userinfo.id'),nullable=True)
    Buyer =Relationship('Usermodel',back_populates='Creator')
    payments = Relationship('Paymodel', back_populates='fruit')
class Paymodel(Base):
    __tablename__= 'payment'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    pay_mode=Column(String(80))
    fruit_id=Column(Integer, ForeignKey('fruitinfo.id'),nullable=True)
    fruit=Relationship('Fruitmodel',back_populates='payments')


# class Usermodel(Base):
#     __tablename__ ='userinfo'           #User , tablename :users

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(90))
#     email = Column(String(90))
#     password=Column(String(90))
#     Creator=Relationship('Fruitmodel',back_populates='Buyer')


