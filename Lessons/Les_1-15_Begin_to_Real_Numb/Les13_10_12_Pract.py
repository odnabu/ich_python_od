# Semenov Artem
# 10.12.24
# Python 13: Practices - Loop While.


# ______ Review of previously covered material ______

# __ Task 1 __
# Для заданного целого числа N подсчитать количество четных чисел, меньше или равных N.

# __ 1-st Variant __ With teacher.
# numb = int(input(f'Enter an integer number:\n numb = '))
# count = 0                           # Создаем счетчик четных чисел.
# i = 1                               # Первое число из последовательности всех чисел до numb.
# str_even = ''                       # Создаем сначала пустой список, куда будут выводиться все четные числа.
# while i <= numb:                    # Проверяем все числа, пока не дойдем до заданного numb.
#     if i % 2 == 0:                  # Проверяем конкретное условие.
#         str_even += str(i) + ' '    # Сразу же добавляем четное число в список.
#         count += 1                  # Когда условие выполняется, добавляем к счетчику 1.
#     i += 1                          # Переходим к следующему числу.
# print(count)                        # Печатаем счетчик.
# print(str_even)                     # Печатаем весь список.

# __ 2-nd Variant __ Oleksii Starodubov 9:24
# n = int(input("enter a number"))
# counter = 0
# while n > 0:
#     if n % 2 == 0:
#         counter += 1
#     n -= 1
# print(counter)

# __ Task 2 __ Fibonacci sequence.
# Вычислите n-е число ряда Фибоначчи с помощью цикла while. Что такое числа Фибоначчи?
# N = int(input("\nEnter a number:\nN = "))  # Номер числа в последовательности.
# f1, f2 = 0, 1       # Значения 1-го и 2-го числа последовательности Фибоначчи.
# count = 1           # Счетчик в цикле.
# while count <= N:
#     print(f1, end = ' ')
#     f1, f2 = (f2, f1 + f2)      # Можно ТУТ без скобок. НО! для кортежей нужны скобки.
#     count += 1
# print(f'\nThe {N} Fibonacci number is: {f2 - f1}')

# __ Task 3 __
# По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.
# Выведите показатель степени и саму степень.

# __ 1-st Variant __ With teacher.
# N = int(input("\nEnter a number:\nN = "))
# power = 0               # Счетчик для перебора степеней - показатель степени, начиная от 0.
# two_power_n = 1         # 2 в степени 0.
# while two_power_n <= N:
#     power += 1
#     two_power_n = 2 ** power
# print(f'Показатель степени 2: power = {power - 1}, \nстепень двойки, не превосходящая N: {2 ** (power - 1)}.')

# __ 2-nd Variant __ Hanna Kulykovska 10:29
# num = int(input("Enter your number: "))
# degree = 0 # степень 0
# res = 1 # это 2 в степени 0
# while res * 2 <= num:
#     degree += 1
#     res *= 2
# print(f"Your degree is {degree} and result of Your degree {res}")

# __ Task 4 __
# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
N = int(input('Enter an integer number:\nN = '))
i = 2
list_lnd = []                           # lnd - least natural divisor
while i < N:
    if N % i == 0:
        list_lnd.append(i)              # Накапливаем все делители числа, созданные циклом while.
    i += 1
print(f'The least natural divisor of your number is: {min(list_lnd)},\nwhat you can see from the next set of divisors: {list_lnd}.')


