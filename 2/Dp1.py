small_bottle = 0.10
big_bottle = 0.25
small_bottles = int(input("Введите количество бутылок литр и меньше: "))
big_bottles = int(input("Введите количество бутылок большего размера: "))


total = (small_bottle*big_bottle)+(small_bottles*big_bottles)
num = "${:.2f}".format(total)
print("Сумма, которую можно получить за сдачу бутылок:З Ниже","\n",num)

