from typing import Any, Dict, Iterator, List


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


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор, который выдает номера банковских карт в вормате ХХХХ ХХХХ ХХХХ ХХХХ.

    :param start: начальное число
    :param stop: конечное число (включительно)
    :return: итератор по номерам карт
    """
    for number in range(start, stop + 1):
        yield (
            f"{number:016d}"[:4]
            + " "
            + f"{number:016d}"[4:8]
            + " "
            + f"{number:016d}"[8:12]
            + " "
            + f"{number:016d}"[12:]
        )
