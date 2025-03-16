# Home Work 28, 14.03.25
""" ___ 54-55: Functional Programming ___ """

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


part_0 = '_____ Problem book _____'
""" _______________________________  Задачник по functools + itertools  _______________________________ """
# C:\Users\odnab\OneDrive\Mine\_Python_Dev_KI_ICH\- Python -\Theory\Python_TfS54-Func-programm-itertools.pdf

""" ___ PB - Task #1 ______________________________________________________________ """
# Создание списка бесконечных натуральных чисел: Используйте itertools.count для создания итератора бесконечных
# натуральных чисел, начиная с 1. Выведите первые 5 чисел.

# See link https://pythonworld.ru/moduli/modul-itertools.html

# +++++++++++++++++
# import itertools
# +++++++++++++++++



""" ___ PB - Task #2 ______________________________________________________________ """
# Создайте список, содержащий символ "A" повторенный 10 раз, используя itertools.repeat.


""" ___ PB - Task #3 ______________________________________________________________ """
# Бесконечное чередование "да" и "нет": Используйте itertools.cycle для создания итератора,
# бесконечно чередующего строки "да" и "нет". Выведите первые 5 элементов.


""" ___ PB - Task #4 ______________________________________________________________ """
# Произведение двух списков: Найдите декартово произведение списков [1, 2] и ['a', 'b']
# с помощью itertools.product. Выведите результат.


""" ___ PB - Task #5 ______________________________________________________________ """
# Перестановки чисел в списке: Создайте список всех перестановок чисел [1, 2, 3]
# с помощью itertools.permutations. Выведите список перестановок.


""" ___ PB - Task #6 ______________________________________________________________ """
# Комбинации чисел без повторений: Генерируйте все комбинации длиной 2 из списка [1, 2, 3, 4]
# без повторений с помощью itertools.combinations. Выведите список комбинаций.


""" ___ PB - Task #7 ______________________________________________________________ """
# Комбинации чисел с повторениями: Генерируйте все комбинации длиной 2 из списка [1, 2, 3]
# с повторениями с помощью itertools.combinations_with_replacement. Выведите список комбинаций.


""" ___ PB - Task #8 ______________________________________________________________ """
# Фильтрация элементов по условию: Используя itertools.filterfalse, создайте
# список всех чисел от 1 до 10, кроме тех, что делятся на 3. Выведите результат.


""" ___ PB - Task #9 ______________________________________________________________ """
# Группировка соседних элементов: Используйте itertools.groupby для группировки соседних элементов
# в списке [1, 2, 2, 3, 3, 3, 4] по их значению.
# Выведите результат в формате списка кортежей (число, количество повторений).


""" ___ PB - Task #10 ______________________________________________________________ """
# Сжатие списка по условию: Создайте список из первых 5 чисел натурального ряда,
# используя itertools.compress, где только числа, которые делятся на 2, будут включены. Выведите результат.




part_1 = '______ Task 1 _____'
""" ______  Task 1  ______________________________________________________________________________________________ """
# Напишите программу, которая принимает список слов от пользователя, (1) использует генераторное выражение (comprehension)
# для создания нового списка, содержащего только те слова, которые начинаются с гласной буквы.
# (2) Затем программа должна использовать функцию map, чтобы преобразовать каждое слово в верхний регистр.
# В результате программа должна вывести новый список, содержащий только слова, начинающиеся с гласной буквы и
# записанные в верхнем регистре.

# 5 vowel and 19 consonant letters and Y and W  -->  See HW9_16_12_string.py, Task 2.
# My favorite Quote from Eger in \Home_Tasks\HW_15-22_ListMethods_to_Excepts\HW20_06_02_Dictionary.py
# quote_phsy = ('-1- Anything we practice, we become better at. Edith Eger, The Choice: Embrace the Possible.'
#           '-2- Whatever you practice, you become better at. Edith Eger, The Gift: 14 Lessons to Save Your Life.')

phrase = 'Anything we practice, we become better at. Edith Eger, The Choice: Embrace the Possible.'
vowel = 'aeiou'            # 5 vowel letters
# if/else in a list comprehension --> See https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension

_1_Variant = '______ 1-st Variant --> SIMPLE  _____'
# Понятно, что эти циклы можно оформить в функции, но я не стала этого сейчас делать, чтобы пока тренировать своё
# логическое мышление на работу с циклами.
# 1 - Obtaining Phrase without any signs:
only_words = []
for word in phrase:
    if word.isalpha() or word.isspace():        # Выделяю по отдельности только буквы и пробелы.
        only_words.append(word)
# print(only_words)
phrase_without_signs = ''.join(only_words)      # Собираю отфильтрованные буквы и пробелы в СЛОВА.
# print(phrase_without_signs)

# 2 - Obtaining Words, that begins from vowels:
words_with_vowel = []
for word in phrase_without_signs.split():
    if word[0].lower() in vowel:
        words_with_vowel.append(word.upper())
# print(words_with_vowel, f'\n {'='*45}')

