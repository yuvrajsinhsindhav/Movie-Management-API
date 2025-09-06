# Movie-Management-API
🎬 Movie Management API

A simple Movie Management API built with FastAPI.
This project supports CRUD operations, database persistence, request validation, and auto-generated Swagger/OpenAPI docs.

Features:-

Add, update, delete, and fetch movies 🎥
Built with FastAPI (lightweight & high-performance)
Database support (SQLite by default, easily switchable)
Automatic Swagger/OpenAPI 3.0 docs at /docs
Proper error handling & validation
Code structured with Handler, Service, DAO layers
Includes unit tests (via pytest)

* Tech Stack

Language: Python 3.10+
Framework: FastAPI
Database: SQLite (default)
ORM: SQLAlchemy
Validation: Pydantic
Testing: Pytest

**📂 Project Structure**
Movie-Management_API/
│── app/
│   ├── __init__.py
│   ├── main.py          # Entry point
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # Database connection
│   ├── handlers/        # Route handlers
│   ├── services/        # Business logic
│   ├── dao/             # Data access layer
│── tests/               # Unit tests
│── requirements.txt
│── README.md
