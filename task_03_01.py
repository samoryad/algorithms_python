from random import randint


def checking(my_list):
    copy_list = my_list.copy()
    for i in range(len(my_list)):
        left_counter, equal_counter, right_counter = 0, 0, 0
        for j in range(len(copy_list)):
            if my_list[i] < copy_list[j]:
                left_counter += 1
            elif my_list[i] == copy_list[j]:
                equal_counter += 1
            elif my_list[i] > copy_list[j]:
                right_counter += 1
        if (left_counter + equal_counter // 2) == (len(copy_list) // 2):
            return my_list[i]


# def checking(my_list):
#     copy_list = my_list.copy()
#     for i in range(len(my_list)):
#         left_counter, equal_counter, right_counter = [], [], []
#         for j in range(len(copy_list)):
#             if my_list[i] < copy_list[j]:
#                 left_counter.insert(-1, my_list[i])
#             elif my_list[i] == copy_list[j]:
#                 equal_counter.insert(-1, my_list[i])
#             elif my_list[i] > copy_list[j]:
#                 right_counter.insert(-1, my_list[i])
#         if (len(left_counter)) == (len(right_counter)):
#             return my_list[i]


m = int(input('Введите натуральное число: '))
list_for_test = [randint(-100, 100) for _ in range(2 * m + 1)]
print(list_for_test)
print(checking(list_for_test))
print(sorted(list_for_test))

"""
так и не смог сделать полностью рабочий алгоритм, много чего пробовал,
но всё равно работает иногда некорректно, например в этом примере, см. ниже: 
(полагаю нужно как-то учесть количество повторяющихся чисел в списке, 
возможно есть встроенные функции, которые помогли это учесть...)
"""
new_list = [5, 5, 3, 1, 2, 3, 5, 3, 3, 2, 5, 5, 5, 5, 7]
print(new_list)
print(sorted(new_list))
print(checking(new_list))
