import os
from fastapi_router_controller import ControllerLoader

dir = os.path.dirname(__file__)

ControllerLoader.load(dir, __package__)
