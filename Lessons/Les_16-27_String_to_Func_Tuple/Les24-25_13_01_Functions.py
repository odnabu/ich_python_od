# Semenov Artem
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 13.01.25
# Python 24 - 25: FUNCTIONS

# ###################################################################################################################
print('.' * 120)

# Функция - объект в памяти компьютера.
# Имя функции -- это ссылка на объект-функцию. NB!!! - it is BETTER the named function as VERB - what makes the function.
# def - <func name>([list of arguments]):
#     operator1         |
#     operator2         | the BODY of function
#     ...               |
#     operatorN         |

#  __ 1-st Variant __

# def greetings():
#     print("Hello User!")
# greetings()

#  __ 2-nd Variant __
# def send_mail():
#     text ="Please, explain how the function works?"
#     print(text)
# send_mail()

#  __ 3-d Variant __
# def send_mail(from_name, age):          # rom_name, age - Параметры функции.
#     text ="Please, explain how the function works?"
#     print(f'My name is \033[33m{from_name}\033[m.\nMy age is \033[34m{age}\033[m.\n{text}')
# send_mail('Oleg', 15)     # 'Oleg' и 15 - Аргументы функции.

#  __ 4-d Variant __
# def send_mail():
#     text = "Hello World!"
#     return text
# print(send_mail())

#  __ 5-th Variant __
# def get_square(number):
#     result = number ** 2
#     return result
# a = get_square(5)
# print(a)

# ___ Oleksandr Kiselov 9:56 ___

#  __ 1-st Variant __
# text = "Hallo"
# def hallo(i):
#     print(text[i])
#     if(i < len(text) - 1):
#         hallo(i + 1)
#     else:
#         return
# hallo(0)

#  __ 2-nd Variant __
# text = "Hallo"
# def hallo(i = 0):
#     print(text[i])
#     if(i < len(text) - 1):
#         hallo(i + 1)
# hallo()


# ###################################################################################################################

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% _________  СТЕК (STACK)  &  Куча (HEAP)  __________ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ___ СТЕК (STACK - упорядоченная куча/стопка) и Куча (HEAP - НЕупорядоченная куча) вызовов ___
# Стек - область (место) в оперативной памяти в компе, куда закидываются функции или операторы (см видео 10:22) -
# - структура данных,  которая отслеживает порядок вызова функций (см.слайд 22, Presentation 13).
# Стек выглядит как столбец, в котором наверху находится последняя функция.
# В стеке выполняется самый последний (верхний) элемент: Last IN --> First out.
# Oleksandr Kiselov 10:18 - вот тут можно понять, как работает стек:
# text = "Hallo"
# def hallo(i = 0):
#     print(text[i])
#     if(i < len(text) - 1):
#         hallo(i + 1)
#     print(i)
# hallo()

# --------------- Как работает стек ---------------
# ___ 1-st Example ___
# def function_a():
#     print("Inside function A")
#     function_b()
# def function_b():
#     print("Inside function B")
# function_a()

# Как это работает:
# Когда вызывается function_a(), она помещается в стек вызовов.
# Внутри function_a происходит вызов function_b(), поэтому она тоже добавляется в стек вызовов.
# Когда function_b() завершает выполнение, она удаляется из стека.
# Управление возвращается в function_a, и она также завершает выполнение, после чего удаляется из стека.
# Стек вызовов в данном случае выглядит так:

# Когда запускается function_a(), стек:
# [function_a()]
# После вызова function_b() внутри function_a, стек:
# [function_a(), function_b()]
# После завершения function_b(), стек:
# [function_a()]
# После завершения function_a(), стек пуст.

# ___ 2-nd Example - more detailed than 1-st Example above ___
# def a():
#     print("Start of function a")
#     b()
#     print("End of function a")
# def b():
#     print("Start of function b")
#     c()
#     print("End of function b")
# def c():
#     print("Start of function c")
#     print("End of function c")
# a()

# ###################################################################################################################

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% _________ Локальные и Глобальные ПЕРЕМЕННЫЕ __________ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# _________ Локальные переменные _________
# Локальные переменные видны только внутри функции.
# def add(x, y):
#     result = x + y                    # 'result' — локальная переменная
#     print(f"Result: {result}")
#     return result

# def main():
#     d = 100
#     be = 209
#     add(d, be)
# main()

# Объяснение:
# При вызове main() создаётся фрейм для функции main.
# В этом фрейме хранятся локальные переменные a и b.
# При вызове add(a, b) создаётся новый фрейм для функции add.
# В этом фрейме хранятся локальные переменные x, y и result.
# После завершения add, её фрейм удаляется из стека, и result исчезает.
# После завершения main, её фрейм тоже удаляется.

# _________ Глобальные переменные _________
# global_var = 10
# def example_function():
#     # Локальная переменная
#     local_var = 5
#     print("Локальная переменная:", local_var)       # Доступ к локальной переменной
#     print("Глобальная переменная:", global_var)     # Доступ к глобальной переменной

# def modify_global():
#     global global_var                               # Указываем, что будем изменять глобальную переменную.
#     global_var = 20
#     print("Глобальная переменная изменена на:", global_var)

# Основной код:
# print("Глобальная переменная до вызова функций:", global_var)
# example_function()                                  # Вызов функции с локальной переменной
# modify_global()                                     # Изменение глобальной переменной.
# print("Глобальная переменная после вызова функций:", global_var)

