from uuid import UUID

from fastapi import APIRouter, status

from config.database import get_db
from src.applications.menu import MenuService
from src.domain.DTO.menu import MenuBase, MenuCreateUpdate
from src.domain.models.menu import Menu

router_menu = APIRouter()


@router_menu.get('')
async def get_menu():
    async with get_db() as session:
        service = MenuService(session)
    return await service.get_menu(Menu)


@router_menu.get('/{target_menu_id}', response_model=MenuBase)
async def get_menu_by_id(target_menu_id: UUID):
    async with get_db() as session:
        service = MenuService(session)
    return await service.get_menu_by_id(Menu, target_menu_id)


@router_menu.post('', status_code=status.HTTP_201_CREATED)
async def create_menu(menu: MenuCreateUpdate):
    async with get_db() as session:
        service = MenuService(session)
    return await service.create_menu(Menu, menu)


@router_menu.patch('/{target_menu_id}')
async def update_menu(target_menu_id: UUID, menu: MenuCreateUpdate):
    async with get_db() as session:
        service = MenuService(session)
    return await service.update_menu(Menu, menu, target_menu_id)


@router_menu.delete('/{target_menu_id}')
async def delete_menu(target_menu_id: UUID):
    async with get_db() as session:
        service = MenuService(session)
    return await service.delete_menu(Menu, target_menu_id)
