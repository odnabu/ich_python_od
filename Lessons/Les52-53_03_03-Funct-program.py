# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 03.03.25
 Python 52-53: Введение в функциональное программирование на Python.
 ################################################################################################################### """

# Video Lesson 51: ---------------.
# Video Practice __: wasn't.
# links:
#   - https://habr.com/ru/articles/257903/ .
#   - https://ru.wikibooks.org/wiki/Python/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BD%D0%B0_Python .

# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# print(f'\tName: {p.name:<10}')
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Ctrl + click on Name of Function - переведет туда, где вызывается функция.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------

print('.' * 120)

""" ___________________________________  Review of previously covered material  ___________________________________ """


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%____________   Functional Programming   ___________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

""" __________ Парадигма программирования __________ """
#  — это подход или методология, которая определяет способ структурирования, организации и написания программного кода.
# Некоторые из популярных парадигм программирования включают:
#   ● Императивное программирование.
#   ● Декларативное программирование.
#   ● Объектно-ориентированное программирование.
#   ● Функциональное программирование.
#   ● Логическое программирование.

""" __________ Виды программирования __________ """
#   ● Императивное программирование - Описывает шаги и инструкции для выполнения конкретной задачи.
#   ● Декларативное программирование - Фокусируется на описании желаемого результата, а не на определении шагов
#     для его достижения.
#   ● ООП - Ставит объекты в центр разработки и использует понятия классов, наследования и инкапсуляции.
""" ● Функциональное программирование """# - Ориентировано на использование функций в качестве основной строительной
#     единицы программы и ставит акцент на неизменяемость данных.
#   ● Логическое программирование - Основано на формальной логике и использует правила и факты для вывода результатов.

""" __________ Функциональное программирование __________ """
# — это программирование, которое подразумевает использование функций в качестве основной
# строительной единицы программы.

""" ______ Принципы функционального программирования ______ """
#   ● Неизменяемость данных.
#   ● Отсутствие побочных эффектов.
#   ● Использование функций высшего порядка.

""" ___ Функциональное программирование - ПРЕИМУЩЕСТВА: ___ """
#   ● Часто используется для решения задач, где необходимо обработать данные, преобразовать их и
#     получить результат, не изменяя исходные данные.
#   ● Полезен при работе с параллельными и распределенными системами, а также при написании
#     чистого и модульного кода.

""" ___ Функции для работы с последовательностями ___ """
#   - len() - Возвращает длину последовательности.
#   - sum() - Возвращает сумму элементов последовательности.
#   - min() и max() - Возвращают наименьший и наибольший элементы соответственно.
# numbers = [1, 2, 3, 4, 5]
# length = len(numbers); print(length)        # 5
# total = sum(numbers); print(total)          # 15
# minimum = min(numbers); print(minimum)      # 1
# maximum = max(numbers); print(maximum)      # 5

""" ___ all() ___ """
# — это функция, которая возвращает True, если все элементы итерируемого объекта являются TRUE, и False в
# противном случае. - проверяет, являются ли объекты внутри НЕ False-ыми.
""" ___ any() ___ """
# — это функция, которая возвращает True, если хотя бы один элемент итерируемого объекта является истинным, и False в
# противном случае.
""" ___ Функции вида iterable → one_element ___ """
# numbers = [1, 2, 3, 4, 5, 0, 'a']
# Так как все числа > 0, формируется генератор:
# all_true = all(num > 0 for num in numbers)      # True
# print('all_true = all... |--> ', all_true)
# all_bool = (num > 0 for num in numbers)         # False - для 0.
# print('all_bool = (...)  |--> ', list(all_bool))
# any_true = any(num < 0 for num in numbers)      # False
# print('all_any = any...  |--> ', any_true)

# item_list = []              # ??????????????? __ NB! __ Video 52, 56:00
# print (all(item_list))      # - проверяет, являются ли объекты внутри НЕ Falst-ыми. |=> вернет True.

""" ______ Отличия sorted() и reversed() в функциональном программировании ______ """

