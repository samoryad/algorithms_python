"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random


def rand_numb(n, number):
    i = int(input('Введите число: '))
    if i == n:
        return print('Вы угадали')
    elif number > 10:
        return print('вы проиграли')
    elif i > n:
        print('число меньше')
        rand_numb(n, number + 1)
    elif i < n:
        print('число больше')
        rand_numb(n, number + 1)


rand_numb(random.randint(1, 100), 0)
