from fastapi import APIRouter
from typing import List
from ..models.models import Player

router = APIRouter()

# Artificial data for testing purposes
PlayersDB: List[Player] = [
    Player(
        username= 'longtroy',
        trophies= 6901,
        favorite_brawler= 'Rico',
        is_looking_for_clan= False,
        win_rate= 0.01,
        games_won= 304
    ),
    Player(
        username= 'deborah44',
        trophies= 7285,
        favorite_brawler= 'Colt',
        is_looking_for_clan= False,
        win_rate= 0.17,
        games_won= 344
    ),
    Player(
        username= 'julie11',
        trophies= 9968,
        favorite_brawler= 'Bull',
        is_looking_for_clan= True,
        win_rate= 0.71,
        games_won= 363
    )    
]


#The endpoint for finding a person by their nickname.
@router.get("/players/filter/")
def filter_player(username: str):
    filtered_players = [player for player in PlayersDB if player.username == username]
    return filtered_players
















