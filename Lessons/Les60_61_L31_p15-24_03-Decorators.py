# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 24.03.25
 Python 60: Decorators.
 ################################################################################################################### """
# Video Lesson 60: ------------.
# Video Practice 61: -----------.
# links:
#   - Presentation: https://lms.itcareerhub.de/pluginfile.php/7899/mod_resource/content/1/Python_31_M.pptx.pdf
#   - Декораторы: https://pythonworld.ru/osnovy/dekoratory.html.
#   - Декораторы в Python: понять и полюбить: https://tproger.ru/translations/demystifying-decorators-in-python.
#   - Как создавать классы в Python: https://highload.tech/kak-sozdavat-klassy-v-python-so-znaniem-dela-razbiraem-na-primerah/.

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



""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%_____________   Декораторы - INTRO   ____________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """
# — это функции, которые принимают другую функцию в качестве аргумента, добавляют к ней некоторую
#   функциональность и возвращают измененную функцию.

""" __________ Функция-обертка __________ """
# — вспомогательная функция, которая принимает оригинальную функцию в качестве аргумента,
#   добавляет к ней дополнительную логику и возвращает измененную функцию.
#   Позволяет каждый раз обращаться к декорированной (дополненной функционалом) функции, НЕ вызывая её каждый раз. Video 60, 20:00
# Внутри функции-обертки можно выполнять различные действия:
#       ● Запись логов
#       ● Проверка аргументов
#       ● Изменение возвращаемого значения итд.

# See Video 60, 26:00: LEGB - локальные (L) и глобальные(G), встроенные (B) и замкнутые (E - enclosing)
# переменные в соответствующей области видимости.
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         # Дополнительная логика ПЕРЕД выполнением функции:
#         result = func(*args, **kwargs)
#         # Дополнительная логика ПОСЛЕ выполнения функции:
#         return result
#     return wrapper

""" __ NB! __    ___ Синтаксис применения декоратора ___ """
#   ● Декораторы применяются к функциям или классам с помощью символа @, за которым следует имя декорирующей функции.
#   ● При вызове декорируемой функции синтаксис декоратора автоматически применяется, что позволяет просто и
#     удобно изменять поведение функции.
            # @decorator
            # def my_function():
            #   # Тело функции
            #   pass

# # ___ EXAMPLE _____________________________________________________________________________________
# def decorator(func):
#     def wrapper():                          # ОБЁРТКА, без которой декоратор НЕ сработает.
#         print("Сейчас выполним функцию:")
#         func()
#         print("Функция выполнена.\n")
#     return wrapper                          # Возвращение ОБЪЕКТА функции в НЕзапущенном состоянии.
#
# # @decorator
# def my_function():
#     # a, b=input("Введите два слова: ").split()
#     # print("Вот они:",b,a)
#     print(f'\tMy function')
#
# # my_function()
#
# # result = decorator(my_function)     # Только в НЕзапущенном формате - т.е. БЕЗ скобок. Так вызывается сам объект, а НЕ результат его работы!
# # print(result)                       # Вернёт ОБЪЕКТ функции декоратора: function decorator.<locals>.wrapper...
# # print(f'{'___ Выполнение функции: ':_<50}')
# # result()                            # А вот так функция ВЫПОЛНИТСЯ.
#
# @decorator
# def my_function():
#     # a, b=input("Введите два слова: ").split()
#     # print("Вот они:",b,a)
#     print(f'\tMy function')
#
# @decorator
# def my_another_function():
#     print(f'\tMy another function')
#
# my_function = decorator(my_function)     # @decorator, причём, ЭТО выражение можно НЕ писать, а просто сразу перейти к принту -->
# print(my_function)                       #
# print(f'{'___ Выполнение функции из ДЕКОРАТОРА: ':_<50}')
# my_function()                         # Можно многократно вызывать измененную функцию!
# my_function()                         # Можно многократно вызывать измененную функцию!
# my_another_function()                         # Можно многократно вызывать измененную функцию!
# # ___ END of Example _____________________________________________________________________________________

""" __________  Декораторы для функций с аргументами: __________ """    # Video 60, 1:05:00
#   ● Декораторы могут быть применены к функциям, которые принимают аргументы.
#   ● Для этого в функции-обертке необходимо использовать *args и **kwargs, чтобы передать все аргументы в
#     декорируемую функцию.
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         # Дополнительная логика перед выполнением функции
#         result = func(*args, **kwargs)
#         # Дополнительная логика после выполнения функции
#         return result
#     return wrapper
# @decorator
# def my_function(arg1, arg2):
#     # Тело функции
#     pass

# # ___ EXAMPLE _____________________________________________________________________________________
# def decorator(func):
# def wrapper(*args, **kwargs):
# print("Сейчас выполним функцию")
# result=func(*args, **kwargs)
# print("Функция выполнена, получено: ",result)
# return result.upper()
# return wrapper
# @decorator
# def my_function(between):
# a, b=input("Введите два слова: ").split()
# return a+between+b
# print("Результат работы декоратора: ",my_function(" and "))
# # ___ END of Example _____________________________________________________________________________________

""" __________  Параметрические декораторы: __________ """    # Video 60, 1:10:00
# — это декораторы, которые позволяют передавать аргументы в декорирующую функцию при ее применении. Для этого
# можно создать дополнительную функцию-обертку, которая принимает аргументы декоратора и возвращает саму
# функцию-обертку, принимающую декорируемую функцию.

# def param_decorator(arg1, arg2):
# def decorator(func):
# def wrapper(*args, **kwargs):
# # Дополнительная логика перед выполнением функции с
# использованием arg1 и arg2
# result = func(*args, **kwargs)
# # Дополнительная логика после выполнения функции с использованием
# arg1 и arg2
# return result
# return wrapper
# return decorator
# @param_decorator(arg1, arg2)
# def my_function():
# # Тело функции

# # ___ EXAMPLE _____________________________________________________________________________________
# def param_decorator(ask_name):
# def decorator(func):
# def wrapper():
# if ask_name:
# name=input("Как вас зовут? ")
# result = func()
# if ask_name:
# print(f"Ваше имя {name}, ваш возраст - {result}")
# else:
# print(f"Ваш возраст - {result}")
# return wrapper
# return decorator
# @param_decorator(True)
# def ask_age():
# age=input("Сколько вам лет? ")
# if age.isdigit():
# return age
# return "неизвестно"
# ask_age()
# # ___ END of Example _____________________________________________________________________________________

""" __ NB! __ __________   Декоратор  @functools.wraps __________ """    # Video 60, 1:26:00
# — это декоратор, который позволяет сохранить атрибуты оригинальной функции при применении декоратора.

# import functools
# def decorator(func):
# @functools.wraps(func)
# def wrapper(*args, **kwargs):
# # Дополнительная логика перед выполнением функции
# result = func(*args, **kwargs)
# # Дополнительная логика после выполнения функции
# return result
# return wrapper


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%______  Создание и применение декораторов  _____%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

""" __________  Применение нескольких декораторов к функции: __________ """
#       ● Функцию можно декорировать с помощью нескольких декораторов, применив их последовательно сверху вниз.
#       ● Это позволяет комбинировать различные аспекты функциональности и изменять поведение
#         функции с использованием разных декораторов.
               # @decorator1
               # @decorator2
               # def my_function():
               #   # Тело функции
               #   pass

""" __________  Создание декораторов: __________ """
# При создании декораторов можно применять декораторы к функциям или классам, чтобы добавить или изменить
# их функциональность, улучшить читаемость и повторное использование кода.

""" __________  Применение декораторов к классам: __________ """
# ● В случае применения декораторов к классам, они могут изменять поведение методов
# класса или добавлять новые методы и атрибуты.
# ● Декораторы классов широко используются для реализации паттернов проектирования и
# обеспечения гибкости в работе с классами.
            # def class_decorator(cls):
                # # Логика перед созданием класса
                # return cls
            #
            # @class_decorator
            # class MyClass:
                # # Тело класса
                # pass


""" ______  Task 1  ______________________________________________________________________________________________ """
# Создайте декоратор `frame`, который **оборачивает результат функции рамкой из 50 символов `-`, выводя по строке
# до и после вызова функции.
# --------------------------------------------------
# Привет, игрок!
# --------------------------------------------------

# # __ 1-st Variant - SIMPLE __
# def frame(func):
#     def wrapper():
#         print('%' * 30)
#         func()              # Пишем func(), потому что потом передадим ее в декоратор.
#         print('%' * 30)
#     return wrapper
#
# @frame
# def say_hello():
#     print(f'\tHello World!')
#
# say_hello()
#
# @frame
# def say_bye():
#     print(f'\tBye-bye!')
#
# say_bye()

# # __ 2-nd Variant + parametric decorator __
# def frame(line_num):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print('%' * line_num)
#             func(*args, **kwargs)              # Пишем func(), потому что потом передадим ее в декоратор.
#             print('%' * line_num)
#         return wrapper
#     return decorator
#
# @frame(40)
# def say_hello(player):
#     print(f'\tHello World! {player}')
#
# say_hello('Olga')
#
# @frame(80)
# def say_bye():
#     print(f'\tBye-bye!')
#
# say_bye()


""" ______  Task 2  ______________________________________________________________________________________________ """
# Реализовать декоратор, который измеряет время выполнения функции и выводит его на консоль.

# # ++++++++++++++
# import time
# # ++++++++++++++
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         # func(*args, **kwargs)
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(f'{func.__name__} took {end - start} seconds.')
#         return res
#     return wrapper
#
#
# @timer
# def sona(interval):
#     time.sleep(interval)
#
# sona(2)
#
# @timer
# def massiv(numb_of_elements):
#     arr = list(range(numb_of_elements))
#     return arr
#
# massiv(50_000_000)
# print(massiv(50_000))


""" ______  Task 3  ______________________________________________________________________________________________ """
# Создайте декоратор `retry`, который **повторяет** вызов функции указанное количество раз, если функция
# вызывает ошибку.

# # __ 1-st Variant - SIMPLE __
# # +++++++++++++++++++++
# import time
# # +++++++++++++++++++++
# def retry(func):
#     def wrapper(*args, **kwargs):
#         for i in range(5):
#             try:
#                 return func(*args, **kwargs)
#             except Exception as e:
#                 print(f'Try number {i+1} --> Ошибка чтения данных из файлу: \033[31m{e}\033[m')
#                 time.sleep(1)
#     return wrapper
#
# @retry
# def read_file(file_name):
#     with open(file_name, "r") as file:
#         return file.read()
#
# print(read_file("anonymous.txt"))

# # __ 2-nd Variant + parametric decorator __
# # +++++++++++++++++++++
# import time
# # +++++++++++++++++++++
# def retry(wait_time, exec_times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(exec_times):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     print(f'Try number {i+1} --> Ошибка чтения данных из файла: \033[31m{e}\033[m')
#                     time.sleep(wait_time)
#         return wrapper
#     return decorator
#
# @retry(1, 5)
# def read_file(file_name):
#     with open(file_name, "r") as file:
#         return file.read()
#
# print(read_file("anonymous.txt"))



# ---------------------------------
# Stanislav M. 12:13
# я вот это хотел спросить, как без сахара использовать параметрические/не декораторы:
# myfunc_with_decorator = decorator(myfunc)
# result = myfunc_with_decorator(500)
# print(result)
#
# myfunc_with_param_decorator = param_decorator(1)(myfunc)
# result = myfunc_with_param_decorator(500)
# print(result)