from typing import Iterable
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import and_, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.domain.DTO.menu import SubmenuCreateUpdate
from src.domain.models.menu import Menu, Submenu


class SubmenuRepository:
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def get_all(self, entity: Submenu, menu_id: UUID) -> Iterable[Submenu]:
        query = await self.__session.execute(select(entity).filter(entity.menu_id == menu_id))
        return query.scalars().all()

    async def get_by_id(self, entity: Submenu, menu_id: UUID, submenu_id: UUID) -> Submenu:
        query = await self.__session.execute(select(entity).filter_by(id=submenu_id, menu_id=menu_id))
        submenu = query.scalar()
        if not submenu:
            raise HTTPException(
                status_code=404, detail="submenu not found")

        return submenu

    async def create(self, entity: Submenu, model: SubmenuCreateUpdate, menu_id: UUID) -> Submenu:
        stmt = select(Menu).filter_by(id=menu_id)
        result = await self.__session.execute(stmt)
        menu = result.scalar_one()
        if not menu:
            raise ValueError("menu not found")

        new_submenu = entity(**model.model_dump(), menu=menu)
        self.__session.add(new_submenu)
        await self.__session.commit()
        await self.__session.refresh(new_submenu)
        return new_submenu

    async def update(self, entity: Submenu, model: SubmenuCreateUpdate, menu_id: UUID, submenu_id: UUID) -> Submenu:
        existing_submenu = await self.get_by_id(entity, menu_id, submenu_id)

        for field, value in model.dict().items():
            setattr(existing_submenu, field, value)

        await self.__session.commit()
        await self.__session.refresh(existing_submenu)
        return existing_submenu

    async def delete(self, entity: Submenu, menu_id: UUID, submenu_id: UUID) -> dict:
        stmt = delete(entity).where(and_(entity.id == submenu_id, entity.menu_id == menu_id))
        result = await self.__session.execute(stmt)
        if result.rowcount == 0:
            raise HTTPException(
                status_code=404, detail="submenu is not found.")

        await self.__session.commit()
        return {"status": True, "message": "The submenu has been deleted"}
