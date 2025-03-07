from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Field, Session, create_engine, select
from pydantic import BaseModel

from typing import Annotated

from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from sqlalchemy.orm import sessionmaker


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:8080",
    "http://0.0.0.0:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database_rul = 'sqlite+aiosqlite:///test.db'


engine = create_async_engine(database_rul)

async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session


sess_dep = Annotated[AsyncSession, Depends(get_session)]

class Task(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    is_done: bool = Field(default=False)


class CreateTask(BaseModel):
    title: str

class EditTask(BaseModel):
    title: str
    is_done: bool

@app.get('/api/tasks')
async def get_all_tasks(session: sess_dep) -> list[Task]:
    all_tasks = await session.exec(select(Task))
    all_tasks = all_tasks.all()
    return all_tasks


@app.post('/api/tasks', status_code=201)
async def create_task(session: sess_dep, task: CreateTask) -> Task:
    new_task = Task()
    new_task.title = task.title
    session.add(new_task)
    await session.commit()
    return new_task

@app.delete('/api/tasks/{id}', status_code=204)
async def delete(session: sess_dep, id: int):
    to_delete = await session.get(Task, id)
    if not to_delete:
        raise HTTPException(404, detail='not found')
    await session.delete(to_delete)
    await session.commit()


@app.put('/api/tasks/{id}')
async def put_task(session: sess_dep, data: EditTask, id: int) -> Task:
    task = await session.get(Task, id)
    if not task:
        raise HTTPException(404, detail='not found')
    task.title = data.title
    task.is_done = data.is_done
    await session.commit()
    return task
    