_2_Variant = '______ 2-nd Variant -->  ЦЕПОЧКИ из элементов ФП: map(), filter(), reduce() _____'
# # phrase_without_signs_2_0 = filter(lambda word: word.isalpha() or word.isspace(), phrase)
# # print(list(phrase_without_signs_2_0))
#
# # ++++++++++++++++++++++++++++++
# from functools import reduce
# # ++++++++++++++++++++++++++++++
#
# phrase_without_signs_2_1 = reduce(lambda letter, space: letter.upper() + space,
#                                   filter(lambda word: word.isalpha() or word.isspace(), phrase)
#                                   )
# # print(f'reduce --> {phrase_without_signs_2_1}', f'\n {'.'*100}')
#
# phrase_without_signs_2_2 = list(map(lambda word: word,
#                                (reduce(lambda letter, space: letter.upper() + space,
#                                     filter(lambda word: word.isalpha() or word.isspace(), phrase))).split(' ')
#                                ))
# # print(f'map --> {phrase_without_signs_2_2}')
#
# # phrase_without_signs_2_3 = [word if word[0].lower() in vowel else None for word in
# #                             map(lambda word: word,
# #                                (reduce(lambda letter, space: letter.upper() + space,
# #                                     filter(lambda word: word.isalpha() or word.isspace(), phrase))).split(' ')
# #                                 )]
# # print(f'list comprehension --> {phrase_without_signs_2_3}')
#
# # --------- CLEAN CODE for LMS ----------------------
# phrase_without_signs_2_4 = list(filter(lambda word: word[0].lower() in vowel,
#                                   map(lambda word: word,
#                                       (reduce(lambda letter, space: letter.upper() + space,
#                                               filter(lambda word: word.isalpha() or word.isspace(), phrase))
#                                        ).split(' ')
#                                       )
#                                   ))
# # print(f'filter words with vowels at the beginning --> {phrase_without_signs_2_4}')

_3_Variant = '______ 3-d Variant --> by Tech.Specification: LIST COMPREHENSION  +  map() _____'
# (1) использует генераторное выражение (comprehension) для создания нового списка, содержащего только те слова,
# которые начинаются с гласной буквы.
# (2) Затем программа должна использовать функцию map, чтобы преобразовать каждое слово в верхний регистр.

# ______ (1) - comprehension: слова, которые начинаются с гласной буквы
# # first_vowel_words_0 = list(filter(lambda word: word[0].lower() in vowel, phrase.split()))
# # print(first_vowel_words_0, f'\n {'-'*45}')
#
# # СУПЕР! Как же эти встроенные методы сокращают работу! ))
# # В итоге я пришла к простому и понятному решению, но с использованием встроенных методов.
# # Смотри по .rstrip('.,') link here https://www.geeksforgeeks.org/python-string-rstrip/
# # first_vowel_words_1 = [word.upper().rstrip('.,') for word in filter(lambda word: word[0].lower() in vowel, phrase.split())]
# first_vowel_words_1 = [word.rstrip('.,') for word in filter(lambda word: word[0].lower() in vowel, phrase.split())]
# # print(first_vowel_words_1, f'\n {'-'*45}')
#
# # Оформлю-ка я фильтрацию слов с гласными в начале в функцию:
# def filter_words(some_string):
#     return [word.rstrip('.,') for word in filter(lambda word: word[0].lower() in vowel, some_string.split())]
#
# filtered_phrase = filter_words(phrase)
# # print(filtered_phrase, f'\n {'-'*45}')

# ______ (2) - map(), чтобы преобразовать каждое слово в верхний регистр
# # Я, правда, не понимаю, зачем это делать отдельной map(), если можно сразу в comprehension реализовать. Ну ладно, ТЗ.
# uppercase_words = list(map(lambda word: word.upper(), first_vowel_words_1))
# # print(uppercase_words, f'\n {'-'*45}')
#
# # Функция преобразования слов в uppercase:
# def convert_to_uppercase(list_strings):
#     return list(map(lambda word: word.upper(), list_strings))
#
# # print(convert_to_uppercase(filtered_phrase), f'\n {'-'*45}')

_4_Variant = '______ 4-th Variant --> Generators with yield and .send() _____'
# В общем, после предыдущих вариантов я даже не буду за это браться, поскольку есть путь проще.
# Правда, я всегда держу в памяти тот факт, что при обработке больших данных использование генераторов просто необходимо,
# во избежание переполнения памяти.
# ------------ Все же СТОИТ ПОПРОБОВАТЬ решить задачу с использованием генератора ----------------------




part_2 = '______ Task 2 _____'
""" ______  Task 2  ______________________________________________________________________________________________ """
# Напишите программу, которая принимает список чисел от пользователя и (1) использует функцию reduce из модуля functools,
# чтобы найти произведение всех чисел в списке. (2) Затем программа должна использовать функцию itertools.accumulate
# для накопления произведений чисел в новом списке. В результате программа должна вывести список,
# содержащий накопленные произведения.

# # +++++++++++++++++++++++++++++++
# import random
# from functools import reduce
# # +++++++++++++++++++++++++++++++
#
# # ____________ (1) Part _________________________
# n_start, n_end, number_of = -13, 21, 10
# list_random_numb = [random.randint(n_start, n_end) for _ in range(number_of)]
# print(f'List of random numbers:  {list_random_numb}')
#
# mult_numbs = reduce(lambda x, y: x * y, list_random_numb)
# print(f'Mult of random numbers with reduce:  {mult_numbs}')
#
# # ____________ (2) Part _________________________
#
# # +++++++++++++++++++++++++++++++
# import itertools
# import operator
# # +++++++++++++++++++++++++++++++
#
# res = list(itertools.accumulate(list_random_numb, operator.mul))
# print(f'Accumulate of random numbers wirth .accumulate:  {res}')


