import uvicorn

from server import create_app

app = create_app()

if __name__ == "__main__":
    params = {"host": "127.0.0.1", "port": 9001}
    uvicorn.run(app, **params)
