import pytest
from typing import Any
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(operations_data: list[dict[str, Any]]) -> None:
    result = filter_by_state(operations_data)
    assert all(op["state"] == "EXECUTED" for op in result)
    assert len(result) == 2


@pytest.mark.parametrize("state,expected_count", [("EXECUTED", 2),
                                                  ("CANCELED", 1),
                                                  ("PENDING", 1),
                                                  ("MISSING", 0),])
def test_filter_by_state_param(operations_data: list[dict[str, Any]], state: str, expected_count: int) -> None:
    result = filter_by_state(operations_data, state)
    assert len(result) == expected_count


def test_sort_by_date_desc(operations_data: list[dict[str, Any]]) -> None:
    sorted_ops = sort_by_date(operations_data)
    dates = [op["date"] for op in sorted_ops]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_asc(operations_data: list[dict[str, Any]]) -> None:
    sorted_ops = sort_by_date(operations_data, reverse=False)
    dates = [op["date"] for op in sorted_ops]
    assert dates == sorted(dates)
