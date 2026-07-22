from fastapi import FastAPI

#from app.api.v1.todo_routes import router as todo_router
from app.api.v1.user_routes import router as user_router


def register_routes(app: FastAPI) -> None:

    app.include_router(
        user_router,
        prefix="/api/v1/users",
        tags=["Users"]
    )

    # app.include_router(
    #     todo_router,
    #     prefix="/api/v1/todos",
    #     tags=["Todos"]
    # )