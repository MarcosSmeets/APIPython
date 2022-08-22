from collections import UserList
from typing import List
from fastapi import APIRouter, HTTPException
from services import UserService, FavoritesServices
from schemas import ErrorOutput, UserCreateInput, StardartOutput, UserFavoriteAddInput

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post('/create', response_model=StardartOutput, responses={400: {'model': ErrorOutput}})
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StardartOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.delete('/delete/{user_id}', response_model=StardartOutput, responses={400: {'model': ErrorOutput}})
async def user_delete(user_id: int):
    try:
        await UserService.create_delete(user_id)
        return StardartOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@user_router.post('/favorite/add', response_model=StardartOutput, responses={400:{'model': ErrorOutput}})
async def user_favorite_add(favorite_add: UserFavoriteAddInput):
    try:
        await FavoritesServices.add_favorite(user_id=favorite_add.user_id, symbol=favorite_add.symbol)
        return StardartOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.delete('delete/favorite/{user_id}', response_model=StardartOutput)
async def delete_favorite(user_id: int, symbol: str):
    try:
        await FavoritesServices.delete_favorite(user_id=user_id, symbol=symbol)
        return StardartOutput('Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@user_router.get('list', response_model=List[UserList])
async def list_user():
    try:
        return await UserService.list_users()
    except Exception as error:
        raise HTTPException(400, detail=str(error))
