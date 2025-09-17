import re
from collections import Counter
from typing import List, Dict


def process_bank_search(data: List[dict], search: str) -> List[dict]:
    """
    Фильтрует список банковских операций по слову/шаблону в описании.

    Args:
        data (List[dict]): Список транзакций.
        search (str): Строка или шаблон для поиска.

    Returns:
        List[dict]: Список транзакций, у которых description содержит строку поиска.
    """
    pattern = re.compile(search, re.IGNORECASE)
    return [operation for operation in data if pattern.search(operation.get("description", ""))]


def process_bank_operations(data: List[dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям на основе поля description.

    Args:
        data (List[dict]): Список транзакций.
        categories (List[str]): Список категорий для подсчета.

    Returns:
        Dict[str, int]: Словарь с категориями и количеством операций.
    """
    counter = Counter()
    for operation in data:
        description = operation.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                counter[category] += 1
    return dict(counter)
