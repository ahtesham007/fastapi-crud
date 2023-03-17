from typing import Optional, Union
from pydantic import BaseModel
from fastapi import Body, FastAPI
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title":"Test1", "content": "cool", "id":1}, {"title":"Test1", "content": "cool", "id":2}]

def find_post(id):
    for post in my_posts:
        if id == post["id"]:
            return post

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def read_posts():
    return {"posts": my_posts}

@app.post("/posts")
def create_posts(payload: Post):
    post_dict = payload.dict()
    post_dict["id"] = randrange(0, 100000000)
    my_posts.append(post_dict)
    return {"post":post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)

    return {"post" : post}

