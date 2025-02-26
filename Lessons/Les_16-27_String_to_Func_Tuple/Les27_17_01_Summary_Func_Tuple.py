# Semenov Artem
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 17.01.25
# Python 27: Summary - Базовые коллекции. Списки.

# ###################################################################################################################
print('.' * 120)

# ______ Review of previously covered material ______


# __ Task 1 __       NB!   РЕШИТЬ  ДРУГИМ  СПОСОБОМ
# Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14 × 10 в
# соответствии с образцом. Для вывода прямоугольника используйте цикл for.
# **********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********

# def draw_box():
#     w = 10
#     h = 14
#     for i in range(h):
#         print('*', end='')
# draw_box()

# def draw_box():
#     w = 10
#     h = 14
#     for i in range(h):
#         if i == 0 or i == h-1:
#             print('*' * w)
#         else:
#             print('*' + ' ' * (w - 2) + '*')
# draw_box()

# __ Task 2 __
# Напишите программу, выводящую следующий список:
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
# Последний элемент списка состоит из 26 символов z.
# __ With  loop WHILE
# def generate_list():
#     result = []
#     i = 0
#     while i < 26:
#         result.append(chr(ord('a') + i) * (i + 1))            # Получаем букву, начиная с 'a'
#         i += 1
#     return result
# print(generate_list())

# __ With loop  FOR
# def generate_list():
#     result = []
#     for i in range (26):
#         result.append(chr(ord('a') + i) * (i + 1))
#     return result
#
# print(generate_list())

# __ Task 3 __ HW13_14_01_Functions_Tuple.py -- Task 1
# Напишите программу, которая принимает два числа и возвращает их сумму и произведение в виде кортежа (sum, product).
# Используйте функцию для вычисления суммы и произведения. Выведите результат на экран с помощью команды print.
# __ 1-st Variant __
# def sumAndProduct(a, b):
#     summ = a + b
#     prod = a * b
#     return summ, prod
#
# result = sumAndProduct(3, 5)
# print(f"Сумма и произведение чисел: {result}")
# print(f"Сумма и произведение чисел: {result[0]}, {result[1]}")

# __ 2-nr Variant __
def sumAndProduct(numbers):
    sum_result = sum(numbers)
    p = 1
    for num in numbers:
        p *= num
    return sum_result, p

# n1, n2 = map(int, input('Enter 2 numbers by space: ').split())
# result = sumAndProduct([n1, n2])
# print(result)

# n1, n2, n3 = map(int, input('Enter 3 numbers by space: ').split())
# result = sumAndProduct([n1, n2, n3])
# print(result)

numbers = list(map(int, input("Введите числа через пробел: ").split()))
result = sumAndProduct(numbers)
print(result)
