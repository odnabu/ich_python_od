# Home Work 27, 06.03.25
""" ___ 52-55: Functional Programming ___ """
# Video Lesson 52: ______________________
# Video Practice 53: _______________________
# Video Practice 54: _______________________
# Video SUMMARY 55: _______________________
# Normal  \033[0;__;__m \033[m    or   BOLD  \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ############################################################################################################### """
# f = 40; f = '.' * f; print(f) - Filler up to.
# print(f, f'\n...')
# print(' ' * 5, f'...') - Indentation in the output of the result
# while True:                      # __ NB! __ See HW14_16_01_Func_Tuple.py, Task 2, "___ Clear code..."
#   ...
#   ask = input("\nDo you want to continue? (y/n): ").lower()
#   if ask == 'n':
#   # if user_n == 'Stop'.lower():
#       break
# def input_numb_list():            #  __ NB! __ See HW16_23_01_List_Matrix.py
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# print(f'\tName: {p.name:<10}')
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------
print('.' * 130)


part_0 = '_____ Problem book _____'
""" _______________________________  Задачник по Функциональному программированию  _______________________________ """
# Python_TfS52-Functional-Programming.pdf

""" ___ PB - Task #1 ______________________________________________________________ """
# Преобразование списка в квадраты: Напишите функцию, преобразующую список чисел в список их квадратов.

# __ 1-st Variant: Сгенерирую последовательный список чисел в некотором диапазоне:
# See https://sky.pro/media/sozdanie-spiska-chisel-v-opredelennom-diapazone-v-python/.
numbers_list_1 = list(range(-3, 21, 2))
# print(f'numbers_list_1 :{' ':>6} {numbers_list_1}')
# ___ or:
numbers_list_2_var = [i for i in range(-3, 21, 2)]
# print(f'numbers_list_2_var: {numbers_list_2_var}')

# __ 2-nd Variant: Сгенерирую список СЛУЧАЙНЫХ чисел в некотором диапазоне:
# # __ or RANDOM numbers, see https://ru.stackoverflow.com/questions/565846/%D0%9A%D0%B0%D0%BA-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA-%D0%B8%D0%B7-%D1%81%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D1%8B%D1%85-%D1%86%D0%B5%D0%BB%D1%8B%D1%85-%D1%87%D0%B8%D1%81%D0%B5%D0%BB-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D1%8F-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%BE%D0%B2%D0%BE%D0%B5-%D0%B2%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5
# # +++++++++++++++++++++++++++++++++++++++++++
import random #, itertools, functools, numpy
# # +++++++++++++++++++++++++++++++++++++++++++
n_start, n_end, number_of = -13, 21, 10
v2 = [random.randint(n_start, n_end) for _ in range(number_of)]#; print(f'v2 = {v2}')
numbers_list_r = tuple(v2)#; print(f'numbers_list_r = {numbers_list_r}')
# v1 = list(numpy.random.randint(n_start, n_end, number_of)); print(f'v1 = {v1}')
# v3 = list(map(lambda _: random.randint(n_start, n_end), range(number_of))); print(f'v3 = {v3}')
# v4 = list(itertools.starmap(lambda: random.randint(n_start, n_end), [()] * number_of)); print(f'v4 = {v4}')
# v5 = list(r(n_start, n_end) for r in [random.randint] * number_of); print(f'v5 = {v5}')
# v6 = [r() for r in [functools.partial(random.randint, n_start, n_end)] * number_of]; print(f'v6 = {v6}')

# ___ List Comprehension:
def squared_numbers_1(list_numbs):
    return [n ** 2 for n in list_numbs]

# print(f'List-1 of squared numbers: {squared_numbers_1(numbers_list_1)}')

# ___ Map:
def squared_numbers_2(list_numbs):
    return list(map(lambda n: n ** 2, list_numbs))

# print(f'List-2 of squared numbers: {squared_numbers_2(numbers_list_1)}')

