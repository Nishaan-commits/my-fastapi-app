from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .. import schemas, database, models, Oauth2
from ..repository import blog

router = APIRouter(
    prefix = "/blog",
    tags = ['blogs']
)




@router.get('', response_model=List[schemas.Blogv2])
def all(db : Session = Depends(database.get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('', status_code=201)
def create(request : schemas.Blog, db : Session = Depends(database.get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.create(request,db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.delete(id,db)


@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db : Session = Depends(database.get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.update(id,request,db)

@router.get('/{id}', status_code=200, response_model=schemas.Blogv2)
def show(id: int, db : Session = Depends(database.get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.show(id,db)