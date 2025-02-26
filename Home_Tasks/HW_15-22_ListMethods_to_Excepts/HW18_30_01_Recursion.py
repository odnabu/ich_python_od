# Home Work 18, 30.01.25
# ___ 34: Recursion. ___
# Normal  \033[0;__;__m \033[m    or   BOLD  \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# f = 40; f = '.' * f; print(f) - Filler up to.
# print(f, f'\n...')
# print(' ' * 5, f'...') - Indentation in the output of the result
# while True:
#   ...
#   ask = input("\nDo you want to continue? (y/n): ").lower()
#   if ask == 'n':
#       break
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
print('.' * 120)


# _____________________________________    Task 1    _____________________________________
# Написать программу, вычисляющую факториал числа. Решить задачу с помощью рекурсии.

# __ Revised by Tanyia                          __ Video __:__:__ __ ?????????????????
# На логическом уровне:
# import time
# def factorial(n):
#     print(f'\tn = \033[1;33m{n}\033[m')
#     if n < 0:
#         return None
#     else:
#         print(f'Not < 0.  Next step --> ')
#     time.sleep(0.5)                                   # See Les34, "__ НЕ хвостовая рекурсия" + https://www.datacamp.com/tutorial/python-time-sleep?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720821&utm_adgroupid=157156375191&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=726015683208&utm_targetid=dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=9068529&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-row-p1_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-jan25&gad_source=1&gclid=Cj0KCQiAhvK8BhDfARIsABsPy4iXEZLV6LpCWA44wSh28KImm1LHOJjAXtSaAWHdspK_T-RqBA4h0SkaApCgEALw_wcB
#     if n == 0:
#         return 1
#     else:
#         print(f'Not == 0. Next step --> ')
#     time.sleep(0.5)
#     if n == 1:
#         print(f'\t\033[1;31mn == 1  |->\033[m')
#         return 1
#     else:
#         print(f'Not == 1. Next step --> ')
#     time.sleep(0.5)
#     # ------------------------------------
#     result = factorial(n - 1)
#     print(f'\tn = \033[1;34m{n}\033[m')
#     print(f' -->  factorial(n - 1):  (\033[1;34m{n}\033[m - 1)! = \033[1;32m{result}\033[m')
#     time.sleep(0.5)
#     print(f'\tn * result = n * factorial(n - 1):  \033[1;34m{n}\033[m * \033[1;32m{result}\033[m = {n * result}')
#     return n * result                           # Уменьшаем числ... __ VIDEO 0:0:43 __ ???????????????
# a = 3
# print(f'Factorial: {a}! = {factorial(a)}.')


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Логический уровень + ФИЗИЧЕСКИЙ - id(n):
# для понимания СТЕКовой структуры в организации хранения пошаговых результатов выполнения функции
# на локальном уровне, т.е. внутреннего процесса работы самой функции.

# See https://www.computer-museum.ru/histussr/rvm.htm :
# Любая ЭВМ в состоянии провести любые вычисления.
# Конкретное же протекание процессов вычисления проявляется лишь на уровне организации преобразований информации:
# задействуются конкретные регистры, коммутаторы, процессоры, линии передачи данных в определенном порядке и сочетании
# и т. д.). С этой точки зрения архитектура ЭВМ – это её структура в состоянии (процессе) реализации алгоритма,
# т. е. как бы ожившая структура. Философской основой такого представления является теория отражения,
# раскрывающая отображение категорий и явлений одной природы (числа, алгоритмы) на объекты другой природы
# (физические элементы, сигналы).

import time
import ctypes

