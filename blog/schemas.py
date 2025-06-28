from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name: str
    email: str
    password: str

class Blog(BaseModel):
    title : str
    body : str

class Userv2(BaseModel):
    name: str
    email: str
    blogs : List[Blog] = []
    class Config():
        from_attributes = True


class Blogv2(BaseModel): 
    title : str
    body : str
    creator: Userv2
    class Config():
        from_attributes = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
    