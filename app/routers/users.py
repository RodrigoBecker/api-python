from typing import Any

from fastapi import status
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv

router = InferringRouter()


@cbv(router)
class UserController:
    @router.get(
        "/user", responses={status.HTTP_200_OK: {"model": "", "decription": ""}}
    )
    async def get_user(self) -> Any:
        return {}
