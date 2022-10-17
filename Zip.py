# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример - часть задания № 33 на применение функции zip_longest из модуля itertools
# zip_longest - учитывает все значения из самой длинной последовательности,
# fillvalue= - заполняет недостающие элементы указанным значением


from random import randint
import itertools


k = randint(2, 5)
ratios = [randint(0, 10) for i in range(k + 1)]


def polinomial(n, rat):
    var = ['*x^']*(n-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(
        rat, var, range(n, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'

    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


print(polinomial(k, ratios))
