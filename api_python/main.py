import src.controllers

from fastapi import FastAPI
from fastapi_router_controller import Controller, ControllersTags

from config import Config

app = FastAPI(
    openapi_tags=ControllersTags,
)

for router in Controller.routers():
    app.include_router(router)
