import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

# BASE DIRECTORY

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# DATABASE PATH

DB_PATH = os.path.join(BASE_DIR, "database", "hids.db")

DATABASE_URL = f"sqlite:///{DB_PATH}"

# ENGINE

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # required for SQLite
    echo=False
)

# THREAD SAFE SESSION

SessionLocal = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

# BASE MODEL

Base = declarative_base()

# GET DB SESSION

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# INIT DATABASE

def init_db():
    """
    Create tables in database
    """
    from database import models  # IMPORTANT: load models first

    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully")


# CLOSE SESSION

def close_db():
    SessionLocal.remove()
