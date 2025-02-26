# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 17.02.25
# Python 44: Iterators & Generators.
# Video Lesson 44: https://player.vimeo.com/video/1057453688?h=eff2771473
# Video Practice 45: https://player.vimeo.com/video/1057479599?h=def68827de
# ###################################################################################################################
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# -----------------------------------------------------------

print('.' * 145)


# _________________________ Review of Home Works _____________________________________________________________________




# %%%%%%%%%%%%%%%%%%%%%%%%%%%_____________   Итераторы   ______________%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Методы с __<name>__ - магические методы.

# __________ Итератор __________

# - объект, который предоставляет последовательный доступ к элементам коллекции или последовательности.
#   Итераторы реализуют 2 основных метода:
#       - __iter__(),
#       - __next__().

# __________   .__iter__()  __________

#   — метод, который возвращает сам итератор (не саму коллекцию, а объект).
#   __ NB! __ Итератор создает НОВЫЙ ОБЪЕКТ!.

# it = my_list.__iter__()             # the SAME !!!        - the explanation see further
# it = iter(my_list)                  # the SAME !!!        - the explanation see further
# print(it.__next__())           # NOT the same !!!    - the explanation see further
# print(next(it))                # NOT the same !!!    - the explanation see further
# print(next(it))                # NOT the same !!!    - the explanation see further


# nums = [1, 2, 3, 4, 5]
# nums.__iter__()
# it = nums.__iter__()           # 18:00 ?????????????????????
# print(it)
# print(type(it))

# __________   .__next__()  __________

#   —  метод, который возвращает следующий элемент в последовательности.
# Запускается только после объявления .__iter__(), т.е. без него метод __next__() НЕ работает!
# Работает с ИНДЕКСАМИ.

# print(it.__next__())            # __ NB! __ Запоминает то место, где остановилось.
# print(it.__next__())
# print("------------")
# print(it.__next__())
# nums[3] = 0
# print(nums)
# print(it.__next__())

# __ NB! __ 27:00
# print(list(it))               # Взяли остаток от it и положили в новую ячейку памяти list()

# print(it.__next__())
# print(it.__next__())
# print(it.__next__())          # ERROR! - список закончился! нечего итерировать.

# new = []                      # Да, здесь список закончился, но извлечь можно.
# for i in it:
#     new.append(i)
# print(new)

# it = nums[::-1].__iter__()           # 35:00 - справа - налево.
# print(it.__next__())
# print(it.__next__())

# __________ Итератор с циклом __________

# it = nums.__iter__()
# for i in it:
#     # print(i)                        # Цикл for взял 1 элемент. __next__ - берет следующий, т.е. 2 и т.д.
#     print(it.__next__())            # ERROR! 1-ый был взят в for, 2 - напечатан, 3 - взят в for, 4 - напечатан...
# # print(it)

# __________ file __________
#   - объект итератора, потому что сам файл является типом IO.

# file = open("numbers.txt")
# print(file.__next__())
# print(file.__next__())
# print(file)
# print(type(file))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# __ NB! __ Объект типа итератор занимает меньше места, чем список.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# iiiiiiiiiiiiiiiiiiiiiiiiiii
# import sys
# iiiiiiiiiiiiiiiiiiiiiiiiiii
# __ Расчет объема памяти:
# numbers = iter(range(1, 1000001))
# print(sys.getsizeof(numbers))
# numbers = range(1, 1000001)
# print(sys.getsizeof(numbers))
# numbers = list(range(1, 1000001))
# print(sys.getsizeof(numbers))

# __________ Цикл for и итераторы __________

# See Python_23_M.pptx.pdf + Video 52:00

# my_list = [1, 2, 3]
# for item in my_list:
#     print(item)

# my_list = [1, 2, 3]
# it = my_list.__iter__()             # the SAME !!!
# print(it)
# it = iter(my_list)                  # the SAME !!!
# print(it)
#
# print(it.__next__())             # NOT the same !!!
# print(next(it))                # NOT the same !!!
# print(next(it))                # NOT the same !!!

# # print(next(it))                 # ERROR  !!!
# print(next(it, None))          # WITHOUT ERROR, but None.