""" ___ PB - Task #2 ______________________________________________________________ """
# Фильтрация нечетных чисел: Создайте функцию, которая возвращает список, содержащий только нечетные
# числа из исходного списка.

def filter_odd_numb(numb_collect):
    return filter(lambda n: n % 2 != 0, numb_collect)

# print('Odd numbers: ', tuple(filter_odd_numb(numbers_list_r)))

""" ___ PB - Task #3 ______________________________________________________________ """
# Перевод всех строк в верхний регистр: Используя map, напишите функцию, которая преобразует все строки
# в списке к верхнему регистру.

# Сгенерирую список СЛУЧАЙНЫХ строк:
# See:
#   + https://sky.pro/media/generacziya-sluchajnyh-strok-s-ispolzovaniem-bukv-verhnego-registra-i-czifr-v-python/
#   + знаки препинания - https://dzen.ru/a/ZD9-FwVoDBX7MXpe
# +++++++++++++++++
import random
import string
# +++++++++++++++++

def generate_string_list(length, number_of_elements):
    string_list = []
    all_symbols = string.ascii_letters
    for _ in range(number_of_elements):
        rand_str = ''.join(random.choice(all_symbols) for _ in range(length))
        string_list.append(rand_str)
    return string_list

str_list = generate_string_list(6, 3)
# print(len(str_list), str_list, sep='\n')

def convert_uppercase(list_of_strings):
    # return [s.upper() for s in list_of_strings]               # 1-st method -- List Comprehension
    return list(map(lambda s: s.upper(), list_of_strings))      # 2-nd Method -- list(map())

# print(convert_uppercase(str_list))

""" ___ PB - Task #4 ______________________________________________________________ """
# Нахождение суммы чисел в списке: Напишите функцию, суммирующую все числа в списке.

# +++++++++++++++++++++++++++++++++++
from functools import reduce
# +++++++++++++++++++++++++++++++++++

def sum_all_numbs(numbs_list):
    return reduce(lambda x1, x2: x1 + x2, numbs_list)

# print(sum_all_numbs(numbers_list_r))
# print(sum_all_numbs(str_list))

""" ___ PB - Task #5 ______________________________________________________________ """
# Поиск минимального числа: Напишите функцию для нахождения минимального числа в списке.

def find_min_number(list_of_numbers):
    return min(list_of_numbers)

# print(find_min_number(numbers_list_r))

""" ___ PB - Task #6 ______________________________________________________________ """
# Объединение слов в предложение: Создайте функцию, которая объединяет список слов в предложение.

# +++++++++++++++++
import os
# +++++++++++++++++
""" __ NB! __ """   # Про адреса к файлам смотри статью на Хабре: https://habr.com/ru/companies/selectel/articles/547290/
# В общем, в абсолютном адресе с Винды нужно ЗАМЕНИТЬ бэкслэш \ на обычный слеш - /.
# print("Текущая директория: ", os.getcwd())
# print(os.path.exists('C:/Users/odnab/PycharmProjects/PythonProject/Lessons/example_Shakespeare.txt'))
""" __ NB! __ """   # Еще хорошая статья про работу с файлами:
# https://pythonru.com/osnovy/rabota-s-fajlami-v-python-s-pomoshhju-modulja-os
# + Особенно хорошо про os.walk() — генератор дерева каталогов.
# + Работа с файлами на Метаните - https://metanit.com/python/tutorial/4.1.php

with open('products.txt', 'r') as file:
    products_list = file.readlines()
# print(products_list)

def take_words(list_of_products):
    only_words = []
    for line in list_of_products:
        words = line.split(', ')
        only_words.append(words[0])
    return only_words

words_list = take_words(products_list)
# print(words_list)

def make_sentance(list_of_words):
    return str(reduce(lambda x1, x2: x1 + ' ' + x2, list_of_words))

# print(f'\033[36mSentance:\033[m ', make_sentance(words_list))

# with open('C:/Users/odnab/PycharmProjects/PythonProject/Lessons/example_Shakespeare.txt', 'r', encoding="utf-8") as file:
#     words_from_poem = file.readlines()

