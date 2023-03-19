from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None
class UserOut(BaseModel):
    id:int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class PostResponse(Post):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Votes(BaseModel):
    post_id: int
    direction: int