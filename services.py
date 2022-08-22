from sqlalchemy import delete
from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select

from database.model import Favorites, User
from database.connection import async_session

class UserService():
    async def create_User(name: str):
        async with async_session as session:
            session.add(User(name=name))
            await session.commit()

    async def delete_user(user_id: int):
        async with async_session() as session:
            await session.execute(delete(User).where(User.id==user_id))
            await session.commit()

    async def list_users():
        async with async_session() as session:
            result = session.execute(select(User))
            return result.scalars().all()   

class FavoritesServices():
    async def add_favorite(user_id: int, symbol: str):
        async with async_session() as session:
            session.add(Favorites(user_id=user_id, symbol=symbol))
            await session.commit()
    
    async def delete_favorite(user_id: int, symbol: str):
        async with async_session() as session:
            await session.execute(delete(Favorites.where(User.id==user_id, Favorites.symbol==symbol)))
            await session.commit()