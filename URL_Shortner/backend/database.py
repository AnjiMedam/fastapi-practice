# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base

# MYSQL_USER = 'root'
# MYSQL_PASSWORD = 'admin@1234'
# MYSQL_HOST = 'localhost'
# MYSQL_PORT = '3306'
# MYSQL_DB = 'url_shortener'

# # Create MySQL engine
# engine = create_engine(
#     f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
# )

engine = create_engine('mysql+pymysql://root:admin%401234@localhost:3306/url_shortener')

# Create tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
