import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Project root = .../backend/db/db.py -> parents[2]
_project_root = Path(__file__).resolve().parents[2]
# override=True: .env wins over pre-set env (systemd/shell may set a stale DATABASE_URL).
load_dotenv(_project_root / ".env", override=True)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

_sqlite = DATABASE_URL.strip().lower().startswith("sqlite")
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if _sqlite else {},
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
