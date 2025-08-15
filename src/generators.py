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