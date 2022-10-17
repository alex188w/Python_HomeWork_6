# Задача 22.    Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
from timeit import default_timer


def wrap(n):
    def time_it(func):
        def wrapper(numb):
            res = 0
            for el in range(n):
                start_time = default_timer()
                func(numb)
                # правая отсечка времени и результат
                delta = default_timer() - start_time
                print(f'Время на выполнение данной программы заняло: {delta}')
                res += delta
            # логгирование
            # и любые другие действия
        return wrapper
    return time_it


@wrap(1)
def sum_lst(n):
    lst = []
    sum_n = 0
    for i in range(n):
        num = random.randint(0, 99)
        lst.append(num)
        if i % 2 != 0:
            sum_n += lst[i]
    print(f'Заданный сисок: {lst}')
    print(f'Сумма элементов на нечетных позициях: {sum_n}')
    return n


@wrap(1)
def sum_lst_1(n):
    lst = [random.randint(0, 99) for i in range(7)]
    print(f'Заданный сисок: {lst}')
    print(
        f'Сумма элементов на нечетных позициях: {sum(list(filter(lambda x: lst.index(x) % 2, lst)))}')
    return n


sum_lst(7)
sum_lst_1(7)
