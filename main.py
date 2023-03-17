from typing import Optional, Union
from pydantic import BaseModel
from fastapi import Body, FastAPI, Response, status, HTTPException
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title":"Test1", "content": "cool", "id":1}, {"title":"Test1", "content": "cool", "id":2}]

def find_post(id):
    for i,post in enumerate(my_posts):
        if id == post["id"]:
            return post, i
    return None, None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def read_posts():
    return {"posts": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(payload: Post):
    post_dict = payload.dict()
    post_dict["id"] = randrange(0, 100000000)
    my_posts.append(post_dict)
    return {"post":post_dict}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post, _ = find_post(id)

    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message" : "not found"}

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id :{id} was not found")

    return {"post" : post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    _, ind = find_post(id)

    if ind == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"id:{id} does not exist"
        )

    my_posts.pop(ind)

@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(id:int, payload:Post):
    _, ind = find_post(id)
    if _ == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"id:{id} does not exist"
        )
    post_dict = payload.dict()
    post_dict["id"] = id
    my_posts[ind] = post_dict
    return {"detail": post_dict}
