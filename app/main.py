from typing import Optional, Union, List
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from random import randrange
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
from . import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts", response_model=List[schemas.PostResponse])
def read_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(payload: schemas.Post, db: Session = Depends(get_db)):

    post = models.Post(**payload.dict())

    db.add(post)
    db.commit()
    db.refresh(post)
    
    return post

@app.get("/posts/{id}", response_model= schemas.PostResponse)
def get_post(id: int, response: Response, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message" : "not found"}

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id :{id} was not found")

    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"id:{id} does not exist"
        )

    post.delete(synchronize_session=False)
    db.commit()

@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED, response_model= schemas.PostResponse)
def update_post(id:int, payload:schemas.Post, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"id:{id} does not exist"
        )
    
    post_query.update(payload.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()

