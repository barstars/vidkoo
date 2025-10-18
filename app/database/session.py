from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import setting
from typing import AsyncGenerator

# Create an asynchronous database engine using the connection URL from settings
engine = create_async_engine(setting.DATABASE_URL)

# Create a session factory that will generate AsyncSession instances
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db() -> AsyncGenerator:
	'''Dependency for FastAPI routes.
	Provides a database session and ensures proper cleanup after the request.
	'''
	async with SessionLocal() as session:
		yield session