# 🏦 Обработка банковских операций

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 О проекте
Проект предназначен для фильтрации, сортировки и анализа банковских операций. Поддерживает работу с JSON, CSV и Excel файлами.

## 🚀 Быстрый старт

```python
from src.readers import load_transactions_from_csv
from src.processors import process_bank_search

# Загрузка транзакций
transactions = load_transactions_from_csv("data/transactions.csv")

# Поиск по описанию
filtered = process_bank_search(transactions, "перевод")
```

## ⚙️ Зависимости

- Python 3.8+
- pandas (для работы с Excel)
- pytest (для запуска тестов)
- python-dotenv (для работы с переменными окружения)

## 🛠 Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/eburgcustom/homework.git
cd homework
```

2. Установите зависимости:
```bash
# С использованием Poetry (рекомендуется)
poetry install
poetry shell

# Или с использованием pip
pip install -r requirements.txt
```

3. Создайте файл `.env` в корне проекта (см. раздел Настройка окружения)

## 🧪 Тестирование

Проект использует `pytest` для автоматизированного тестирования.

### Запуск тестов
```bash
# Все тесты
pytest

# С подробным выводом
pytest -v

# Только определенный тестовый файл
pytest tests/test_utils.py
```

## ⚙️ Настройка окружения

Создайте файл `.env` в корне проекта:
```
# Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL=INFO

# Путь к файлу с логами
LOG_FILE=logs/app.log

# Настройки API (если используются)
API_KEY=your_api_key_here
```
## Модуль generators

Модуль содержит генераторы для работы с транзакциями:

### filter_by_currency(transactions, currency_code)
Возвращает итератор по транзакциям с заданным кодом валюты.

Пример:
```
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```
### transaction_descriptions(transactions)
Возвращает описания транзакций по очереди.

Пример:
```
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```
### card_number_generator(start, stop)
Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

Пример:
```
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```
## Декоратор log

Модуль `decorators` содержит декоратор `@log`, который автоматически логирует выполнение функций.

### Пример использования:

```
from src.decorators import log

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
```
### Пример вывода:

В файл mylog.txt:
```
[2025-08-23 23:12:00] my_function ok
```
В случае ошибки:
```
[2025-08-23 23:12:05] my_function error: ZeroDivisionError. Inputs: (1, 0), {}
```
## 📚 Документация

### Поддержка форматов
Проект поддерживает чтение транзакций из:
- JSON файлов (`*.json`)
- CSV файлов (`*.csv`)
- Excel файлов (`*.xlsx`, `*.xls`)

### Пример вывода
```
2023-09-18 14:30:00 Перевод организации  
Visa Platinum 7000 79** **** 6361 -> Счет **9589  
Сумма: 1000 RUB
```

### Обработка ошибок
Функции выбрасывают следующие исключения:
- `FileNotFoundError` - если файл не найден
- `ValueError` - если формат данных неверный
- `KeyError` - если отсутствуют обязательные поля