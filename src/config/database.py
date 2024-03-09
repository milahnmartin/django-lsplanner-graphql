from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database URL (replace with your actual database URL)
DATABASE_URL = "postgresql://lsplanner:lsplanner@localhost/lsplanner"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
