"""
Basic smoke tests for the database layer.
Run with: pytest tests/
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.database import initialize_database, get_session
from app.models import Category


def test_initialize_database_creates_tables():
    initialize_database()
    with get_session() as session:
        assert session is not None


def test_category_model_defaults():
    category = Category(name="Test")
    assert category.monthly_budget == 0
