"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

# опять, похоже в первом задании ошибка, значение возвращалось None, исправил
# также округлил во втором задании получающееся число (до коррекции оно
# было Float)
from timeit import timeit
import cProfile


# решение 1
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return ''
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return str(num) + revers(enter_num, revers_num)


# решение 2
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return round(revers_num)


# решение 3
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print(revers(123456789), revers_2(123456789), revers_3(123456789))

cProfile.run('revers(123456789)')
cProfile.run('revers_2(123456789)')
cProfile.run('revers_3(123456789)')


print(timeit(
    "revers(123456789)",
    setup="from __main__ import revers",
    number=100000))
print(timeit(
    "revers_2(123456789)",
    setup="from __main__ import revers_2",
    number=100000))
print(timeit(
    "revers_3(123456789)",
    setup="from __main__ import revers_3",
    number=100000))

# слишком малое число для анализа затраченного времени через cProfile, но и по этим данным видно,
# что в рекурсии (решение 1) идёт большее кол-во вызовов (ncalls = 10/1) => она медленнее всех,
# решение 2 (через цикл) получилось более затратным скорее всего из-за большего количества вычислений по
# сравнению с решением 3 (через срезы), поэтому 3 вариант - оптимальный
# (да и самый лаконичный)
