'''
Напишите программу, которая считывает список чисел lst из первой строки и число
x из второй строки, которая выводит все позиции, на которых встречается число
x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку
"Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
'''

lst = [int(i) for i in input().split()]
x = int(input())
if len(lst) == 1 and lst[0] == x:
    print(0)
if x not in lst:
    print('Отсутствует')
else:
    for i in range(len(lst) - 1):
        if x == lst[i]:
            print(i, end=' ')
        else:
            continue
