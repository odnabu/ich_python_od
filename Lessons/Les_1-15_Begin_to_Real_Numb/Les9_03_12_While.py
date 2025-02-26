# Semenov Artem
# 03.12.24
# Python 9: Практика + цикл While

# ___ Review of previously covered material ___
# num1 = int(input("\nEnter a 1-st number: "))
# num2 = int(input("\nEnter a 2-nd number: "))
# if num1 > num2:
#     print(f'\nThe number {num1} is greater than the number {num2}: {num1} > {num2}.')
# elif num2 > num1:
#     print(f'\nThe number {num1} is less than the number {num2}: {num1} < {num2}.')
# else:
#     print(f'\nThe number {num1} is equal the number {num2}: {num1} = {num2}.')
# print(f'\nError in entrences numbers.')

# ______ Loop WHILE ______
# while True:     # Цикл ЗДЕСЬ выполняется вечно. Для его остановки нужно нажать кнопку в PyCharm.
#     num1 = int(input("\nEnter a 1-st number: "))
#     num2 = int(input("Enter a 2-nd number: "))
#     if num1 > num2:
#         print(f'\nThe number {num1} is greater than the number {num2}: {num1} > {num2}.')
#     elif num2 > num1:
#         print(f'\nThe number {num1} is less than the number {num2}: {num1} < {num2}.')
#     else:
#         print(f'\nThe number {num1} is equal the number {num2}: {num1} = {num2}.')
#     print(f'\nError in entrances numbers.')

# ___ Простое прерывание цикла ___
# while True:     # Цикл ЗДЕСЬ прерывается командой break. _NB!_ ОТСТУПЫ в теле цикла!
#     num1 = int(input("\nEnter a 1-st number: "))
#     num2 = int(input("Enter a 2-nd number: "))
#     if num1 > num2:
#         print(f'\nThe number {num1} is greater than the number {num2}: {num1} > {num2}.')
#     elif num2 > num1:
#         print(f'\nThe number {num1} is less than the number {num2}: {num1} < {num2}.')
#     else:
#         print(f'\nThe number {num1} is equal the number {num2}: {num1} = {num2}.')
#     print(f'\nError in entrances numbers.')
#     ask = input("\nDo you want to continue? (y/n): ").lower()
#     if ask == 'n':
#         break

# ___ Сумма последовательности ___
# Работа цикла называется ИТЕРАЦИЕЙ.
num = int(input("\nEnter a number: "))  # Конечное число в сумме.
s = 0   # Для хранения вычисленной суммы.
i = 1   # Значение текущего слагаемого.
while i <= num:     # Заголовок (тело) цикла.
    s += i      # s=s+i
    i += 1      # i=i+1
    print(s)
print(f'Цикл завершен. Сумма s = {s}.')

# ___ Цикл с диапазоном ___
# num = int(input("\nEnter a number: "))  # Количество чисел в сумме.
# s = 0   # Для хранения вычисленной суммы.
# i = 1   # Значение текущего слагаемого.
# while i<= num and i <= 50:
#     s += i      # s=s+i
#     i += 1      # i=i+1
#     print(s)
# print(f'Цикл завершен. Сумма s = {s}.')

# __ Ряд чисел убывающей последовательности __
# n = -10
# i = -1
# while i >= n:
#     print(i)
#     i -= 1

# __ Password __
# pass_true = 'od'
# ps = ''
# while ps != pass_true:
#     ps = input('\nEnter your password: ')
# print(f'Password is TRUE. Code is done.')

# _NB!_ Home Task: задача с ограничением количества введений пароля.

# __ Все числа, кратные 3 - это перебор чисел от __ и до __.
# num = int(input(f'\nEnter a number: '))
# i = 1
# while i <= num:
#     if i % 3 == 0:
#         print(i)
#     i += 1      # i=i+1

# __ Вечный цикл, который можно прервать только извне __
# i = 0
# while True:
#     i += 1
# print('End loop.')

# __ Прерывание цикла командой break __
# i = 0
# while True:
#     i += 1
#     break
# print('End loop.')

# ___ Operator CONTINUE ___
# s = 0
# d = 1
# while d != 0:
#     d = int(input(f'Enter an integer number: '))
#     if d % 2 == 0:
#         continue
#     s += d      # Будет считать сумму только нечетных чисел. Четные игнорирует.
#     print(f's = {s}.')
# print(f'End loop.')

# ___ Operator ELSE ___
# # s = 1/2 + 1/3 + 1/4 + 1/5 + 1/0 - Цикл должен прерваться, если появляется 1/0.
# s = 0
# i = -10
# while i < 100:
#     if i == 0:
#         break
#     s += 1/i
#     i += 1
# else:
#     print(f'Sum is right.')
# print(f's = {s}')

# s = 0
# i = -10
# while i < -1:
#     if i == 0:
#         break
#     s += 1/i
#     i += 1
# else:       # Если цикл выполняется правильно, то дальше выполняется условие else.
#     print(f'Sum is right.')
# print(f's = {s}')

# ___ Module TIME ___
import time     # Лучше вводить в начале кода.
import random
# start_time = time.time()
# num1 = int(input('Enter an integer 1-st number: '))
# num2 = int(input('Enter an integer 2-nd number: '))
# summ = int(input(f'{num1} + {num2} =  '))
# print(summ)
# end_time = time.time()
# result_time = end_time - start_time
# print(round(result_time, 2))

# ___ Module RANDOM ___
# s = random.randint(1, 10)       # Генерация ЦЕЛЫХ чисел.
# print(s)

# a = random.random()       # Генерация ДРОБНЫХ чисел от 0 до 1.
# print(round(a, 2))

# b = random.randrange(1, 20, 3)    # Start, End. Step.
# print(b)

# list_names = ['Bob', 'Jim', 'Helga', 'John']        # Случайный выбор из списка.
# one_name = random.choice(list_names)
# print(one_name)