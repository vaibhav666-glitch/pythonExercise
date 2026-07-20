from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

# Create the SQLAlchemy Engine
engine = create_engine(
    settings.database_url,
    echo=False,          # Set True to print SQL queries in the terminal
    future=True
)

# Session Factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

# Base class for all ORM models
Base = declarative_base()


def get_db():
    """
    Dependency that provides a database session.

    A new session is created for every request and
    automatically closed after the request finishes.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()