{{ config(materialized='table') }}

SELECT
    region,
    product,
    DATE_TRUNC('month', date) AS month,
    SUM(units_sold) AS total_units,
    SUM(revenue) AS total_revenue,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM {{ source('public', 'raw_sales') }}
GROUP BY region, product, DATE_TRUNC('month', date)
ORDER BY month, region