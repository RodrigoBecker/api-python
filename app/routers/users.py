from typing import Any

from fastapi import status
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from starlette.status import HTTP_201_CREATED, HTTP_202_ACCEPTED
from starlette.types import Message

from app.interfaces.commons import APIBadRequest, APIForbidden
from app.interfaces.users import (UserCreateInput, UserCreateOutput,
                                  UserDeletedOutput, UsersOutput)
from app.services.service_users import UseCaseServiceUsers

router = InferringRouter()


@cbv(router)
class UserController:
    def __init__(self) -> None:
        self.__service = UseCaseServiceUsers()

    @router.get(
        path="/user",
        responses={
            status.HTTP_200_OK: {"model": UsersOutput, "decription": "Received user"},
            status.HTTP_400_BAD_REQUEST: {
                "model": APIBadRequest,
                "description": "Bad Request User, Please check your request",
            },
            status.HTTP_403_FORBIDDEN: {"model": APIForbidden, "description": ""},
        },
    )
    async def get_user(self) -> Any:
        return self.__service.get_users()

    @router.post(
        "/user",
        status_code=HTTP_201_CREATED,
        responses={
            status.HTTP_201_CREATED: {"model": UserCreateOutput, "description": ""},
            status.HTTP_403_FORBIDDEN: {"model": APIForbidden, "description": ""},
        },
    )
    async def insert_user(self, payload: UserCreateInput) -> Any:
        self.__service.insert_user(user=payload)
        return UserCreateOutput(message="User created successul!").dict()

    @router.delete(
        "/user/{id_user}",
        status_code=HTTP_202_ACCEPTED,
        responses={
            status.HTTP_202_ACCEPTED: {"model": UserDeletedOutput, "description": ""},
            status.HTTP_403_FORBIDDEN: {"model": APIForbidden, "decription": ""},
        },
    )
    async def delete_user(self) -> Any:
        return {}
