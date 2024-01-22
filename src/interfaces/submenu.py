from uuid import UUID

from fastapi import APIRouter, status

from config.database import get_db
from src.applications.submenu import SubmenuService
from src.domain.DTO.menu import SubmenuBase, SubmenuCreateUpdate
from src.domain.models.menu import Submenu

router_submenu = APIRouter()


@router_submenu.get('')
async def get_menu(target_menu_id: UUID):
    async with get_db() as session:
        service = SubmenuService(session)
    return await service.get_submenu(Submenu, target_menu_id)


@router_submenu.get('/{target_submenu_id}', response_model=SubmenuBase)
async def get_menu_by_id(target_menu_id: UUID, target_submenu_id: UUID):
    async with get_db() as session:
        service = SubmenuService(session)
    return await service.get_submenu_by_id(Submenu, target_menu_id, target_submenu_id)


@router_submenu.post('', status_code=status.HTTP_201_CREATED)
async def create_submenu(submenu: SubmenuCreateUpdate, target_menu_id: UUID):
    async with get_db() as session:
        service = SubmenuService(session)
    return await service.create_submenu(Submenu, submenu, target_menu_id)


@router_submenu.patch('/{target_submenu_id}')
async def update_menu(target_menu_id: UUID, target_submenu_id: UUID, submenu: SubmenuCreateUpdate):
    async with get_db() as session:
        service = SubmenuService(session)
    return await service.update_submenu(Submenu, submenu, target_menu_id, target_submenu_id)


@router_submenu.delete('/{target_submenu_id}')
async def delete_menu(target_menu_id: UUID, target_submenu_id: UUID):
    async with get_db() as session:
        service = SubmenuService(session)
    return await service.delete_submenu(Submenu, target_menu_id, target_submenu_id)
