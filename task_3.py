"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from collections import deque
from timeit import timeit


def check_list():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_list.append(1)
    my_list.insert(0, 1)
    my_list.pop()
    my_list.pop(0)
    my_list.append(1)
    my_list.insert(0, 1)
    my_list.pop()
    my_list.pop(0)


def check_deque():
    deq_obj = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    deq_obj.append(1)
    deq_obj.appendleft(1)
    deq_obj.pop()
    deq_obj.popleft()
    deq_obj.append(1)
    deq_obj.appendleft(1)
    deq_obj.pop()
    deq_obj.popleft()


print(timeit(
    "check_list()",
    setup="from __main__ import check_list",
    number=1000000))

print(timeit(
    "check_deque()",
    setup="from __main__ import check_deque",
    number=1000000))

"""
у меня получилось примерно одинаково, то список быстрее, то дек, наверное в случаях специфических команд
Deque, например, rotate он должен быть быстрее:
для 10000:
0.0183363
0.0210211
для 100000:
0.1435883
0.09274850000000001
для 1000000:
0.91443
0.9213043
"""
