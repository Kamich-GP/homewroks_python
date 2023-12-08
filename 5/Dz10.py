class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Гав-Гав")

class Cat(Animal):
    def make_sound(self):
        print("Мяу")

class Cow(Animal):
    def make_sound(self):
        print("Ммууу")

dog = Dog()
dog.make_sound()
cat = Cat()
cat.make_sound()
cow = Cow()
cow.make_sound()
