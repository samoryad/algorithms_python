"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib


s = str(input('Введите строку: '))
set_substr = set()
for i in range(len(s)):
    if i == 0:
        for j in range(len(s) - 1):
            set_substr.add(hashlib.sha256(
                (s[i:j]).encode('utf-8')).hexdigest())
    else:
        for j in range(len(s), i, -1):
            set_substr.add(hashlib.sha256(
                (s[i:j]).encode('utf-8')).hexdigest())

print('Количество подстрок в строке =', len(set_substr))
