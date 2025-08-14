import pytest


@pytest.fixture
def card_number():
    return "1234567812345678"


@pytest.fixture
def account_number():
    return "87654321"


@pytest.fixture
def operations_data():
    return [{"state": "EXECUTED", "date": "2023-07-15"},
            {"state": "CANCELED", "date": "2023-07-16"},
            {"state": "EXECUTED", "date": "2023-07-14"},
            {"state": "PENDING", "date": "2023-07-15"},]
