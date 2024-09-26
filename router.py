from html.entities import html5

from repository import TaskRepo
from schemas import STask, STaskAdd, STaskId
from typing import Annotated
from fastapi import Depends, APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepo.find_all()
    return tasks


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepo.add_one(task)
    return {"ok": True, "task_id": task_id}