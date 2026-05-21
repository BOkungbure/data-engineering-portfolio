from fastapi import FastAPI
from datetime import date

app = FastAPI(
    title="Analytics API",
    description="Business metrics API by Yomi Okungbure",
    version="1.0.0"
)

# --- Sample Data (replace with real DB queries later) ---
sales_data = [
    {"date": "2026-01-01", "region": "North", "revenue": 52000, "units": 430},
    {"date": "2026-02-01", "region": "North", "revenue": 61000, "units": 510},
    {"date": "2026-01-01", "region": "South", "revenue": 47000, "units": 390},
    {"date": "2026-02-01", "region": "South", "revenue": 53000, "units": 445},
]

# --- Endpoints ---
@app.get("/")
def root():
    return {"message": "Analytics API is live 🚀", "author": "Yomi Okungbure"}

@app.get("/metrics/revenue")
def get_revenue():
    """Returns total revenue across all regions."""
    total = sum(row["revenue"] for row in sales_data)
    return {"total_revenue": total, "currency": "USD"}

@app.get("/metrics/revenue/{region}")
def get_revenue_by_region(region: str):
    """Returns revenue for a specific region."""
    filtered = [row for row in sales_data if row["region"].lower() == region.lower()]
    if not filtered:
        return {"error": f"No data found for region: {region}"}
    total = sum(row["revenue"] for row in filtered)
    return {"region": region, "total_revenue": total, "currency": "USD"}

@app.get("/metrics/summary")
def get_summary():
    """Returns a full summary of all metrics."""
    return {"data": sales_data, "record_count": len(sales_data)}