"""  NB!  """ # Эти функции НЕ меняют объект!
# sorted() - Принимает итерируемый объект и возвращает новый список, содержащий отсортированные
#            элементы исходного объекта.
# reversed() - Принимает итерируемый объект и возвращает новый ОБЪЕКТ обратного итератора, который позволяет
#            перебирать элементы в обратном порядке.
""" ___ FSCIT: ___ """
#   ● sorted - Не изменяет исходный объект --> вернет НОВЫЙ список - list.
#   ● reversed - Не изменяет исходный объект и не создает новый список --> вернет итератор - iterator.

"""  NB!  """ # реализация функции all(): CODE - Video 52, 1:05:00

# __ Example:
# numbers = [3, 1, 4, 2, 5]
# print(numbers)
# sorted_numbers = sorted(numbers)          # [1, 2, 3, 4, 5]
# print(sorted_numbers)
# reversed_numbers = reversed(numbers)      # <list_reverseiterator object at 0x7f4b930b3d00>
# print(reversed_numbers)

# -------------------------------------------------------
# See Video 54, 8:00
# l = [1, 2, 6, 3, 4, 5]
# r = reversed(l)
"""  NB!  """ # Вернет ОБЪЕКТ ИТЕРАТОРА, который можно еще преобразовать в коллекцию:
# print(f'r{' ':<8}|-->  {r}')
# print(f'list(r){' ':<2}|--> ', list(r))          # А вот тут уже вернет список!
#
# s = sorted(l, reverse=True)
# print(f's{' ':<8}|-->  {s}')
# # ..........
#
# words = ['two', 'three', 'one']
# w_sorted = sorted(words, key=len)
# print(list(w_sorted))
# -------------------------------------------------------

# Что будет выведено в результате выполнения фрагмента кода:
# numb = (22, 10, 5, 34, 29)
# print(list(reversed(numb)))

""" ______ Встроенные методы enumerate() и zip() ______ """

""" ___ enumerate() ___ """
# — функция, которая принимает итерируемый объект и возвращает итератор, который генерирует кортежи,
# состоящие из индекса элемента и самого элемента. Полезно, когда необходимо получить доступ к индексам элементов во
# время итерации.
# fruits = ['apple', 'banana', 'orange']
# for index, fruit in enumerate(fruits, start=1):
#     print(index, fruit)
# # Output:
# # 0 apple
# # 1 banana
# # 2 orange

""" ___ zip() ___ """
# — это функция, которая принимает несколько итерируемых объектов и возвращает итератор, который генерирует
# кортежи, содержащие элементы из каждого итерируемого объекта на соответствующих позициях. Это позволяет
# объединять элементы из разных последовательностей.
# numbers = [111, 222, 333, 444]          # Пройдется ТОЛЬКО ао МЕНЬШЕМУ списку!
# letters = ['a', 'b', 'c']
# zipped1 = zip(numbers, letters)
# for num, letter in zipped1:
#     print(num, letter)
# # Output:
# # 1 a
# # 2 b
# # 3 c
# words = ['one', 'two', 'three']
# zipped2 = zip(numbers, letters, words)
# for num, letter, words in zipped2:
#     print(num, letter, words)

# Что будет выведено в результате выполнения фрагмента кода:
# colour = ["Black", "Purple", "Brown", "Yellow", "Blue"]
# print(list(enumerate(colour)))          # Будет список с кортежами.

""" ______ Введение в map-filter-reduce ______ """      # Video 52, 1:20:00
# - это функции высшего порядка, которые широко используются в функциональном программировании.

""" ___ map() ___ """
# — это функция, которая применяет функцию к каждому элементу итерируемого объекта и возвращает итератор с
# преобразованными значениями. Это функция ГЕНЕРАТОРНОГО типа: значения ПОТРАЧЕНЫ (данные не хранятся в памяти) и 
# больше к ним обратиться НЕЛЬЗЯ. Так же и в саму функцию можно передать итератор.
# numbers = [1, 2, 3, 4, 5]
# squared = map(lambda x: x ** 2, numbers)        # [1, 4, 9, 16, 25]
# print(squared)
# print(list(squared))

