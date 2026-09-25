import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from datetime import date

from app.database import initialize_database
from app.repositories import add_transaction, monthly_summary


def test_add_transaction_and_summary():
    initialize_database()

    today = date.today()

    add_transaction(
        transaction_date=today,
        transaction_type="income",
        category_name="Salary",
        merchant="Employer",
        amount=5000,
        payment_method="Bank Transfer",
    )

    summary = monthly_summary(today.year, today.month)

    assert summary["income"] >= 5000
