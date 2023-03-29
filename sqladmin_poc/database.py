from contextlib import contextmanager
from typing import Iterator
from typing import Type
from urllib.parse import quote

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import as_declarative


@as_declarative()
class Base:
    __name__: str

    id: Mapped[int] = Column(Integer, primary_key=True)

class Post(Base):
    __allow_unmapped__ = True
    __tablename__ = "post"

    content = Column(String(50))



def get_url() -> str:
    """
    Return the database URL to connect to.
    """
    host = "127.0.0.1"
    port = "5432"
    username = "admin"
    password = "admin"
    dbname = "shipping-service"
    return f"postgresql://{username}:{password}@{host}:{port}/{dbname}"


def _create_session() -> Type[Session]:
    """
    Create, initialize and return a database session
    """
    # Setup database parameters
    url = get_url()
    engine = create_engine(url)

    # Create engine and session
    SessionMaker = sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
    )
    return SessionMaker  # type: ignore


SessionMaker: Type[Session] = _create_session()


def session_generator() -> Iterator[Session]:
    """
    Returns a lazy session instance, only connects to db when transaction begins. Closes connection auto-magically.
    More info: https://fastapi.tiangolo.com/tutorial/sql-databases/#main-fastapi-app
    """
    db: Session = SessionMaker()
    try:
        yield db
    finally:
        db.close()


get_db = contextmanager(session_generator)
