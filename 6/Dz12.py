#красными строками обозначается начало и конец
#1
n = int(input("Введите число: "))
#Если n меньше одного то принт
if n < 1:
    print("Введите пожалуйста положительное число.")
else:
#Сумма
    sum = n * (n + 1) / 2
    print("Сумма натуральных чисел от 1 до", n, "ровна", sum)

#2
my_list=(6,'a',"5")
#проверяем наш список/и выводим список
for p in my_list:
    print(p)

#3
all_prod={"Весь магазин":{}}
#cсоздаю цикл
while True:
    admin=input("Что вы хотите сделать?(добавить/список/выход): ")
    #выход
    if admin=="выход":
        break
        #функция добваить
    elif admin=="добавить":
        prod_name=input("Введите название продукта: ")
        prod_count =input("Введите кол-во: ")
        all_prod["Весь магазин"][prod_name]=int(prod_count)
        print(f'Продукт"{prod_name}"добавлен в список')
    elif admin == "список":
        # функция список
        print("Спиок продуктов и их кол-во")
        for prod,count in all_prod["Весь магазин"].items():
            print(f'{prod}:{count}')
    else:
        print("Неверное значение")

print("Программа завершена")

#4
#[1:5]/от:до:промежуток List
p=["ivan","pavel","jordan","Forjer","Sasa","Om"]
print(p[1:3])

#5
#В этой части кода я создаю переменную х и задаю некий список затем я делаю так чтобы он фильтровал анонимную функцию
x=[1,2,3,4]
a= filter(lambda a:a*2==4,x)
print(list(a))

#6
#В этой части кода я создаю функцию my1 и создаю переменную "x" после чего ищу джердан в х если он есть то принт если нет то пропуск
def my1():
    x=['Jordan',"Pahsa","Pavel"]
    if "Jordan" in x:
        print(x)
    else:
        pass

#7
#В этой части кода я создаю класс и кидаю в него переменные, после чего беру и вывожу их через класс
class Car():
    name="Bugatti"
    color="white"
    max_speed= 300

print(Car.name,Car.color,Car.max_speed)

#8
#в этой части кода я взял так сказать (ребенка) и присвоил ему сво-ва родителя(Car)
class Car:
   def __init__(self, model, color, year):
       self.model = model
       self.color = color
       self.year = year
class SuperCar(Car):
   def __init__(self, model, color, year, sponsor="Mers"):
       super().__init__(model, color, year)
       self.sponsor = sponsor
test= SuperCar(model="Bugatti",color="red",year=2022)
print(test.color)
test2= Car(model="Bentayga",color="blue",year=2021)
print(test2.year)

#9
#set убирает лишние символы|они не дубоирубтся
num = [1,1,2,3,2,2,3,4,5,5,5,4]
num1 = set(num)
print(num1)

#10
numbers = [1, 2, 3, 6, 8]
#добавляем число 9 в конец списка
numbers.append(9)
#выводим список на экран
print(numbers)

#11
#Тут я вывожу возвраст студента через (ключ) если можно так сказать
students = {'John': 20,'Jordan': 23,'Alex': 21,'Sasha': 19}
print(students['John'])