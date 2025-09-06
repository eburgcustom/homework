import json
import logging
import os
from typing import Any, Dict, List

os.makedirs("logs", exist_ok=True)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


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
            logger.warning("Файл %s не найден или пустой", file_path)
            return []

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.info("Файл %s успешно загружен, найдено %d транзакций", file_path, len(data))
            return data

        logger.error("Файл %s содержит некорректный формат (ожидался список)", file_path)
        return []
    except FileNotFoundError:
        logger.error("Файл %s не найден", file_path)
        return []
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования JSON в файле %s", file_path)
        return []
    except OSError as e:
        logger.error("Ошибка при работе с файлом %s: %s", file_path, str(e))
        return []
