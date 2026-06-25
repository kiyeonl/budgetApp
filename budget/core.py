"""Core business logic for the budget CLI app."""

from __future__ import annotations

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
