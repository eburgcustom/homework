from typing import Any, Dict, List

from src.processors import process_bank_search
from src.readers import load_transactions_from_csv, load_transactions_from_excel
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Основная логика проекта: взаимодействие с пользователем
    и работа с банковскими транзакциями.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    print("4. Выход")

    choice = input("Ваш выбор: ").strip()
    try:
        if choice == "1":
            file_path = input("Введите путь к JSON-файлу: ").strip()
            transactions = load_transactions(file_path)
            print("Для обработки выбран JSON-файл.")
        elif choice == "2":
            file_path = input("Введите путь к CSV-файлу: ").strip()
            transactions = load_transactions_from_csv(file_path)
            print("Для обработки выбран CSV-файл.")
        elif choice == "3":
            file_path = input("Введите путь к Excel-файлу: ").strip()
            transactions = load_transactions_from_excel(file_path)
            print("Для обработки выбран XLSX-файл.")
        elif choice == "4":
            print("До свидания!.")
            return
        else:
            print("Неверный выбор. Завершение работы.")
            return
    except Exception as e:
        print(f"Ошибка при загрузке данных: {str(e)}")
        return

    # Фильтрация по статусу
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        status = input(
            f"Введите статус, по которому необходимо выполнить фильтрацию.\n"
            f"Доступные для фильтровки статусы: {', '.join(valid_statuses)}\n").upper()
        if status in valid_statuses:
            break
        print(f'Статус операции "{status}" недоступен.')

    filtered = [tx for tx in transactions if str(tx.get("state", "")).upper() == status]
    print(f'Операции отфильтрованы по статусу "{status}"')

    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    # Сортировка
    sort_answer = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_answer == "да":
        order = input("Отсортировать по убыванию? Да/Нет): ").strip().lower()
        reverse = order == "да"
        filtered.sort(key=lambda tx: tx.get("date", ""), reverse=reverse)

    # Фильтр по валюте (рубли)
    rub_answer = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if rub_answer == "да":
        filtered = [tx for tx in filtered if tx.get("currency_code") == "RUB"]

    # Фильтр по слову в описании
    desc_answer = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if desc_answer == "да":
        word = input("Введите слово для поиска: ").strip()
        if word:
            filtered = process_bank_search(filtered, word)
            if not filtered:
                print(f"\nНе найдено ни одной транзакции, содержащих '{word}'.")
                return

    # Вывод результата
    print("\nРаспечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered)}\n")

    for tx in filtered:
        try:
            date = get_date(tx.get("date", ""))
        except ValueError:
            date = tx.get("date", "")

        description = tx.get("description", "")

        try:
            from_account = mask_account_card(str(tx.get("from", "")))
        except (ValueError, IndexError):
            from_account = tx.get("from", "")

        try:
            to_account = mask_account_card(str(tx.get("to", "")))
        except (ValueError, IndexError):
            to_account = tx.get("to", "")

        amount = tx.get("amount", "")
        currency = tx.get("currency_code", "")

        print(f"{date} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
