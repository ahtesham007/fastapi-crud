from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List, Optional
from sqlalchemy import func
from ..database import get_db
from sqlalchemy.orm import Session
from .. import schemas, models, oauth2

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get("/", response_model=List[schemas.PostOut])
def read_posts(db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # posts = db.query(models.Post).filter(
    #     models.Post.title.contains(search)).limit(limit).offset(skip).all()
    posts = db.query(models.Post, func.count(models.Votes.post_id).label("votes")).join(
        models.Votes, models.Votes.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(payload: schemas.Post, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    post = models.Post(owner_id=current_user.id, **payload.dict())

    db.add(post)
    db.commit()
    db.refresh(post)

    return post


@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post, func.count(models.Votes.post_id).label("votes")).join(
        models.Votes, models.Votes.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message" : "not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id :{id} was not found")

    if post.Post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"id:{id} does not exist"
        )

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.PostResponse)
def update_post(id: int, payload: schemas.Post, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"id:{id} does not exist"
        )
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    post_query.update(payload.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()
