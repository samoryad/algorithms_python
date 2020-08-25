"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.

Начал проверку на валидацию.
Нужно доработать алгоритм на вставку между значениями слева и справа со спуском вниз узлов.
Я не успел, да и сложновато реализовать на мой взгляд, хотя есть подозрение, что существует простое
решение с использованием втроенных функций Python.
"""


class BinaryTree:
    def __init__(self, root_obj, root_list=[]):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        # список с занятыми узлами
        self.root_list = root_list
        self.root_list.append(root_obj)

    # добавить левого потомка
    def insert_left(self, new_node):
        # проверка, есть ли такой узел
        if new_node not in self.root_list:
            # если у узла нет левого потомка
            if self.left_child is None:
                # проверка, чтобы новый узел слева не мог быть больше
                # минимального родителя
                if new_node < min(self.root_list):
                    self.root_list.append(new_node)
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.left_child = BinaryTree(new_node)
                    self.root_list.pop()
                    self.root = new_node
                else:
                    print('неверный корень нового узла, он должен быть меньше')
            # если у узла есть левый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                self.root_list.pop()
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        else:
            print('неверный корень нового узла, такой узел уже существует')

    # добавить правого потомка
    def insert_right(self, new_node):
        # проверка, есть ли такой узел
        if new_node not in self.root_list:
            # если у узла нет правого потомка
            if self.right_child is None:
                # проверка, чтобы новый узел справа не мог быть меньше
                # максимального родителя
                if new_node > max(self.root_list):
                    self.root_list.append(new_node)
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.right_child = BinaryTree(new_node)
                    self.root_list.pop()
                    self.root = new_node
                else:
                    print('неверный корень нового узла, он должен быть больше')
            # если у узла есть правый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                self.root_list.pop()
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        else:
            print('неверный корень нового узла, такой узел уже существует')

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root_list.append(obj)
        self.root = obj

    # метод доступа к корню

    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_left(2)
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
r.insert_left(4)
print(r.get_left_child().get_root_val())
"""
пока работать не будет, требуется доработка на вставку между значениями.
r.insert_left(6)
print(r.get_left_child().get_root_val())
"""
print(r.root_list)
