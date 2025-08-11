from typing import List, Dict, Any


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по ключу 'state'.

    :param data: Список словарей с данными операций.
    :param state: Значение состояния (по умолчанию 'EXECUTED').
    :return: Новый список словарей, содержащий только операции с указанным состоянием.
    """
    return [item for item in data if item.get("state") == state]