from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

import crud
from database.db import get_db, Base, engine
from schemas.schem import User


app = FastAPI()
Base.metadata.create_all(bind=engine)
apikey_scheme = APIKeyHeader(name='autoriz')
@app.post('/',response_model=User)
def create(user: User,db:Session = Depends(get_db)):
    return crud.create(db,user)

@app.get('/')
def show(id:int,db:Session = Depends(get_db)):
    return crud.show_user(id,db)
@app.post('/tt')
def create_token(user: User, db: Session = Depends(get_db)):
    return crud.create_token(db, user)

@app.get("/self", )
def get_user_by_id(access_token: Annotated[str, Depends(apikey_scheme)], db: Session = Depends(get_db)):
    return crud.get_user_by_token(access_token=access_token, db=db)

@app.post('/vhod')
def auto(user: User,db:Session = Depends(get_db)):
    return crud.vhod(db,user)