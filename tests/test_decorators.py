import pytest

from src.decorators import log


def test_log_success_console(capsys):
    """
    Тест успешного выполнения функции с декоратором log без указания filename.
    Проверяет:
    - вывод функции в консоль сообщения 'имя функции ок'
    - корректное возвращаемое значение
    """

    @log()
    def add(x: int, y: int) -> int:
        return x + y

    result = add(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "add ok" in captured.out


def test_log_error_console(capsys):
    """
    Тест ошибки выполнения функции с декоратором log без указания filename.
    Проверяет:
    - вывод сообщения в консоль об ошибке с типом исключения
    - наличие входных аргументов в сообщении
    """

    @log()
    def div(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    captured = capsys.readouterr()
    assert "div error:" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_success_file(tmp_path):
    """
    Тест успешного выполнения функции с декоратором log и записи в файл.
    Проверяет корректное сохранение строки 'имя функции ок' в лог файл.
    """
    log_file = tmp_path / "log.txt"

    @log(filename=log_file)
    def mul(x: int, y: int) -> int:
        return x * y

    result = mul(3, 4)
    assert result == 12
    content = log_file.read_text()
    assert "mul ok" in content


def test_log_error_file(tmp_path):
    """
    Тест ошибки выполнения функции с декоратором log и записи в файл.
    Проверяет:
    - корректную запись об ошибке с типом исключения
    - наличие входных аргументов в лог файл
    """
    log_file = tmp_path / "log.txt"

    @log(filename=log_file)
    def sub(x: int, y: int) -> int:
        return x - y if y != 0 else 1 / 0  # вызов ZeroDivisionError

    with pytest.raises(ZeroDivisionError):
        sub(10, 0)

    content = log_file.read_text()
    assert "sub error:" in content
    assert "Inputs: (10, 0), {}" in content
