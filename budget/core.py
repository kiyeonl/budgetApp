"""Core business logic for the budget CLI app."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any


def add_transaction(
    transactions: list[dict[str, Any]],
    transaction: dict[str, Any],
) -> list[dict[str, Any]]:
    """Add a transaction to the transaction list.

    Args:
        transactions: Existing transaction records.
        transaction: Transaction data to append.

    Returns:
        A new list containing the added transaction.
    """
    new_transactions = transactions.copy()
    new_transactions.append(
        {
            "date": transaction["date"],
            "type": transaction["type"],
            "category": transaction["category"],
            "description": transaction["description"],
            "amount": transaction["amount"],
            "memo": transaction["memo"],
        }
    )
    return new_transactions


def get_balance(transactions: list[dict[str, Any]]) -> float:
    """Return the balance by summing all transaction amounts.

    Args:
        transactions: Existing transaction records.

    Returns:
        The total balance.
    """
    if not transactions:
        return 0.0
    return float(sum(transaction["amount"] for transaction in transactions))


def filter_by_category(
    transactions: list[dict[str, Any]],
    category: str,
) -> list[dict[str, Any]]:
    """Return transactions whose category matches the given category.

    Args:
        transactions: Existing transaction records.
        category: Category name to match.

    Returns:
        A new list of matching transactions.
    """
    normalized_category = category.casefold()
    return [
        transaction.copy()
        for transaction in transactions
        if transaction["category"].casefold() == normalized_category
    ]


def load_transactions_from_csv(csv_path: Path) -> list[dict[str, Any]]:
    """Load transactions from a CSV file.

    Args:
        csv_path: Path to the CSV file.

    Returns:
        A list of transaction dictionaries.
    """
    transactions: list[dict[str, Any]] = []
    with csv_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            transactions.append(
                {
                    "date": row["date"],
                    "type": row["type"],
                    "category": row["category"],
                    "description": row["description"],
                    "amount": int(row["amount"]),
                    "memo": row["memo"],
                }
            )
    return transactions


def monthly_summary(transactions: list[dict[str, Any]]) -> dict[str, dict[str, int]]:
    """Summarize transactions by month.

    Args:
        transactions: Existing transaction records.

    Returns:
        Monthly totals keyed by YYYY-MM.
    """
    summary: dict[str, dict[str, int]] = {}
    for transaction in transactions:
        month = transaction["date"][:7]
        if month not in summary:
            summary[month] = {"income": 0, "expense": 0, "net": 0}
        amount = int(transaction["amount"])
        if amount >= 0:
            summary[month]["income"] += amount
        else:
            summary[month]["expense"] += amount
        summary[month]["net"] += amount
    return summary
