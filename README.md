
# Task Management API

A structured RESTful API built using **FastAPI** and **SQLAlchemy** to manage tasks with strong validation, enum-based status control, and proper timestamp tracking.

This project demonstrates clean architecture principles, separation of concerns, and scalable API design.

---

## Tech Stack

- **FastAPI** – Modern high-performance web framework (ASGI)
- **SQLAlchemy ORM** – Database abstraction layer
- **MySQL** – Relational database
- **Pydantic** – Data validation and serialization
- **Uvicorn** – ASGI server

---

## Features

- Full CRUD operations
- Enum-based task status:
  - `pending`
  - `in_progress`
  - `completed`
  - `cancelled`
- Conditional validation for `cancelled_reason`
- `created_at` timestamp (auto-generated)
- `updated_at` timestamp (null until first update)
- Pagination support
- Status filtering
- Clean modular architecture
- Automatic OpenAPI documentation

---

## Project Structure
```
task-management-api/
│
├── app/
│   ├── main.py        # API routes & dependency injection
│   ├── models.py      # SQLAlchemy ORM models
│   ├── schemas.py     # Pydantic schemas & validation logic
│   ├── crud.py        # Database CRUD operations
│   ├── database.py    # Database engine & session configuration
│
├── .env               # Environment variables
├── requirements.txt   # Project dependencies
├── README.md          # Project documentation
└── LICENSE
```



---

## Setup Instructions

### 1️ Clone the repository

```bash
git clone <https://github.com/NAOUFELEX/task-management-api.git>
cd task-management-api

### 2️ Create virtual environment
python -m venv venv

Activate it:

venv\Scripts\activate

### 3 Install dependencies

pip install -r requirements.txt


### Run the Application

Server will run at:

http://127.0.0.1:8000