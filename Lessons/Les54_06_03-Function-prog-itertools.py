# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 06.03.25
 Python 54: Функциональное программирование на Python. Модуль itertools.
 ################################################################################################################### """
import math

# Video Lesson 54: ---------------.
# Video Practice __: wasn't.
# links:
#   - "C:\Users\odnab\OneDrive\Mine\_Python_Dev_KI_ICH\- Python -\Theory\Python_LfS28.docx-Func-programm-itertools.pdf".
#   - .

# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------

print('.' * 120)

""" ___________________________________  Review of previously covered material  ___________________________________ """


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%______   Встроенные функции map и filter   _____%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

""" ______ map ______ """
# — это встроенная функция, которая возвращает итератор с преобразованными значениями. Чтобы сохранить результат,
# нужно преобразовать в коллекцию. Иначе, если принтануть результат map, то снова обратиться к элементам внутри нее
# уже НЕ получится!

""" ______ filter ______ """
# — это встроенная функция, которая возвращает итератор, содержащий только элементы, для которых функция-
# предикат возвращает True.

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# squared = map(lambda x: x ** 2, numbers)
# print(squared)                                  # Выведет объект итератора.
# print(list(squared))                            # [1, 4, 9, 16, 25]
# even = filter(lambda x: x % 2 == 0, numbers)
# print(list(even))                               # Выведет объект итератора.
# print(even)                                     # [2, 4]

""" ______ Взаимозаменяемость map-filter и циклов с условиями ______ """    # See Video, ?????????
# numbers = [1, 2, 3, 4, 5]
# # Comprehension:
# squared = [x ** 2 for x in numbers]
# print(squared)                 # [1, 4, 9, 16, 25]
# # Map-Filter:
# squared = list(map(lambda x: x ** 2, numbers))
# print(squared)      # [1, 4, 9, 16, 25]
# # Loop with condition:
# squared = []
# for x in numbers:
#     squared.append(x ** 2)
# print(squared)                          # [1, 4, 9, 16, 25]

# # ___________________________________________________________ CODE from Taniya
# from time import time
#
# numbers = [n for n in range(1_000_000)]
#
# # print(filter(lambda x: x % 2 == 0, numbers), map(lambda x: x ** 2, numbers))
#
# start = time()
# # result = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
# result = filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers))
# end = time() - start
# print(result, end)
#
# start = time()
# result = (x for x in result if x % 2 == 0)
# result = (x ** 2 for x in numbers)
# end = time() - start
# print(result, end)
#
# start = time()
# result = [x for x in result if x % 2 == 0]
# result = [x ** 2 for x in numbers]
# end = time() - start
# print(end)
#
#
# # 6.198883056640625e-06
# # 0.000006198883056640625
# # 0.09259486198425293
# # ___________________________________________________________ ______________

""" ______ Достоинства и недостатки каждого подхода ______ """
#   - Списковые включения - Считаются более краткими и читабельными, особенно для простых операций на списках.
#   - Map-filter - Более гибкая и обобщенная функциональность, особенно если требуется применять
#     пользовательские функции.
#   - Больше гибкости и контроля, особенно при сложных манипуляциях с данными.


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%______   Построение цепочек из элементов   _____%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """
"""                                         функционального программирования                                       """

""" ______ Построение цепочек ______ """
# — это возможность строить цепочки из различных элементов функционального программирования, таких как map, filter,
# reduce и другие функции, что позволяет последовательно применять функции к данным и преобразовывать их.

# __ 1-st Variant: __
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers)))
# print(result)     # Результат: 20

# __ 2-nd Variant: __
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# first = map(lambda x: x ** 2, numbers)
# first_list_ml = list(map(lambda x: x ** 2, numbers))
# # first_list_l = list(first)
# print(first, first_list_ml, "first_list_l")
# second = filter(lambda x: x % 2 == 0, first)
# print(second)
# third = reduce(lambda x, y: x + y, second)
# print(third)


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%______________   Модуль itertools   _____________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """
# Slide 27
""" ______ reduce из модуля functools ______ """
# — это функция, которая применяет указанную функцию к элементам последовательности, сводя их к одному значению.

