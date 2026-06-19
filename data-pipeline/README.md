# 🎮 Gaming Analytics Data Pipeline

A end-to-end data engineering pipeline built with **dbt**, **PostgreSQL**, **Apache Airflow**, and **Power BI** — using Steam gaming data to demonstrate modern analytics engineering practices.

---

## 🏗️ Architecture

```
Raw Data (CSV Seeds)
      ↓
  dbt Staging Models      ← clean & rename columns
      ↓
  dbt Mart Models         ← business logic & metrics
      ↓
  PostgreSQL (Docker)     ← data warehouse
      ↓
  Apache Airflow          ← orchestration (scheduled daily)
      ↓
  Power BI Dashboard      ← visualization layer
```

---

## 📁 Project Structure

```
data-engineering-portfolio/
├── .github/
│   └── workflows/
│       └── dbt_ci.yml              # CI/CD pipeline
├── airflow/
│   ├── dags/
│   │   └── dbt_pipeline.py         # Airflow DAG
│   ├── docker-compose.yaml
│   └── .env
├── analytics-api/                  # FastAPI project (Project 1)
└── data-pipeline/
    └── analytics/                  # dbt project
        ├── models/
        │   ├── staging/
        │   │   ├── stg_games.sql
        │   │   └── schema.yml
        │   └── marts/
        │       ├── mart_game_performance.sql
        │       └── schema.yml
        ├── seeds/
        │   └── raw_data.csv
        ├── dbt_project.yml
        └── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Docker Desktop
- dbt-core 1.8.0
- dbt-postgres 1.8.0

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/data-engineering-portfolio.git
cd data-engineering-portfolio/data-pipeline/analytics
```

### 2. Install dbt
```bash
pip install dbt-core==1.8.0 dbt-postgres==1.8.0
```

### 3. Start PostgreSQL via Docker
```bash
docker run --name dbt-postgres \
  -e POSTGRES_USER=dbt_user \
  -e POSTGRES_PASSWORD=dbt_pass \
  -e POSTGRES_DB=dbt_db \
  -p 5432:5432 \
  -d postgres:15
```

### 4. Configure dbt profile
Add to `~/.dbt/profiles.yml`:
```yaml
data_pipeline:
  target: dev
  outputs:
    dev:
      type: postgres
      host: localhost
      user: dbt_user
      password: dbt_pass
      port: 5432
      dbname: dbt_db
      schema: public
      threads: 4
```

### 5. Run the pipeline
```bash
dbt debug       # test connection
dbt seed        # load raw CSV data
dbt run         # build models
dbt test        # run data quality tests
dbt docs serve  # view data lineage
```

---

## 🔄 Airflow Orchestration

```bash
cd airflow
docker compose up airflow-init
docker compose up -d
```

Open Airflow UI at http://localhost:8080
- Username: `airflow`
- Password: `airflow`

The `dbt_pipeline` DAG runs daily: `seed → run → test`

---

## 📊 dbt Models

| Model | Type | Description |
|-------|------|-------------|
| `stg_games` | View | Cleans and renames raw Steam data |
| `mart_game_performance` | Table | Game metrics with approval % calculations |

### Key Metrics
- `approval_pct` — positive ratings as a % of total ratings
- `total_ratings` — sum of positive and negative ratings

---

## ✅ Data Tests

| Test | Column | Model |
|------|--------|-------|
| `not_null` | `game_name` | `stg_games` |
| `unique` | `appid` | `stg_games` |
| `not_null` | `approval_pct` | `mart_game_performance` |
| `not_null` | `price` | `mart_game_performance` |

---

## 🔧 CI/CD Pipeline

GitHub Actions runs on every push to `main`:
1. Spins up a PostgreSQL service container
2. Installs dbt
3. Runs `dbt seed → dbt run → dbt test`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| dbt-core 1.8.0 | Data transformation |
| PostgreSQL 15 | Data warehouse |
| Apache Airflow 2.9 | Pipeline orchestration |
| Docker | Containerisation |
| GitHub Actions | CI/CD |
| Power BI | Visualisation |
| Python 3.11 | Scripting & automation |

---

## 👤 Author

**Yomi**  
Data Analyst → Analytics Engineer  
[LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)

---

## 📄 License

MIT License
