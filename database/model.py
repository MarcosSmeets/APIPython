from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

base = declarative_base()

class User(base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, )
    name = Column(String)
    Favorites = relationship('Favorite', backref='user', lazy='subquery')

class Favorites(base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

