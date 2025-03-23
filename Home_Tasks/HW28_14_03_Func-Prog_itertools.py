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

# See links:
#   - https://pythonworld.ru/moduli/modul-itertools.html
#   - https://proglib.io/p/iteriruemsya-pravilno-20-priemov-ispolzovaniya-v-python-modulya-itertools-2020-01-03

# +++++++++++++++++
import itertools
# +++++++++++++++++

# ______ 1-st Variant - List COMPREHENSION ______
n = 5
counter = itertools.count(start=0, step=1)
result_1 = [next(counter) for _ in range(n)]
# print(f'1-st Var with List Comprehension: {' ':<1}{result_1}')
# ______ 2-nd Variant - Loop FOR ______
list_cnt = []
for i in range(n):
    list_cnt.append(next(counter))
# print(f'2-nd Var with Loop FOR: {' ':<11}{list_cnt}')
# ______ 3-d Variant - map() ______
result_2 = list(map(lambda x: counter.__next__(), range(n)))
# print(f'3-d Var with map(): {' ':<15}{result_2}')
# ______ 4-th Variant -  ______

""" ___ PB - Task #2 ______________________________________________________________ """
# Создайте список, содержащий символ "A" повторенный 10 раз, используя itertools.repeat.
rep = 10
list_repeat = list(itertools.repeat('A', rep))
# print(list_repeat)

""" ___ PB - Task #3 ______________________________________________________________ """
# Бесконечное чередование "да" и "нет": Используйте itertools.cycle для создания итератора,
# бесконечно чередующего строки "да" и "нет". Выведите первые 5 элементов.
# See p.4, https://proglib.io/p/iteriruemsya-pravilno-20-priemov-ispolzovaniya-v-python-modulya-itertools-2020-01-03
times = 5
yes_no = itertools.cycle(['Yes', 'No'])
# for _ in range(times):
    # print(next(yes_no) )

""" ___ PB - Task #4 ______________________________________________________________ """
# Произведение двух списков: Найдите декартово произведение списков [1, 2] и ['a', 'b']
# с помощью itertools.product. Выведите результат.
l1 = [1, 2]
l2 = ['a', 'b']
multiply_lists = list(itertools.product(l1, l2))
# print(multiply_lists)

""" ___ PB - Task #5 ______________________________________________________________ """
# Перестановки чисел в списке: Создайте список всех перестановок чисел [1, 2, 3]
# с помощью itertools.permutations. Выведите список перестановок.
l3 = [1, 2, 3]
permutations_list = list(itertools.permutations(l3))
# print(f'permutations: {permutations_list}')

""" ___ PB - Task #6 ______________________________________________________________ """
# Комбинации чисел без повторений: Генерируйте все комбинации длиной 2 из списка [1, 2, 3, 4]
# без повторений с помощью itertools.combinations. Выведите список комбинаций.
l4 = [1, 2, 3]
combinations_list = list(itertools.combinations(l4, 2))
# print(f'combinations: {combinations_list}')

""" ___ PB - Task #7 ______________________________________________________________ """
# Комбинации чисел с повторениями: Генерируйте все комбинации длиной 2 из списка [1, 2, 3]
# с повторениями с помощью itertools.combinations_with_replacement. Выведите список комбинаций.
# 10. Комбинаторика - размещение: combinations_with_replacement(iterable, r) - комбинации длиной r из iterable с
# повторяющимися элементами.
l5 = [1, 2, 3]
comb_list_with_repeat = list(itertools.combinations_with_replacement(l5, 2))
# print(f'combinations_with_replacement: {comb_list_with_repeat}')

""" ___ PB - Task #8 ______________________________________________________________ """
# Фильтрация элементов по условию: Используя itertools.filterfalse, создайте
# список всех чисел от 1 до 10, кроме тех, что делятся на 3. Выведите результат.
# Метод .filterfalse() дополняет обычный фильтр filter():
#   itertools.filterfalse(func, iterable) - все элементы, для которых func возвращает ложь.
list6 = list(range(-3, 8))
# print(f'list6:          {list6}')
def filter_func(n):
    if n % 3 == 0:
        return True
    return False

