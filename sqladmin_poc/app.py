from fastapi import FastAPI
from .database import get_db
from .database import Post
from sqlalchemy import select

app = FastAPI()


@app.get("/")
def root():
    with get_db() as db:
        return [*db.scalars(select(Post))]
