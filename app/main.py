from fastapi import FastAPI
from fastapi.params import Body


from typing import Optional,List
from random import randrange

from . import models,schemas
from .database import SessionLocal, engine,get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import utils
from .routers import post, user, auth,vote
from .config import settings  

from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Insta Buzz",
    description="Api for Social APP",
    version="1.0.0",
)
 

origins = [ "*"
    # "http://wwww.google.com",
    # "https://www.youtube.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World"}



