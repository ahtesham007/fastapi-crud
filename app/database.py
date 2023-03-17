from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = "release_user"
encoded_pwd = encoded_pwd = quote_plus('release_password@123')
host = "localhost"
port = "3306"
db = "fastapi"

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