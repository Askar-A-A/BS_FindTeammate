from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import schemas, models, dependencies

router = APIRouter()

#endpoint for test
@router.get("/players/", response_model=List[schemas.PlayerOut])
def read_players(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    players = db.query(models.Player).offset(skip).limit(limit).all()
    if not players:
        raise HTTPException(status_code=404, detail="No players found")
    return players


