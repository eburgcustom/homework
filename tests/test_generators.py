import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 4,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 5,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.mark.parametrize(
    "currency_code,expected_ids",
    [
        ("USD", [1, 2, 4]),
        ("RUB", [3, 5]),
        ("EUR", []),
    ],
)
def test_filter_by_currency(sample_transactions, currency_code, expected_ids):
    """
    Проверяет, что filter_by_currency возвращает транзакции только
    с заданным кодом валюты.
    Условия:
    - USD → возвращает id [1, 2, 4]
    - RUB → возвращает id [3, 5]
    - неизвестная валюта → пустой список
    """
    result = list(filter_by_currency(sample_transactions, currency_code))
    assert [t["id"] for t in result] == expected_ids


def test_filter_by_currency_empty_list():
    """
    Проверяет, что filter_by_currency возвращает пустой список,
    если входной список транзакций пуст.
    """
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(sample_transactions):
    """
    Проверяет, что transaction_descriptions возвращает список
    описаний транзакций в порядке их следования.
    """
    result = list(transaction_descriptions(sample_transactions))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_transaction_descriptions_empty():
    """
    Проверяет, что transaction_descriptions возвращает пустой список,
    если транзакций нет.
    """
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start,stop,expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    """
    Проверяет, что card_number_generator возвращает правильные
    отформатированные номера карт с ведущими нулями.
    Условия:
    - Числа из диапазона [start, stop] включительно.
    - Формат: 'XXXX XXXX XXXX XXXX'.
    """
    assert list(card_number_generator(start, stop)) == expected
