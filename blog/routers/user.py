from fastapi import APIRouter, HTTPException, status, Depends
from .. import database, schemas, models
from sqlalchemy.orm import Session
from ..repository import user

get_db = database.get_db
router = APIRouter(
    prefix = '/user',
    tags=['user']
)

@router.post('', response_model=schemas.Userv2)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}', response_model=schemas.Userv2)
def get_user(id: int, db : Session = Depends(get_db)):
    return user.get(id,db)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_user(id: int, db: Session = Depends(get_db)):
    return user.eliminate(id,db)

@router.delete('', status_code=status.HTTP_200_OK)
def delete_all(db : Session = Depends(get_db)):
    return user.Nuke(db)