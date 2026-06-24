# 📊 Analytics API

A FastAPI-based REST API that exposes business metrics stored in PostgreSQL, demonstrating backend engineering practices commonly used by Analytics Engineers and Data Engineers.

## Project Overview

This project replaces manual SQL queries and spreadsheet reporting with REST endpoints that deliver business metrics on demand.

It demonstrates how analytics teams can expose trusted data to downstream applications through APIs instead of manual exports.

## Architecture

```text
                Client
                  │
                  ▼
          FastAPI REST API
                  │
                  ▼
          PostgreSQL (Neon)
                  │
                  ▼
        Business Metrics & SQL
```

## Features

- RESTful API built with FastAPI
- PostgreSQL integration
- Parameterized SQL queries
- Automatic OpenAPI documentation
- Automated unit testing with Pytest
- GitHub Actions CI pipeline
- Environment variable configuration

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Backend language |
| FastAPI | REST API framework |
| PostgreSQL | Database |
| Neon | Hosted PostgreSQL |
| Pytest | Testing |
| GitHub Actions | Continuous Integration |

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Health check |
| GET | `/metrics/revenue` | Total revenue |
| GET | `/metrics/revenue/{region}` | Revenue by region |
| GET | `/metrics/summary` | Sales summary |
| GET | `/metrics/filter` | Filter by date range |
| GET | `/metrics/trends` | Monthly revenue trends |
| GET | `/metrics/top-region` | Highest revenue region |

## Project Structure

```text
analytics-api/
├── main.py
├── requirements.txt
├── test_main.py
├── .env.example
└── README.md
```

## Running Locally

```bash
git clone https://github.com/BOkungbure/data-engineering-portfolio.git
cd data-engineering-portfolio/analytics-api
pip install -r requirements.txt
uvicorn main:app --reload
```

Open the interactive API documentation at:

```text
http://localhost:8000/docs
```

## Running Tests

```bash
pytest -v
```

## CI/CD

Every push to the `main` branch automatically:

- Installs project dependencies
- Runs the automated test suite
- Verifies the application builds successfully

using GitHub Actions.

## Skills Demonstrated

- Backend API Development
- FastAPI
- PostgreSQL
- SQL
- Automated Testing
- CI/CD
- Git
- API Documentation
- Environment Variables

## Future Improvements

- JWT Authentication
- Docker support
- Pagination
- API versioning
- Request logging
- Rate limiting
- Redis caching
- Cloud deployment

## Author

**Yomi Okungbure**

Transitioning from Data Analyst to Analytics Engineer through hands-on engineering projects.

## License

MIT License
