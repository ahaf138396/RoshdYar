from fastapi import FastAPI

from middlewares import all_middlewares

app = FastAPI(
    title="سامانه رشدیار",
    description="سامانه جامع مراکز نوآوری",
    debug=False
    )

# افزودن middleware
all_middlewares(app)
