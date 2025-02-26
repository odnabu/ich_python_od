# Semenov Artem
# 06.12.24
# Python 11: Loop While, Conditional operators IF / ELIF / ELSE.
import time         # Лучше ставить в самом начале кода.
import random

# ___ Review of previously covered material ___
# _ NB! _ ПОВТОРИТЬ!!!
#       - Тернарный условный оператор. См. презентацию Python 11: Summary 3.
#       - While - continue.
#       - While - else.
#       - while True = while "что угодно"
#       - While - pass.
#       - Pass.
#       - random.shuffle() - перемешивание. random.choice() - случайны выбор.

# ______ PRACTICE ______

# ___ Task 1 __
# Калькулятор, который работает вечно.
# while True:
#     a = float(input(f'Enter a number a = '))
#     b = float(input(f'Enter a number b = '))
#     operation = input(f'Enter a operation:\n + - plus, - - minus, * - multiplication, / - division : ')
#     if operation == '+':
#         result = a + b
#         print(f'The sum of numbers: {a} + {b} = {result}')
#     elif operation == '-':
#         result = a - b
#         print(f'The difference of numbers: {a} - {b} = {result}')
#     elif operation == '*':
#         result = a * b
#         print(f'The product of numbers: {a} * {b} = {result}')
#     elif operation == '/':
#         result = a / b
#         print(f'The quotient of numbers: {a} / {b} = {result}')
#             #     the division by 0.
#     else:
#         print('Invalid enter')
#     ask = input(f'Do you want to continue? (y/n): ').lower()
#     if ask == 'n':
#         break
# print('Thank you for using our program!')

# ___ Task 2 ___
# Угадывание числа. Из ДЗ.

# ___ Вариант Аллы - рабочий ___
# a = int(input('Диапазон ввода от 0 до ?: '))
# comp = random.randint(0,a) # В данном случае задуманное число будет одно
# start = time.time()
# user = int(input(f'Угадайте число от 0 до {a}: '))
# while user != comp:
#     if user > comp:
#         print('Ваше число больше загаданного!')
#     elif user < comp:
#         print('Ваше число меньше загаданного!')
#     user = int(input(f'Загадай число снова (введи число от 0 до {a}): '))
# else:
#     print('Вы угадали число!')
# end = time.time()
# result = end - start
# print(f'Вы угадали число за {round(result, 1)} секунд')

# ___ Мой вариант - NB! - ОТСТУПЫ В ЦИКЛЕ перед user = int(input... ___
lim_a = int(input('Укажите диапазон чисел от 0 до некоторого числа: limit = '))
comp = random.randint(0,lim_a)
start = time.time()
user = int(input(f'Угадайте число от 0 до {lim_a}: '))
while user != comp:
    if user > comp:
        print('Ваше число больше загаданного.')
    elif user < comp:
        print('Ваше число меньше загаданного.')
    user = int(input(f'Введите снова число от 0 до {lim_a}: '))
else:
    print('Вы угадали число!')
end = time.time()
time_inter = end - start
print(f'Вы угадали число за {round(time_inter)} секунд.')


# ___ Task 3 ___ Fibonacci numbers.
# n = int(input("\nEnter a number of numbers in Fibonacci sequence:\nn = "))  # Количество чисел в последовательности.
# f1, f2 = 0, 1       # Значения 1-го и 2-го числа последовательности.
# count = 0           # Счетчик в цикле.
# temp = 1
# while count < n:
#     if count == 0:
#         print(f'The first {n} Fibonacci numbers: ', f1, end='')       # Выводим числа через запятую в одну строку с помощью опции end=', ' в команде print.
#     else:
#         print(f', {f1}', end='')      # Не даем переходить на новую строку.
#     # f1, f2 = f2, f1 + f2
#     # Или такой вариант:f1, f2 = (f2, f1 + f2)
#     f1 = temp
#     temp = f2
#     f2 = f1 + f2
#     count += 1
# print(f'\n End of Fibonacci sequence: {f1}')

