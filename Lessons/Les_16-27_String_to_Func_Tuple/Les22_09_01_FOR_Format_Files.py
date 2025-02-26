# Semenov Artem
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115) -or- print('__ NB! ' * 15, end='__')     # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# f = 40; f = '.' * f; print(f) - Filler up to.
# print(f, f'\n...')
# print(' ' * 5, f'...') - Indentation in the output of the result
# print('__ NB! ', '%.' * 50, end=' __')

# 09.01.25
# Python 22: Loop FOR. Основы работы с файлами

# ______ Review of previously covered material ______

# __ Task 1 __
# Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов.
# __ 1-st Var __
# phr = input("Enter a phrase : ").split()
# print(f'Number of words in phrase {len(phr)}.')
# __ 2-nd Var __
# phr = input("Enter a phrase : ")
# print(f'Number of words in phrase {phr.count(' ') + 1}.')

# __ Task 2 __
# Напишите программу, которая считает вхождение заданной подстроки в заданную строку.
# Например, для подстроки “ab” и строки “Abrakadabra” программа напечатает 2.
# phr = input("Enter a phrase : ").lower()
# path = input("Enter a path : ").lower()
# text = phr.count(path)
# print(f'Number of "path" in phrase {text}.')

# __ Task 3 __
# Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку. При решении этой задачи не стоит пользоваться циклами
# и инструкцией if.
# phr = input("Enter a phrase with 2 words: ").split()
# print(phr[1] + " " + phr[0])

# ________________________ Loop FOR ________________________
# for <variable> in <iterable object>:
#       operator_1
#       operator_2
#       operator_3
#       ...
#       operator_n
# __ Sets or Lists __
# list1 = [1, 2, 3, 4, 5]         # Iterable object - i.e. Collection - set of numbers.
# for item in list1:
#     print(item)

# __ Text __
#  * FOR *
# text = 'Python'                   # Iterable object too - i.e. Collection - just text.
# for char in text:
#     print(char)

# * WHILE *
# text = 'Python'
# i = 0
# while i < len(text):
#     print(text[i])
#     i += 1

# for char in 'Python':
#     print(char.upper())

# for i in range(10):         # range - makes a Collection from Number.
#     print(i)

# list1 = [1, 2, 3, 4, 5]
# for item in list1:
#     print(item)

# list1 = [1, 2, 3, 4, 5]       # ALL the numbers.
# for item in list1:
#     a = item ** 2
#     print(a)

# list1 = [1, 2, 3, 4, 5]          # Only the last one.
# for item in list1:
#     a = item ** 2
# print(a)

# list1 = [1, 2, 3, 4, 5]
# for i in list1:
#     list1[i] = 0
#     print(list1)

# list1 = [1, 2, 3, 4, 5]       # Without ERROR
# list2 = [0, 1, 2, 3, 4]
# for i in list2:
#     list1[i] = 0
#     print(list1)

# list1 = [1, 2, 3, 4, 5]         # With ERROR
# list2 = [0, 1, 5, 3, 4]         # The set with numbers of indexes.
# for i in list2:
#     print(i)
#     list1[i] = 0
#     print(list1)

# list1 = [6, 7, 8, 9, 10]         # With ERROR
# list2 = [0, 1, 2, 3, 5]          # The set with numbers of indexes.
# for i in list2:
#     print(i)
#     list1[i] = 0
#     print(list1)

# list1 = 'Python'
# for i in list1:
#     list1[i] = 0
#     print(list1)

# __ RANGE __
# range(start, stop, step)
# for i in range(5):
#     print(i)

# for i in range(2, 501):       # With limit
#     print(i)

# for i in range(2, 501, 50):     # With STEP
#     print(i)

# text = 'Hello World!'
# for char in text:
#     print(char, end=' ')

# text = 'Hello World!'
# for char in range(len(text)):       # Т.к. len возвращает число, то range от 11.
#     print(char, end=' ')

# text = 'Hello World!'
# for char in range(len(text)):       # Т.к. len возвращает число, то range от 11.
#     print(text[char], end=' ')

# text = 'Hello World!'
# for char in range(len(text)):       # Т.к. len возвращает число, то range от 11.
#     print(text[char], end=' ')
#     print(char)

# text = 'Hello World!'
# for char in range(len(text)):       # Т.к. len возвращает число, то range от 11.
#     print(text[char], end=' ')
#     print(char * 2)

# __ Function ENUMERATE __
# Возвращает пару: индекс и значение.
# text = 'Hello World!'
# for index, data in enumerate(text):
#     print(index, data)                 # NB! Возвращает индекс и значение.

# text = 'Hello World!'
# for index, data in enumerate(text):
#     print(index, data, end=' ')

# text = 'Hello World!'
# for index in range(len(text)):
#    print(text[index].upper() * 5, end=' ')

# ###################################################################################################################

# ___ Other from Lecture and Lesson from Thema STRINGS and FOR-loops on ICH ___

# __ Task 1 __
# Ниже представлен пример работы «чистильщика строк», найдите и исправьте ошибку:
# letters = 'AbltOJFHgtlbgndfWLFNT'
# for letter in letters:
#     if letter.upper() = letters:
#         letters.replace(letter, '')
# print(letters)

# letters = 'AbltOJFHgtlbgndfWLFNT'
# print(letters[0])
# if letters[0].upper() in letters:
#     # print('Yes')
#     print(letters.replace(letters[0], '_'))

# __ from Copilot __
# letters = 'AbltOJFHgtlbgndfWLFNT'
# new_letters = ''
# for letter in letters:
#     if not letter.isupper():
#         new_letters += letter
# print(new_letters)
# letter не является числом, это отдельный символ строки letters. Когда ты проходишься по строке с помощью
# цикла for letter in letters, каждая итерация цикла присваивает переменной letter один символ из строки letters.
# Функция .isupper() работает с символами строк, и поскольку letter является символом строки в каждой итерации цикла,
# ты можешь использовать .isupper() для проверки, является ли этот символ заглавным.
# print('__ NB! ', '%.' * 50, end=' __')

#  __ NB!  %.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%. __
#
#       Запомни, в циклах for в Python мы перебираем элементы в последовательности (строки, списки и т.д.), а не их индексы.
#       Конечно, если тебе нужно работать именно с индексами, ты можешь использовать функцию enumerate().
#
#  __ NB!  %.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%.%. __

# letters = 'AbltOJFHgtlbgndfWLFNT'
# for index, letter in enumerate(letters):
#     print(f'Index: {index}, Letter: {letter}')

# ___ My Variant - Shorter than Copilot's Variant___
# letters = 'AbltOJFHgtlbgndfWLFNT'
# for letter in letters:
#     if letter.isupper():
#         letters = letters.replace(letter, '_')
# print(letters)



