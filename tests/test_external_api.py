import pytest
from unittest.mock import patch
from src.external_api import get_amount_in_rub


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get):
    """
    Тестирует конвертацию суммы транзакции из USD в рубли.
    Используется Mock API-запроса для подстановки курса валют.
    """
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    mock_get.return_value.json.return_value = {"rates": {"RUB": 75}}
    mock_get.return_value.status_code = 200

    result = get_amount_in_rub(transaction)
    assert isinstance(result, float)
    assert result == 7500.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_eur(mock_get):
    """
    Тестирует конвертацию суммы транзакции из EUR в рубли.
    Используется Mock API-запроса с фиксированным курсом.
    """
    transaction = {"operationAmount": {"amount": "50", "currency": {"code": "EUR"}}}

    mock_get.return_value.json.return_value = {"rates": {"RUB": 90}}
    mock_get.return_value.status_code = 200

    result = get_amount_in_rub(transaction)
    assert result == 4500.0


def test_convert_to_rub_rub():
    """
    Тестирует конвертацию суммы транзакции, если валюта уже в рублях.
    API-запрос выполняться не должен, сумма возвращается как float.
    """
    transaction = {"operationAmount": {"amount": "1234.56", "currency": {"code": "RUB"}}}
    result = get_amount_in_rub(transaction)
    assert result == 1234.56
