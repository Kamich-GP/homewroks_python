st = {}

def add_student():
    name = input("Введите имя студента: ")
    class1 = int(input("Введите класс студента: "))
    st[name] = class1
    print(f"Студент {name} добавлен в систему")

def r_student():
    name = input("Введите имя студента которого нужно удалить: ")
    if name in st:
        del st[name]
        print(f"Студент {name} удален из системы")
    else:
        print(f"Студент {name} не найден в системе")

def p_students():
    if not st:
        print("Система не содержит студентов.")
    else:
        print("Список студентов и их классы:")
        for name, grade in st.items():
            print(f"{name} в {grade} класс(е)")

while True:
    admin = input("Что вы хотите сделать? (удалить/добавить/студенты/выход): ")

    if admin.lower() == "выход":
        break

    elif admin.lower() == "добавить":
        add_student()

    elif admin.lower() == "удалить":
        r_student()

    elif admin.lower() == "студенты":
        p_students()

    else:
        print("Неверное значение| Введите правильную команду!")

print("Программа завершена Удачи:З|делал Егор")