""" ______ accumulate ______ """
# — это функция, которая выполняет свертку данных, накапливая промежуточные результаты, что позволяет
# поэтапно применять указанную функцию к элементам последовательности и сохранять каждый промежуточный результат.

""" ______ Функции для работы с последовательностями ______ """
#   - Модуль itertools - Предлагает функцию accumulate.
#   - Модуль operator - Предоставляет функции для использования в reduce и accumulate.

""" ______ Модуль itertools.accumulate ______ """

# ++++++++++++++++++++++++++++++++
import itertools
import operator
from functools import reduce
# ++++++++++++++++++++++++++++++++

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
numbers = [1, 2, 3, 4, 5]

result_0 = math.prod(numbers)
# print(f'math.prod --> {result_0}')

result_1 = reduce(operator.mul, numbers)
# print(f'reduce() --> {result_1}')
result_1_let = reduce(lambda x, y: x + y, letters)
# print(f'reduce(letters) --> {result_1_let}')

result_2 = itertools.accumulate(numbers, operator.mul, initial=1)
# print(f'itertools.accumulate(..., \033[31minit=1\033[m) --> {list(result_2)}')
result_3 = itertools.accumulate(numbers, operator.mul)
# print(f'Only Info about iterator --> {result_3}')
# print(f'Result of LIST(itertools.accumulate()) --> {list(result_3)}')

""" ______ Функции для работы с последовательностями ______ """

""" ___ Модуль itertools ___ """
# Предлагает функции для генерации комбинаторных объектов, таких как:
#   - комбинации (combinations),
#   - перестановки (permutations),
#   - декартово произведение (product).

""" ___ Генерация комбинаторных объектов ___ """
# ________________________________________________ CODE from Taniya

# ++++++++++++++++++++++
# import itertools
# ++++++++++++++++++++++

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
# ___ Комбинации ___
combinations = list(itertools.combinations(letters, 2))     # Комбинации из 2-х элементов (пар).
# print(f'Combinations of 2 elements:  {combinations}')
combinations = list(itertools.combinations(letters, 3))     # Комбинации из 3-х элементов (тройки).
# print(f'Combinations of 3 elements:  {combinations}', "\n")
# ___ Перестановки ___
permutations = list(itertools.permutations(numbers))
# print(f'Permutations:  {permutations} \nNumber of permutations = {len(permutations)}.')
permutations_2 = list(itertools.permutations(numbers, 2))
# print(f'Permutations of 2 elements:  {permutations_2} \nNumber of permutations of 2 = {len(permutations_2)}.', "\n")
# ___ Декартово произведение ___
product = list(itertools.product(letters, numbers))
# print(f'"Product" makes all possible combinations:  {product}')
# ________________________________________________ _________________


""" ___ zip_longest ___ """
# — это метод, который позволяет создавать итератор сопоставляющий элементы нескольких последовательностей,
# даже если они имеют разную длину, что полезно, когда требуется обработать данные, учитывая разные длины
# или пропуски в последовательностях.

# ++++++++++++++++++
import itertools
# ++++++++++++++++++

letters = ['a', 'b', 'c']
numbers = [1, 2]
zipped_fillvalue = itertools.zip_longest(letters, numbers, fillvalue='-')       # Заполнитель недостающего элемента.
print(f'With fillvalue:  {list(zipped_fillvalue)}')
zipped_0 = itertools.zip_longest(letters, numbers, [0])                         # Что добавить - список, состоящий из ноля.
print(f'{list(zipped_0)}')

""" ___ Метод itertools.zip_longest ___ """


# ++++++++++++++++++++++++++++
# from functools import reduce
# ++++++++++++++++++++++++++++


""" ______  Task 1  ______________________________________________________________________________________________ """
#