# ###################################################################################################################

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% _________  Global Space Names __________ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# - Пространство имен - место, где каждая функция в Python хранит свои
# локальные переменные и другие объекты. Это словари, где имена переменных связаны с их значениями.

# Python использует правило LEGB (Local, Enclosing, Global, Built-in) для поиска имени:
#   - Local (локальное): Поиск имени сначала происходит в локальном пространстве имён.
#   - Enclosing (замыкающее): Если локальное пространство отсутствует, поиск продолжается в замыкающем пространстве
#     (например, в функции, которая содержит текущую функцию).
#   - Global (глобальное): Если имя не найдено в локальном и замыкающем пространстве, поиск продолжается в глобальном.
#   - Built-in (встроенное): Если имя отсутствует во всех вышеуказанных пространствах, Python проверяет встроенное пространство имён.

# В Python вложенные функции выполняются в порядке, который называется LIFO (Last In, First Out),
# что означает "последний вошел, первый вышел". Это означает, что самая внутренняя функция выполняется первой,
# и только после ее завершения продолжается выполнение внешней функции.
# x = "global"
# def outer_function():
#     x = "enclosing"
#     print(x)
#
#     def inner_function():
#         x = "local"
#         print(x)            # Вывод: local
#         x = "End local"
#         print(x)
#     inner_function()
#
#     x = "End enclosing"
#     print(x)
#
# outer_function()

# ###################################################################################################################

# ___ PRACTICE ___

# __ Task 1 __
# Перепишите решение следующей задачи с использованием функции. У нас есть две логические переменные:
# isWeekday, isVacation (выходной день и каникулы). Они могут принимать разные значения, всего 4 комбинации:
# true - true, true - false, false - false, false - true. Есть правило: мы можем поспать,
# если день не рабочий или мы на каникулах. Напишите программу, которая в зависимости от значений двух переменных
# печатает, можем ли мы поспать или нет. То есть для значений isWeekday = False и isVacation = False
# программа должна печатать “можете поспать”.

# def Week_daying(isWeekday, isVacation):
#     ''' Определяет, можем ли мы поспать. Если день не рабочий (is_weekday == False)
#     или мы на каникулах (is_vacation == True), возвращает 'можете поспать', иначе 'не можете поспать'. '''
#     if not isWeekday or isVacation:
#         return "You may sleep"
#     elif isWeekday and not isVacation:
#         return "You need go to work"
#     elif isWeekday and isVacation:
#         return "You can sleep"
#     else:
#         return "You need go to work"
# day_week = input('Print the day: ').strip().lower() == 'true'
# vacation = input('Print the vacation: ').strip().lower() =='true'
# result = Week_daying(day_week, vacation)
# print(result)

# __ Task 2 __ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Написать функцию для определения большего числа.
# def comparison_numbs(numb1, numb2):
#     if numb1 < numb2:
#         return f'Numb {numb1} is less than Numb {numb2}.'
#     elif numb1 > numb2:
#         return f'Numb {numb2} is greater than Numb {numb1}.'
#     else:
#         return f'Numb {numb1} is equal to Numb {numb2}.'
# input_numb1 = int(input('Enter 1-st integer number: '))
# input_numb2 = int(input('Enter 2-nd integer number: '))
#
# print(comparison_numbs(input_numb1, input_numb2))
# ____________ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# __ Task 3 __
# Даны два целых числа A и B (при этом A ≤ B). Напишите функцию, которая печатает все числа от A до B включительно.
# __ 1-st Variant __
# def print_numbs(a, b):
#     for i in range(int(a), int(b) + 1):
#         print(i)
#         # i += 1            # Тоже не нужно, потому что это для цикла while.
#         # return i          # Остановится выполнение цикла, поэтому return здесь НЕ нужен!
# a, b = input('Enter 2 numbers with space: ').split()
# # a, b = int, (a, b)
# print_numbs(a, b)

# __ 2-nd Variant __
# def print_numbs(a, b):
#     while a <= b:
#         print(a)
#         a = a + 1
#
# a, b = 2, 5
# print_numbs(a, b)

# __ 3-d Variant __
# a, b = 2, 5
# print(list(range(a, b + 1)))

# __ Task 4 __
# Напишите функцию, которая возвращает факториал заданного числа. Факториалом числа n называется
# произведение 1 × 2 × ... × n. Обозначение: n!.
# По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
# Во всех задачах считывайте входные данные через input() и выводите ответ через print().
# __ Factorial with FOF - simple variant __
# n = 5
# print(list(range(1, n + 1)))
# f = 1                                 # See https://sky.pro/wiki/python/cikl-for-v-python-iteraciya-po-spisku/.
# for i in range(1, n + 1):
#     f *= i
#     print(f)
# print(f'{n}\033[1;33m!\033[0m = \033[1;33m{f}\033[0m.')

# __ Factorial with FOR in DEF - CORRECT ! __
# def factorial_n(n):
#     if n == 0:
#         # return 1
#         print(f'{n}\033[1;31m!\033[0m is \033[1;31m1\033[0m.')
#     else:
#         f = 1
#         for i in range(1, n + 1):
#             f *= i
#         # print(f)
#         print(f'{n}\033[1;33m!\033[0m = \033[1;33m{f}\033[0m.')
# inp_numb = int(input('Enter an integer number: '))
# factorial_n(inp_numb)

