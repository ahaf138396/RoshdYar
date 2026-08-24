from datetime import datetime
from typing import List, Optional

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Text, CheckConstraint, \
    ForeignKeyConstraint
from sqlalchemy.orm import Mapped, relationship

from base import Base

class User(Base):
    __tablename__ = "users"

    __table_args__ = (
        CheckConstraint(sqltext="NOT (is_removed = TRUE AND is_active = TRUE)",
                        name="ck_user_removed_not_active"),
    )

    # User ID
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)

    # User Credential Info
    username: Mapped[str] = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = Column(String(255), nullable=False)
    email: Mapped[str] = Column(String(255), unique=True, index=True, nullable=False)

    # Role
    role: Mapped[str] = Column(
        String(50),
        ForeignKey("roles.id"),
        default="user",
        nullable=False,
    )

    is_superuser: Mapped[bool] = Column(Boolean, default=False, nullable=False)
    is_active: Mapped[bool] = Column(Boolean, default=True, Nullable=False)
    is_removed: Mapped[bool] = Column(Boolean, default=False, nullable=False)

class UserProfile(Base):
    __tablename__ = "user_profiles"

    # User ID
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False,
    )

    # Name
    first_name: Mapped[str] = Column(String(255), nullable=False)
    last_name: Mapped[str] = Column(String(255), nullable=False)

    # Communication Way
    phone_number: Mapped[str] = Column(String(255), nullable=False)
    email: Mapped[str] = Column(String(255), unique=True, index=True, nullable=False)

    # Remove Request
    removed_at: Mapped[datetime] = Column(DateTime(timezone=True), nullable=False)

class RemovedUser(Base):
    __tablename__ = "removed_users"
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False,
        index=True
    )
    removed_at: Mapped[datetime] = Column(DateTime(timezone=True), nullable=False)
    removed_by: Mapped[User] = relationship(
        "User",
        back_populates="removed_users",
        foreign_keys=[User.id]
    )


