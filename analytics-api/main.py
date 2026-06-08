import os
from fastapi import FastAPI, Query
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI(
    title="Analytics API",
    description="Business metrics API by Yomi Okungbure",
    version="2.0.0"
)

def get_connection():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)

@app.get("/")
def root():
    return {"message": "Analytics API is live 🚀", "author": "Yomi Okungbure"}

@app.get("/metrics/revenue")
def get_revenue():
    """Returns total revenue across all regions."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(revenue) AS total_revenue FROM sales;")
    result = cursor.fetchone()
    conn.close()
    return {"total_revenue": result["total_revenue"], "currency": "USD"}

@app.get("/metrics/revenue/{region}")
def get_revenue_by_region(region: str):
    """Returns revenue for a specific region."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT SUM(revenue) AS total_revenue FROM sales WHERE LOWER(region) = LOWER(%s);",
        (region,)
    )
    result = cursor.fetchone()
    conn.close()
    if result["total_revenue"] is None:
        return {"error": f"No data found for region: {region}"}
    return {"region": region, "total_revenue": result["total_revenue"], "currency": "USD"}

@app.get("/metrics/summary")
def get_summary():
    """Returns all records from the sales table."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales ORDER BY date;")
    rows = cursor.fetchall()
    conn.close()
    return {"data": [dict(row) for row in rows], "record_count": len(rows)}

@app.get("/metrics/filter")
def filter_by_date(
    start_date: date = Query(..., description="Start date e.g. 2026-01-01"),
    end_date: date = Query(..., description="End date e.g. 2026-12-31")
):
    """Returns all sales records within a date range."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM sales WHERE date BETWEEN %s AND %s ORDER BY date;",
        (start_date, end_date)
    )
    rows = cursor.fetchall()
    conn.close()
    return {"data": [dict(row) for row in rows], "record_count": len(rows)}

@app.get("/metrics/trends")
def get_trends():
    """Returns month-over-month revenue growth by region."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            region,
            TO_CHAR(date, 'YYYY-MM') AS month,
            SUM(revenue) AS monthly_revenue,
            LAG(SUM(revenue)) OVER (PARTITION BY region ORDER BY TO_CHAR(date, 'YYYY-MM')) AS previous_month_revenue,
            ROUND(
                (SUM(revenue) - LAG(SUM(revenue)) OVER (PARTITION BY region ORDER BY TO_CHAR(date, 'YYYY-MM')))
                * 100.0
                / NULLIF(LAG(SUM(revenue)) OVER (PARTITION BY region ORDER BY TO_CHAR(date, 'YYYY-MM')), 0),
                2
            ) AS growth_percentage
        FROM sales
        GROUP BY region, TO_CHAR(date, 'YYYY-MM')
        ORDER BY region, month;
    """)
    rows = cursor.fetchall()
    conn.close()
    return {"trends": [dict(row) for row in rows]}

@app.get("/metrics/top-region")
def get_top_region():
    """Returns the highest revenue generating region."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT region, SUM(revenue) AS total_revenue
        FROM sales
        GROUP BY region
        ORDER BY total_revenue DESC
        LIMIT 1;
    """)
    result = cursor.fetchone()
    conn.close()
    return {"top_region": dict(result)}
