"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from collections import namedtuple

first_hex_number = input('Введите первое число: ')
second_hex_number = input('Введите второе число: ')

RES = namedtuple('number', 'number list_el')

first_number = RES(
    number=first_hex_number,
    list_el=list(first_hex_number)
)
second_number = RES(
    number=second_hex_number,
    list_el=list(second_hex_number)
)

sum_decimal = int(first_number.number, 16) + int(second_number.number, 16)
sum_numbers = RES(
    number=sum_decimal,
    list_el=list(hex(sum_decimal))
)
mul_decimal = int(first_number.number, 16) * int(second_number.number, 16)
mul_numbers = RES(
    number=mul_decimal,
    list_el=list(hex(mul_decimal))
)

print(f'Сумма чисел из примера: {"".join(sum_numbers.list_el)[2:].upper()}, \
произведение: {"".join(mul_numbers.list_el)[2:].upper()}')
