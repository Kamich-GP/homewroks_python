import random# импортирую рандом
igr= input("Сделайте выбор: камень, ножницы или бумага: ")

voz = ["камень", "бумага", "ножницы"]
com= random.choice(voz)#делаю так чтобы компьютер выберал значение
print(f"Вы выбрали {igr}, компьютер выбрал {com}")


#логические вычисления
if igr == com:
    print(f"Оба выбрали {igr}. Ничья")
elif igr == "камень":
    if com == "ножницы":
        print("Камень бьет ножницы Вы выиграли")
    else:
        print("Бумага покрывает камень. Вы проиграли")
elif igr == "бумага":
    if com == "камень":
        print("Бумага оборачивает камень. Вы выиграли")
    else:
        print("Ножницы режут бумагу. Вы проиграли.")
elif igr == "ножницы":
    if com == "бумага":
        print("Ножницы режут бумагу. Вы выиграли.")
    else:
        print("Камень бьет ножницы. Вы проиграли.")
else:
    print("ОШИБКА ,Вы написали неверно попробуйте(Камень/Ножницы/Бумага)!")