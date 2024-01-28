from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request, Depends

from ..models.models import Player
from ..database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="project/app/templates")


@router.get("/players/filter/", response_class=HTMLResponse)
async def filter_players(
    request: Request, 
    username = None, 
    trophies = None, 
    favorite_brawler = None, 
    is_looking_for_clan = None,
    win_rate = None, 
    games_won = None,
    db: Session = Depends(get_db)
):
    
    query = db.query(Player)
    if username:
        query = query.filter(Player.username == username)
    if trophies or trophies == 0:
        query = query.filter(Player.trophies >= trophies)
    if favorite_brawler:
        query = query.filter(Player.favorite_brawler == favorite_brawler)
    if is_looking_for_clan == True:
        query = query.filter(Player.is_looking_for_clan == is_looking_for_clan)
    if win_rate or win_rate == 0:
        query = query.filter(Player.win_rate >= win_rate)
    if games_won or games_won == 0:
        query = query.filter(Player.games_won >= games_won)

    filtered_players = query.all()
    context = {"request": request, "filtered_players": filtered_players}
    return templates.TemplateResponse("content.html", context)



#my old endpoints 

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


# Artificial data for testing purposes
# PlayersDB: List[Player] = [
#     Player(
#         username= 'longtroy',
#         trophies= 6901,
#         favorite_brawler= 'Rico',
#         is_looking_for_clan= False,
#         win_rate= 0.01,
#         games_won= 304
#     ),
#     Player(
#         username= 'deborah44',
#         trophies= 7285,
#         favorite_brawler= 'Colt',
#         is_looking_for_clan= False,
#         win_rate= 0.17,
#         games_won= 344
#     ),
#     Player(
#         username= 'julie11',
#         trophies= 9968,
#         favorite_brawler= 'Bull',
#         is_looking_for_clan= True,
#         win_rate= 0.71,
#         games_won= 363
#     ),    
#     Player(
#         username='markus77',
#         trophies=5420,
#         favorite_brawler='Brock',
#         is_looking_for_clan=True,
#         win_rate=0.65,
#         games_won=120
#     ),
#     Player(
#         username='amy_blue',
#         trophies=8150,
#         favorite_brawler='Piper',
#         is_looking_for_clan=False,
#         win_rate=0.59,
#         games_won=410
#     ),
#     Player(
#         username='victorZ',
#         trophies=3750,
#         favorite_brawler='Barley',
#         is_looking_for_clan=True,
#         win_rate=0.48,
#         games_won=180
#      ),
#     Player(
#         username='stealth_ninja',
#         trophies=9022,
#         favorite_brawler='Leon',
#         is_looking_for_clan=False,
#         win_rate=0.76,
#         games_won=635
# ),
#     Player(
#         username='el_primo',
#         trophies=10032,
#         favorite_brawler='El Primo',
#         is_looking_for_clan=False,
#         win_rate=0.80,
#         games_won=702
# )
# ]









