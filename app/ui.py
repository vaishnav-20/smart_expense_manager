import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

from datetime import date

from .database import initialize_database
from .repositories import (
    add_transaction,
    monthly_summary,
    category_spending
)

from .analytics import (
    load_transactions,
    calculate_financial_metrics,
    detect_expense_anomalies
)


class ExpenseManagerApp:

    def __init__(self):

        initialize_database()

        self.root = tk.Tk()

        self.root.title(
            "Smart Expense Manager"
        )

        self.root.geometry(
            "1100x700"
        )

        self.build_ui()

    def build_ui(self):

        title = ttk.Label(
            self.root,
            text="SMART EXPENSE MANAGER",
            font=("Segoe UI", 22, "bold")
        )

        title.pack(
            pady=15
        )

        self.create_form()

        self.create_dashboard()

    def create_form(self):

        frame = ttk.LabelFrame(
            self.root,
            text="Add Transaction",
            padding=10
        )

        frame.pack(
            fill="x",
            padx=15
        )

        self.date_entry = ttk.Entry(
            frame
        )

        self.date_entry.insert(
            0,
            str(date.today())
        )

        self.date_entry.grid(
            row=0,
            column=0,
            padx=5
        )

        self.type_entry = ttk.Entry(
            frame
        )

        self.type_entry.insert(
            0,
            "expense"
        )

        self.type_entry.grid(
            row=0,
            column=1,
            padx=5
        )

        self.category_entry = ttk.Entry(
            frame
        )

        self.category_entry.insert(
            0,
            "Food"
        )

        self.category_entry.grid(
            row=0,
            column=2,
            padx=5
        )

        self.merchant_entry = ttk.Entry(
            frame
        )

        self.merchant_entry.grid(
            row=0,
            column=3,
            padx=5
        )

        self.amount_entry = ttk.Entry(
            frame
        )

        self.amount_entry.grid(
            row=0,
            column=4,
            padx=5
        )

        ttk.Button(
            frame,
            text="Add Transaction",
            command=self.add_transaction
        ).grid(
            row=0,
            column=5,
            padx=10
        )

    def create_dashboard(self):

        self.dashboard = ttk.Label(
            self.root,
            text="Loading..."
        )

        self.dashboard.pack(
            pady=30
        )

        ttk.Button(
            self.root,
            text="Refresh Dashboard",
            command=self.refresh
        ).pack()

        self.refresh()

    def add_transaction(self):

        try:

            add_transaction(
                date.fromisoformat(
                    self.date_entry.get()
                ),

                self.type_entry.get(),

                self.category_entry.get(),

                self.merchant_entry.get(),

                float(
                    self.amount_entry.get()
                ),

                "UPI"
            )

            messagebox.showinfo(
                "Success",
                "Transaction added."
            )

            self.refresh()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def refresh(self):

        df = load_transactions()

        metrics = calculate_financial_metrics(
            df
        )

        text = (
            f"Income: Rs. {metrics['income']:,.2f}\n"
            f"Expenses: Rs. {metrics['expense']:,.2f}\n"
            f"Balance: Rs. {metrics['balance']:,.2f}\n"
            f"Savings Rate: {metrics['savings_rate']}%\n"
            f"Average Expense: Rs. {metrics['average_expense']:,.2f}"
        )

        self.dashboard.config(
            text=text,
            font=("Segoe UI", 16)
        )

    def run(self):

        self.root.mainloop()
