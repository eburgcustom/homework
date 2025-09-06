import logging
import os


os.makedirs("logs", exist_ok=True)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: int | str) -> str:
    """Возврат маски карты в формате XXXX XX** **** XXXX, где
    X — это цифра номера
    """

    card_str = str(card_number)

    if len(card_str) != 16 or not card_str.isdigit():
        logger.error("Некорректный номер карты: %s", card_number)
        raise ValueError("Номер карты должен состоять из 16 цифр.")

    masked = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    logger.info("Карта %s замаскирована как %s", card_number, masked)
    return masked


def get_mask_account(account_number: int | str) -> str:
    """Возвращает маску номера счета. Номер счета замаскирован и отображается
    в формате **XXXX, где X — это цифра номера
    """

    account_str = str(account_number)

    if len(account_str) < 4 or not account_str.isdigit():
        logger.error("Некорректный номер счёта: %s", account_number)
        raise ValueError("Номер счёта должен содержать минимум 4 цифры.")

    masked = f"**{account_str[-4:]}"
    logger.info("Счёт %s замаскирован как %s", account_number, masked)
    return masked