# my_list = [1, 2, 3]
# iterator = iter(my_list)
# while True:
#     # print(next(iterator))                # ERROR !!! 1:02:00
#     try:
#         print(next(iterator))
#     except StopIteration:
#         print("End of iteration.")
#         break


# %%%%%%%%%%%%%%%%%%%%%%%%%%%_____________   Генераторы   ______________%%%%%%%%%%%%%%%%%%%%%%%%%%%

# - функции, которые возвращают последовательность значений, сохраняя при этом свое состояние между вызовами.
#   Генераторы имеют более сложную логику, чем у итератора.
# __ NB! __ Все генераторы - итераторы, НО не все итераторы - генераторы.
# __ NB! __ генераторы ОЧЕНЬ актуальны при работе с БОЛЬШИМИ данными!!!

# __ NB! __   В Python признаком генератора является наличие в функции ключевого слова yield.
#             Т.е., чтобы задать генератор, нужно добавить ключевое слово yield в функцию вместО/(вместЕ с) return.

# В функции генератора может использоваться как yield, так и return, но с небольшими различиями в их поведении:
#       - yield: Приостанавливает выполнение функции и возвращает значение, которое может быть восстановлено
#                при следующем вызове генератора.
#       - return: Останавливает выполнение функции и завершает генератор.
# Если в генераторе используется return с каким-либо значением, это значение будет проигнорировано.

# Генераторы позволяют создавать итерируемые последовательности, которые могут быть перебраны ОДИН раз,
# с возможностью приостанавливать выполнение функции и возобновлять её позже с того же места.


# __________ yield __________

# - ключевое слово, используется в генераторах для определения значений, которые будут возвращены при
#   каждом вызове метода  .__next__().
# Когда функция встречает yield, она возвращает значение и приостанавливает своё выполнение.
# При следующем вызове генератора выполнение возобновляется с того места, где оно было приостановлено.
#  Запоминает .... ???????????? 1:10:00

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
# gen = my_generator()
# print(gen)
# print(type(gen))
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))            # ERROR! - список закончился!

# ___ Пример ___ +++ return в генераторе
# def my_generator():
#     yield 1
#     yield 2
#     return f"\033[31mEnd\033[m"
#
# gen = my_generator()
# print(next(gen))                # выведет 1.
# print(next(gen))                # выведет 2.
# # print(next(gen))                # выведет ERROR -- StopIteration: End.
# try:
#     print(next(gen))            # StopIteration: End
# except StopIteration as e:
#     print(e.value)              # А так красную ERROR не выведет, т.к. для StopIteration прописано слово End.

# __ Другой пример с yield и return вместе __
# def mixed_generator():
#     yield 1
#     yield 2
#     return              # Завершает генератор
#     yield 3             # Эта строка не выполнится
#
# # Создание генератора
# gen = mixed_generator()
# # Перебор значений генератора
# for value in gen:
#     print(value)

# ___ Пример с циклом for в обработке данных ___ +++  return в генераторе
# def process_data(data):
#     for i in data:
#         if i == "STOP":
#             return "Processing stopped"       # Завершает генератор
#         yield i
#
# gen = process_data(["a", "b", "c", "STOP", "d"])
# for item in gen:
#     print(item)


# __________ Генераторные выражения __________

# - компактный способ создания генераторов, используя синтаксис списковых включений.
# Они позволяют создавать генераторы без явного определения функции с ключевым словом yield.
# Более полезен, чем список.
#       - Один раз пройтись - генераторные выражения.
#       - Много раз пройтись - списки.
# see here https://ru.hexlet.io/courses/python-declarative-programming/lessons/generator-expressions/theory_unit: -->
# Список — это последовательность элементов, поэтому его нужно обойти ровно один раз. А иногда даже не требуется
# доходить до конца списка — например, если мы ищем один конкретный элемент. Тут важно вспомнить, что map и filter
# не порождают списки сами по себе, а вместо этого порождают новые итераторы на основе итераторов-аргументов.
# Конвейеры данных на основе итераторов получаются довольно эффективными, особенно в сочетании с функциями из модуля itertools. Так происходит потому, что никакая работа не выполняется, пока ее результат не понадобится принимающей стороне на выходе конвейера.
# У генераторов списков есть еще одна важная особенность — весь список будет создан так или иначе, даже если от списка
# будут нужны не все элементы. Обычно выполнение цикла можно прервать с помощью break, но прервать вычисление
# генератора списков не получится.
# Иногда последовательности не нужно вычислять целиком. На самом деле получать и хранить законченные списки не нужно
# практически никогда.
# # В тех редких случаях, когда нужен именно список, пригодятся генераторы списков (см. ниже пример с []).
# Но большинство задач решается с помощью генераторных выражений --> ().
#
# Выглядят они как генераторы списков. Разница только в круглых скобках () вместо квадратных:

# my_generator = (x ** x for x in range(700))            # -- () --> ГЕНЕРАТОРНОЕ ВЫРАЖЕНИЕ -- Generator expression.
# my_list_generator = [x ** x for x in range(700)]          # -- [] --> генератор списков -- list comprehensions.
# print(my_generator)
# for item in my_generator:
#     print(item)

# import sys                                      # __ NB! __ - подключение пакета sys
# print(sys.getsizeof(my_generator))              # для 7 = 200 - объем памяти результата ГЕНЕРАТОРНОГО ВЫРАЖЕНИЯ.
# print(sys.getsizeof(my_list_generator))         # для 7 = 120 - объем памяти результата генератор списков.

# для 700 = 200  - объем памяти результата ГЕНЕРАТОРНОГО ВЫРАЖЕНИЯ.
# для 700 = 6136 - объем памяти результата генератор списков.
# |=> Генераторное выражение хранит логику, в отличие от генератора списков. Потому объем результатов генераторного
# выражения при разных числах - одинаков, а у генератора списков - растёт.

# See "Python: коллекции, часть 4/4: Все о выражениях-генераторах, генераторах списков, множеств и словарей",
# link: https://habr.com/ru/articles/320288/#4
# 4. Выражения-генераторы
# Выражения-генераторы (generator expressions) доступны, начиная с Python 2.4.
#   __ NB! __   Основное их отличие от генераторов коллекций в том, что они выдают элемент по-одному,
#   не загружая в память сразу всю коллекцию.
#   __ NB! __   если мы создаем большую структуру данных без использования генератора, то она загружается в
#   память целиком, соответственно, это увеличивает расход памяти Вашим приложением, а в крайних случаях памяти
#   может просто не хватить и Ваше приложение «упадет» с MemoryError. В случае использования выражения-генератора,
#   такого не происходит, так как элементы создаются по-одному, в момент обращения.
#   __ NB! __   там же по ссылке "Особенности выражений-генераторов".

# Пример выражения-генератора:
# list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
# my_gen = (i for i in list_a)            # выражение-генератор
# print(next(my_gen))                     # -2 - получаем очередной элемент генератора
# print(next(my_gen))                     # -1 - получаем очередной элемент генератора

# Генератор словаря (dictionary comprehension), по сути - переворачивание словаря:
import sys                                              # __ NB! __ - подключение пакета sys
# dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': 3}             # __ NB! __ it not depends on from the number of elements: , 'e': 4, 'f': 5, 'g': 6
# dict_gen_abc = {k: v for k, v in dict_abc.items()}
# dict_123 = {v: k for k, v in dict_abc.items()}        # Reversed dictionary.
# print(dict_123)  # {1: 'a', 2: 'b', 3: 'd'}
#                  # Обратите внимание, мы потеряли "с"! Так как значения были одинаковы,
#                  # то когда они стали ключами, только последнее значение сохранилось.
# print(f'Size of dictionary - dict_abc: {sys.getsizeof(dict_abc)}')      # __ NB! __ it not depends on from the number of elements.
# print(f'Size of generator of the dictionary above - dict_gen_abc: {sys.getsizeof(dict_gen_abc)}')   # __ NB! __ it not depends on from the number of elements.