def factorial(n):
    print(f'\tn = \033[1;33m{n}\033[m\t\033[37mid(n) = {id(n)}\033[m')
    if n < 0:
        return None
    else:
        print(f'Not < 0.  Next step --> ')
    time.sleep(0.5)
    if n == 0:
        return 1
    else:
        print(f'Not == 0. Next step --> ')
    time.sleep(0.5)
    if n == 1:
        print(f'\t\033[1;31mn == 1  |->\033[m')
        return 1
    else:
        print(f'Not == 1. Next step --> ')
    time.sleep(0.5)
    # ------------------------------------
    result = factorial(n - 1)
    print(f'\tn = \033[1;34m{n}\033[m\t\033[37mid(n) = {id(n)}\033[m')
    print(f' -->  factorial(n - 1):  (\033[1;34m{n}\033[m - 1)! = \033[1;32m{result}\033[m')
    time.sleep(0.5)
    print(f'\tn * result = n * factorial(n - 1):  \033[1;34m{n}\033[m * \033[1;32m{result}\033[m = {n * result}')
    print(f'\t\t\t\033[37mReverse id(n) - {ctypes.cast(id(n), ctypes.py_object).value}\033[m')   # inverse function of id(...) built-in function
    return n * result                           # Уменьшаем числ... __ VIDEO 0:0:43 __ ???????????????

a = 3
print(f'\n..................................\n'
      f'\t\tFactorial: {a}! = {factorial(a)}.'
      f'\n..................................\n')
# # print(f' Reverse id(n) - {ctypes.cast(id(n), ctypes.py_object).value}')       #  __ NB! __  INVERSE function of id(...) built-in function
                                                        # https://stackoverflow.com/questions/24815771/python-inverse-function-of-id-built-in-function

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# _____ Clear Code with Recursion for lms-platform as Homework _____
# def factorial(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))

# _____________________________________    Task 2    _____________________________________
# Напишите программу, которая использует рекурсию для вычисления суммы цифр числа. Создайте функцию sum_digits,
# которая принимает один аргумент - число, для которого нужно вычислить сумму цифр.
# Используйте условие выхода из рекурсии, когда число состоит из одной цифры. Выведите результат на экран.
#       Пример вывода:
#           Введите число: 12345
#           Сумма цифр числа 12345 равна 15
# numb = 12345
# print(str(numb))
# print(numb % 10)
# print(len(str(numb)))

# __ Loop WHILE __
# numb = 12345
# def sep_number(n):
#     sum_num = 0
#     while n > 0:
#         sum_num += n % 10
#         n = n // 10
#         # print(n % 10)
#     return sum_num
#
# print(sep_number(numb))

# __ Revised by Tanyia                          __ Video 1:10:00 __ ?????????????????
# import time
# numb = 12345
# def sep_number(n):
#     print(f'n = {n} (before n is not < 10). Next step --> ')
#     time.sleep(0.5)
#     if n < 10:
#         print(f'\tn < 10   because  n = {n}.  \033[31m|->\033[m \n'
#               f'================================================')
#         return n
#     time.sleep(1)
#     n_dev_10 = sep_number(n//10)            # Здесь и начинается рекурсия, тк вызывается обращение к самой функции.
#     print(f'n_dev_10 = {n_dev_10} --> \n-----------------------------------')
#     time.sleep(1)
#     result = n % 10 + n_dev_10
#     print(f'\tresult = n % 10 + n_dev_10 = {result}. --> ')
#     time.sleep(1)
#     return result
#
# print(f'Summ of digits in number {numb} is {sep_number(numb)}.')

# ----------------------- my testing
# sum_num = 0
# while numb > 0:
#     sum_num += numb % 10
#     numb = numb // 10
# print(sum_num)

# n = 25
# suma = 0
# while n > 0:
#     suma += n % 10
#     n = n // 10
#
# print("Сумма:", suma)
# -----------------------

# _____ Clear Code with Recursion for lms-platform as Homework _____
# numb = 12345
# def sep_number(n):
#     if n < 10:
#         return n
#     n_dev_10 = sep_number(n // 10)
#     result = n % 10 + n_dev_10
#     return result
#
# print(f'Summ of digits in number {numb} is {sep_number(numb)}.')
