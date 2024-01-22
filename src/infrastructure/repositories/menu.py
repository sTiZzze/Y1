from typing import Iterable
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.domain.DTO.menu import MenuCreateUpdate
from src.domain.models.menu import Menu


class MenuRepository:
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def get_all(self, entity: Menu) -> Iterable[Menu]:
        query = await self.__session.execute(select(entity))
        return query.scalars().all()

    async def get_by_id(self, entity: Menu, menu_id: UUID) -> Menu:
        query = await self.__session.execute(select(entity).filter_by(id=menu_id))
        menu = query.scalar()
        if not menu:
            raise HTTPException(
                status_code=404, detail="menu not found")
        return menu

    async def create(self, entity: Menu, model: MenuCreateUpdate) -> Menu:
        new_menu = entity(**model.model_dump())
        self.__session.add(new_menu)
        await self.__session.commit()
        await self.__session.refresh(new_menu)
        return new_menu

    async def update(self, entity: Menu, model: MenuCreateUpdate, menu_id: UUID) -> Menu:
        existing_menu = await self.get_by_id(entity, menu_id)

        for field, value in model.dict().items():
            setattr(existing_menu, field, value)

        await self.__session.commit()
        await self.__session.refresh(existing_menu)
        return existing_menu

    async def delete(self, entity: Menu, menu_id: UUID) -> dict:
        stmt = delete(entity).where(entity.id == menu_id)
        result = await self.__session.execute(stmt)
        if result.rowcount == 0:
            raise HTTPException(
                status_code=404, detail="Menu is not found.")

        await self.__session.commit()
        return {"status": True, "message": "The menu has been deleted"}
