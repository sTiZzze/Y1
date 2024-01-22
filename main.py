from fastapi import FastAPI

from src.interfaces.dish import router_dish
from src.interfaces.menu import router_menu
from src.interfaces.submenu import router_submenu

app = FastAPI()

app.include_router(router_menu, prefix="/api/v1/menus", tags=["menus"])
app.include_router(router_submenu, prefix="/api/v1/menus/{target_menu_id}/submenus", tags=["submenus"])
app.include_router(router_dish,
                   prefix="/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes",
                   tags=["dishes"])
