"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""
from pympler import asizeof
from memory_profiler import profile
import time


# Решение №1
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __getitem__(self, index):
        return self.matrix[index]

    @profile
    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


t1 = time.process_time()

matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(matrix_1)
print(asizeof.asizeof(matrix_1))
matrix_2 = Matrix([[5, 26, 1], [-6, 48, -100], [7, 8, 9]])
# print(matrix_2)
print(asizeof.asizeof(matrix_2))
s = matrix_1 + matrix_2
# print(s)
print(asizeof.asizeof(s))

t2 = time.process_time()
time_diff = t2 - t1
print(f"Выполнение заняло {time_diff} сек")
print()

# Решение №2
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda r: '   '.join(
            map(str, r)), self.matrix)) + '\n'

    @profile
    def __add__(self, other):
        return Matrix(map(lambda r_1, r_2: map(
            lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))


t1 = time.process_time()

my_m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(my_m1)
print(asizeof.asizeof(my_m1))
my_m2 = Matrix([[5, 26, 1], [-6, 48, -100], [7, 8, 9]])
# print(my_m2)
print(asizeof.asizeof(my_m2))
s = my_m1 + my_m2
# print(s)
print(asizeof.asizeof(s))

t2 = time.process_time()
time_diff = t2 - t1
print(f"Выполнение заняло {time_diff} сек")

"""
Интерпретатор - Python 3.8, разрядность ОС - 64 bit

Результат выполнения:
816
816
Filename: C:/Users/DeLL G3-15/PycharmProjects/Python_Algorithms_2020_07_19/lesson_06/Lesson_06. Practice/task_1_2.py

Line #    Mem usage    Increment   Line Contents
================================================
    25     27.5 MiB     27.5 MiB       @profile
    26                                 def __add__(self, other):
    27     27.5 MiB      0.0 MiB           other = Matrix(other)
    28     27.5 MiB      0.0 MiB           result = []
    29     27.5 MiB      0.0 MiB           numbers = []
    30     27.5 MiB      0.0 MiB           for i in range(len(self.matrix)):
    31     27.5 MiB      0.0 MiB               for j in range(len(self.matrix[0])):
    32     27.5 MiB      0.0 MiB                   summa = other[i][j] + self.matrix[i][j]
    33     27.5 MiB      0.0 MiB                   numbers.append(summa)
    34     27.5 MiB      0.0 MiB                   if len(numbers) == len(self.matrix):
    35     27.5 MiB      0.0 MiB                       result.append(numbers)
    36     27.5 MiB      0.0 MiB                       numbers = []
    37     27.5 MiB      0.0 MiB           return Matrix(result)


848
Выполнение заняло 0.0625 сек

816
816
Filename: C:/Users/DeLL G3-15/PycharmProjects/Python_Algorithms_2020_07_19/lesson_06/Lesson_06. Practice/task_1_2.py

Line #    Mem usage    Increment   Line Contents
================================================
    66     27.5 MiB     27.5 MiB       @profile
    67                                 def __add__(self, other):
    68     27.5 MiB      0.0 MiB           return Matrix(map(lambda r_1, r_2: map(
    69     27.5 MiB      0.0 MiB               lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))


256
Выполнение заняло 0.0 сек

Комментарий:
Пример не очень показательный, но видно, что не смотря на разные решения (второе решение более 
компактное и интересное, да и более быстрое), память тратится почти одинаково, только результат во втором случае
менее весомый. Безусловно, второй вариант более предпочтительнее.
"""