from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware
from .api.endpoints import router 

app = FastAPI()
app.include_router(router)
# CORS settings
origins = [
    "http://localhost:5500",  # Frontend server (Live Server)
    # "http://localhost:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Generator function to handle the lifecycle of a SQLAlchemy database session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Initialize the database tables
Base.metadata.create_all(bind=engine)

