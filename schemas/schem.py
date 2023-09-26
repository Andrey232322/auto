from passlib.context import CryptContext
from pydantic import BaseModel


class User(BaseModel):
    id:int
    name:str
    hashed_password:str
class Token(BaseModel):
    access_token: str

