import os
from dotenv import load_dotenv

load_dotenv()

# PostgreSQL: DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/booking
DATABASE_URL = os.getenv("DATABASE_URL")
