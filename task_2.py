"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

# похоже в примере была ошибка: если в функции recursive_reverse возвращать return str(number % 10)
# в обратную строку добавится 0, поэтому заменил на: return ''
from timeit import timeit


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


# для ускорения работы алгоритма применил декоратор - мемоизацию, теперь многие значения уже будут в памяти, их
# можно просто оттуда доставать, тем самым экономя время рекурсии
def memorize(func):
    memory = {}

    def check_memory(n):
        value = memory.get(n)
        if value is None:
            value = func(n)
            memory[n] = value
        return value
    return check_memory


@memorize
def recursive_reverse_1(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print('до мемоизации:')
print(456, recursive_reverse(456), timeit(
    "recursive_reverse(456)",
    setup="from __main__ import recursive_reverse",
    number=100000))
print(456789, recursive_reverse(456789), timeit(
    "recursive_reverse(456789)",
    setup="from __main__ import recursive_reverse",
    number=100000))
print('после мемоизации:')
print(456, recursive_reverse(456), timeit(
    "recursive_reverse_1(456)",
    setup="from __main__ import recursive_reverse_1",
    number=100000))
print(456789, recursive_reverse(456789), timeit(
    "recursive_reverse_1(456789)",
    setup="from __main__ import recursive_reverse_1",
    number=100000))
