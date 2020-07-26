"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.
"""
lst = [4, 5, 6, 7, 3, 9, 10, 11, 2, 13, -7, 14, 15]


def minimum_01(lst):
    min_number = max(lst)
    for el in range(len(lst)):
        if lst[el] < min_number:
            min_number = lst[el]
    return min_number


print(lst)
print(minimum_01(lst))

"""
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
"""


def minimum_02(lst):
    return min(lst)


print(minimum_02(lst))

"""
Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""
