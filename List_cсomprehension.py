# 12.   Для натурального n создать список, состоящий из элементов последовательности 3n + 1.
# Пример: Для n = 6: [4, 7, 10, 13, 16, 19]


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
def consist(n):
    lst = []
    for i in range(1, int(n) + 1):
        elem = 3 * i + 1
        lst.append(elem)
    print(lst)
    return n


@wrap(1)
def consist_1(n):
    lst = [3 * i + 1 for i in range(1, int(n) + 1)]
    print(lst)
    return lst


consist(num)
consist_1(num)
