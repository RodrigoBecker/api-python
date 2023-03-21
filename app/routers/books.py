from typing import Any

from fastapi import status

from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from starlette.status import HTTP_201_CREATED, HTTP_202_ACCEPTED

from app.interfaces.commons import APIBadRequest, APIForbidden
from app.interfaces.books import (
    BooksCreateInput,
    BooksCreateOutput,
    BooksDeleteOutput,
    BooksOutput,
    BooksUpdateInfoInput,
)

router = InferringRouter()


@cbv(router)
class BookController:
    @router.get(
        path="/book",
        responses={
            status.HTTP_200_OK: {"model": BooksOutput, "description": ""},
            status.HTTP_400_BAD_REQUEST: {"model": APIBadRequest, "description": ""},
            status.HTTP_403_FORBIDDEN: {"model": APIForbidden, "description": ""},
        },
    )
    async def get_book(self) -> Any:
        return {}

    @router.post(
        path="/book",
        status_code=HTTP_201_CREATED,
        responses={
            status.HTTP_201_CREATED: {"model": BooksCreateOutput, "description": ""},
            status.HTTP_400_BAD_REQUEST: {"model": APIBadRequest, "description": ""},
            status.HTTP_403_FORBIDDEN: {"model": APIForbidden, "description": ""},
        },
    )
    async def insert_book(self, payload: BooksCreateInput) -> Any:
        return

    @router.put(
        path="/book",
        responses={
            status.HTTP_400_BAD_REQUEST: {"model": APIBadRequest, "description": ""},
            status.HTTP_403_FORBIDDEN: {"model": APIForbidden, "description": ""},
        },
    )
    async def update_info_book(self, payload: BooksUpdateInfoInput) -> Any:
        return

    @router.delete(
        path="/book",
        status_code=HTTP_202_ACCEPTED,
        responses={
            status.HTTP_202_ACCEPTED: {"model": BooksDeleteOutput, "description": ""},
            status.HTTP_400_BAD_REQUEST: {"model": APIBadRequest, "description": ""},
            status.HTTP_403_FORBIDDEN: {"model": APIForbidden, "description": ""},
        },
    )
    async def delete_book(self) -> Any:
        return
