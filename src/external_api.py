import os
from typing import Dict

import requests


def get_amount_in_rub(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction (Dict): Словарь с данными о транзакции.

    Returns:
        float: Сумма транзакции в рублях.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    api_key = os.getenv("API_KEY")  # ключ хранится в .env
    url = "https://api.apilayer.com/exchangerates_data/latest"

    headers = {"apikey": api_key}
    params = {"base": currency, "symbols": "RUB"}

    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()

    rate = response.json()["rates"]["RUB"]
    return float(amount * rate)
