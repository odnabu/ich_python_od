# Semenov Artem
# 12.12.24
# Python 14: Practices - Loop While & Modul DECIMAL

# ______ Review of previously covered material ______
# __ Task 1 __
# Определите сумму всех элементов последовательности, завершающейся числом 0.
# Числа, следующие за первым нулем, учитывать не нужно. Числа считываем с клавиатуры с помощью input().
# __ 1-st Var __
# sum_num = 0
# list_num = ''
# while True:
#     # sum_num = 0               # Если поставить тут sum_num = 0, а не перед циклом, то всегда цикл будет начинаться с 0.
#     num = int(input('Enter a number: num = '))
#     list_num = list_num + str(num) + ', '
#     sum_num += num
#     if num == 0:
#         break
#     print('The sum of your entered numbers is', sum_num)
# print(f'The sum of ALL your numbers {list_num} is {sum_num}', end = '.')

# В нашем коде в конце ставится точка посредством end, а Дмитрий говорил от том
# чтобы при выводе строки чисел после последнего числа не выводилась запятая.
# Hanna's Variant:
# num_sum = 0
# line = ''
# while True:
#     num = int(input('Enter a number: '))
#     if num == 0:
#         break
#     if line:                # Если строка не пустая, добавляем запятую перед числом
#         line += ', '
#     line += str(num)
#     num_sum += num
# print(f"Sum of Your numbers {line} is {num_sum}")

# __ 2-st Var __ ОШИБКА!!! т.к. Функцию int нельзя применить к списку!!!
# list_num = ''
# while True:
#     # sum_num = 0               # Если поставить тут sum_num = 0, а не перед циклом, то всегда цикл будет начинаться с 0.
#     num = int(input('Enter a number: num = '))
#     list_num = list_num + str(num)
#     if num == 0:
#         list_num = int(list_num)            # Функцию int нельзя применить к списку!!!
#         break
# print(f'The sum of ALL your numbers {list_num} is {sum_num}', end = ' .')

# __ 3-d Var __  WORK IT !!!
# list_num = ''
# while True:
#     # sum_num = 0               # Если поставить тут sum_num = 0, а не перед циклом, то всегда цикл будет начинаться с 0.
#     num = int(input('Enter a number: num = '))
#     list_num = list_num + str(num)
#     # n //=
#     if num == 0:
#         list_num1 = int(list_num)            # Функцию int нельзя применить к списку!!!
#         break
# print(f'The sum of ALL your numbers {list_num} is {list_num1}', end = ' .')

# list_num1st = list_num1 // 10 // 10 // 10
# print(list_num1st)
# list_num2nd = list_num1 % 10
# print(list_num2nd)

# __ Example to __ 3-d Var __
# number  = 123
# num = number
# total_summary = 0
# while number > 0:
#     digit = number % 10
#     total_summary += digit
#     number //= 10               # number = number = // 10
# print(f'The sum of ALL numbers in {num} = {total_summary}')


# ______ Modul DECIMAL ______ Функции и Классы ______

# Модуль - коллекция функция или классов.
# import math
# print(math.pi)                  # Ставим точку, чтобы вызвать методы которые есть в модуле math.
# print(math.ceil(3.14))          # Округление в большую сторону.
# print(math.floor(3.14))         # Округление в меньшую сторону.

# import math as m
# print(m.sqrt(9))
# print(int(8/4))

# from math import pi, e, ceil
# print(ceil(pi))
# floor = 7
# print(floor(pi))

# ______ COMPLEX NUMBERS ______
# NB! Пакета для комплексных чисел in Python НЕТ!

# В Python для работы с мнимыми числами используется встроенный тип complex, который позволяет создавать
# комплексные числа. Мнимую единицу (обозначаемую как iii или jjj) можно представить с помощью этого типа.
# Чтобы создать мнимую единицу, достаточно указать число 1j (или -1j для отрицательной мнимой единицы).

# # Мнимая единица в Python
# imaginary_unit = 1j
# # Пример использования мнимой единицы
# z = 3 + 4j  # Комплексное число 3 + 4i
# print(f"Мнимая единица: {imaginary_unit}")
# print(f"Комплексное число: {z}")
# print(f"Модуль комплексного числа: {abs(z)}")


# ______ Modul decimal. class Decimal ______
# Позволяет работать с фиксированной точностью.

# __ 1-st Case __
# from decimal import Decimal
# price = Decimal(input('Enter price: '))         # For example 19.99
# quantity = Decimal(input('Enter quantity: '))   # For example 3
# total = price * quantity
# total = total.quantize(Decimal('0.001'))        # указываем 2 знака после запятой - фиксированная точность для валюты.
# print(f'The total price is {total}.')

# __ 2-nd Case __
# from decimal import Decimal, getcontext
# getcontext().prec = 10          # Устанавливаем точность результата расчета.
# num1 = Decimal('1')
# num2 = Decimal('7')
# sum = num1 / num2
# print(sum)

# __ 3-d Case __
# При работе с числами с плавающей точкой (то есть float) мы сталкиваемся с тем, что в результате вычислений
# мы получаем не совсем верный результат:
# number = 0.1 + 0.1 + 0.1
# print(number)               # 0.30000000000000004
# Проблему может решить использование функции round(), которая округлит число. Однако есть и другой способ,
# который заключается в использовании встроенного модуля decimal.
# Ключевым компонентом для работы с числами в этом модуле является класс Decimal.
# Для его применения нам надо создать его объект с помощью конструктора.
# В конструктор передается строковое значение, которое представляет число:
# from decimal import Decimal
# # Создание Decimal из строки
# num_str = '3.141592653589793'
# decimal_num = Decimal(num_str)
# # Вывод значения
# print(decimal_num)
# # Однако нельзя смешивать в операциях дробные числа float и Decimal:
# number = Decimal("0.1")
# number = number + 0.1   # здесь возникнет ошибка

# __ 4-th Case __
# from decimal import Decimal
# # Создание Decimal из строки
# num_str = 3.141592653589793
# decimal_num = Decimal(num_str)
# # Вывод значения
# print(decimal_num)