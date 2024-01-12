from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    trophies = Column(Integer)
    favorite_brawler = Column(String)
    is_looking_for_clan = Column(Boolean, default=False)
    win_rate = Column(Float)
    games_won = Column(Integer)

    def __repr__(self):
        return f"<Player(username='{self.username}', trophies={self.trophies}, 
        favorite_brawler='{self.favorite_brawler}', is_looking_for_clan={self.is_looking_for_clan}, 
        win_rate={self.win_rate}, games_won={self.games_won})>"
