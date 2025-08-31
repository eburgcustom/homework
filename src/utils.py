import json
import os
from typing import Any, Dict, List


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.

    Args:
        file_path (str): Путь до JSON-файла.

    Returns:
        List[Dict[str, Any]]: Список транзакций.
        Если файл пустой, не существует или содержит не список — вернётся пустой список.
    """
    try:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return []

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            return []
        return data
    except (json.JSONDecodeError, OSError):
        return []
