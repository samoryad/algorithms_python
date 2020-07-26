"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class StackClass:
    def __init__(self, max_quant):
        self.elems = [[]]
        self.max_quant = max_quant

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems[len(self.elems) - 1]) < self.max_quant:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return self.elems[len(self.elems) - 1].pop()

    def get_val(self):
        return self.elems[len(self.elems) -
                          1][len(self.elems[len(self.elems) - 1]) - 1]

    def stack_size(self):
        current_size = 0
        for i in self.elems:
            current_size += len(i)
        return current_size

    def stack_count(self):
        return len(self.elems)


if __name__ == '__main__':
    # создаёи объект с максимальным значением 5 тарелок в стопке
    plates_obj = StackClass(5)
    # проверяем, пустой ли стек
    print(plates_obj.is_empty())  # -> стек пустой
    # наполняем стек
    plates_obj.push_in(1)
    plates_obj.push_in(2)
    plates_obj.push_in(3)
    plates_obj.push_in(4)
    plates_obj.push_in(5)
    plates_obj.push_in(6)
    plates_obj.push_in(7)
    plates_obj.push_in(8)
    plates_obj.push_in(9)
    plates_obj.push_in(10)
    plates_obj.push_in(11)
    plates_obj.push_in(12)
    plates_obj.push_in(13)
    print(plates_obj.elems)
    # получаем значение первого элемента с вершины стека, но не удаляем сам
    # элемент из стека
    print(plates_obj.get_val())  # -> 13
    # узнаем размер стека
    print(plates_obj.stack_size())  # -> 13
    # проверяем, пустой ли стек
    print(plates_obj.is_empty())  # -> false, стек уже непустой
    # кладем еще 3 элемента в стек
    plates_obj.push_in(14)
    plates_obj.push_in(15)
    plates_obj.push_in(16)
    print(plates_obj.elems)
    # узнаем размер стека
    print(plates_obj.stack_size())  # --> 16 тарелок всего
    # узнаем сколько стопок во всём стеке
    print(plates_obj.stack_count())  # --> 4 стопки
    # убираем элемент с вершины стека и возвращаем его значение
    print(plates_obj.pop_out())  # -> 16
    # снова убираем элемент с вершины стека и возвращаем его значение
    print(plates_obj.pop_out())  # -> 15
    # вновь узнаем размер стека
    print(plates_obj.stack_size())  # -> 14
    # узнаем сколько стопок во всём стеке
    print(plates_obj.stack_count())  # -> 3
    print(plates_obj.elems)
