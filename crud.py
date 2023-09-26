import uuid

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from model.models import User, Token
from schemas.schem import User as shem_user
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED
import hashlib


def create(db:Session,user:shem_user):
    if db.scalar(select(User).where(User.name == user.name)):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail='Такой юзер есть'
        )
    #user.hashed_password = hashlib.sha384(user.hashed_password.encode())
    users = User(id=user.id,name=user.name,hashed_password=user.hashed_password)
    db.add(users)
    db.commit()
    db.refresh(users)
    return users
def show_user(id:int,db):
    return db.query(User).filter(User.id == id).first()

def create_token(db: Session, user_data: shem_user):
    user: User = db.scalar(select(User).where(User.name == user_data.name))
    if not user:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    token: Token = Token(user_id=user.id, access_token=str(uuid.uuid4()))
    db.add(token)
    db.commit()
    return {"access_token": token.access_token}
def get_user_by_token(access_token: str, db: Session):
    token = db.scalar(select(Token).where(Token.access_token == access_token))
    if token:
        return {
            "id": token.user.id,
            "name": token.user.name
        }
    else:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="UNAUTHORIZED"
        )
