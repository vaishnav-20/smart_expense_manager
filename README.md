# Smart Expense Manager

A desktop personal-finance analytics application built with Python.

## Stack
- Python, OOP
- Tkinter (desktop UI)
- SQLite + SQLAlchemy (ORM, advanced SQL queries)
- Pandas / NumPy (financial analytics, anomaly detection)
- Matplotlib (charts)
- ReportLab (PDF reports)
- CSV/Excel import-export

## Setup
```bash
pip install -r requirements.txt
python main.py
```

## Features
- Add income/expense transactions through a form UI
- SQLAlchemy-backed relational schema (Category, Transaction, Budget)
- Monthly income/expense/balance summaries via SQL aggregation
- Category-wise spending breakdown
- Pandas/NumPy-based financial metrics: savings rate, average expense, std-dev
- IQR-based anomaly detection for unusual expenses
- Bar chart of category spending (Matplotlib)
- CSV import of transactions
- PDF report generation (ReportLab)

## Project layout
```
Smart_Expense_Manager/
├── main.py
├── app/            # application package (models, database, services, ui, etc.)
├── data/           # SQLite database file
├── exports/        # exported files
├── reports/        # generated PDF reports
└── charts/         # generated chart images
```

## Next steps to make it portfolio-grade
- Full CRUD screens for transactions/categories
- Budget-vs-actual monthly/yearly SQL analytics
- Recurring transaction scheduling
- Authentication and multi-user support
- Alembic database migrations
- Logging and a pytest test suite
