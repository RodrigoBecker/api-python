from fastapi import FastAPI
from app.routers.users import router as user_router
from app.routers.books import router as book_router

API_VERSION = "v1"


tags_metadata = [{"name": "Users"}, {"name": "Books"}]


def create_app() -> FastAPI:
    app = FastAPI(
        title="API PYTHON",
        description="My First API with python",
        version=API_VERSION,
        openapi_tags=tags_metadata,
        root_path="",
    )

    app.router.redirect_slashes = True
    app.include_router(user_router, prefix=f"/{API_VERSION}", tags=["Users"])
    app.include_router(book_router, prefix=f"/{API_VERSION}", tags=["Books"])

    return app