# Все строки из файла с нумерацией:
# for i, element in enumerate(words_from_poem):
    # # string.rstrip()  или  string = string.replace("\n","")  - удалить переносы строк:
    # # print(i, element.replace("\n",""))
    # print(i, element.rstrip())

# # Строки из Сонета 5:
# line1 = 23; line2 = 25
# some_lines = words_from_poem[line1:line2]
# # print(some_lines)
# list_of_words = []
# for line in some_lines:
#     for word in line.split():
#         list_of_words.append(word)
# print(list_of_words)

# print(make_sentance(list_of_words))


""" ___ PB - Task #7 ______________________________________________________________ """
# Фильтрация строк по длине: Напишите функцию, фильтрующую список строк и возвращающую только те строки,
# длина которых больше 3 символов.
# ORIGINAL EXAMPLE See in  Lessons/Les50_27_02_File-System.py

# # +++++++++++++++
# import os
# # +++++++++++++++
#
# # Ищу и считываю файл  |-->   Имя файла, который нужно найти:
# file_name = "example_Shakespeare.txt"
# # file_name = "products.txt"
# # Проверяем, существует файл или каталог:
# # print(f'\033[33mФайл существует:\033[m {os.path.exists(file_name)}')
#
#
# # Функция поиска файла в директории на уровень выше (".."), т.е. в папке с проектом PythonProject и поддиректориях:
# def find_file(file_name, search_directory):
#     for root, dirs, files in os.walk(search_directory):
#         if file_name in files:
#             # Возвращаю абсолютный путь к файлу:
#             return os.path.join(root, file_name)
#     return None
#
# # Поиск файла в директории и поддиректориях:
# # directory_path = r'C:\Users\odnab\PycharmProjects\PythonProject'
# directory_path = '..'
# file_path = find_file(file_name, directory_path)
#
# # ___   -2- Открытие файла:   ___
# if file_path:
#     print(f"\033[33mФайл найден, адрес:\033[m  {file_path}")
#     # Открываю файл для чтения:
#     try:
#         with open(file_path, 'r', encoding="utf-8") as file:
#             content = file.readlines()          # Выведет СПИСОК строк.            # print(content)
#             row_length = 5
#             print(f"Строки, длина которых больше \033[33m{row_length}\033[m: ")
#             # ___ 1-st Variant ____________________________________________________
#             # for line in content:
#             #     if len(line) > row_length:
#             #         print(line.rstrip())
#             # ___ 2-nd Variant ____________________________________________________
#             only_rows = filter(lambda row: len(row) > row_length, content)
#             for line in only_rows:
#                 print(line.rstrip())             # Если так, то --> Выведет ПОСТРОЧНО, как в 1-st Variant.
#             # # print(list(only_rows))            # Если так, то --> Выведет СПИСОК строк.
#     except FileNotFoundError as e_fnf:
#         notice_fnf = f"\033[31m{e_fnf}\033[m"
#         print(f"{notice_fnf}: возможно ошибка в имени или адресе файла.")
#     except Exception as e:
#         print(f"Ошибка при открытии файла: {e}")
# else:
#     print(f"Файл \033[34m'{file_name}'\033[m \033[31mне найден\033[m.")



""" ___ PB - Task #8 ______________________________________________________________ """
# Умножение всех чисел в списке: Создайте функцию, которая возвращает результат умножения всех чисел в списке.

# __ With  reduce(lambda x: x..., <list>) __

# ++++++++++++++++++++++++++++
from functools import reduce
# ++++++++++++++++++++++++++++

def multiply_numbers(list_of_numbers):
    return reduce(lambda x, y: x * y, list_of_numbers)

numbers_list_3 = list(range(-5, 7, 2))
# print(numbers_list_3)
# print(multiply_numbers(numbers_list_3))


""" ___ PB - Task #9 ______________________________________________________________ """
# Преобразование имён: Используя map, напишите функцию, добавляющую префикс "Mr. " к каждому имени в списке.

