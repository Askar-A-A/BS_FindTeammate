from pydantic import BaseModel


class PlayerBase(BaseModel):
    username: str
    trophies: int
    favorite_brawler: str
    is_looking_for_clan: bool
    win_rate: float
    games_won: int

    class Config:
        orm_mode = True


class PlayerOut(PlayerBase):
    id: int