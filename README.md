# 🐮 CoW Protocol Trading Intelligence – Web3 Data Pipeline

This project is a fully open-source, end-to-end Web3 data pipeline that analyzes trading activity on [CoW Protocol](https://cow.fi/), built using a Medallion architecture and Delta Lake format.

The pipeline ingests data from the [Dune Analytics API](https://dune.com/docs/api/), processes it using PySpark, and serves business-ready KPIs through a Streamlit dashboard.

---

## 🛠️ Architecture

The pipeline follows the [Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture):

```plaintext
data/
├── bronze/  # Raw Dune API responses
├── silver/  # Cleaned & normalized datasets
└── gold/    # Business metrics (e.g., top traders, token trends)
```


### Tools Used

| Layer            | Technology          |
|------------------|---------------------|
| Ingestion        | Python + Dune API   |
| Processing       | PySpark             |
| Storage          | Delta Lake (local filesystem) |
| Visualization    | Streamlit           |
| Version Control  | Git + GitHub        |

---

## 📊 KPIs & Dashboard

The dashboard provides:

- Top traders by ETH volume
- Most actively traded tokens
- Daily transaction trends
- Unique wallets over time (wallet churn)

> 🔗 **Coming soon**: Deploy via Docker or Streamlit Community Cloud  
> 🖼 **Preview**: *(Insert screenshot or GIF here)*

---

## 🚀 How to Run It Locally

### Prerequisites

- Python 3.9+
- pip or poetry
- Optional: Docker

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/cow-trading-intelligence.git
cd cow-trading-intelligence

