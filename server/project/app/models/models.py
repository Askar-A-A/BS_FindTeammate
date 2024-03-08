from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime
from ..database import Base


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    trophies = Column(Integer)
    favorite_brawler = Column(Boolean)
    is_looking_for_clan = Column(Boolean, default=False)
    win_rate = Column(Float)
    games_won = Column(Integer)

    def __repr__(self):
        return f"<Player(username='{self.username}', trophies={self.trophies}, " + \
                f"favorite_brawler='{self.favorite_brawler}', is_looking_for_clan={self.is_looking_for_clan}, " + \
                f"win_rate={self.win_rate}, games_won={self.games_won})>"
                
 

class User(Base):
    __tablename__ = 'users' 
            
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    is_verified = Column(Boolean, default=False)
    join_date = Column(DateTime, default=datetime.utcnow)
    
    
    
class Profile(Base):
    __tablename__ = 'profiles'
    
    id = Column(Integer, primary_key=True, index=True)
    profile_picture_url = Column(String, nullable=True)  
    
    favorite_brawlers = Column(String, nullable=True)
    is_looking_for_clan = Column(String, nullable=True)
    minigames_preference = Column(String, nullable=True)
    is_ranking_up = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    is_lookin_for_relationship = Column(String, nullable=True)
    


# class UserOut(Base):
#     id: int
#     username: str
#     email: str
#     is_verified: bool
#     join_date: datetime

#     class Config:
#         orm_mode = True