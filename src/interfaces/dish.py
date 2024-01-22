from uuid import UUID

from fastapi import APIRouter, status

from config.database import get_db
from src.applications.dish import DishService
from src.domain.DTO.menu import DishCreateUpdate
from src.domain.models.menu import Dish

router_dish = APIRouter()


@router_dish.get('')
async def get_dish(target_submenu_id: UUID):
    async with get_db() as session:
        service = DishService(session)
    return await service.get_dish(Dish, target_submenu_id)


@router_dish.get('/{target_dish_id}')
async def get_dish_by_id(target_submenu_id: UUID, target_dish_id: UUID):
    async with get_db() as session:
        service = DishService(session)
    return await service.get_dish_by_id(Dish, target_submenu_id, target_dish_id)


@router_dish.post('', status_code=status.HTTP_201_CREATED)
async def create_dish(dish: DishCreateUpdate, target_submenu_id: UUID):
    async with get_db() as session:
        service = DishService(session)
    return await service.create_dish(Dish, dish, target_submenu_id)


@router_dish.patch('/{target_dish_id}')
async def update_dish(target_submenu_id: UUID, target_dish_id: UUID, dish: DishCreateUpdate):
    async with get_db() as session:
        service = DishService(session)
    return await service.update_dish(Dish, dish, target_submenu_id, target_dish_id)


@router_dish.delete('/{target_dish_id}')
async def delete_dish(target_menu_id: UUID, target_submenu_id: UUID, target_dish_id: UUID):
    async with get_db() as session:
        service = DishService(session)
    return await service.delete_dish(Dish, target_menu_id, target_submenu_id, target_dish_id)
