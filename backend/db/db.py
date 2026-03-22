import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Project root = .../backend/db/db.py -> parents[2]
_project_root = Path(__file__).resolve().parents[2]
load_dotenv(_project_root / ".env")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False},
    echo=False,  # Set to True for SQL debug logging
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_engine():
    """Expose engine for migrations and direct access."""
    return engine