# __ With  map(lambda x: x..., <list>) __
def add_prefix(list_od_names):
    return map(lambda name: 'Herr ' + name, list_od_names)

# See the list of greatest german physicists: https://www.google.com/search?q=greatest+german+physicists&sca_esv=3f2e39702a0b213c&sxsrf=AHTn8zp49oiFmqNfpehSibERK60u70inbQ%3A1741848220999&ei=nH7SZ9XVPOr1i-gPtLeWoAM&oq=germany+physicists&gs_lp=Egxnd3Mtd2l6LXNlcnAiEmdlcm1hbnkgcGh5c2ljaXN0cyoCCAUyBxAAGIAEGA0yBxAuGIAEGA0yBhAAGA0YHjIGEAAYDRgeMgYQABgNGB4yCBAAGAUYDRgeMggQABgFGA0YHjIIEAAYBRgNGB4yCBAAGAUYDRgeMggQABgFGA0YHkiY2AFQ3RRYpHdwAngAkAEAmAFgoAG6A6oBATW4AQHIAQD4AQGYAgagAsUDwgIKEAAYsAMY1gQYR8ICBxAjGLACGCfCAgQQABgemAMAiAYBkAYIkgcDMi40oAfGMg&sclient=gws-wiz-serp
# All physicists from Germany: https://en.wikipedia.org/wiki/List_of_German_physicists
""" __ NB! __ """   # All interesting information from the list of famous german physicists in DataDase-file in
# DataBase VSC-Worbench: C:\Users\odnab\OneDrive\Mine\_Python_Dev_KI_ICH\- Data Bases -\Less_and_HW\HomeWorks\HW05_db_05_01_Constrains.sql

last_names = ['Einstein', 'Gauss', 'Pauli', 'Heisenberg', 'Roentgen', 'Laue', 'Helmholtz', 'Born', 'Ohm', 'Hertz']
# print(list(add_prefix(last_names)))


# --------------------------------------------     SEARCH     -------------------------------------------------------
# Поиск слова в файле: See https://ru.stackoverflow.com/questions/274131/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA-%D1%81%D0%BB%D0%BE%D0%B2%D0%B0-%D0%B2-%D1%84%D0%B0%D0%B9%D0%BB%D0%B5
# + https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-15-metody-raboty-s-faylami-i-faylovoy-sistemoy-2023-02-06

# ++++++++++++++++++++++++
import os
import re
# ++++++++++++++++++++++++

def find_word_in_files(word, directory):
    # Список файлов, содержащих указанное слово
    found_files = []
    # Обходим все файлы и поддиректории
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):  # Проверяем, является ли файл Python-скриптом
                file_path = os.path.join(root, file)
                try:
                    # Открываем файл для чтения
                    with open(file_path, 'r', encoding="utf-8") as f:
                        content = f.read()
                        # Проверяем наличие слова в содержимом файла
                        if re.search(rf"\b{word}\b", content):
                            found_files.append(file_path)
                except Exception as e:
                    # Игнорируем ошибки (например, при открытии бинарных файлов)
                    print(f"Не удалось открыть файл: {file_path}. Ошибка: {e}")
    # Вывод результата
    if found_files:
        print(f"Слово \033[33m'{word}'\033[m \033[32mнайдено\033[m в следующих файлах:")
        for found_file in found_files:
            print(found_file)
    else:
        print(f"Слово \033[33m'{word}'\033[m \033[31mНЕ найдено\033[m ни в одном файле в папке {directory}.")

# Пример вызова функции
search_word = "execute"  # Слово для поиска
project_directory_H = r'..\Home_Tasks'  # Путь к директории проекта
find_word_in_files(search_word, project_directory_H)
project_directory_L = r'..\Lessons'  # Путь к директории проекта
find_word_in_files(search_word, project_directory_L)
# -------------------------------------------------------------------------------------------------------------------


""" ___ PB - Task #10 ______________________________________________________________ """
# Сортировка чисел по убыванию: Напишите функцию, сортирующую список чисел по убыванию.

