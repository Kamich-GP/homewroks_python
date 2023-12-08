#1)Создание списка| элемент и его индекс
numbers = [10, 20, 30, 40, 50]
numbers_ind = [(number, index) for index, number in enumerate(numbers)]
#2)Создание списка строк в верхнем регистре
words = ["patato", "car", "mustang"]
words_upper = [word.upper() for word in words]
#3)Фильтрация списка чисел(четные)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_even = [x for x in numbers if x % 2 == 0]
#4)Было на уроке
names = ['Pavel','Jordan','Sasha']
names2 = [name for name in names if 'o' in name]
#5)Создание квадратов чисел (от 2 до 30)
squares = [x**2 for x in range(2, 31)]
#6)Генерация матрицы(матрица это двумерный массив в котором данные хранятся в строках и столбцах) 2 на 2 с нулями
my = ['2','33','Jordan','Pavel']
my2 = [i + '2' for i in my if 'a' in i]
#7)Создание списка длин слов пропуская слова длиной менее 3 символов
words = ['Salam', 'World', 'Python', 'list', 'title']
leng = [len(word) for word in words if len(word) >= 3]