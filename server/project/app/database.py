from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends
from typing import Annotated

URL_DATABASE = 'postgresql://postgres:plmoknijbuhvuhhu123@localhost/bsfind_db'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

# db_dependency = Annotated[Session, Depends(get_db)]

