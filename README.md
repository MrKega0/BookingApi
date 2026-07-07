# Booking API

Учебный проект: REST API для системы записи на услуги (FastAPI + SQLAlchemy async).

## Запуск

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger: http://127.0.0.1:8000/docs

## Структура

Логика появления слоёв — сверху вниз:

```
app/
  config.py            — 1. настройки
  deps.py              — 2. зависимости (сессия БД)
  db/
    base.py            — 3. база SQLAlchemy
    session.py         — 4. подключение к БД
    services/          — 5. сущность «услуга» (всё про неё в БД)
      model.py         —    таблица
      schemas.py       —    форматы запроса/ответа
      crud.py          —    запросы к БД
  routers/
    services.py        — 6. HTTP-эндпоинты для услуг
  main.py              — 7. собираем приложение
```

Новая сущность (например, `bookings`):
- папка `db/bookings/` → model, schemas, crud
- файл `routers/bookings.py`
- подключить в `main.py`

## Эндпоинты

- `GET /` — проверка, что сервер жив
- `GET /services` — список услуг
- `POST /services` — создать услугу

По умолчанию база — SQLite (`booking.db`). PostgreSQL — через `DATABASE_URL` (см. `.env.example`).
