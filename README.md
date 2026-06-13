# Clinic Service API
FastAPI clinic services directory for Sierra Leone — SDG 3: Good Health and Well-being

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Problem
In Sierra Leone, patients often travel to health facilities without knowing
whether that facility offers the service they need. There is no single open
directory of clinics and their services. This API solves that.

## SDG Alignment
This project supports SDG 3 — Good Health and Well-being by making clinic
and service information searchable and openly available. The is_free field
flags Free Healthcare Initiative coverage, supporting **SDG 10 — Reduced
Inequalities**. The MIT license makes it a digital public good.

## Features
- Search clinics by name, district or service
- Full CRUD for clinics, services and reviews
- JWT authentication with role-based access
- Async external health feed endpoint
- Swagger UI and ReDoc documentation

## Tech Stack
- FastAPI + Python 3.11
- PostgreSQL + SQLAlchemy ORM
- OAuth2 + JWT (python-jose)
- bcrypt password hashing (passlib)
- Supabase (hosted PostgreSQL)

## Getting Started

### Prerequisites
- Python 3.11+
- Git

### Setup
```bash
git clone https://github.com/alenajall/Clinic-service-api.git
cd Clinic-service-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Fill in your DATABASE_URL and SECRET_KEY in .env
```

## Run

```bash
uvicorn app.main:app --reload
```

## Docs
 • Swagger UI: http://localhost:8000/docs
 • ReDoc: http://localhost:8000/redoc

## API Workflow
 1. Register: POST /api/v1/auth/register
 2. Login: POST /api/v1/auth/login → copy the token
 3. Click Authorize in Swagger UI → paste token
 4. Search clinics: GET /api/v1/clinics/search?service=malaria
 5. Create clinic (admin only): POST /api/v1/clinics/

## API Endpoints

> 
> |Method|Path                              |Auth   |Description     |
> |------|----------------------------------|-------|----------------|
> |POST  |/api/v1/auth/register             |No     |Register user   |
> |POST  |/api/v1/auth/login                |No     |Get JWT token   |
> |GET   |/api/v1/clinics/                  |No     |List clinics    |
> |GET   |/api/v1/clinics/search            |No     |Search clinics  |
> |POST  |/api/v1/clinics/                  |Admin  |Create clinic   |
> |PUT   |/api/v1/clinics/{id}              |Admin  |Update clinic   |
> |DELETE|/api/v1/clinics/{id}              |Admin  |Delete clinic   |
> |GET   |/api/v1/clinics/{id}/health-alerts|No     |Live health data|
> |GET   |/api/v1/services/                 |No     |List services   |
> |POST  |/api/v1/services/                 |Admin  |Create service  |
> |GET   |/api/v1/reviews/clinic/{id}       |No     |Get reviews     |
> |POST  |/api/v1/reviews/                  |Patient|Add review      |

## Running Tests

```bash
pytest
```

## Team
 • Jalloh (Member 1) — Database & Core
 • Aminata Bangura (Member 2) — Authentication & Security
 • Musu Bangura (Member 3) — API Routes & Endpoints
 • Alpha Kanji Daramy (Member 4) — Documentation, Testing & SDG

## License
MIT — see LICENSE
