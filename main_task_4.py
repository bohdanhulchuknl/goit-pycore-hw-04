def parse_input(user_input):
    """
    Розбирає введений користувачем рядок на команду та її аргументи.

    Аргументи:
    user_input (str): Введений користувачем рядок.

    Повертає:
    tuple: Команда та список аргументів.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    """
    Додає новий контакт до словника контактів.

    Аргументи:
    args (list): Список аргументів, що містить ім'я та номер телефону.
    contacts (dict): Словник контактів.

    Повертає:
    str: Повідомлення про успішне додавання контакту.
    """
    if len(args) != 2:
        return "Invalid arguments. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Змінює існуючий контакт у словнику контактів.

    Аргументи:
    args (list): Список аргументів, що містить ім'я та новий номер телефону.
    contacts (dict): Словник контактів.

    Повертає:
    str: Повідомлення про успішне оновлення контакту або про помилку.
    """
    if len(args) != 2:
        return "Invalid arguments. Usage: change [name] [new phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    """
    Виводить номер телефону за ім'ям.

    Аргументи:
    args (list): Список аргументів, що містить ім'я.
    contacts (dict): Словник контактів.

    Повертає:
    str: Номер телефону або повідомлення про помилку.
    """
    if len(args) != 1:
        return "Invalid arguments. Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    """
    Виводить всі збережені контакти з номерами телефонів.

    Аргументи:
    contacts (dict): Словник контактів.

    Повертає:
    str: Список всіх контактів з номерами телефонів.
    """
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    """
    Основна функція, яка управляє основним циклом обробки команд.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Available commands: hello, add [name] [phone], change [name] [new phone], phone [name], all, close, exit")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command. Available commands: hello, add [name] [phone], change [name] [new phone], phone [name], all, close, exit")

if __name__ == "__main__":
    main()