'''
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно
смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое
слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести
лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.
'''

with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    text = input_file.read()

d = dict()
for i in range(len(text)):
    if text[i] not in d:
        d[text[i]] = text.count(text[i])
key_list = list(d.keys())
val_list = list(d.values())

position = val_list.index(max(d.values()))
print(key_list[position], max(d.values()))

output_file.write("{} {}".format(key_list[position], max(d.values())))