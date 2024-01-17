from fastapi import APIRouter
from typing import List

router = APIRouter()

# Artificial data for testing purposes
players: List[dict] = [
    {
        'username': 'longtroy',
        'trophies': 6901,
        'favorite_brawler': 'Rico',
        'is_looking_for_clan': False,
        'win_rate': 0.01,
        'games_won': 304
    },
    {
        'username': 'deborah44',
        'trophies': 7285,
        'favorite_brawler': 'Colt',
        'is_looking_for_clan': False,
        'win_rate': 0.17,
        'games_won': 344
    },
    {
        'username': 'julie11',
        'trophies': 9968,
        'favorite_brawler': 'Bull',
        'is_looking_for_clan': True,
        'win_rate': 0.71,
        'games_won': 363
    }
]

@router.get("/players/list/")
def read_players():
    return players


















#endpoint for test
# @router.get("/players/", response_model=List[schemas.PlayerOut])
# def read_players(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
#     players = db.query(models.Player).offset(skip).limit(limit).all()
#     if not players:
#         raise HTTPException(status_code=404, detail="No players found")
#     return players