def total_salary(path: str) -> tuple:
    """
    Аналізує файл із заробітними платами розробників та повертає загальну та середню суму заробітної плати.

    Аргументи:
    path (str): Шлях до текстового файлу, який містить дані про заробітні плати розробників.
        Кожен рядок у файлі має формат 'прізвище,заробітна плата'.

    Повертає:
    tuple: Кортеж із двох чисел:
        - загальна сума заробітної плати (int)
        - середня заробітна плата (float)
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_salary = 0
            count = 0
            for line in file:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
                count += 1
            average_salary = total_salary / count if count > 0 else 0
            return total_salary, average_salary
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0


total, average = total_salary("./files/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")