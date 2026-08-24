from datetime import datetime
from typing import List, Optional

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, relationship

from base import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)

    # Role Name
    role_name: Mapped[str] = Column(String(255), nullable=False)

    # Check Role Activation ( For Custom Roles )
    is_active: Mapped[bool] = Column(Boolean, default=True)