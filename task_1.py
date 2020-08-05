"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

# странно, но у меня получается, что список заполняется быстрее, правда на небольших количествах (10000) это менее
# заметно, там иногда словарь выигрывает, но на 100000 итерациях - список
# всё же быстрее.
# Возможно, нужно заполнять их другими методами
import time


def check_time(func):
    def wrapper(n):
        start_val = time.time()
        func(n)
        end_val = time.time()
        return end_val - start_val
    return wrapper


@check_time
def fill_dict(n):
    full_dict = {key: key for key in range(0, n)}
    return full_dict


@check_time
def fill_list(n):
    full_list = [i for i in range(0, n)]
    return full_list


@check_time
def fill_tuple(n):
    full_tuple = {i for i in range(0, n)}
    return full_tuple


print(f'{fill_dict(1000000)} - словарь')
print(f'{fill_list(1000000)} - список')
print(f'{fill_tuple(1000000)} - кортеж')
