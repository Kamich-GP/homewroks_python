contacts ={}
#Добавит контакт
def add_contact():
    name = input("Введите имя контакта: ,Для пропуска нажмите Enter ")
    number = input("Введите номер контакта: ,Для пропуска нажмите Enter ")
    contacts[name] = number

#Удалить контакт
def delete_contact():
    name = input("Введите имя контакта, который нужно удалить: ")
    if name in contacts:
        del contacts[name]
        print("Контакт успешно удален")
    else:
        print("Контакт не найден")

#Обновить контакт
def upgrate_contact():
    name = input("Введите имя контакта, который нужно обновить: ")
    if name in contacts:
        print(f"Имя: {name}; Номер:", contacts[name])
        new_name = input("Введите новое имя контакта:,Для пропуска нажмите Enter ")
        new_number = input("Введите новый номер контакта:, Для пропуска нажмите Enter ")

        if new_name:
            contact = [name, new_name]
            contact.remove(new_name)
            print(contact)

        if new_number:
            contacts[name] = new_number

        print("Контакт обновлен")
    else:
        print("Контакт не найден")
#Показать список контактов
def show_contacts():
    print("Cписок контактов:")
    for name, number in contacts.items():
        print(f"Имя:{name} ;Номер:{number}")
#Цикл до окончания (Выход)
while True:
    print("\nВыберите действие:")
    print("1.Добавить контакт")
    print("2. Удалить контакт")
    print("3. Изменить контакт")
    print("4. Вывести список контактов")
    print("5. Выйти(Ввести 'Выход')")

    choice = input("Введите номер действия: ")
#Выбор
    if choice == "1":
        add_contact()
    elif choice == "2":
        delete_contact()
    elif choice == "3":
        upgrate_contact()
    elif choice == "4":
        show_contacts()
    elif choice == "Выход":
        break
    else:
        print("Некорректный ввод:з Попробуйте еще раз")