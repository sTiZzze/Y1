import uuid
from datetime import datetime

from sqlalchemy import UUID, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from config.database import Base


class AbstractModel(Base):
    __tablename__ = "abstract_instance"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now())