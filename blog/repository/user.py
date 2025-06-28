from .. import models, schemas
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..hashing import Hash

def create(request: schemas.User, db: Session):
    new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get(id,db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"User with user id = {id} does not exist!")
    return user

def eliminate(id, db: Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The User with User id {id} does not exist!")
    user.delete(synchronize_session=False)
    db.commit()
    return 'User Vanquished Succesfully'

def Nuke(db: Session):
    users = db.query(models.User).delete(synchronize_session=False)
    db.commit()
    return "Global Cataclysm"