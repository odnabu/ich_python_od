# Semenov Artem
# 02.12.24
# Python 6: Условные операторы IF, ELIF, ELSE

# ___ IF ___
# Выполняет блоки кода по проверке условий.
# print (4 > 2)
# a = 5
# print (a < 0)

# x = 4
# if x < 0:   # Тело условного оператора IF (с отступом!)
#     # print(x)
#     x = -x
# print(x)

# x = -4
# if x < 0:   # Тело условного оператора IF (с отступом! = 1 Tab = 4 Space)
#     # print(x)
#     x = -x
# print(x)

# x = 4
# if x < 0:
#     x = -x
#     print(x)
# print(f'\nThe End')

# _NB!_ Поменять значения переменных МЕСТАМИ:
# a = float(input("Enter a = "))
# b = float(input("Enter b = "))
# if a < b:
#     a, b = b, a
# print(f'a = {a}, b = {b}')

# x = int(input("Enter x = "))
# if x >= -4 and x <= 10:
#     print(f'x = {x} got in interval.')
# print(f'x = {x} is out the interval.')

# x = int(input("Enter x = "))
# if -4 <= x <= 10:
#     print(f'x = {x} is in the interval.')
# print(f'x = {x} is out the interval.')

# x = int(input("Enter x = "))
# if x:   # FALSE will be when 0. In other cases - TRUE.
#     print(f'{x} The number is true')

# if True:
#     print("True")

# __ ELSE __
# list_marks = [1, 5, 2, 4, 3]     # Список или коллекция значений
# if 5 in list_marks:
#     print(f'Student will be lost the exam.')
# else:
#     print(f'Student will NOT be lost the exam.')

# list_marks = [1, 2, 4, 3]     # Список или коллекция значений
# if 5 in list_marks:
#     print(f'Student will be lost the exam.')
# else:
#     print(f'Student will NOT be lost the exam.')

# x = int(input("Enter x = "))
# if x < 0:
#     print(f'The number {x} is negative')
# else:
#     print(f'The number {x} is positive')

# x = int(input("Enter x = "))      # Четное или НЕчетное.
# if x % 2 == 0:    # % - Остаток от деления. Выводится не дробная часть, а часть от целого.
#     print("The number is Even")
# else:
#     print("The number is Odd")

# __ ELIF __ Лучше, чтобы в коде были ELIF вместо многих IF.
# x = int(input("Enter x = "))
# y = int(input("Enter y = "))
# if x > y:
#     print(f'{x} is greater than {y}')
# elif x < y:
#     print(f'{x} is less than {y}')
# # else:
# #     print(f'{x} is equal to {y}')
# elif x == y:
#     print(f'{x} is equal to {y}')
# else:
#     print(f'Error. The mission is impossible.')

# ___ SEPARATOR ___
# a = '1. Python'
# b = '2. C++'
# c = '3. Java'
# d = '4. JavaScript'
# print(a, b, c, d, sep='\n')     #  end='\n\n' - сепаратор в одной строке через пробел.
                                  #  sep='\n' - сепаратор по строкам.
# ask = int(input('Choose the course (from 1 ro 4): '))
# if ask == 1:
#     print(f'Your course is {a}.')
# elif ask == 2:
#     print(f'Your course is {b}.')
# elif ask == 3:
#     print(f'Your course is {c}.')
# elif ask == 4:
#     print(f'Your course is {d}.')
# else:
#     print(f'You didn\'t choose anything.')

# ___ Тернарный условный оператор ___
# Т.е. вложенный оператор. Используется, если условие простое.
a = 12; b = 7
# if a > b:
#     rez = a
# else:
#     rez = b
# print(rez)

# Тернарный оператор:
# rez = a if a > b else b
# print(rez)

# age = 10
# status = '+18' if age >= 18 else 'Not now 18.'
# print(status)

# Условный оператор ничего не возвращает. Просто проверяет равенство: TRUE or FALSE.
# d = if 5 > 2
# _NB!_ Тернарный условный оператор имеет 3 операнда и возвращает значение.

# _NB!_ Python чувствителен к регистру введения текстовых данных!
# rain = input(f'Is it rain? (Y or N): ').upper()
# if rain == 'Y':
#     wind = input(f'Is it wind? (Y or N): ').upper()
#     if wind == 'Y':
#         print(f'Stay at home!')
#     elif wind == 'N':
#         print('Take an umbrella!')
#     else:
#         print('Sorry, I don\'t understand.')
# elif rain == 'N':
#     print('Have a nice day!')
# else:
#     print('Sorry, I don\'t understand.')