import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.engine import CursorResult
from sqlalchemy.ext.asyncio.engine import AsyncConnection
from sqlalchemy.schema import CreateTable

import domains
import tables
from conf.settings import settings
from dependencies import engine_begin, engine_connect

app = FastAPI()


@app.on_event("startup")
async def startup():
    print("on startup")


@app.on_event("shutdown")
async def shutdown():
    print("on shutdown")


@app.get("/init")
async def create_database(conn: AsyncConnection = Depends(engine_begin)):
    # await conn.execute(CreateTable(tables.todos))
    return {"Database": "Created"}


@app.get("/")
async def read_all(conn: AsyncConnection = Depends(engine_connect)):
    cr: CursorResult = await conn.execute(tables.todos.select())
    # 순차적 데이터 조작이 필요한 경우 CursorResult 인스턴스 이용
    """
    for row in cr:
        print(row)
    """
    # 데이터를 단순히 반환하기 위해서는 fetchall()
    return cr.fetchall()


@app.post("/")
async def create_todo(
    todo: domains.Todo, conn: AsyncConnection = Depends(engine_begin)
):
    await conn.execute(
        tables.todos.insert().values(
            title=todo.title,
            description=todo.description,
            priority=todo.priority,
            complete=todo.complete,
        )
    )
    return successful_response(201)


@app.get("/todo/{todo_id}")
async def read_todo(todo_id: int, conn: AsyncConnection = Depends(engine_connect)):
    todo_model = await conn.execute(
        tables.todos.select().where(tables.todos.c.id == todo_id)
    ).first()

    if todo_model:
        return todo_model

    raise http_exception()


@app.put("/{todo_id}")
async def update_todo(
    todo_id: int, todo: domains.Todo, conn: AsyncConnection = Depends(engine_begin)
):
    todo_model = await conn.execute(
        tables.todos.select().where(tables.todos.c.id == todo_id)
    ).first()

    if todo_model:
        await conn.execute(
            tables.todos.update()
            .where(tables.todos.c.id == todo_id)
            .values(
                title=todo.title,
                description=todo.description,
                priority=todo.priority,
                complete=todo.complete,
            )
        )
        return successful_response(200)

    raise http_exception()


@app.delete("/{todo_id}")
async def delete_todo(todo_id: int, conn: AsyncConnection = Depends(engine_begin)):
    todo_model = await conn.execute(
        tables.todos.select().where(tables.todos.c.id == todo_id)
    ).first()

    if todo_model:
        await conn.execute(tables.todos.delete().where(tables.todos.c.id == todo_id))

        return successful_response(200)

    raise http_exception()


def successful_response(status_code: int):
    return {"status": status_code, "transaction": "Successful"}


def http_exception():
    return HTTPException(status_code=404, detail="Todo not found")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings["HOST"],
        port=settings["PORT"],
        debug=settings["DEBUG"],
        reload=settings["RELOAD"],
    )
