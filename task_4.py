"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit


def check_dict():
    standard_dict = {'Name': 'Gogi', 'Age': '23', 'Country': 'Georgia'}
    standard_dict.get('Name')
    standard_dict['phone'] = "89265622325"
    standard_dict['Country'] = 'Russia'
    standard_dict.popitem()
    standard_dict.get('phone')
    sorted(standard_dict.items(), key=lambda item: item[0])
    sorted(standard_dict.items(), key=lambda item: item[1])


def check_ordered_dict():
    new_dict = OrderedDict(
        [('Name', 'Gogi'), ('Age', '23'), ('Country', 'Georgia')])
    new_dict.get('Name')
    new_dict['phone'] = "89265622325"
    new_dict['Country'] = 'Russia'
    new_dict.popitem()
    new_dict.get('phone')
    sorted(new_dict.items(), key=lambda item: item[0])
    sorted(new_dict.items(), key=lambda item: item[1])


print(timeit(
    "check_dict()",
    setup="from __main__ import check_dict",
    number=1000000))

print(timeit(
    "check_ordered_dict()",
    setup="from __main__ import check_ordered_dict",
    number=1000000))


"""
у меня получилось, что обычный словарь всё же чуть выигрывает у упорядоченного,
правда, когда начинаются сортировки, время сокращается, возможно в этом преимущество OrderedDict
для 10000:
0.033973800000000005
0.0449017
для 100000:
0.2261136
0.277702
для 1000000:
2.1265926
2.6953423
"""
