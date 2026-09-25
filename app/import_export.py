import pandas as pd

from .repositories import add_transaction


def import_csv(path):

    df = pd.read_csv(path)

    required = {
        "date",
        "type",
        "category",
        "amount"
    }

    missing = required - set(
        df.columns
    )

    if missing:
        raise ValueError(
            f"Missing columns: {missing}"
        )

    for _, row in df.iterrows():

        add_transaction(
            transaction_date=pd.to_datetime(
                row["date"]
            ).date(),

            transaction_type=row["type"],

            category_name=row["category"],

            merchant=row.get(
                "merchant",
                ""
            ),

            amount=float(
                row["amount"]
            ),

            payment_method=row.get(
                "payment_method",
                "Cash"
            )
        )

    return len(df)
