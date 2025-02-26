# Home Work 12, 12.01.25
# ___ STRINGS ___
# Normal  \033[0;__;__m \033[m    or   BOLD  \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# f = 40; f = '.' * f; print(f) - Filler up to.
# print(f, f'\n...')
# print(' ' * 5, f'...') - Indentation in the output of the result

# ___ Task 1 ___
# Напишите программу, которая запрашивает у пользователя число N и выводит на экран таблицу умножения от 1 до N.
# Используйте вложенный цикл for для создания таблицы умножения. Выведите результат на экран с помощью команды print.
# ____ 1-st Variant ____ My Variant - for me.
# while True:
#     f = 40; f = '.' * f; print(f)
#     numb = int(input("Enter an integer number: "))
#     print(f, f'\nMultiplication table for \033[1;33m{numb}\033[m from 1 to 10: ')
#     for i in range(1, 10):
#         print(' ' * 5, f'{numb} * {i} = {numb * (i)}')
#     print(f)
#     ask = input("\nDo you want to continue? (y/n): ").lower()
#     if ask == 'n':
#         break
# ____ 2-nd Variant ____ In accordance with the task:
# f = 40; f = '.' * f; print(f)
# numb = int(input("Enter an integer number: "))
# print(f, f'\nMultiplication table from 1 to \033[1;33m{numb}\033[m: ')
# row1 = list(range(1, numb + 1))
# # print(row1, row1[0])                  # Проверяю все ли элементы есть в списке.
# # for i in range(1, numb + 1):          # Цикл для выведения последовательности в ряд.
# #     print(i, end=' ')
# # print('\n')
# # for i in range(numb):                 # Цикл для выведения элементов из списка row1.
# #     print(f'{row1[i]}', end=' ')
# # print('\n')
#
# # Вложенные циклы: see https://www.bzfar.org/publ/algorithms_programming/programming_languages/python_vlozhennye_cikly/42-1-0-194.
# # end='\t' - табуляция.
# for i in range(1, numb + 1):                 # Берем i=1 член из разложения в ряд.
#     for j in range(numb):                    # Теперь перебираем все члены списка row1 и ...
#         print(f'{row1[j] * i}', end='\t')    # ... умножаем их на 1-ый член разложения i=1. Потом берем i=2 и т.д.
#     print()

# _____ Final code for ICH _____
# f = 40; f = '.' * f; print(f)
# numb = int(input("Enter an integer number: "))
# print(f, f'\nMultiplication table from 1 to \033[1;33m{numb}\033[m: ')
# row1 = list(range(1, numb + 1))
# for i in range(1, numb + 1):                 # Берем i=1 член из разложения в ряд.
#     for j in range(numb):                    # Теперь перебираем все члены списка row1 и ...
#         print(f'{row1[j] * i}', end='\t')    # ... умножаем их на 1-ый член разложения i=1. Потом берем i=2 и т.д.
#     print()

# __ Another Variant from link above __
# https://www.bzfar.org/publ/algorithms_programming/programming_languages/python_vlozhennye_cikly/42-1-0-194.
# f = 40; f = '.' * f; print(f)
# numb = int(input("Enter an integer number: "))
# for i in range(1, numb + 1):                            # начало внешнего цикла
#     for j in range(1, numb + 1):                        # начало вложенного цикла
#         print(i, '*', j, '=', i * j, end='\t')          # вывод таблицы умножения
#     print()                                             # переход на новую строку

# __ Variant from Python_Summary6.pdf, Slide 66 __
N = int(input("Введите N: "))
L = len(str(N * N)) + 2
# print(str(N * N), L)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(f"{i*j:{L}d}",end="")                 #  целoе числo с минимальной шириной - see slide 17 and here down.
    # print("\n")
    print()

# _____ Форматирование чисел _____
# print()
# print("1 - The number is: {:d}.".format(123))                    # целочисленные аргументы.
# print("2 - {:5d}.".format(12))                                   # ___ целые числа с минимальной шириной. ___
# print("3 - The float number is: {:f}.".format(123.4567898))      # аргументы с плавающей точкой.
# print("4 - {:8.3f}.".format(12.2346))                            # заполнение для чисел с плавающей точкой.
# print("5 - bin: {0:b}, oct: {0:o}, hex: {0:x}.".format(12))      # восьмеричный, двоичный и шестнадцатеричный формат.

# _____ Динамическое форматирование _____
# string = "{:{fill}{align}{width}}"                                 # динамический шаблон формата строки.
# print(string.format('cat', fill='*', align='^', width=5))    # передача кодов формата в качестве аргументов.
# term = 'Energy'
# print(f'Definition of {term:*^10}.')
# print(f'Definition of {'Force':*^10}.')
# num = "{:{align}{width}.{precision}f}"                             # динамический шаблон формата float.
# print(num.format(123.236, align='>', width=8, precision=2))  # передача кодов формата в качестве аргументов.

# ___ Task 2 ___
# Напишите программу, которая принимает два списка одинаковой длины и создает новый список,
# содержащий пары элементов из исходных списков. Используйте функцию zip() для создания пар элементов.
# Выведите результат на экран с помощью команды print.
# f = 40; f = '.' * f; print(f)
# print('Enter the same number of characters in both sets.')
# set_numb = list(input('Enter \033[1;36m1-st\033[m set of symbols separated by spaces: ').split())
# set_let = list(input(f'Enter \033[1;34m2-nd\033[m set of symbols separated by spaces: ').split())
# zip_sets = zip(set_numb, set_let)
# print(f'List of pairs: {list(zip_sets)}')



# ###################################################################################################################

# ___ Determining days of the week dates ___

# print(f, f'\n***  Determining days of the week dates  ***')
# # Получение дня недели по дате: https://sky.pro/media/poluchenie-dnya-nedeli-po-date-v-python/.
# import datetime
# day_begin = int(input('Enter a start day: '))
# day_end = int(input('Enter an end day: '))
# month = int(input('Enter a number month: '))
# year = int(input('Enter a year: '))
# date_start = datetime.datetime(year, month, day_begin)      # Создание объекта datetime.
# date_finish = datetime.datetime(year, month, day_end)
# print(f, f'\nThe range of dates you selected: ')
#
# dat_rang = list(range(day_begin, day_end))
# print(dat_rang)
# week_day_start = date_start.isoweekday()
# week_day_finish = date_finish.isoweekday()
# week_day_rang = list(range(week_day_start, date_finish))


# print(date.isoweekday())                                    # Вывод НОМЕРА дня недели.




