import sqlalchemy as sa
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import database, oauth2, models, schemas


router = APIRouter(
    prefix="/vote",
    tags=["vote"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote,
         current_user: models.User = Depends(oauth2.get_current_user),
         db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {vote.post_id} does not exist.")

    vote_query = db.query(models.Vote)\
            .filter(sa.and_(models.Vote.user_id == current_user.id, models.Vote.post_id == vote.post_id))
    found_vote = vote_query.first()

    if vote.vote_dir == 1:
        if found_vote:  # you can't like a post more than once
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User {current_user.id} has already voted "
                                                                             f"on post {vote.post_id}.")

        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}

    else:
        if not found_vote:  # you cannot delete a vote that doesn't exist'
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You haven't liked the post before.")

        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "successfully deleted vote"}

