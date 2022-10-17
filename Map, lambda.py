# Задача 16. Задайте список из n чисел последовательности
# 〖(1+1/n)〗^n  и выведите на экран их сумму.

from timeit import default_timer

num = input("Введите натуральное число n: ")
try:
    tmp = int(num)
except:
    print('Введенное значение не является натуральным числом')
    exit()


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
    sum = 0
    for i in range(1, int(n) + 1):
        elem_n = (1 + 1/i) ** i
        sum += elem_n
        lst.append(elem_n)
    print(
        f'Заданная последовательность 〖(1+1/n)〗^ n от 1 до {num} имеет вид: \n {lst}')
    print(f'Сумма элементов данной последовательности составляет: {sum}')
    return n, sum


@wrap(1)
def sum_lst_1(n):
    lst = [x for x in range(1, int(n) + 1)]
    res = list(map(lambda x: (1+1/x) ** x, lst))
    print(
        f'Заданная последовательность 〖(1+1/n)〗^ n от 1 до {num} имеет вид: \n {res}')
    print(f'Сумма элементов данной последовательности составляет: {sum(res)}')
    return n


sum_lst(num)
sum_lst_1(num)
