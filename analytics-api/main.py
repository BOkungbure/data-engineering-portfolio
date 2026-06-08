import os
from fastapi import FastAPI
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
