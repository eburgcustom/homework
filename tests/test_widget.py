import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("data,expected", [
    ("Счет 12345678", "Счет **5678"),
    ("Visa Classic 1234567812345678", "Visa Classic 1234 56** **** 5678"),
])
def test_mask_account_card_valid(data: str, expected: str) -> None:
    """
    Проверяет, что mask_account_card корректно маскирует
    номера счетов и карт в переданной строке.
    """
    assert mask_account_card(data) == expected


def test_mask_account_card_empty() -> None:
    """
    Проверяет, что mask_account_card выбрасывает ValueError
    при передаче пустой строки.
    """
    with pytest.raises(ValueError):
        mask_account_card("")


@pytest.mark.parametrize("date_str,expected", [
    ("2023-07-15T14:48:00", "15.07.2023"),
    ("2000-01-01T00:00:00", "01.01.2000"),
])
def test_get_date_valid(date_str: str, expected: str) -> None:
    """
    Проверяет, что get_date корректно преобразует дату
    из формата ISO 8601 в формат DD.MM.YYYY.
    """
    assert get_date(date_str) == expected
