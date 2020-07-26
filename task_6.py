"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class QueueClass:
    def __init__(self):
        self.basic_queue = []
        self.second_queue = []
        self.finished_tasks = []

    def is_empty(self):
        return self.basic_queue == []

    def to_queue(self, item):
        self.basic_queue.insert(0, item)

    def to_finished_tasks(self):
        elem = self.basic_queue.pop()
        return self.finished_tasks.append(elem)

    def todo_queue(self):
        self.second_queue.insert(0, self.basic_queue.pop())

    def from_queue(self):
        self.finished_tasks.append(self.basic_queue.pop())

    def size(self):
        return len(self.basic_queue)


if __name__ == '__main__':
    trial = QueueClass()
    trial.to_queue("1")
    trial.to_queue("2")
    trial.to_queue("3")
    trial.to_queue("4")
    print(trial.basic_queue)
    trial.from_queue()
    print(trial.basic_queue)
    print(trial.finished_tasks)
    trial.from_queue()
    print(trial.basic_queue)
    print(trial.finished_tasks)
    trial.todo_queue()
    print(trial.basic_queue)
    print(trial.second_queue)
