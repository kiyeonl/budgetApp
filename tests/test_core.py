"""Tests for budget core logic."""

from budget.core import add_transaction, filter_by_category, get_balance


def test_add_transaction_increases_length() -> None:
    """Adding a transaction should increase the list length by one."""
    transactions = []
    transaction = {
        "date": "2026-01-07",
        "type": "수입",
        "category": "급여",
        "description": "월급",
        "amount": 3500000,
        "memo": "1월급여",
    }

    result = add_transaction(transactions, transaction)

    assert len(result) == len(transactions) + 1


def test_add_transaction_preserves_negative_amount() -> None:
    """Expense transactions should keep negative amounts unchanged."""
    transactions = []
    transaction = {
        "date": "2026-01-05",
        "type": "지출",
        "category": "식비",
        "description": "점심식사",
        "amount": -12000,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["amount"] == -12000


def test_add_transaction_preserves_positive_amount() -> None:
    """Income transactions should keep positive amounts unchanged."""
    transactions = []
    transaction = {
        "date": "2026-01-28",
        "type": "기타수입",
        "category": "기타수입",
        "description": "중고 판매",
        "amount": 25000,
        "memo": "중고마켓",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["amount"] == 25000


def test_add_transaction_allows_empty_description() -> None:
    """Empty descriptions should be stored without modification."""
    transactions = []
    transaction = {
        "date": "2026-01-12",
        "type": "지출",
        "category": "교통",
        "description": "",
        "amount": -1500,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["description"] == ""


def test_get_balance_returns_sum_of_amounts() -> None:
    """Balance should equal the sum of positive and negative amounts."""
    transactions = [
        {
            "date": "2026-01-04",
            "type": "지출",
            "category": "여행",
            "description": "항공권",
            "amount": -979796,
            "memo": "메모_3",
        },
        {
            "date": "2026-01-15",
            "type": "수입",
            "category": "기타수입",
            "description": "중고 판매",
            "amount": 135541,
            "memo": "",
        },
        {
            "date": "2026-02-01",
            "type": "수입",
            "category": "급여",
            "description": "월급",
            "amount": 4358625,
            "memo": "",
        },
    ]

    assert get_balance(transactions) == 3514370


def test_get_balance_returns_zero_for_empty_list() -> None:
    """Empty transaction lists should return zero balance."""
    assert get_balance([]) == 0.0


def test_filter_by_category_matches_case_insensitively() -> None:
    """Category matching should ignore case differences."""
    transactions = [
        {
            "date": "2026-01-04",
            "type": "지출",
            "category": "여행",
            "description": "항공권",
            "amount": -979796,
            "memo": "메모_3",
        },
        {
            "date": "2026-01-15",
            "type": "지출",
            "category": "문화/여가",
            "description": "영화관",
            "amount": -64470,
            "memo": "현금",
        },
        {
            "date": "2026-02-01",
            "type": "수입",
            "category": "급여",
            "description": "월급",
            "amount": 4358625,
            "memo": "",
        },
    ]

    result = filter_by_category(transactions, "여행")

    assert result == [transactions[0]]
    assert filter_by_category(transactions, "여행") == filter_by_category(
        transactions,
        "여행",
    )
    assert filter_by_category(transactions, "문화/여가") == [transactions[1]]


def test_filter_by_category_returns_empty_list_for_missing_category() -> None:
    """Unknown categories should return an empty list."""
    transactions = [
        {
            "date": "2026-02-01",
            "type": "수입",
            "category": "급여",
            "description": "월급",
            "amount": 4358625,
            "memo": "",
        }
    ]

    assert filter_by_category(transactions, "식비") == []


def test_filter_by_category_returns_independent_result() -> None:
    """Filtered results should not share state with the source list."""
    transactions = [
        {
            "date": "2026-01-04",
            "type": "지출",
            "category": "여행",
            "description": "항공권",
            "amount": -979796,
            "memo": "메모_3",
        },
        {
            "date": "2026-02-01",
            "type": "수입",
            "category": "급여",
            "description": "월급",
            "amount": 4358625,
            "memo": "",
        },
    ]

    result = filter_by_category(transactions, "여행")
    result[0]["description"] = "변경"

    assert transactions[0]["description"] == "항공권"
