"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit
import cProfile
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1, 5, 7, 5, 5]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    return f'Чаще всего встречается число {Counter(array).most_common(1)[0][0]}, ' \
        f'оно появилось в массиве {Counter(array).most_common(1)[0][1]} раз(а)'


def func_4():
    my_dict = {i: array.count(i) for i in array}
    my_list = sorted(my_dict.items(), key=lambda key_value: key_value[1])
    return f'Чаще всего встречается число {my_list[-1][0]}, ' \
        f'оно появилось в массиве {my_list[-1][1]} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(timeit(
    "func_1()",
    setup="from __main__ import func_1",
    number=100000))
print(timeit(
    "func_2()",
    setup="from __main__ import func_2",
    number=100000))
print(timeit(
    "func_3()",
    setup="from __main__ import func_3",
    number=100000))
print(timeit(
    "func_4()",
    setup="from __main__ import func_4",
    number=100000))

cProfile.run("func_1()")
cProfile.run("func_2()")
cProfile.run("func_3()")
cProfile.run("func_4()")

# к сожалению мне не удалось получить алгоритм быстрее заданных, но самый лаконичный получился, наверное,
# алгоритм №3 (правда "под капотом" происходит большее количество вызовов, чем в других алгоритмах)
# первый вариант получился самым быстрым (он один раз пробегает по списку и вычисляет самый повторяющийся элемент).
# Второй и четвёртый чуть медленнее (они должны создать новые список и словарь соответственно
# и работать дополнительно с ними, ncalls показывает это наглядно).
