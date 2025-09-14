from typing import Any, Dict, Hashable, List

import pandas as pd


def load_transactions_from_csv(file_path: str) -> list[dict[Hashable, Any]]:
    """
    Загружает транзакции из CSV-файла.

    Args:
        Путь к CSV-файлу.

    Returns:
        Список словарей транзакций.
        Если файл не найден или содержит некорректные данные — возвращает пустой список.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception:
        return []


def load_transactions_from_excel(file_path: str) -> List[Dict[Hashable, Any]]:
    """
    Загружает транзакции из Excel-файла (XLSX).

    Args:
        file_path (str): Путь к Excel-файлу.

    Returns:
        List[Dict[str, Any]]: Список словарей транзакций.
        Если файл не найден или содержит некорректные данные — возвращает пустой список.
    """
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except Exception:
        return []
