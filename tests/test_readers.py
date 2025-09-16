from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src.readers import load_transactions_from_csv, load_transactions_from_excel


def test_load_transactions_from_csv_success():
    """Тест успешного чтения CSV файла с транзакциями."""
    mock_data = [{"date": "2023-01-01", "amount": 100}, {"date": "2023-01-02", "amount": 200}]

    with patch("pandas.read_csv") as mock_read_csv:
        mock_df = MagicMock()
        mock_df.to_dict.return_value = mock_data
        mock_read_csv.return_value = mock_df

        with patch("os.path.exists", return_value=True):
            result = load_transactions_from_csv("dummy_path.csv")

            assert result == mock_data
            mock_read_csv.assert_called_once_with("dummy_path.csv")


def test_load_transactions_from_csv_file_not_found():
    """Тест обработки отсутствующего CSV файла."""
    with patch("os.path.exists", return_value=False):
        with pytest.raises(FileNotFoundError):
            load_transactions_from_csv("nonexistent.csv")


def test_load_transactions_from_csv_empty_file():
    """Тест обработки пустого CSV файла."""
    with patch("pandas.read_csv", side_effect=pd.errors.EmptyDataError("File is empty")):
        with patch("os.path.exists", return_value=True):
            with pytest.raises(ValueError, match="Файл пуст"):
                load_transactions_from_csv("empty.csv")


def test_load_transactions_from_csv_unexpected_error():
    """Тест обработки непредвиденной ошибки при чтении CSV."""
    with patch("pandas.read_csv", side_effect=Exception("Unexpected error")):
        with patch("os.path.exists", return_value=True):
            with pytest.raises(ValueError, match="Ошибка при чтении файла: Unexpected error"):
                load_transactions_from_csv("broken.csv")


def test_load_transactions_from_excel_success():
    """Тест успешного чтения Excel файла с транзакциями."""
    mock_data = [{"date": "2023-02-01", "amount": 300}, {"date": "2023-02-02", "amount": 400}]

    with patch("pandas.read_excel") as mock_read_excel:
        mock_df = MagicMock()
        mock_df.to_dict.return_value = mock_data
        mock_read_excel.return_value = mock_df

        with patch("os.path.exists", return_value=True):
            result = load_transactions_from_excel("dummy_path.xlsx")

            assert result == mock_data
            mock_read_excel.assert_called_once_with("dummy_path.xlsx")


def test_load_transactions_from_excel_file_not_found():
    """Тест обработки отсутствующего Excel файла."""
    with patch("os.path.exists", return_value=False):
        with pytest.raises(FileNotFoundError):
            load_transactions_from_excel("nonexistent.xlsx")


def test_load_transactions_from_excel_empty_file():
    """Тест обработки пустого Excel файла."""
    with patch("pandas.read_excel", side_effect=pd.errors.EmptyDataError("File is empty")):
        with patch("os.path.exists", return_value=True):
            with pytest.raises(ValueError, match="Файл пуст"):
                load_transactions_from_excel("empty.xlsx")


def test_load_transactions_from_excel_unexpected_error():
    """Тест обработки непредвиденной ошибки при чтении Excel."""
    with patch("pandas.read_excel", side_effect=Exception("Unexpected excel error")):
        with patch("os.path.exists", return_value=True):
            with pytest.raises(ValueError, match="Ошибка при чтении файла: Unexpected excel error"):
                load_transactions_from_excel("broken.xlsx")
