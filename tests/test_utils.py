import pytest
import json
import os
from src.utils import load_transactions


def test_load_transactions_valid_file(tmp_path):
    """
    Тестирует корректную загрузку списка транзакций из JSON-файла.
    Проверяет, что функция возвращает список словарей при валидном файле.
    """
    file_path = tmp_path / "transactions.json"
    data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    file_path.write_text(json.dumps(data), encoding="utf-8")

    result = load_transactions(str(file_path))
    assert isinstance(result, list)
    assert result == data


def test_load_transactions_empty_file(tmp_path):
    """
    Тестирует поведение при пустом JSON-файле.
    Ожидается возврат пустого списка.
    """
    file_path = tmp_path / "empty.json"
    file_path.write_text("", encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == []


def test_load_transactions_not_a_list(tmp_path):
    """
    Тестирует поведение при JSON-файле, содержащем не список (например, словарь).
    Ожидается возврат пустого списка.
    """
    file_path = tmp_path / "wrong.json"
    file_path.write_text(json.dumps({"id": 1}), encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == []


def test_load_transactions_file_not_found():
    """
    Тестирует поведение при отсутствии файла.
    Ожидается возврат пустого списка.
    """
    result = load_transactions("non_existent.json")
    assert result == []
