
# FastAPI Backend Starter

A production-ready FastAPI starter template with a scalable project structure and modern development tools.

## Features

- FastAPI
- uv package manager
- Environment-based configuration
- Modular project structure
- SQLAlchemy (planned)
- Alembic migrations (planned)
- PostgreSQL (planned)
- Redis (planned)
- JWT Authentication (planned)
- Docker support (planned)
- Pytest (planned)
- GitHub Actions (planned)

## Project Structure

```text
.
├── app
│   ├── api
│   ├── core
│   ├── db
│   ├── middleware
│   ├── models
│   ├── repositories
│   ├── schemas
│   ├── services
│   ├── utils
│   └── main.py
├── migrations
├── tests
├── docker
├── scripts
├── pyproject.toml
├── uv.lock
└── README.md
```

## Getting Started

```bash
uv sync
uv run uvicorn app.main:app --reload
```

API Documentation:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Development Workflow

- main → Production
- develop → Integration
- feature/* → Feature development

## Configuration

The project uses **pydantic-settings** to manage configuration.

Create your local environment file:

```bash
cp .env.example .env
```

Application settings are loaded automatically from `.env`.