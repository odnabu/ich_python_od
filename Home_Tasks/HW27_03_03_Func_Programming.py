# Home Work 27, 06.03.25
""" ___ 52-54: Functional Programming ___ """
# Video Lesson 52: ______________________
# Video Practice 53: _______________________
# Video Practice 54: _______________________
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


part_0 = '______ Problem book _____'
""" _______________________________  Задачник по Функциональному программированию  _______________________________ """
# Python_TfS52-Functional-Programming.pdf

""" ___ PB - Task #1 ______________________________________________________________ """
# Преобразование списка в квадраты: Напишите функцию, преобразующую список чисел в список их квадратов.

# __ 1-st Variant: Сгенерирую последовательный список чисел в некотором диапазоне:
# See https://sky.pro/media/sozdanie-spiska-chisel-v-opredelennom-diapazone-v-python/.
# # numbers_list = list(range(-3, 21, 2))
# # print(f'numbers_list:{' ':>6} {numbers_list}')
# # ___ or:
# numbers_list_2_var = [i for i in range(-3, 21, 2)]
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

# # ___ List Comprehension:
# def squared_numbers_1(list_numbs):
#     return [n ** 2 for n in list_numbs]
#
# print(f'List-1 of squared numbers: {squared_numbers_1(numbers_list)}')
#
# # ___ Map:
# def squared_numbers_2(list_numbs):
#     return list(map(lambda n: n ** 2, list_numbs))
#
# print(f'List-2 of squared numbers: {squared_numbers_2(numbers_list)}')

""" ___ PB - Task #2 ______________________________________________________________ """
# Фильтрация нечетных чисел: Создайте функцию, которая возвращает список, содержащий только нечетные
# числа из исходного списка.

# def filter_odd_numb(numb_collect):
#     return filter(lambda n: n % 2 != 0, numb_collect)
#
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

with open('C:/Users/odnab/PycharmProjects/PythonProject/Lessons/example_Shakespeare.txt', 'r', encoding="utf-8") as file:
    words_from_poem = file.readlines()

# Все строки из файла с нумерацией:
# for i, element in enumerate(words_from_poem):
#     # string.rstrip()  или  string = string.replace("\n","")  - удалить переносы строк:
#     # print(i, element.replace("\n",""))
#     print(i, element.rstrip())

# Строки из Сонета 5:
line1 = 23; line2 = 25
some_lines = words_from_poem[line1:line2]
# print(some_lines)
list_of_words = []
for line in some_lines:
    for word in line.split():
        list_of_words.append(word)
# print(list_of_words)

# print(make_sentance(list_of_words))


""" ___ PB - Task #7 ______________________________________________________________ """
# Фильтрация строк по длине: Напишите функцию, фильтрующую список строк и возвращающую только те строки,
# длина которых больше 3 символов.





""" ___ PB - Task #8 ______________________________________________________________ """
# Умножение всех чисел в списке: Создайте функцию, которая возвращает результат умножения всех чисел в списке.


""" ___ PB - Task #9 ______________________________________________________________ """
# Преобразование имён: Используя map, напишите функцию, добавляющую префикс "Mr. " к каждому имени в списке.


""" ___ PB - Task #10 ______________________________________________________________ """
# Сортировка чисел по убыванию: Напишите функцию, сортирующую список чисел по убыванию.






part_1 = '______ Task 1 _____'
""" ______  Task 1  ______________________________________________________________________________________________ """
# Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов только четных чисел из списка,
# используя функциональные подходы (например, map, filter и reduce).
# Пример вывода:
# Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
# Результат: 72



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

