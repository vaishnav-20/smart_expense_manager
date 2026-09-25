import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd

from app.analytics import calculate_financial_metrics, detect_expense_anomalies


def test_calculate_financial_metrics_empty():
    df = pd.DataFrame(columns=["date", "type", "category", "merchant", "amount", "payment_method"])
    metrics = calculate_financial_metrics(df)
    assert metrics["income"] == 0
    assert metrics["balance"] == 0


def test_calculate_financial_metrics_basic():
    df = pd.DataFrame([
        {"type": "income", "amount": 1000},
        {"type": "expense", "amount": 200},
        {"type": "expense", "amount": 300},
    ])
    metrics = calculate_financial_metrics(df)
    assert metrics["income"] == 1000
    assert metrics["expense"] == 500
    assert metrics["balance"] == 500


def test_detect_expense_anomalies_small_sample():
    df = pd.DataFrame([
        {"type": "expense", "amount": 100},
        {"type": "expense", "amount": 120},
    ])
    result = detect_expense_anomalies(df)
    assert len(result) == 2
