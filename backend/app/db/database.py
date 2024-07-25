import os

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import registry, sessionmaker

database_url = os.environ.get("DATABASE_URL")
async_database_url = os.environ.get("ASYNC_DATABASE_URL")

if not database_url or not async_database_url:
    raise ValueError("Database url is not set")

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async_engine = create_async_engine(async_database_url)

mapper_registry = registry()
Base = mapper_registry.generate_base()
