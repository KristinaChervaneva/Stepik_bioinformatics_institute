'''
Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:

Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.
'''

def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x and x <= 2:
        return - x / 2
    elif 2 < x:
        return (x - 2) ** 2 + 1
