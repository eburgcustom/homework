from typing import Iterator, List, Dict, Any


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Генератор, который поочерёдно возвращает транзакции,
    у которых код валюты совпадает с переданным currency_code.

    :param transactions: список словарей с данными транзакций
    :param currency_code: код валюты (например, "USD")
    :return: итератор по транзакциям
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор, который поочерёдно возвращает описание каждой операции.

    :param transactions: список словарей с данными транзакций
    :return: итератор по строкам-описаниям
    """
    for transaction in transactions:
        yield transaction.get("description", "")