from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os



DATABASE_URL = os.getenv("DB_URL") if os.getenv("DB_URL") else "postgresql://lsplanner:lsplanner@localhost/lsplanner"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
