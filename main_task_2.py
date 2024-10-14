def get_cats_info(path:str) -> list:
    """
    Читає файл із інформацією про котів та повертає список словників з даними про кожного кота.

    Аргументи:
    path (str): Шлях до текстового файлу, який містить дані про котів.
        Кожен рядок у файлі має формат 'ідентифікатор,ім'я,вік'.

    Повертає:
    list: Список словників, де кожен словник містить інформацію про одного кота з ключами:
        - "id" (str): Унікальний ідентифікатор кота
        - "name" (str): Ім'я кота
        - "age" (str): Вік кота
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_dict = {"id": cat_id, "name": name, "age": age}
                cats_info.append(cat_dict)
            return cats_info
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


cats_info = get_cats_info("./files/cats.txt")
print(cats_info)