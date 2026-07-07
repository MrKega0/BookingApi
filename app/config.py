import os

# PostgreSQL: DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/booking
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./booking.db")
