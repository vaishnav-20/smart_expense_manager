from datetime import datetime, date

from sqlalchemy import (
    String,
    Integer,
    Float,
    Date,
    DateTime,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from .database import Base


class Category(Base):

    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    monthly_budget: Mapped[float] = mapped_column(
        Float,
        default=0
    )

    transactions = relationship(
        "Transaction",
        back_populates="category"
    )


class Transaction(Base):

    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    transaction_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    transaction_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id")
    )

    merchant: Mapped[str] = mapped_column(
        String(150),
        default=""
    )

    amount: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    payment_method: Mapped[str] = mapped_column(
        String(50),
        default="Cash"
    )

    description: Mapped[str] = mapped_column(
        String(500),
        default=""
    )

    recurring: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    category = relationship(
        "Category",
        back_populates="transactions"
    )


class Budget(Base):

    __tablename__ = "budgets"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id")
    )

    year: Mapped[int] = mapped_column(
        Integer
    )

    month: Mapped[int] = mapped_column(
        Integer
    )

    amount: Mapped[float] = mapped_column(
        Float
    )
