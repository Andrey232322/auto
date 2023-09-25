from passlib.context import CryptContext
from pydantic import BaseModel


class User(BaseModel):
    id:int
    name:str
    hashed_password:str


class User_no_password(BaseModel):
    id:int
    name:str

