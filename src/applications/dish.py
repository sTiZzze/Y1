from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db
from src.infrastructure.repositories.dish import DishRepository


class DishService:
    def __init__(self, session: AsyncSession = Depends(get_db)):
        self.__session = DishRepository(session)

    async def get_dish(self, entity, submenu_id):
        return await self.__session.get_all(entity, submenu_id)

    async def get_dish_by_id(self, entity, submenu_id, dish_id):
        return await self.__session.get_by_id(entity, submenu_id, dish_id)

    async def create_dish(self, entity, model, submenu_id):
        return await self.__session.create(entity, model, submenu_id)

    async def update_dish(self, entity, model, submenu_id, dish_id):
        return await self.__session.update(entity, model, submenu_id, dish_id)

    async def delete_dish(self, entity, menu_id, submenu_id, dish_id):
        return await self.__session.delete(entity, menu_id, submenu_id, dish_id)
