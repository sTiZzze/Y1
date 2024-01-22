from typing import Iterable
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import and_, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.domain.DTO.menu import DishCreateUpdate
from src.domain.models.menu import Dish, Submenu
from src.infrastructure.utils.dish_format import format_str


class DishRepository:
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def get_all(self, entity: Dish, submenu_id: UUID) -> Iterable[Dish]:
        query = await self.__session.execute(select(entity).filter(entity.submenu_id == submenu_id))
        return query.scalars().all()

    async def get_by_id(self, entity: Dish, submenu_id: UUID, dish_id: UUID) -> Dish:
        query = await self.__session.execute(select(entity).filter_by(id=dish_id, submenu_id=submenu_id))
        dish = query.scalar()
        if not dish:
            raise HTTPException(
                status_code=404, detail="dish not found")

        dish.price = format_str(dish.price)
        return dish

    async def create(self, entity: Dish, model: DishCreateUpdate, submenu_id: UUID) -> Dish:
        stmt = select(Submenu).filter_by(id=submenu_id)
        result = await self.__session.execute(stmt)
        submenu = result.scalar_one()
        if not submenu:
            raise ValueError("submenu not found")

        new_dish = entity(**model.model_dump(), submenu=submenu)
        self.__session.add(new_dish)
        await self.__session.commit()
        await self.__session.refresh(new_dish)
        new_dish.price = format_str(new_dish.price)
        return new_dish

    async def update(self, entity: Dish, model: DishCreateUpdate, submenu_id: UUID, dish_id: UUID) -> Dish:
        existing_dish = await self.get_by_id(entity, submenu_id, dish_id)

        for field, value in model.dict().items():
            setattr(existing_dish, field, value)

        await self.__session.commit()
        await self.__session.refresh(existing_dish)
        existing_dish.price = format_str(existing_dish.price)
        return existing_dish

    async def delete(self, entity: Dish, menu_id, submenu_id: UUID, dish_id: UUID) -> dict:
        stmt = delete(entity).where(and_(entity.id == dish_id, entity.submenu_id == submenu_id))
        result = await self.__session.execute(stmt)
        if result.rowcount == 0:
            raise HTTPException(
                status_code=404, detail="Dish is not found.")

        await self.__session.commit()
        return {"status": True, "message": "The dish has been deleted"}
