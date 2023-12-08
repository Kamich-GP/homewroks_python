class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print("brand:", self.brand)
        print("year:", self.year)

class Car(Vehicle):
    def __init__(self, brand, year, AWD):
        super().__init__(brand, year)
        self.AWD = AWD

    def display_info(self):
        super().display_info()
        print("four-wheel drive:", self.AWD)

class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_power):
        super().__init__(brand, year)
        self.engine_power = engine_power

    def display_info(self):
        super().display_info()
        print("engine power:", self.engine_power)

car1 = Car("Bentley Bentayga", 2022, "four-wheel drive")
motorcycle1 = Motorcycle("Bmw:M 1000 RR", 2022, "193 horsepower")

car1.display_info()
print()
motorcycle1.display_info()