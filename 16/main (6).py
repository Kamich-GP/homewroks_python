import unittest


class Calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def calc1(self):
        return self.num1 * self.num2


    def calc2(self):
        return self.num1 / self.num2


    def calc3(self):
        return self.num1 + self.num2


    def calc4(self):
        return self.num1 - self.num2


num1 = int(input(': '))
num2 = int(input(': '))
calc = Calc(num1=num1, num2=num2)

print(calc.calc1())
print(calc.calc2())
print(calc.calc3())
print(calc.calc4())


class TestOne(unittest.TestCase):
    def test_check_1(self):
        check1 = calc.calc1()
        self.assertEqual(check1, 10, '/e')


    def test_check_2(self):
        check2 = calc.calc2()
        self.assertEqual(check2, 10, '/e')


    def test_check_3(self):
        check3 = calc.calc3()
        self.assertEqual(check3, 10, '/e')


    def test_check_4(self):
        check4 = calc.calc4()
        self.assertEqual(check4, 10, '/e')



        # self.assertEqual(calc1(num1, num2), "that's right", '/e')
        # self.assertEqual(calc2(num1, num2), "that's right", '/e')
        # self.assertEqual(calc3(num1, num2), "that's right", '/e')
        # self.assertEqual(calc4(num1, num2), "that's right", '/e')


# while True:


    # elif start == 'n':
    #     break

    # else:
    #     print('ERROR')





