from unittest.mock import patch, MagicMock

from src.readers import load_transactions_from_csv, load_transactions_from_excel


def test_load_transactions_from_csv_success():
    """
    Тест успешной загрузки данных из CSV.
    Проверяет, что данные из DataFrame корректно преобразуются в список словарей.
    """
    mock_data = [{"date": "2023-01-01", "amount": 100}, {"date": "2023-01-02", "amount": 200}]

    mock_df = MagicMock()
    mock_df.to_dict.return_value = mock_data

    with patch("pandas.read_csv", return_value=mock_df):
        result = load_transactions_from_csv("fake.csv")

    assert result == mock_data
    mock_df.to_dict.assert_called_once_with(orient="records")


def test_load_transactions_from_csv_file_not_found():
    """
    Тест обработки ошибки при отсутствии CSV-файла.
    Проверяет, что функция возвращает пустой список.
    """
    with patch("pandas.read_csv", side_effect=FileNotFoundError):
        result = load_transactions_from_csv("missing.csv")

    assert result == []


def test_load_transactions_from_excel_success():
    """
    Тест успешной загрузки данных из Excel.
    Проверяет, что данные из DataFrame корректно преобразуются в список словарей.
    """
    mock_data = [{"date": "2023-02-01", "amount": 300}, {"date": "2023-02-02", "amount": 400}]

    mock_df = MagicMock()
    mock_df.to_dict.return_value = mock_data

    with patch("pandas.read_excel", return_value=mock_df):
        result = load_transactions_from_excel("fake.xlsx")

    assert result == mock_data
    mock_df.to_dict.assert_called_once_with(orient="records")


def test_load_transactions_from_excel_file_not_found():
    """
    Тест обработки ошибки при отсутствии Excel-файла.
    Проверяет, что функция возвращает пустой список.
    """
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result = load_transactions_from_excel("missing.xlsx")

    assert result == []


def test_load_transactions_from_excel_invalid_format():
    """
    Тест обработки ошибки при некорректном содержимом Excel.
    Проверяет, что функция возвращает пустой список.
    """
    with patch("pandas.read_excel", side_effect=ValueError("Invalid Excel format")):
        result = load_transactions_from_excel("bad.xlsx")

    assert result == []
