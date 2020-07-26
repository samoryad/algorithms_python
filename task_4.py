"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

# Если я правильно понял задание...
# 1: Сложность = O(n); T(n) = n + 4
system_authentication = {"login": "password"}  # O(1)


def check_in_01(username, password, auth):
    login_list = list(system_authentication.items())  # O(n)
    if auth is True:  # O(1)
        if username == login_list[0][0] and password == login_list[0][1]:  # O(1) + O(1)
            print("welcome")
        else:
            print('login or password is not correct')
    else:
        print('your account is not active, please activate it')


check_in_01('login', 'password', True)
check_in_01('df', 'fsdf', True)
check_in_01('login', 'password', False)


# 2: Сложность = O(1); T(n) = 4  -  этот вариант лучше
system_authentication_01 = ["login", "password", True]  # O(1)

def check_in_02(username, password, auth):
    if auth == system_authentication_01[2]:  # O(1)
        if username == system_authentication_01[0] and password == system_authentication_01[1]:  # O(1) + O(1)
            print("welcome")
        else:
            print('login or password is not correct')
    else:
        print('your account is not active, please activate it')


check_in_02('login', 'password', True)
check_in_02('df', 'fsdf', True)
check_in_02('login', 'password', False)