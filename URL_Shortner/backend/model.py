# model.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class URL(Base):
    __tablename__ = 'url_mapping'
    id = Column(Integer, primary_key=True, index=True)
    uni_code = Column(String, unique=True, index=True)
    original_url = Column(String, index=True)
