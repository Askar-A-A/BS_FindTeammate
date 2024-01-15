from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)

# Generator function to handle the lifecycle of a SQLAlchemy database session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    



db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)


app.include_router(api.router, prefix="/api", tags=["APIEndpoints"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])