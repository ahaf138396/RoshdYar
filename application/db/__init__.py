from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from ..configs.db import get_db

class Base(DeclarativeBase):
    pass

settings = get_db()
engine = create_async_engine(settings.database_url, echo=False, future=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get() -> AsyncIterator[AsyncSession]:
    async with AsyncSessionLocal() as session:
        yield session