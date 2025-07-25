def get_mask_card_number(card_number: int | str) -> str:
    """Возврат маски карты в формате XXXX XX** **** XXXX, где
    X — это цифра номера
    """

    card_str = str(card_number)

    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр.")

    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int | str) -> str:
    """Возвращает маску номера счета. Номер счета замаскирован и отображается
    в формате **XXXX, где X — это цифра номера
    """

    account_str = str(account_number)

    if len(account_str) < 4 or not account_str.isdigit():
        raise ValueError("Номер счёта должен содержать минимум 4 цифры.")

    return f"**{account_str[-4:]}"
