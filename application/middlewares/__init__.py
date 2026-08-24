from cors import add_cors_middleware
from typing import Optional

async def all_middlewares(app, handler:Optional):
    add_cors_middleware(app)

__all__ = ["all_middlewares"]