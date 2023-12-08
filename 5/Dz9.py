class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

pers = Person("Jordan", 23)
pers1 = Person("Oleg", 22)
pers2 = Person("Sasha", 21)

people = [pers, pers1, pers2]

for pers in people:
    print("Name:", pers.name)
    print("Age:", pers.age)