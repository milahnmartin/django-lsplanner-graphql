from fastapi import FastAPI
from src.routes import user, quota

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    app.include_router(user.router)
    app.include_router(quota.router)
