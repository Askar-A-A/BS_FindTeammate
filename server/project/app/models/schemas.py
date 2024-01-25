from pydantic import BaseModel
from typing import Optional


class PlayerBase(BaseModel):
    username: Optional[str] = None
    trophies: Optional[int] = None
    favorite_brawler: Optional[str] = None
    is_looking_for_clan: Optional[bool] = None
    win_rate: Optional[float] = None
    games_won: Optional[int] = None

    class Config:
        orm_mode = True


class PlayerOut(PlayerBase):
    id: int