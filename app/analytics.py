import pandas as pd
import numpy as np

from sqlalchemy import select

from .database import get_session
from .models import Transaction, Category


def load_transactions():

    with get_session() as session:

        rows = session.execute(
            select(Transaction, Category.name)
            .join(
                Category,
                Transaction.category_id == Category.id
            )
        ).all()

    records = []

    for transaction, category in rows:

        records.append({
            "date": transaction.transaction_date,
            "type": transaction.transaction_type,
            "category": category,
            "merchant": transaction.merchant,
            "amount": transaction.amount,
            "payment_method": transaction.payment_method
        })

    return pd.DataFrame(records)


def calculate_financial_metrics(df):

    if df.empty:
        return {
            "income": 0,
            "expense": 0,
            "balance": 0,
            "savings_rate": 0,
            "average_expense": 0,
            "expense_std": 0
        }

    income = df.loc[
        df["type"] == "income",
        "amount"
    ].sum()

    expenses = df.loc[
        df["type"] == "expense",
        "amount"
    ]

    total_expense = expenses.sum()

    balance = income - total_expense

    savings_rate = (
        balance / income * 100
        if income > 0
        else 0
    )

    return {
        "income": income,
        "expense": total_expense,
        "balance": balance,
        "savings_rate": round(
            savings_rate,
            2
        ),
        "average_expense": round(
            expenses.mean(),
            2
        ) if not expenses.empty else 0,

        "expense_std": round(
            np.std(expenses),
            2
        ) if not expenses.empty else 0
    }


def detect_expense_anomalies(df):

    expenses = df[
        df["type"] == "expense"
    ].copy()

    if len(expenses) < 4:
        return expenses

    q1 = expenses["amount"].quantile(0.25)
    q3 = expenses["amount"].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return expenses[
        (expenses["amount"] < lower) |
        (expenses["amount"] > upper)
    ]
