from fastapi import FastAPI


def register_startup_events(app: FastAPI):

    @app.on_event("startup")
    async def startup():

        print("Application Started")

    @app.on_event("shutdown")
    async def shutdown():

        print("Application Stopped")