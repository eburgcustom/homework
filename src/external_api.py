import os
from typing import Any, Dict

import requests


def get_amount_in_rub(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction (Dict[str, Any]): Словарь с данными о транзакции.
            Ожидается структура:
            {
                "operationAmount": {
                    "amount": <число или строка>,
                    "currency": {"code": "USD" | "EUR" | "RUB" | ...}
                }
            }


    Returns:
        float: Сумма транзакции в рублях.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    api_key = os.getenv("API_KEY")  # ключ хранится в .env
    url = "https://api.apilayer.com/exchangerates_data/convert"

    headers = {"apikey": api_key}
    params = {"from": currency, "to": "RUB", "amount": amount}

    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()

    data: Dict[str, Any] = response.json()

    if "result" not in data:
        raise ValueError(f"Invalid API response: {data}")

    return float(data["result"])
