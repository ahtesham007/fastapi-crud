from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

user = os.getenv('user')
encoded_pwd = quote_plus(os.getenv('pwd'))
host = os.getenv('host')
port = os.getenv('port')
db = os.getenv('db')

SQLALCHEMY_DATABASE_URL = f'mysql+mysqlconnector://{user}:{encoded_pwd}@{host}:{port}/{db}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
