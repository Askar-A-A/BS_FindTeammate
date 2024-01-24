from fastapi import APIRouter, Request
from typing import List, Optional
from ..models.models import Player
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os



templates = Jinja2Templates(directory="project/app/templates")



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
    ),    
    Player(
        username='markus77',
        trophies=5420,
        favorite_brawler='Brock',
        is_looking_for_clan=True,
        win_rate=0.65,
        games_won=120
    ),
    Player(
        username='amy_blue',
        trophies=8150,
        favorite_brawler='Piper',
        is_looking_for_clan=False,
        win_rate=0.59,
        games_won=410
    ),
    Player(
        username='victorZ',
        trophies=3750,
        favorite_brawler='Barley',
        is_looking_for_clan=True,
        win_rate=0.48,
        games_won=180
     ),
    Player(
        username='stealth_ninja',
        trophies=9022,
        favorite_brawler='Leon',
        is_looking_for_clan=False,
        win_rate=0.76,
        games_won=635
),
    Player(
        username='el_primo',
        trophies=10032,
        favorite_brawler='El Primo',
        is_looking_for_clan=False,
        win_rate=0.80,
        games_won=702
)
]



@router.get("/players/filter/", response_class=HTMLResponse)
async def filter_players(request: Request,
                         username: Optional[str] = None, 
                         trophies: Optional[int] = None, 
                         favorite_brawler: Optional[str] = None, 
                         is_looking_for_clan: Optional[str] = None,  # Change to str
                         win_rate: Optional[float] = None, 
                         games_won: Optional[int] = None):

    # Interpret the checkbox string as a boolean
    is_looking_for_clan_bool = is_looking_for_clan == "on" if is_looking_for_clan else False

    filtered_players = [player for player in PlayersDB if 
                        (username is None or player.username == username) and
                        (trophies is None or player.trophies >= trophies) and
                        (favorite_brawler is None or player.favorite_brawler == favorite_brawler) and
                        (is_looking_for_clan is None or player.is_looking_for_clan == is_looking_for_clan_bool) and
                        (win_rate is None or player.win_rate >= win_rate) and
                        (games_won is None or player.games_won >= games_won)]
    context = {"request": request, "filtered_players": filtered_players}
    
    return templates.TemplateResponse("content.html", context)


#The endpoint for finding a person by their nickname.
# @router.get("/players/filter-name/")
# def filter_player_name(username: str):
#     filtered_players = [player for player in PlayersDB if player.username == username]
#     return filtered_players


# @router.get("/players/filter-trophies/")
# def filter_player_trophies(trophies: int):
#     filtered_player = [player for player in PlayersDB if player.trophies >= trophies]
#     return filtered_player


# @router.get("/players/filter-favorite_brawler/")
# def filter_player_brawler(favorite_brawler: str):
#     filtered_player = [player for player in PlayersDB if player.favorite_brawler == favorite_brawler]
#     return filtered_player


# @router.get("/players/filter-is_looking_for_clan/")
# def filter_player_clan(is_looking_for_clan: bool):
#     filtered_player = [player for player in PlayersDB if player.is_looking_for_clan == is_looking_for_clan]
#     return filtered_player


# @router.get("/players/filter-win-rate/")
# def filter_player_winrate(win_rate: float):
#     filtered_player = [player for player in PlayersDB if player.win_rate >= win_rate]
#     return filtered_player


# @router.get("/players/filter-games-won/")
# def filter_player_gw(games_won: int):
#     filtered_player = [player for player in PlayersDB if player.games_won >= games_won]
#     return filtered_player












