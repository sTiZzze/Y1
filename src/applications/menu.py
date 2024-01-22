from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db
from src.infrastructure.repositories.menu import MenuRepository


class MenuService:
    def __init__(self, session: AsyncSession = Depends(get_db)):
        self.__session = MenuRepository(session)

    async def get_menu(self, entity):
        return await self.__session.get_all(entity)

    async def get_menu_by_id(self, entity, id):
        return await self.__session.get_by_id(entity, id)

    async def create_menu(self, entity, model):
        return await self.__session.create(entity, model)

    async def update_menu(self, entity, model, id):
        return await self.__session.update(entity, model, id)

    async def delete_menu(self, entity, id):
        return await self.__session.delete(entity, id)
