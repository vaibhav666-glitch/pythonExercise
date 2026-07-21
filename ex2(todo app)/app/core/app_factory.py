from fastapi import FastAPI

from app.routes import register_routes
from app.core.startup import register_startup_events


def create_application() -> FastAPI:
    """
    Application Factory.

    Responsible only for creating
    and configuring the FastAPI application.
    """

    app = FastAPI(
        title="Todo API",
        version="1.0.0",
        description="Todo Application",
    )

    register_routes(app)

    register_startup_events(app)

    return app