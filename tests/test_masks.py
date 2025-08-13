import pytest
from typing import Union
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card,expected", [("1234567812345678", "1234 56** **** 5678"),
                                           (1234567812345678, "1234 56** **** 5678"),])
def test_get_mask_card_number_valid(card: Union[str, int], expected: str) -> None:
    assert get_mask_card_number(card) == expected


@pytest.mark.parametrize("card", ["1234", "abcd567812345678", "", "123456781234567"])
def test_get_mask_card_number_invalid(card: Union[str, int]) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card)


@pytest.mark.parametrize("account,expected", [("12345678", "**5678"),
                                              (12345678, "**5678"),])
def test_get_mask_account_valid(account: Union[str, int], expected: str) -> None:
    assert get_mask_account(account) == expected


@pytest.mark.parametrize("account", ["123", "abcd", "", "12 34"])
def test_get_mask_account_invalid(account: Union[str, int]) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account)
