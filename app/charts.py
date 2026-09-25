import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from .config import CHART_DIR


def category_chart(data):

    categories = [
        row[0]
        for row in data
    ]

    amounts = [
        row[1]
        for row in data
    ]

    path = CHART_DIR / "category_spending.png"

    plt.figure(figsize=(9, 5))

    plt.bar(
        categories,
        amounts
    )

    plt.title(
        "Expense by Category"
    )

    plt.xlabel(
        "Category"
    )

    plt.ylabel(
        "Amount"
    )

    plt.xticks(
        rotation=35
    )

    plt.tight_layout()

    plt.savefig(
        path,
        dpi=150
    )

    plt.close()

    return path
