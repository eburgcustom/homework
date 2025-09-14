import os

from typing import Any, Dict, Hashable, List

import pandas as pd


def load_transactions_from_csv(file_path: str) -> list[dict[Hashable, Any]]:
    """
   Загружает финансовые операции из CSV-файла.

    Args:
        file_path: Путь к CSV-файлу с транзакциями.

    Returns:
        Список словарей с финансовыми операциями.
        Каждый словарь представляет одну транзакцию.

    Raises:
        FileNotFoundError: Если файл не существует.
        ValueError: Если файл содержит некорректные данные.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except pd.errors.EmptyDataError:
        raise ValueError("Файл пуст")
    except pd.errors.ParserError as e:
        raise ValueError(f"Ошибка парсинга CSV: {e}")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении файла: {e}")


def load_transactions_from_excel(file_path: str) -> List[Dict[Hashable, Any]]:
    """
    Загружает финансовые операции из Excel-файла (XLSX).

    Args:
        file_path: Путь к Excel-файлу с транзакциями.

    Returns:
        Список словарей с финансовыми операций.
        Каждый словарь представляет одну транзакцию.

    Raises:
        FileNotFoundError: Если файл не существует.
        ValueError: Если файл содержит некорректные данные.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except pd.errors.EmptyDataError:
        raise ValueError("Файл пуст")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении файла: {e}")