""" ___ filter() ___ """
# — это функция, которая применяет функцию-предикат к каждому элементу итерируемого объекта и возвращает
# итератор, содержащий только элементы, для которых предикат возвращает True.
# numbers = [1, 2, 3, 4, 5]
# even = filter(lambda x: x % 2 == 0, numbers)      # [2, 4]
"""  NB!  """  #  Video 52, 1:29:00 -- ОТЛИЧНОЕ объяснение lambda-функции.
# print(even)
# print(list(even))

""" ___ reduce() ___ """      # __ NB! __ ???????????????? Video 52, 1:32:00
# — это функция, которая применяет функцию двух аргументов к элементам итерируемого объекта, последовательно сводя их
# к одному значению.
# # ++++++++++++++++++++++++++++
# from functools import reduce
# # ++++++++++++++++++++++++++++
# numbers = [1, 2, 3, 4, 5]
# # product = reduce(lambda x, y: x * y, numbers)             # 120
# # print(product)
# product = reduce(lambda x, y: x * y, numbers, 1000)         # 120000
# print(product)



""" ______  Task 1  ______________________________________________________________________________________________ """
# 1) Подсчитать общую длину слов с помощью любой функции высшего порядка.
# 2) Подсчитать общую длину слов с помощью reduce.
colour = ["Black", "Purple", "Brown", "Yellow", "Blue"]

# ___ 1-st Part ___
# colours_len = map(lambda word: len(word), colour)
# # print(colours_len)
# # print(list(colours_len))        # т.к. map - ленивый итератор, его результаты держатся в памяти только ДО первого
                                    # использования, и память потом очищается. Значит, делать что-либо с данными уже нельзя.
# # print(sum(colours_len))    # Будет 0, т.к. map() выдает объект.
# print(sum(colours_len))      # ????????????? Video 53, 0:06 --> Будет 26, т.к. закомментированы 3 верхние строки.

# ___ 2-nd Part ___
# # ++++++++++++++++++++++++++++
from functools import reduce
# # ++++++++++++++++++++++++++++
# __ 1-st Variant: __
# colours_len1 = reduce(lambda x, y: x + y, map(lambda word: len(word), colour), 0)
# print(colours_len1)
# __ 2-nd Variant: __
# colours_len2 = len(reduce(lambda x, y: x + y, colour))
# print(colours_len2)
# __ 3-d Variant: __
# colours_len3 = reduce(lambda x, y: x + len(y), colour, 0)
# print(colours_len3)

""" ______  Task 2  ______________________________________________________________________________________________ """
# 1. **Считать данные из текстового файла**, в котором каждая строка содержит информацию в следующем формате:
#    имя,дата,сумма,категория,город
# 2. **Сгруппировать данные по годам и месяцам**, создавая для каждого года и месяца отдельную папку в указанной директории.
# 3. **Создать файлы для каждой категории товаров**, в которых должны быть указаны все продажи по данной категории в формате:
#    дата,имя продавца,сумма
#    - Все записи в файле **должны быть отсортированы по дате**.
# 4. **Создать общий отчёт по каждому месяцу** (`monthly_report.txt`), в котором указана суммарная выручка по
#    каждой категории и общая сумма:
#    Automotive,109539
# 5. **Программа должна принимать аргументы командной строки**:
#    sh
#    python sales_report.py <input_file> <output_directory>
#
#    Где:
#    - `<input_file>` — путь к входному файлу с продажами.
#    - `<output_directory>` — папка, куда будут сохранены отчёты.

# # +++++++++++++++++++++++
# import argparse
# import os
# # +++++++++++++++++++++++

# ___ 1-st Part:
# pars = argparse.ArgumentParser()
# pars.add_argument("--input_file", "-if", type=str, help="path to file with data", required=True)
# pars.add_argument("--output_directory", "-od", type=str, help="path to directory with reports", required=True)
# args = pars.parse_args()

# ГДЕ в коде выше (строка 262) -- Запуск скрипта с обязательными флагами из консоли:
# python "путь к script" -if "путь к базовому файлу" -od "путь к файлу с анализом"
# script = r''
# -if = r''
# -od = r''