# print(f'filter():       {list(filter(filter_func, list6))}')
# print(f'.filterfalse(): {list(itertools.filterfalse(filter_func, list6))}')


""" ___ PB - Task #9 ______________________________________________________________ """
# Группировка соседних элементов: Используйте itertools.groupby для группировки соседних элементов
# в списке [1, 2, 2, 3, 3, 3, 4] по их значению.
# Выведите результат в формате списка кортежей (число, количество повторений).
# .groupby() объединяет смежные словари в группы по общему ключу. __ NB! __ Предварительно отсортируйте данные.
# .groupby(iterable, key=None) - группирует элементы
# по значению. Значение получается применением функции key к элементу (если аргумент key не указан, то
# значением является сам элемент).
l7 = [1, 2, 2, 3, 3, 3, 4]
# Как работает groupby:
#   1) Что делает groupby:
#       - Он группирует соседние элементы с одинаковыми значениями.
#       - Для каждой группы возвращает:
#           * key — значение, которое объединяет элементы группы.
#           * group — итератор, содержащий элементы этой группы.
#   2) Что возвращает group:
#       group — это итератор, и чтобы увидеть, какие элементы в группе, его нужно либо итерировать
#       (например, с помощью цикла for), либо преобразовать в список с list().
# ИТАК |=>  Для каждого уникального ключа (key) возвращается итератор (group), который содержит соседние элементы
# с этим значением. С помощью генератора списка создаём кортежи, где: key — значение элемента,
# len(list(group)) — длина группы, то есть количество повторений элемента.
groupby_list = [(key, len(list(group))) for key, group in itertools.groupby(l7)]
print(groupby_list)



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

# %%%%%%%%%%%%%%%%%%%%%%_____________ See https://habr.com/ru/articles/866616/ _____________%%%%%%%%%%%%%%%%%%%%%%

# Генератор - это особый вид итератора - объекта, который отдает значения по одному за раз.
# __ NB! __ Любая функция содержащая yield является генераторной функцией.
# При вызове генераторная функция возвращает генератор-итератор или просто генератор.
# __ NB! __ Генераторная функция и генератор - это разные объекты, хотя и связанные друг с другом.
''' Признак генератора - ключевое слово YIELD, что с английского означает "УСТУПАТЬ". '''

# ===  Получение значений из генератора: ===
# Так же как и итератор, генератор не хранит все значения, а вычисляет их "на лету".
# Генератор можно обойти только один раз. Когда мы запрашиваем значение из генератора, выполняется тело генератора
# до ключевого слова yield. Встретив yield генератор возвращает значение, стоящее справа от yield в вызвавший его код
# и запоминает свою позицию. Если значение справа от yield отсутствует, то генератор возвращает None.
# __ NB! __ Когда мы в следующий раз запросим значение из генератора, то \\\ выполнение продолжится с сохраненной позиции ///
# до следующего yield и так же вернется значение справа от yield.
# __ NB! __ Получить значение из генератора можно в цикле или используя функции next и send.

# Смотри еще здесь https://sky.pro/media/filtracziya-slovarya-v-python-dlya-polucheniya-tolko-opredelennyh-klyuchej/

# Переделанный пример из статьи 866616 на Хабре, ссылка на которую выше:
def gen_function(words):
    # ___ СЮДА определенно НУЖНО ДОБАВИТЬ ЧТО-ТО ___
    list_words = words.split()
    yield list_words
    # while i < len(list_words):
    #     yield list_words[i-1]
    #     i += 1

gen = gen_function(phrase)
# print(next(gen))

# for w in gen:
#     print(w)


# Декомпозиция задачи с генераторами:
# 1) беру слово из фразы и отправляю его для ожидания в yield.
# 2) в каждом слове во фразе проверяю 1-ую букву на принадлежность списку с гласными.
# 2) если слово начинается с гласной, отправляю его для ожидания в yield.



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


