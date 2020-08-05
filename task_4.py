"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib
from uuid import uuid4

cache = {}
salt = uuid4().hex


def check_url(url):
    global cache
    global salt
    h = hashlib.sha256((salt + url).encode('utf-8')).hexdigest()
    if h in cache:
        print('страница есть в кэше')
    else:
        print('такой страницы нет, добавляю её в кэш')
        cache[h] = url


check_url('https://yandex.ru')
check_url('https://mail.ru')
check_url('https://yandex.ru')
check_url('https://yandex.ru')
check_url('https://mail.ru')


"""
через ООП не успел доделать, нужно скорее всего сделать основные операции в классе, а логику уже с экземплярами класса,
планировал копать туда,
здесь же в if нужно поменять обращение к методу класса на значение из этого метода, поэтому работает некорректно.

class CacheUrlClass:
    def __init__(self, salt, url):
        self.hash_dict = {}
        self.salt = salt
        self.url = url

    def create_hash(self):
        return hashlib.sha256((self.salt + self.url).encode('utf-8')).hexdigest()

    def check_dict(self):
        if self.create_hash() in self.hash_dict:
            return print('страница есть в кэше')
        else:
            self.add_dict()

    def add_dict(self):
        self.hash_dict[self.create_hash()] = self.url


if __name__ == '__main__':
    salt = uuid4().hex
    trial = CacheUrlClass(salt, 'https://yandex.ru/')
    print(trial.create_hash())
    print(trial.check_dict())
    trial = CacheUrlClass(salt, 'https://mail.ru/')
    print(trial.create_hash())
    trial.check_dict()
    trial = CacheUrlClass(salt, 'https://yandex.ru/')
    print(trial.create_hash())
    trial.check_dict()
    print(trial.hash_dict)
"""
