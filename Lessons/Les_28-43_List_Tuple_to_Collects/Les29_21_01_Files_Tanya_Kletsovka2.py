# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 22.01.25
# Python 29: ADDITIONAL  CLASS (2-nd Lesson with Tatiana Kletsovka) - Работа с файлами.

# ###################################################################################################################
print('.' * 120)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% _________  Работа с файлами  __________ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# _____ open() _____ - Instruction -
# Открывает файл, возвращает объект файл.
# Метод (list(объект).split()) содержит информацию об объекте. Метод может быть изменен по дополнительным встроенным в метод критериям.
# print(type("example_Shakespeare.txt"))                        # String.
# print(type(open("Text_files/example_Shakespeare.txt")))       # _io.
# print(type(open("Text_files/test_text.txt")))                 # _io.

# file1 = open("Text_files/example_Shakespeare.txt")
# print(file1.encoding)

# file = open("Text_files/example_Shakespeare.txt", encoding="utf-8")
# print(file.name)
# print(file.mode)              # Read / Write / Add
# print(file.encoding)
# print(file.read())
# print(file.read())
# print(file.readline())          # Строка
# print(file.readline())          # Будет читаться каждая следующая строка.
# print(file.readlines())          # Список. Выведутся так же табуляторы \t и переносы строк \n.
# print(file.readlines())          # Выведется пустая коллекция.
# file.close()

#  __ Режимы __
# file = open("Text_files/names.txt", "x")      # x - следит,есть ли такой файл. Если есть, выведет ошибку.
# file.write("sd")

# file = open("Text_files/names_2.txt", "x")      # x- в новый файл допишет без проблем.
# file.write("sd")

# file = open("Text_files/names_2.txt", "w")      # w - ПЕРЕзапись.
# file.write("Anothe text...")

# file = open("Text_files/names_2.txt", "a")      # a (append) - ДОзапись. Всегда в конец файла.
# file.write("\nSome new text...")

# from time import sleep                              # ????????????
# file = open("Text_files/names_2.txt", "r")
# sleep(2)
# file.write("   ***   ")

# file = open("Text_files/names_2.txt", "a+")       # a+ - добавлять в конец + Читать.
# file.seek(0)
# print(file.read())
# file.write("\n123")

# file = open("Text_files/names_2.txt", "a+")
# file.seek(0)
# print(file.readline())
# file.write("\n123")

# file = open("Text_files/names_2.txt", "a+")
# file.write("\n123 *** some text...")

# file = open("Text_files/names_2.txt", "w")
# file.writelines(["1 - text\n", "2 - text\n", "3 - text\n"])

#    NB!   __ FILE is ITERABLE object __
# file = open("Text_files/names.txt", "r")
# __ 1-st Var __
# for line in file:                 # Лучше использовать этот метод, а не file.readlines().
#     print(line, end="")
# __ 2-nd Var __
# for line in file.readlines():       # НО... ??????? Смотри мой вопрос на 12:30 --> 13:45 (~ 1:15).
#     print(line, end="")

# file.close()

# _____ WITH ... AS _____ - Контекстный менеджер -
# WITH работает с объектом, которому он может присвоить ключевое слово AS.
# # file = open("Text_files/names.txt", "r")        # |
# # for line in file:                               # | можно записать через WITH ... AS.
# #     print(line, end="")                         # |
# # file.close()                                    # |

# with open("Text_files/names.txt", "r") as file:
#     for line in file:
#         print(line, end="")

# with open("Text_files/names.txt", "r") as file1:
#     for line in file1:
#         print(line, end="")

# for i in range(5):
#     pass
# print(i)
# print(file1)


# __ Task 1 __
# Напишите программу, которая запрашивает у пользователя имя файла (переменная file) и целое
# число (переменная lines), а затем выводит на печать построчно последние строки в количестве
# lines (на всякий случай проверим, что задано положительное целое число). Протестируем функцию
# на файле article.txt со следующим содержимым:
#    ***
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
# path = "Text_files/article.txt"   # input("Enter the name of file: ")           # article.txt
# lines_number = int(input("Enter the number of lines: "))
# with open(path, 'r', encoding='utf-8') as file:
#     # print(file.readlines())
#     # print((file.readlines())[1:2])
#     print(file.readlines()[-lines_number:])

with open(file ='../Text_files/names.txt', mode ='r', encoding='utf-8') as file:
    content = file.read()
    for i, row in enumerate(content.split('\n')):
        print('\n----------', end='')
        for j in row.split('\t'):
            print(f'\n{j}', end='')


