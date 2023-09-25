from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud
from database.db import get_db, Base, engine
from schemas.shem import User,User_no_password


app = FastAPI()
Base.metadata.create_all(bind=engine)
@app.post('/',response_model=User_no_password)
def create(user: User,db:Session = Depends(get_db)):
    return crud.create(db,user)

@app.get('/')
def show(id:int,db:Session = Depends(get_db)):
    return crud.show_user(id,db)