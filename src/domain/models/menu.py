import uuid
from typing import List

from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database import Base
from src.domain.models.abstract_models import AbstractModel


class Menu(Base):
    __tablename__ = 'menu'
    __mapper_args__ = {"concrete": True}
    __table_args__ = {"postgresql_inherits": AbstractModel.__table__.name}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    submenus: Mapped[List["Submenu"]] = relationship("Submenu", back_populates="menu", lazy="selectin")

    @property
    def submenus_count(self) -> int:
        return len(self.submenus)

    @property
    def dishes_count(self) -> int:
        return sum(submenu.dishes_count for submenu in self.submenus)


class Submenu(Base):
    __tablename__ = 'submenu'
    __mapper_args__ = {"concrete": True}
    __table_args__ = {"postgresql_inherits": AbstractModel.__table__.name}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    menu_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey(
        'menu.id', ondelete='CASCADE'), nullable=False)
    menu: Mapped["Menu"] = relationship("Menu", back_populates="submenus")
    dishes: Mapped[List["Dish"]] = relationship("Dish", back_populates="submenu", lazy="selectin")

    @property
    def dishes_count(self) -> int:
        return len(self.dishes)


class Dish(Base):
    __tablename__ = 'dish'
    __mapper_args__ = {"concrete": True}
    __table_args__ = {"postgresql_inherits": AbstractModel.__table__.name}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    price: Mapped[float] = mapped_column(Float(precision=2), nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    submenu_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey(
        'submenu.id', ondelete='CASCADE'), nullable=False)
    submenu: Mapped["Submenu"] = relationship("Submenu", back_populates="dishes")
