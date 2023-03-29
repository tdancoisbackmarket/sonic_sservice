from fastapi import FastAPI
from .database import get_db
from .database import Post
from .database import get_url
from sqlalchemy import create_engine
from sqlalchemy import select
from sqladmin import Admin, ModelView
app = FastAPI()

admin = Admin(app, create_engine(get_url()))


class PostAdmin(ModelView, model=Post):
    column_list = [Post.id, Post.content]


admin.add_view(PostAdmin)

@app.get("/")
def root():
    with get_db() as db:
        return [*db.scalars(select(Post))]
