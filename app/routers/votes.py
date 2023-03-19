from fastapi import status, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from .. import schemas, models, oauth2

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(payload: schemas.Votes, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.id == payload.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"post id:{payload.post_id} does not exist"
        )
    vote_query = db.query(models.Votes).filter(
            models.Votes.post_id == payload.post_id, models.Votes.user_id == current_user.id)
    found_vote = vote_query.first()

    if payload.direction == 1:
        if found_vote:
            raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=f"User {current_user.id} already voted for post {payload.post_id}"
        )
        new_vote = models.Votes(user_id=current_user.id, post_id=payload.post_id) 
        db.add(new_vote)
        db.commit()
        return {"message": "Successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Vote doesn't exist"
        )
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Successfully deleted vote"}
    