# 5.3 Генерация строк:
# Для создания строки вместо синтаксиса выражений-генераторов используется метод строки .join(), которому в качестве
# аргументов можно передать выражение генератор.
#   __ NB! __   элементы коллекции для объединения в строку должны быть строками!
# list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
# # используем генератор прямо в .join() одновременно приводя элементы к строковому типу
# str_diff = "-2-1012345"
# my_str = ''.join(str(x) for x in list_a)
# print(my_str)                                   # -2-1012345
# print(f'Size of list list_a: {sys.getsizeof(list_a)}.\n'
#       f'Size of string str_diff: {sys.getsizeof(str_diff)}')
# print(f'Size of string my_str: {sys.getsizeof(my_str)}')


# __ NB! __
# Итератор VS Генератор VS Итерируемый объект:
#       - Итератор - Объект, который реализует методы __iter__() и __next__(), позволяющие
#         последовательно обходить элементы.
#       - Генератор - Функция, которая использует ключевое слово yield для возврата значений,
#         сохраняя при этом свое состояние между вызовами.
#       - Итерируемый объект - Объект, который может быть использован в цикле for.
#         Он возвращает итератор при вызове функции iter().

# __ 1-st Variant __
# def show_letters(some_str):
#     for symbol in some_str:
#         if symbol.isalpha():
#             yield symbol

# __ 2-nd Variant __
# def show_letters(some_str):
#     yield from (letter for letter in some_str if letter.isalpha())          # выполнится, т.к. с from.
#     # yield (letter for letter in some_str if letter.isalpha())             # без from -- НЕ работает!
#
# for i in show_letters("kf23r89h2i"):
#     print(i)


# __________ itertools __________

# - модуль, который предоставляет набор функций для работы с итерируемыми объектами.

# ___ Islice ___
# — функция, которая позволяет создавать итераторы, представляющие собой срезы исходного итерируемого объекта.

# iiiiiiiiiiiiiiiiiiiiiiiiiii
# import itertools
# iiiiiiiiiiiiiiiiiiiiiiiiiii

# my_list = [1, 2, 3, 4, 5]
# my_iterator = itertools.islice(my_list, 1, 4)
# for item in my_iterator:
#     print(item) # Выводит 2, 3, 4

# Какой будет результат выполнения кода (догадайтесь, что делает незнакомая функция, по ее названию):
# iiiiiiiiiiiiiiiiiiiiiiiiiii
# import itertools
# iiiiiiiiiiiiiiiiiiiiiiiiiii
# colors = ['red', 'green', 'blue']
# sizes = ['S', 'M', 'L']
# # for color, size in itertools.product(colors, sizes):          # Выведет 9 пар, тк перемножение.
# #     print(color, size)
# for color, size in zip(colors, sizes):                          #  Только 3 пары.
#     print(color, size)

# Какой будет результат выполнения кода (догадайтесь, что делает незнакомая функция, по ее названию):
# iiiiiiiiiiiiiiiiiiiiiiiiiii
# import itertools
# iiiiiiiiiiiiiiiiiiiiiiiiiii
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# for item in itertools.chain(list1, list2):
#     print(item)



# ______  Task 1  ____________________________________________________________________________________________________
# Создать генератор, который будет делать то же самое что и range с одним аргументом.
# __ 1-st Variant __
# def make_range(start, stop):
#      # start = 0
#      while start < stop:
#         yield start
#         # return start            # Error!
#         start += 1
#
# for i in make_range(1, 10):
#     print(i)


# __ 2-nd Variant __
# def my_range(start, stop=None, step=1):
#     if stop is None:                      # Если указан только один аргумент, то это "stop"
#         stop = start
#         start = 0
#     while start < stop:
#         yield start
#         start += step
#
# # for i in my_range(3):
# #     print(i)
# for i in my_range(1, 11, 2):
#     print(i)

# ______  Task 2  ____________________________________________________________________________________________________
# 1. Написать функцию validateCustomers(customer), которая принимает на входе список кортежей:
#       ● Имя
#       ● Фамилия
#       ● Дата рождения
#       ● Номер банковского счета (iban)
# Функция возвращает мапу, где ключом является строка имя+фамилия, а значением - список
# сообщений об ошибках, возникших при валидации пользователя по следующим правилам:
#       ● Имя и фамилия не должны быть пустыми.
#       ● Возраст валиден, если он больше 18 лет.
#       ● Iban должен соответствовать стандарту длины (начинаться с кода страны и содержать
#         правильное количество символов)
# Решение должно использовать исключения и итераторы.

