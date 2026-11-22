import os
from dotenv import load_dotenv
from pathlib import Path
from fastapi.templating import Jinja2Templates

load_dotenv()

templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

# PostgreSQL: DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/booking
DATABASE_URL = os.getenv("DATABASE_URL")
print(1)