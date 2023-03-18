from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    hashed_pwd = pwd_context.hash(password)
    return hashed_pwd

def verify(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)