"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828,
    41.62921998361278,
    18.45859540989644,
    12.128870723745806,
     8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806,
    18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import timeit
import random


def merge_sorting(my_list):
    if len(my_list) > 1:
        center = len(my_list) // 2
        left_part = my_list[:center]
        right_part = my_list[center:]
        merge_sorting(left_part)
        merge_sorting(right_part)

        left_idx, right_idx, tot_idx = 0, 0, 0
        while left_idx < len(left_part) and right_idx < len(right_part):
            if left_part[left_idx] < right_part[right_idx]:
                my_list[tot_idx] = left_part[left_idx]
                left_idx += 1
            else:
                my_list[tot_idx] = right_part[right_idx]
                right_idx += 1
            tot_idx += 1

        while left_idx < len(left_part):
            my_list[tot_idx] = left_part[left_idx]
            left_idx += 1
            tot_idx += 1

        while right_idx < len(right_part):
            my_list[tot_idx] = right_part[right_idx]
            right_idx += 1
            tot_idx += 1
        return my_list


n = int(input('Введите число элементов списка, число элементов должно быть более 1: '))
float_list = [random.uniform(0, 50) for _ in range(n)]
print(float_list)
print(merge_sorting(float_list))

print(
    f' Время, затраченное на сортировку "слиянием" списка из {n} элементов: ')
print(timeit.timeit(
    "merge_sorting(float_list)",
    setup="from __main__ import merge_sorting, float_list",
    number=1))
