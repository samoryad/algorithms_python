"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
from statistics import median
from random import randint
import numpy
import timeit


def shell_sorting(my_list):
    def new_increment(my_list):
        i = int(len(my_list) / 2)
        yield i
        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(round(i / 2.2))
            yield i

    for increment in new_increment(my_list):
        for i in range(increment, len(my_list)):
            for j in range(i, increment - 1, -increment):
                if my_list[j - increment] < my_list[j]:
                    break
                my_list[j], my_list[j - increment] = my_list[j - increment], my_list[j]
    return my_list


def my_median(some_list):
    half = len(some_list) // 2
    some_list.sort()
    if not len(some_list) % 2:
        return (some_list[half - 1] + some_list[half]) / 2.0
    return some_list[half]


m = int(input('Введите натуральное число: '))

list_for_test = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Исходный список: {list_for_test}')
print(f'Медиана: {median(list_for_test)}')
print(f'Отсортированный список: {sorted(list_for_test)}')
print(
    timeit.timeit(
        "median(list_for_test)",
        setup="from __main__ import median, list_for_test",
        number=1))

list_for_test = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Исходный список: {list_for_test}')
print(f'Медиана: {numpy.median(list_for_test)}')
print(f'Отсортированный список: {sorted(list_for_test)}')
# как посмотреть время ещё одной функции median, но уже из библиотеки numpy?, не смог разобраться
# print(
#     timeit.timeit(
#         "median(list_for_test)",
#         setup="from __main__ import median, list_for_test",
#         number=1))

list_for_test = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Исходный список: {list_for_test}')
print(f'Медиана: {shell_sorting(list_for_test)[len(list_for_test) // 2]}')
print(f'Отсортированный список: {sorted(list_for_test)}')
print(
    timeit.timeit(
        "shell_sorting(list_for_test)",
        setup="from __main__ import shell_sorting, list_for_test",
        number=1))

list_for_test = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Исходный список: {list_for_test}')
print(f'Медиана: {my_median(list_for_test)}')
print(f'Отсортированный список: {sorted(list_for_test)}')
print(
    timeit.timeit(
        "my_median(list_for_test)",
        setup="from __main__ import my_median, list_for_test",
        number=1))

"""
К сожалению, не нашёл синтаксис проверки времени numpy.median.
Как быть в случае, если из разных библиотек одинаковые функции импортируются?
Сортировка Шелла довольно сложная, особенно в коде.
Действительно, встроенные функции работают быстрее:
10 элементов:
4.099999999951365e-06
# 3.7999999999982492e-06
4.2500000000167404e-05
2.2999999997885823e-06
100 элементов:
1.3599999999946988e-05
# 1.3299999999993872e-05
0.0007036000000000264
2.300000000010627e-06
"""