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
    player_tag: Optional[str] = None
    is_verified: Optional[bool] = None
    join_date: Optional[datetime] = None


class UserIn(BaseModel):
    username: constr(min_length=1, max_length=200)
    email: EmailStr
    player_tag: constr(min_length=8)
    password: constr(min_length=8)


class UserOut(UserBase):
    id: int    
    

class ProfileBase(BaseModel):
    profile_picture_url: Optional[str] = None
    favorite_brawlers: Optional[str] = None
    is_looking_for_clan: Optional[bool] = None
    minigames_preference: Optional[str] = None
    is_ranking_up: Optional[bool] = None
    gender: Optional[str] = None
    is_looking_for_relationship: Optional[bool] = None

    class Config:
        orm_mode = True

class ProfileCreate(ProfileBase):
    pass

class ProfileOut(ProfileBase):
    id: int    