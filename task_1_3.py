"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce
from pympler import asizeof
import memory_profiler
import time


# решение №1
def mul_list(el_1, el_2):
    return el_1 * el_2


t1 = time.process_time()
m1 = memory_profiler.memory_usage()

uniq_list = [el for el in range(100, 1001, 2)]
print(asizeof.asizeof(uniq_list))
result = reduce(mul_list, uniq_list)
# print(result)
print(asizeof.asizeof(result))

t2 = time.process_time()
m2 = memory_profiler.memory_usage()

time_diff = t2 - t1
mem_diff = m2[0] - m1[0]
print(f"Выполнение заняло {time_diff} сек and {mem_diff} Mib")
print()

# решение №2
t1 = time.process_time()
m1 = memory_profiler.memory_usage()

result = reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)])
# print(result)
print(asizeof.asizeof(result))

t2 = time.process_time()
m2 = memory_profiler.memory_usage()

time_diff = t2 - t1
mem_diff = m2[0] - m1[0]
print(f"Выполнение заняло {time_diff} сек and {mem_diff} Mib")

"""
Интерпретатор - Python 3.8, разрядность ОС - 64 bit

Результат выполнения:
18184
560
Выполнение заняло 0.0 сек and 0.015625 Mib

560
Выполнение заняло 0.0 сек and 0.0 Mib

Комментарий:
Пример довольно показательный. В первом решении память тратится ещё и на создание списка чисел от 100 до 1000.
Поэтому, второй вариант предпочтительнее.
"""