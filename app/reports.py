from reportlab.lib.pagesizes import A4

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_report(
    summary,
    categories,
    output_path
):

    document = SimpleDocTemplate(
        str(output_path),
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Smart Expense Manager",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"Income: Rs. {summary['income']:,.2f}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Expenses: Rs. {summary['expenses']:,.2f}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Balance: Rs. {summary['balance']:,.2f}",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    table_data = [
        ["Category", "Amount"]
    ]

    for category, amount in categories:

        table_data.append([
            category,
            f"Rs. {amount:,.2f}"
        ])

    elements.append(
        Table(table_data)
    )

    document.build(elements)
