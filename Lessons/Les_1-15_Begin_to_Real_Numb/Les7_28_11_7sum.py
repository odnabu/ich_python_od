# Semenov Artem
# 29.11.24
# Python 7: Summary session 2

# ___ ОШИБКА в ДЗ !!! ___
# print(f'___ Task 2 ___\n')
## log_val_1 = True
## log_val_2 = False
# # Проблема ввода булевых в Python можно решить одним из таких способов:
# log_val_1 = input('Enter the first logical value (True or False): ') == 'True'
# log_val_2 = input('Enter the second logical value (True or False): ') == 'True'
# print(f'\nResult of logical AND: {log_val_1 & log_val_2}.')
# print(f'Result of logical OR: {log_val_1 | log_val_2}.')
# print(f'Result of logical NOT for 1-st: {not log_val_1}.')
# print(f'Result of logical NOT for 2-st: {not log_val_2}.')
# print(f'The result of comparing two values for equality: {log_val_1 == log_val_2}.')
# print(f'The result of comparing two values for inequality: {log_val_1 != log_val_2}.')

# __ Другое решение ДЗ __
# a = 1; b = 0
# print(bool(a))
# print(bool(b))
# a = int(input('Enter a 1-st bool value: '))
# b = int(input('Enter a 2-nd bool value: '))
# print(bool(a))
# print(bool(b))

# a = input('Enter a 1-st bool value: ') == 'True'
# b = input('Enter a 2-nd bool value: ') == 'True'
# c = True == 'True'; print(c)
# d = True; print(type(d))
# print(type(a), bool(a))
# print(type(b), bool(b))
# print(type(b))

# a = input('Enter a 1-st number: ')
# b = input('Enter a 2-st number: ')
# print(a - b)    # NB! TypeError: unsupported operand type(s) for -: 'str' and 'str'

# a = float(input('Enter a 1-st number: '))
# b = float(input('Enter a 2-st number: '))
# print(a - b)

# ___ NB! ___ Проблема введения БУЛЕВЫХ в Python.
# Если в bool (команда, которая определяет "пусто" или "НЕ пусто") есть хоть что-нибудь, т.е. он НЕ содержит даже пробела,
# то результат всегда будет TRUE, потому что по умолчанию bool воспринимает данные
# как строковые.
# a = '12'
# b = ''
# c = ' '
# print(type(a), type(b), type(c))
# b1 = bool(a); b2 = bool(b); b3 = bool(c)
# print(b1, b2, b3)

# _______ NB!!! _______
# НО, Alexander Golubenko 9:45:  eval функция переводящая в булевы значения.
# user_input = input("Enter True or False):")
# result = eval(user_input)
# print(type(result))
# print(f"Result is: {result}")
# Stanislav M. 9:58:  И правда можно, но как я понял вроде это плохая практика
# Alexander Golubenko 9:59:  Очень плохая
# # Alexander Golubenko 9:59:  Это принудительное булево выполнение
# _____________________


# ___ math - Mathematical Modul ___
import math
# # from math import factorial
# print(math.pi)

# Округление чисел с плавающей точкой в большую сторону:
# print(f'ceil -3.14 = {math.ceil(-3.14)}');    print(f'ceil -4.14 = {math.ceil(-4.14)}')
# Округление чисел с плавающей точкой в меньшую сторону:
# print(f'floor 3.14 = {math.floor(3.14)}'); print(f'floor 4.14 = {math.floor(4.14)}')
# print(f'factorial = {math.factorial(6)}')
# # print(factorial(6))

# Отбрасывание дробной части:
# print(f'trunc 3.14 = {math.trunc(3.14)}');  print(f'trunc 4.14 = {math.trunc(4.14)}')
# print(f'int 3.14 = {int(3.14)}');   print(f'int 4.14 = {int(4.14)}')
# print(f'log = {math.log(3.14)}')
# print(f'log10 = {math.log10(3.14)}')

# -- Модуль числа
# x = int(input('Enter a number: '))
# print(abs(x))

# -- map. min. max. ...
# a, b, c, d, e = map(int, input('Enter 5 integer numbers: ').split())
# print(min(a, b, c, d, e))
# print(max(a, b, c, d, e))
# print(sum((a, b, c, d, e)))     # Функция sum требует двойных скобок ((--)).

# -- Katet & Hipotenusa
# a, b, = map(int, input('Enter 2 katets: ').split())
# c = ((a ** 2) + (b ** 2)) ** 0.5
# print(c)

# ___ Task 1 ____ В летний лагерь нужно отвезти n детей и m вожатых
# с помощью автобусов. Максимальная вместимость каждого автобуса 20 человек.
# Допишите программу для вычисления минимального числа автобусов,
# необходимых для перевозки детей вместе с вожатыми.
# Результат выведите в консоль в виде целого числа.
# n = int(input('Enter a number of Kids: '))
# m = int(input('Enter a number of Adults: '))
# print(math.ceil((n + m) / 20))

# ___ Task 2 ___ Гелевая ручка стоит x рублей. Сегодня магазин
# предоставляет скидку в 10% на каждую купленную ручку.
# Какое наибольшее количество таких ручек можно будет купить
# на 500 рублей? Результат выведите в консоль в виде целого числа.
pr_prev = float(input('Enter price before discount pr_prev =  '))
pr_new = pr_prev * 0.9
receipt = 500
number = math.trunc(receipt / pr_new)
print(f'Maximal number of pens is {number}')

