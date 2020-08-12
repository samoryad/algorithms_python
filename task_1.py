"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# переделал создание нового списка через генератор, он чуть быстрее цикла
# с append
def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


print(func_1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
      timeit(
    "func_1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])",
    setup="from __main__ import func_1",
    number=100000))
print(func_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
      timeit(
    "func_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])",
    setup="from __main__ import func_2",
    number=100000))
