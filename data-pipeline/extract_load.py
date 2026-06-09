import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def extract(filepath: str) -> pd.DataFrame:
    """Extract raw data from CSV file."""
    print(f"Extracting data from {filepath}...")
    df = pd.read_csv(filepath)
    print(f"Extracted {len(df)} rows.")
    return df

def load(df: pd.DataFrame):
    """Load raw data into PostgreSQL."""
    print("Loading data into PostgreSQL...")
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    # Create raw table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS raw_sales (
            id SERIAL PRIMARY KEY,
            date DATE,
            region VARCHAR(50),
            product VARCHAR(50),
            units_sold INTEGER,
            revenue INTEGER,
            loaded_at TIMESTAMP DEFAULT NOW()
        );
    """)

    # Clear existing data before reload
    cursor.execute("TRUNCATE TABLE raw_sales RESTART IDENTITY;")

    # Insert new data
    rows = [tuple(row) for row in df.itertuples(index=False)]
    execute_values(cursor, """
        INSERT INTO raw_sales (date, region, product, units_sold, revenue)
        VALUES %s;
    """, rows)

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Loaded {len(df)} rows into raw_sales.")

def run():
    df = extract("raw_data.csv")
    load(df)
    print("EL complete ✅")

if __name__ == "__main__":
    run()