# See here:  https://sky.pro/wiki/python/sortirovka-spiska-vremennykh-metok-v-python-po-ubyvaniyu/
# Для сортировки списка в обратном порядке используйте:
#       - метод .sort() с аргументом reverse=True для сортировки на месте,
#       - функцию sorted(), чтобы создать новый, отсортированный список.


# print(f'Original list:     {numbers_list_2_var}.')

# __ 1-st Variant __ Создаёт новый, отсортированный список. Исходный список остаётся без изменений:
# print(f'Sorted descending-list with FUNCTION --> New list:  {sorted(numbers_list_2_var, reverse=True)}')

# # __ 2-nd Variant __ Сортирует список на месте:
# numbers_list_2_var.sort(reverse=True)
# print(f'Sorted descending-list with METHOD:  {numbers_list_2_var}')

# __ 3-d Variant __ Кастомизация сортировки с помощью lambda-функции:
# Использование lambda-функции в качестве значения параметра key в функциях sorted() или sort().
# Это позволяет установить собственное правило сортировки:
my_list = [('apples', 2), ('bananas', 3), ('carrots', 1)]
# Сортируем по количеству, а не по алфавиту:
my_list.sort(key=lambda item: item[1], reverse=True)
# print(my_list)

# __ 4-th Variant __ Использование метода .reverse() для обращения порядка элементов:
#  __ NB! __ Для уже СОРИТРОВАННОГО списка.
# Если список уже отсортирован по возрастанию, но нужно изменить порядок его элементов на обратный:
numbers_list_2_var.reverse()
# print(f'Reversed list with method .reverse(): {numbers_list_2_var}')

# Если применить .reverse() к НЕсортированному списку, то он просто обратит его:
list_random_numb = list(numbers_list_r)
# print(f'Random number\'s list: {list_random_numb}')
list_random_numb.reverse()
# print(f'Reversed random number\'s list: {list_random_numb}')

# __ 5-th Variant __ срезы для инвертирования списка:
descending_list = numbers_list_2_var[::-1]
# print(f'Reversed list with slices (срезы): {descending_list}')  # Тут получился возврат к оригиналу, т.к.
                                                                # список УЖЕ отсортирован в __ 4-th Var __.

part_1 = '______ Task 1 _____'
""" ______  Task 1  ______________________________________________________________________________________________ """
# Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов только четных чисел из списка,
# используя функциональные подходы (например, map, filter и reduce).
# Пример вывода:
# Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
# Результат: 72

# ___ Декомпозиция задачи ___
#   1) фильтрация четных чисел из списка - filter()
#   2) сумма их квадратов - reduce()

# # ++++++++++++++++++++++++++++
# from functools import reduce
# # ++++++++++++++++++++++++++++
#
# list_numbs = [4, 6, 3, 4, 2, 3, 9, 0, 7]
#
# def sum_squared_numbers(numb_list):
#     even = filter(lambda x: x % 2 == 0, numb_list)
#     squared_numbs = map(lambda x: x ** 2, even)
#     return reduce(lambda x1, x2: x1 + x2, squared_numbs)

# print(sum_squared_numbers(list_numbs))


part_2 = '______ Task 2 _____'
""" ______  Task 2  ______________________________________________________________________________________________ """
# Напишите функцию, которая принимает на вход список функций и значение, а затем применяет композицию этих функций
# к значению, возвращая конечный результат.
# Пример использования:
# add_one = lambda x: x + 1
# double = lambda x: x * 2
# subtract_three = lambda x: x - 3
# functions = [add_one, double, subtract_three]
# compose_functions(functions, 5) должно вывести 9

# def compose_functions(functions_list, value):
#     for function in functions_list:
#         value = function(value)
#     return value
#
#
# add_one = lambda x: x + 1
# double = lambda x: x * 2
# subtract_three = lambda x: x - 3
# functions = [add_one, double, subtract_three]

# print(compose_functions(functions, 3))
