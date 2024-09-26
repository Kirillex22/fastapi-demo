from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from db import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print("base cleared and gotova k rabote")
    yield
    print("turning off")
app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)



