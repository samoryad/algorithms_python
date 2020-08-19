import timeit
import random


# версия с проверкой, улучшенная
def bubble_sort_min_01(lst_obj):
    n = 1
    while n < len(lst_obj):
        check = True
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                check = False
        if check:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort_min_01(orig_list))
# замеры 10
print(
    timeit.timeit(
        "bubble_sort_min_01(orig_list)",
        setup="from __main__ import bubble_sort_min_01, orig_list",
        number=1))

orig_list = [random.randint(-100, 100) for _ in range(100)]
print(orig_list)
print(bubble_sort_min_01(orig_list))
# замеры 100
print(
    timeit.timeit(
        "bubble_sort_min_01(orig_list)",
        setup="from __main__ import bubble_sort_min_01, orig_list",
        number=1))

orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(orig_list)
print(bubble_sort_min_01(orig_list))
# замеры 1000
print(
    timeit.timeit(
        "bubble_sort_min_01(orig_list)",
        setup="from __main__ import bubble_sort_min_01, orig_list",
        number=1))


"""
Результаты обычной версии:
9.199999999997405e-06 - 10 элементов
0.0005747999999999968 - 100 элементов
0.041811 - 1000 элементов

Результаты улучшенной версии:
2.8000000000007186e-06 - 10 элементов
5.190000000000056e-05 - 100 элементов
9.369999999998824e-05 - 1000 элементов
Улучшение заментно, особенно на большом количестве элементов списка!
"""
