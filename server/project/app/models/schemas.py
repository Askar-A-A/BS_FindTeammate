from typing import Optional
from pydantic import BaseModel, EmailStr, constr
from datetime import datetime


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
    
    
class UserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_verified: Optional[bool] = None
    join_date: Optional[datetime] = None


class UserIn(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: EmailStr
    password: constr(min_length=6)


class UserOut(UserBase):
    id: int    