import sys
from pathlib import Path
from colorama import init, Fore, Style

def list_directory(path: Path, indent: str = ""):
    """
    Рекурсивно виводить структуру директорії, використовуючи кольорове форматування для директорій та файлів.

    Аргументи:
    path (Path): Об'єкт Path, що представляє шлях до директорії.
    indent (str): Рядок, що використовується для відступу при виведенні вкладених елементів (за замовчуванням "").

    Виводить:
    Імена директорій та файлів.
    """
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
                list_directory(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Permission denied: {item}{Style.RESET_ALL}")

def main():
    """
    Основна функція, яка ініціалізує кольорове форматування, перевіряє аргументи командного рядка,
    та викликає функцію list_directory для виведення структури директорії.

    Аргументи:
    Немає.

    Виводить:
    Структуру директорії з кольоровим форматуванням або повідомлення про помилку, якщо шлях недійсний.
    """
    init(autoreset=True)
    if len(sys.argv) != 2:
        print("Usage: python main_task_3.py <directory_path>")
        return

    directory_path = Path(sys.argv[1])
    if not directory_path.exists():
        print(f"{Fore.RED}Error: The path '{directory_path}' does not exist.{Style.RESET_ALL}")
        return
    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: The path '{directory_path}' is not a directory.{Style.RESET_ALL}")
        return

    list_directory(directory_path)

if __name__ == "__main__":
    main()