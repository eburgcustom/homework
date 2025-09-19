import pytest

from src.processors import normalize_transaction, process_bank_operations, process_bank_search


@pytest.fixture
def sample_data():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 100,
            "currency_name": "RUB",
            "currency_code": "RUB",
            "from": "Счет 1111",
            "to": "Счет 2222",
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2023-09-06T11:30:32Z",
            "amount": 200,
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Visa 1234",
            "to": "Mastercard 5678",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2023-09-07T11:30:32Z",
            "amount": 300,
            "currency_name": "EUR",
            "currency_code": "EUR",
            "from": "",
            "to": "Счет 9999",
            "description": "Открытие вклада",
        },
    ]


def test_process_bank_search_found(sample_data):
    """Поиск по описанию находит совпадения"""
    result = process_bank_search(sample_data, "организации")
    assert len(result) == 1
    assert result[0]["description"] == "Перевод организации"


def test_process_bank_search_case_insensitive(sample_data):
    """Поиск не зависит от регистра"""
    result = process_bank_search(sample_data, "ПЕРЕВОД")
    assert len(result) == 2
    descriptions = [tx["description"] for tx in result]
    assert "Перевод организации" in descriptions
    assert "Перевод с карты на карту" in descriptions


def test_process_bank_search_no_matches(sample_data):
    """Поиск возвращает пустой список, если совпадений нет"""
    result = process_bank_search(sample_data, "ипотека")
    assert result == []


def test_process_bank_search_empty_data():
    """Поиск в пустом списке возвращает пустой список"""
    result = process_bank_search([], "перевод")
    assert result == []


def test_process_bank_operations_counts(sample_data):
    """Подсчёт категорий работает корректно"""
    categories = ["Перевод организации", "Перевод с карты на карту", "Открытие вклада"]
    result = process_bank_operations(sample_data, categories)

    assert result["Перевод организации"] == 1
    assert result["Перевод с карты на карту"] == 1
    assert result["Открытие вклада"] == 1


def test_process_bank_operations_with_missing_category(sample_data):
    """Если категории нет — возвращается 0"""
    categories = ["Оплата кредита"]
    result = process_bank_operations(sample_data, categories)

    assert result["Оплата кредита"] == 0


def test_process_bank_operations_empty_data():
    """Подсчёт на пустом списке возвращает 0 для всех категорий"""
    categories = ["Перевод организации", "Открытие вклада"]
    result = process_bank_operations([], categories)

    assert result["Перевод организации"] == 0
    assert result["Открытие вклада"] == 0


def test_normalize_transaction_extracts_amount_and_currency():
    """Проверка извлечения суммы и валюты из operationAmount"""
    tx = {
        "id": 1,
        "operationAmount": {
            "amount": "1000",
            "currency": {"name": "RUB", "code": "RUB"},
        }
    }
    normalized = normalize_transaction(tx)
    assert normalized["amount"] == "1000"
    assert normalized["currency_name"] == "RUB"
    assert normalized["currency_code"] == "RUB"


def test_normalize_transaction_without_operation_amount():
    """Проверяет корректность работы, если operationAmount отсутствует"""
    tx = {"id": 2, "description": "Операция без суммы"}
    normalized = normalize_transaction(tx)
    # ничего не должно сломаться
    assert "amount" not in normalized
    assert "currency_name" not in normalized
    assert "currency_code" not in normalized
