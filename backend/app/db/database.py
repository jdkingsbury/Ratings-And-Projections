import os

from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker

database_url = os.environ.get("DATABASE_URL")
if not database_url:
    raise ValueError("Database url is not set")

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

mapper_registry = registry()
Base = mapper_registry.generate_base()
