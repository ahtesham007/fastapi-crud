from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# user = os.getenv('user')
user = settings.user
encoded_pwd = quote_plus(settings.pwd)
host = settings.host
port = settings.port
db = settings.db

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
