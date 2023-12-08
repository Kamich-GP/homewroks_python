sum = float(input("Введите сумму заказа: "))

nal = 0.19
pay = 0.09

sl = sum * nal
sp = sum * pay

#Вычисление общей суммы с налогом и чаем
num_sum = sum + sl + sp

#Вывод результатов
a = "{:.2f}".format(sl)#Налог
b = "{:.2f}".format(sp)#Чай
c = "{:.2f}".format(num_sum)#Сумма(Итого)

print("Налог: $", a)
print("Чай: $", b)
print("Итого: $", c)