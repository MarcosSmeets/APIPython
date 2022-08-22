from email import message
from lib2to3.pytree import Base
from turtle import st
from unicodedata import name
from pydantic import BaseModel

from database.model import Favorites

class UserCreateInput(BaseModel):
    name: str

class StardartOutput(BaseModel):
    message: str

class ErrorOutput(StardartOutput):
    detail: str

class UserFavoriteAddInput(BaseModel):
    user_id: int
    symbol: str

class Favorite(BaseModel):
    id: int
    symbol: str
    user_id: int

    class Config:
        orm_mode = True

class ListUsers(BaseModel):
    id: int
    name: str
    favorite: list[Favorite]

    class Config:
        orm_mode = True

