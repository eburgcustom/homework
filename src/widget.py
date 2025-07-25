from datetime import datetime
from .masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """ Маскирует номер карты/счёта в переданной строке. """
    parts = data.split()
    if not parts:
        raise ValueError("Пустая строка")

    # Определяем тип (карта или счёт)
    if parts[0] == "Счет":
        account_number = parts[-1]
        masked_number = get_mask_account(account_number)
        return f"Счет {masked_number}"
    else:
        card_number = parts[-1]
        masked_number = get_mask_card_number(card_number)
        return ' '.join(parts[:-1] + [masked_number])


def get_date(date_str: str) -> str:
    """ Преобразует дату из формата ISO в DD.MM.YYYY. """
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")