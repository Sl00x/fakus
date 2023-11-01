from fastapi.responses import JSONResponse
from fastapi_router_controller import Controller
from fastapi import APIRouter, status, Query, Body, Depends

from ..services.User import User

router = APIRouter(prefix="")
controller = Controller(router, openapi_tag={
    'name': 'Main Routes',
    'description': 'Main is an example of route using only get method'
})


@controller.use()
@controller.resource()
class RootController:
    def __init__(self, userService: User = Depends()) -> None:
        self.userService = userService

    @controller.route.get('/')
    def index(self, kwargs: None):
        print("coucou hibou")
        return self.userService.find()
