from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db
from src.infrastructure.repositories.submenu import SubmenuRepository


class SubmenuService:
    def __init__(self, session: AsyncSession = Depends(get_db)):
        self.__session = SubmenuRepository(session)

    async def get_submenu(self, entity, menu_id):
        return await self.__session.get_all(entity, menu_id)

    async def get_submenu_by_id(self, entity, menu_id, submenu_id):
        return await self.__session.get_by_id(entity, menu_id, submenu_id)

    async def create_submenu(self, entity, model, menu_id):
        return await self.__session.create(entity, model, menu_id)

    async def update_submenu(self, entity, model, menu_id, submenu_id):
        return await self.__session.update(entity, model, menu_id, submenu_id)

    async def delete_submenu(self, entity, menu_id, submenu_id):
        return await self.__session.delete(entity, menu_id, submenu_id)
