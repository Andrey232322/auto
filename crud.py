from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from model.models import User
from schemas.shem import User as shem_user
from starlette.status import HTTP_400_BAD_REQUEST
import hashlib
def create(db:Session,user:shem_user):
    if db.scalar(select(User).where(User.name == user.name)):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail='Такой юзер есть'
        )
    user.hashed_password = hashlib.sha384(user.hashed_password.encode())
    users = User(id=user.id,name=user.name,hashed_password=user.hashed_password.hexdigest())
    db.add(users)
    db.commit()
    db.refresh(users)
    return users
def show_user(id:int,db):
    return db.query(User).filter(User.id == id).first()