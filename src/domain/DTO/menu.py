from uuid import UUID

from pydantic import BaseModel, constr, validator


class MenuBase(BaseModel):
    id: UUID
    title: constr(max_length=50)
    description: constr(max_length=256)
    submenus_count: int
    dishes_count: int

    class Config:
        from_attributes = True


class MenuCreateUpdate(BaseModel):
    title: constr(max_length=50)
    description: constr(max_length=256)

    class Config:
        from_attributes = True


class SubmenuBase(BaseModel):
    id: UUID
    title: constr(max_length=50)
    description: constr(max_length=256)
    menu_id: UUID
    dishes_count: int

    class Config:
        from_attributes = True


class SubmenuCreateUpdate(BaseModel):
    title: constr(max_length=50)
    description: constr(max_length=256)

    class Config:
        from_attributes = True


class DishCreateUpdate(BaseModel):
    title: constr(max_length=50)
    description: constr(max_length=256)
    price: float

    @validator("price")
    def validate_price(cls, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        return value

    class Config:
        from_attributes = True
