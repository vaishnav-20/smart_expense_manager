from datetime import date

from sqlalchemy import (
    select,
    func,
    case
)

from .database import get_session
from .models import Transaction, Category


def add_transaction(
    transaction_date,
    transaction_type,
    category_name,
    merchant,
    amount,
    payment_method,
    description=""
):

    with get_session() as session:

        category = session.scalar(
            select(Category).where(
                Category.name == category_name
            )
        )

        if category is None:

            category = Category(
                name=category_name
            )

            session.add(category)
            session.flush()

        transaction = Transaction(
            transaction_date=transaction_date,
            transaction_type=transaction_type,
            category_id=category.id,
            merchant=merchant,
            amount=amount,
            payment_method=payment_method,
            description=description
        )

        session.add(transaction)

        session.commit()


def monthly_summary(year, month):

    with get_session() as session:

        income = session.scalar(
            select(
                func.coalesce(
                    func.sum(Transaction.amount),
                    0
                )
            ).where(
                Transaction.transaction_type == "income",
                func.extract(
                    "year",
                    Transaction.transaction_date
                ) == year,
                func.extract(
                    "month",
                    Transaction.transaction_date
                ) == month
            )
        )

        expenses = session.scalar(
            select(
                func.coalesce(
                    func.sum(Transaction.amount),
                    0
                )
            ).where(
                Transaction.transaction_type == "expense",
                func.extract(
                    "year",
                    Transaction.transaction_date
                ) == year,
                func.extract(
                    "month",
                    Transaction.transaction_date
                ) == month
            )
        )

        return {
            "income": income or 0,
            "expenses": expenses or 0,
            "balance": (income or 0) - (expenses or 0)
        }


def category_spending(year, month):

    with get_session() as session:

        query = (
            select(
                Category.name,
                func.sum(Transaction.amount).label(
                    "total"
                )
            )
            .join(
                Transaction,
                Transaction.category_id == Category.id
            )
            .where(
                Transaction.transaction_type == "expense",
                func.extract(
                    "year",
                    Transaction.transaction_date
                ) == year,
                func.extract(
                    "month",
                    Transaction.transaction_date
                ) == month
            )
            .group_by(
                Category.name
            )
            .order_by(
                func.sum(
                    Transaction.amount
                ).desc()
            )
        )

        return session.execute(query).all()
