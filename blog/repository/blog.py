from .. import models, schemas
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
 

def get_all(db : Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request : schemas.Blog,db : Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit() #executes
    db.refresh(new_blog)
    return new_blog

def delete(id,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} does not exist")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Destroyed'

def update(id,request : schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} Does not Exist")
    blog.title = request.title
    blog.body = request.body
    db.commit()
    return 'Updated'

def show(id,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the {id} does not exist!")
    return blog