# country_length = {
#     "DE": 22, # Германия (Germany)
#     "FR": 27, # Франция (France)
#     "GB": 22, # Великобритания (United Kingdom)
#     "IT": 27, # Италия (Italy)
#     "ES": 24, # Испания (Spain)
#     "NL": 18, # Нидерланды (Netherlands)
#     "BE": 16, # Бельгия (Belgium)
#     "CH": 21, # Швейцария (Switzerland)
#     "AT": 20, # Австрия (Austria)
#     "SE": 24, # Швеция (Sweden)
#     "PL": 28, # Польша (Poland)
#     "NO": 15, # Норвегия (Norway)
#     "DK": 18, # Дания (Denmark)
#     "FI": 18, # Финляндия (Finland)
#     "PT": 25, # Португалия (Portugal)
# }
#
# iiiiiiiiiiiiiiiiiiiiiiiiiii
# import json
# from datetime import datetime
# iiiiiiiiiiiiiiiiiiiiiiiiiii
#
#
# def validate_customers(customers):
#     errors_map = {}
#     for customer in customers:
#         first_name, last_name, date_of_birth, iban = customer.values()
#         errors = []
#
#         # Проверка имени и фамилии
#         try:
#             validate_name(first_name, last_name)
#         except ValueError as e:
#             errors.append(str(e))
#
#         # Проверка возраста
#         try:
#             age = calculate_age(date_of_birth)
#             validate_age(age)
#         except ValueError as e:
#             errors.append(str(e))
#
#         # Проверка IBAN
#         try:
#             validate_iban(iban)
#         except ValueError as e:
#             errors.append(str(e))
#
#         if errors:
#             errors_map[f"{first_name} {last_name}"] = errors
#
#     return errors_map
#
#
# def validate_name(first_name, surname):
#     if not first_name or not surname:
#         raise ValueError("Имя или фамилия пустые.")
#
# def calculate_age(date_of_birth):
#     try:
#         birth_date = datetime.strptime(date_of_birth, "%d-%m-%Y")
#     except ValueError as e:
#         raise ValueError(f"Дата {date_of_birth} не соответствует формату: {e}")
#     today = datetime.today()
#     # age = (datetime.now() - birth_date).days // 365  # Упрощенный вариант
#     age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
#     return age
#
# def validate_age(age):
#     if age < 18:
#         raise ValueError("Возраст меньше 18 лет")
#
#
# def validate_iban(iban):
#     country_code = iban[:2]
#     country_length = {
#         "DE": 22,  # Германия (Germany)
#         "FR": 27,  # Франция (France)
#         "GB": 22,  # Великобритания (United Kingdom)
#         "IT": 27,  # Италия (Italy)
#         "ES": 24,  # Испания (Spain)
#         "NL": 18,  # Нидерланды (Netherlands)
#         "BE": 16,  # Бельгия (Belgium)
#         "CH": 21,  # Швейцария (Switzerland)
#         "AT": 20,  # Австрия (Austria)
#         "SE": 24,  # Швеция (Sweden)
#         "PL": 28,  # Польша (Poland)
#         "NO": 15,  # Норвегия (Norway)
#         "DK": 18,  # Дания (Denmark)
#         "FI": 18,  # Финляндия (Finland)
#         "PT": 25,  # Португалия (Portugal)
#     }
#
#     if country_code not in country_length:
#         raise ValueError(f"Страна {country_code} не существует.")
#
#     if len(iban) != country_length[country_code]:
#         raise ValueError(f"Неверная длина IBAN для страны {country_code}.")
#
#
# def load_customers_from_json(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as f:
#             return json.load(f)
#     except FileNotFoundError:
#         raise FileNotFoundError(f"Файл {file_path} не найден.")
#     except json.JSONDecodeError:
#         raise ValueError("Ошибка при разборе JSON файла.")
#
#
# # Пример использования:
# try:
#     customers = load_customers_from_json("customers.json")
#     result = validate_customers(customers)
#
#     for customer, errors in result.items():
#         print(f"{customer}:")
#         for error in errors:
#             print(f"  {error}")
# except Exception as e:
#     print(e)



