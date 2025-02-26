# Semenov Artem
# 09.12.24
# Python 12: Real numbers.


# ___ Review of previously covered material ___

# __ Task 1 __ IF / ELIF / ELSE
# У вас есть целое число X. Нужно написать программу, которая напечатает разницу между числом 21 и X,
# если X<=21 и напечатает удвоенную разницу 21 и X в противном случае.
# x = int(input(f'Enter an integer number: '))
# if x <= 21:
#     print(21 - x)
# else:
#     print(2 * (21 - x))

#  ________ Тернарный условный оператор ________
#  __ 1-sn Variant __
# rez = print(21 - x) if x <= 21 else print(2 * (21 - x))
#  __ 2-nd Variant __
# rez = (21 - x) if x <= 21 else (2 * (21 - x))
# print(rez)
# print(f'The real number is: {rez + 1}')

# __ Task 2 __
# У вас есть целое число X. Напишите программу, которая печатает разницу 100 и X,
# если X больше 10 и меньше 100, и печатает X - в противном случае.
# x = int(input(f'Enter an integer number: '))
# if 10 < x < 100:
#     print(100 - x)
# else:
#     print(x)

#  Тернарный условный оператор: 1-sn Variant
# rez = print(100 - x) if 10 < x < 100 else print(x)
# __ or __
# rez = print(100 - x) if x < 100 and x > 10 else print(x)
#  Тернарный условный оператор: 2-nd Variant
# rez = print((100 - x) if 10 < x < 100 else (x))

# __ Task 1 __ Loop While
# Напишите программу, которая запрашивает у пользователя целое положительное число и проверяет, является ли оно простым.
# Простое число - это число, которое делится только на 1 и на само себя без остатка. Используйте цикл while и
# проверку деления числа на все числа от 2 до N-1 для решения задачи. Выведите соответствующее сообщение на экран
# с помощью команды print.

# __ 1-st Variant __
# x = int(input(f'Enter an integer number: '))
# i = 2
# while i < x:
#     if x % i == 0:
#         print(f'{x} is NOT a prime number.')
#         break
#     else:
#         i += 1
# else:
#     print(f'{x} is a Prime number.')

# __ 2-nd Variant __
# x = int(input(f'Enter an integer number: '))
# if x <= 1:
#     print(f'{x} должно быть больше 1.')
# else:
#     is_true = True
#     i = 2
#     while i < x:
#         if x % i == 0:
#             is_true = False
#             break
#         i += 1
#     if is_true:
#         print(f'{x} is a Prime number.')
#     else:
#         print(f'{x} is NOT a Prime number.')

# ___ Task 3 ___ CONTINUE
# __ 1-st Variant __
# x = int(input(f'Enter an integer number: '))
# count = 0
# while count < x:
#         if count == 5:
#             continue
#         print(f'{count}')
#         count += 1

# __ 2-nd Variant __
# x = int(input(f'Enter an integer number: '))
# count = 0
# while count < x:
#     count += 1          # Если count += 1 поставить здесь (до условия), то 3 просто выкинется из списка.
#     if count == 3:
#         continue
#     print(f'{count}')


# ______ REAL NUMBERS in Python ______

# binary_numb = input('Enter a binary number: ')  # 00000101.000000
# print(f'{int(binary_numb, 2)}')