# print(args.input_file)
# print(args.output_directory)
""" __ NB! __   В консоли ввожу команду    |-->    """
# #        python Lessons/Les52-53_03_03-Function-programming.py --output_directory Lessons/report --input_file Lessons/sales_data.txt
# #     --> Или с флагами:
# #        python Lessons/Les52-53_03_03-Function-programming.py -od Lessons/report -if Lessons/sales_data.txt

# print(f'\033[34mVerification of file exists:\033[m {os.path.isfile(args.input_file)}')
# os.makedirs(args.output_directory, exist_ok=True)       # ??????????????? Video 53, 1:14:00
#
# with open(args.input_file, 'r') as file:
#     data = file.readlines()
#
# print(data)

# ___ 2-nd Part:
""" __ NB! __ """   # See Golubenko ALL SOLUTION  |-->

# ---------------------------------------------- Посмотреть в ВИДЕО 52 ???????????????????
# filepaths = "../../example_Shakespeare.txt"
# os.system(f"Python {filepaths}")
# print(f'\033[34m\033[m Finished')
# --------------------------------------------------------------------------------------

# ___ Декомпозиция задачи --> Псевдокод ___
# 1 - Список словарей.
# 2 - Словарь{критерий (ключ): список подходящих словарей (значение)}.
# 3 - Создать папки (год, месяц) и файлы
# 4 - Рассчитать сумму по группе и записать в файл.


""" ---- Продолжение решения задачи -- ALL SOLUTION   \\\\\   NB!  ////   see Golubenko  ------------------------- """

# +++++++++++++++++++++++
import argparse
import os
from datetime import datetime
from collections import defaultdict
# +++++++++++++++++++++++

# 1. ___ **Считать данные из текстового файла** ___ |--> Список словарей
parser = argparse.ArgumentParser()
parser.add_argument("--input_file", "-f", type=str, help="path to file", required=True)
parser.add_argument("--output_directory", "-od", type=str, help="path to output directory with report", required=True)

args = parser.parse_args()

if not os.path.exists(args.output_directory):
    os.makedirs(args.output_directory)

def create_dict_from_file(input_file):
    records = []
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                seller, date, amount, product, city = line.strip().split(',')
                record = {
                    'seller': seller,
                    'date': date,
                    'amount': amount,
                    'product': product,
                    'city': city,
                }
                records.append(record)
    except FileNotFoundError as e:
        print(e)

    return records

# ___ 2. **Сгруппировать данные по годам и месяцам** ___  |--> Словарь{критерий (ключ): список подходящих словарей (значение)}.
def group_by_year_month(records):
    grouped = defaultdict(list)
    for record in records:
        date_obj = datetime.strptime(record['date'], '%Y-%m-%d')
        year_month = date_obj.strftime('%Y-%m')                             # Year, month
        # if year_month not in grouped:
        #    grouped[year_month] = []
        grouped[year_month].append(record)

    return grouped

# 3. ___ **Создать файлы для каждой категории товаров** ___  |--> - Создать папки (год, месяц) и файлы
def save_grouped_data(grouped, output_directory):
    for year_month, records in grouped.items():
        year, month = year_month.split('-')
        # Create map:
        dir_path = os.path.join(output_directory, year, month)
        os.makedirs(dir_path, exist_ok=True)
        # Write in file:
        file_path = os.path.join(dir_path, f"{year}_{month}_sales.txt")
        with open(file_path, 'w', encoding='utf-8') as file:
            for record in records:
                file.write(
                    f"{record['seller']},{record['date']},{record['amount']},{record['product']},{record['city']}\n")


# 4. **Создать общий отчёт по каждому месяцу**
records = create_dict_from_file(args.input_file)
# print(records)        # Создаем словарь из файла
grouped = group_by_year_month(records)
for i in grouped.items():
    print(i)
    # Группируем по годам и месяцам
save_grouped_data(grouped, args.output_directory)  # Сохраняем сгруппированные файлы.

# -------------------------------------------------------------------------------------------------------------







