"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
from timeit import timeit


def simple(i):
    # Без использования «Решета Эратосфена»
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def simple_2(n):
    # С «Решетом Эратосфена»
    length = 10000 # для решения этой задачи достаточно 10000 элементов
    list_numbers = [el for el in range(length + 1)]
    list_numbers[1] = 0
    i = 2
    while i <= length:
        if list_numbers[i] != 0:
            j = i + i
            while j <= length:
                list_numbers[j] = 0
                j = j + i
        i += 1
    return [number for number in list_numbers if number != 0][n - 1]


simple_number_index = int(
    input('Введите порядковый номер искомого простого числа: '))
print(simple(simple_number_index))
print(simple_2(simple_number_index))
print(timeit(
    "simple(simple_number_index)",
    setup="from __main__ import simple, simple_number_index",
    number=100))
print(timeit(
    "simple_2(simple_number_index)",
    setup="from __main__ import simple_2, simple_number_index",
    number=100))

"""
Мои данные:
время на поиск 10 числа:
Без "Решета" - 0.001948599999999967
С "Решетом" - 0.34315209999999996

время на поиск 100 числа:
Без "Решета" - 0.21150240000000053
С "Решетом" - 0.3371921999999996

время на поиск 1000 числа:
Без "Решета" - 40.0245567
С "Решетом" - 0.3364644000000041
"""
# судя по всему, в первом случае квадратичная сложность O(n^2), а во втором ближе к n(log(n)),
# поэтому при нарастании элементов второй алгоритм начинает выиграывать у первого
# (это хорошо видно на графике сложности алгоритмов)

# задание сначала пробовал через сделать через set, но почему-то оно не работает на элементах более 130,
# так и не понял почему при преобразовании списка в set (a = set(a) из примера по ссылке) при создании списка
# более 130 элементов, числа появляются не на своём месте...
