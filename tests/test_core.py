"""Tests for budget core logic."""

from budget.core import add_transaction


def test_add_transaction_increases_length() -> None:
    """Adding a transaction should increase the list length by one."""
    transactions = []
    transaction = {
        "date": "2026-06-25",
        "type": "income",
        "category": "salary",
        "description": "June salary",
        "amount": 3500000,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert len(result) == len(transactions) + 1
