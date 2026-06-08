# 📊 Analytics API

A production-ready REST API built with **FastAPI** and **PostgreSQL** that serves business metrics to stakeholders — replacing manual Power BI data pulls with live, automated endpoints.

![CI/CD](https://github.com/BOkungbure/data-engineering-portfolio/actions/workflows/api-tests.yml/badge.svg)

---

## 🎯 Project Goal
Demonstrate how a data analyst can bridge into data/analytics engineering by building a real API that serves business metrics from a live database — complete with automated testing and CI/CD.

---

## 🛠️ Tech Stack
Category	Tool
Framework	FastAPI
Database	PostgreSQL (hosted on Neon)
Testing	Pytest
CI/CD	GitHub Actions
Language	Python 3.11
📡 API Endpoints
Method	Endpoint	Description
GET	/	Health check — confirms API is live
GET	/metrics/revenue	Total revenue across all regions
GET	/metrics/revenue/{region}	Total revenue for a specific region
GET	/metrics/summary	All sales records from the database
GET	/metrics/filter?start_date=&end_date=	Sales records filtered by date range
GET	/metrics/trends	Month-over-month revenue growth % per region
GET	/metrics/top-region	Highest revenue generating region
💡 Example Requests
Get revenue for North region:

GET /metrics/revenue/North
json
Copy
{
  "region": "North",
  "total_revenue": 113000,
  "currency": "USD"
}
Get trends:

GET /metrics/trends
json
Copy
{
  "trends": [
    {
      "region": "North",
      "month": "2026-01",
      "monthly_revenue": 52000,
      "previous_month_revenue": null,
      "growth_percentage": null
    },
    {
      "region": "North",
      "month": "2026-02",
      "monthly_revenue": 61000,
      "previous_month_revenue": 52000,
      "growth_percentage": 17.31
    }
  ]
}
🚀 Running Locally
1. Clone the repo:

bash
Copy
git clone https://github.com/BOkungbure/data-engineering-portfolio.git
cd data-engineering-portfolio/analytics-api
2. Install dependencies:

bash
Copy
pip install -r requirements.txt
3. Create a .env file:

bash
Copy
DATABASE_URL=your_neon_connection_string_here
4. Start the API:

bash
Copy
uvicorn main:app --reload
5. Visit the docs:

http://localhost:8000/docs
🧪 Running Tests
bash
Copy
pytest test_main.py -v
📁 Project Structure
analytics-api/
├── main.py           # API endpoints
├── test_main.py      # Automated tests
├── requirements.txt  # Dependencies
└── README.md         # You are here
👤 Author
Yomi Okungbure — Analytics Engineer in Progress
LinkedIn | GitHub
