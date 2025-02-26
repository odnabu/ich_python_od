# Semenov Artem
# 05.12.24
# Python 10: Практика + цикл While

# ___ Review of previously covered material ___

# Fibonacci sequence - SIMPLE VARIANT -
n = int(input("\nEnter a number of numbers in Fibonacci sequence:\nn = "))  # Количество чисел в последовательности.
f1, f2 = 0, 1       # Значения 1-го и 2-го числа последовательности.
count = 0           # Счетчик в цикле.
while count < n:
    if count == 0:
        print(f'The first {n} Fibonacci numbers: ', f1, end='')       # Выводим числа через запятую в одну строку с помощью опции end=', ' в команде print.
    else:
        print(f', {f1}', end='') # Не даем переходить на новую строку.
    f1, f2 = f2, f1 + f2
    count = count + 1
print()

# # Fibonacci sequence - Hanna's VARIANT -
# while True: #
#     num = int(input("Enter a number: ")) # Запрос ввода числа от пользователя
#     a, b = 0, 1 #Инициализация первых двух чисел последовательности Фибоначчи
#     count = 0 #Счётчик, который будет отслеживать количество уже сгенерированных чисел
#     print("First", num, "numbers of Fibonacci series:", end="") #Выводит заголовок перед последовательностью end="" предотвращает автоматический перевод строки после заголовка
#     while count < num: # Внутренний цикл для генерации чисел Фибоначчи. Будет работать, пока количество сгенерированных чисел меньше запрошенного
#         print(a, end="" if count == num - 1 else ", ") # Выводит текущее число последовательности end="" для последнего числа (без запятой)", " между числами (с запятой)
#         a, b = b, a + b #Ключевая строка для генерации чисел Фибоначчи
#         count += 1
#     ask = input("\nWould You like to enter another number (y/n)?:")
#     if ask == "n":
#         print("Goodbye")
#         break

# ___ Task 1 ___
# 1. Даны два целых числа a и b. Напишите программу, которая
# находит большее из двух чисел и печатает сообщение, какое число больше.
# a, b = map(int, input("Enter your pare of integer numbers: ").split(','))
# print(a, b)
# a = int(input('Enter a 1-st integer numbers: a = '))
# b = int(input('Enter a 2-nd integer numbers: b = '))
# if a > b:
#     print(f'Number {a} is greater than {b}.')
# elif a == b:
#     print(f'Number {a} is equal to number {b}.')
# else:
#     print(f'Number {a} is less than number {b}.')

# ___ Task 2 ___
# Напишите программу, которая находит наибольшее из трех чисел.
# a = int(input('Enter a 1-st integer numbers: a = '))
# b = int(input('Enter a 2-nd integer numbers: b = '))
# c = int(input('Enter a 3-nd integer numbers: c = '))
# # print(max(a, b, c))
# if b < a > c:
#     print(f'Number {a} is greater than {b} and {c}.')
# elif a < b > c:
#     print(f'Number {b} is greater than {c} and {b}.')
# else:
#     print(f'Number {c} is greater than {a} and {b}.')

# ___ Task 3 ___
# Есть логическая переменная  weekday. Напишите программу, которая выводит
# сообщение “рабочий день”, если переменная истинна и сообщение “выходной” - если ложна.

# __ 1-st Variant:
# weekday = bool(int(input(f'1 - Рабочий день, 0 - Выходной день: ')))
# if weekday:                # Можно без weekday == 1 - т.к. всё пустое и 0 - FALSE.
#     print(f'Рабочий день.')
# else:
#     print(f'Рабочий день.')

# __ 2-st Variant:
# weekday = int(input(f'1 - Рабочий день, 2 - Выходной день: '))
# if weekday == 1:                # Можно без weekday == 1 - т.к. всё пустое и 0 - FALSE.
#     print(f'Рабочий день.')
# elif weekday == 2:
#     print(f'Выходной день.')
# else:
#     print(f'Error.')

# ___ Task 4 ___
# У нас есть две логические переменные: isWeekday, isVacation (выходной день и каникулы).
# Они могут принимать разные значения, всего 4 комбинации: true - true, true - false, false - false, false - true.
# Есть правило: мы можем поспать, если день не рабочий или мы на каникулах.
# # Напишите программу, которая в зависимости от значений двух переменных печатает, можем ли мы поспать или нет.
# То есть для значений isWeekday = False и isVacation = False программа должна печатать “можете поспать”.

# __ 1-st Variant
# isWeekday = bool(int(input(f'Введите 1, если рабочий день, и НЕрабочий = 0: ')))
# isVacation = bool(int(input(f'Введите 1, если каникулы, и работа = 0: ')))
# if isWeekday == False or isVacation ==True:
#     print(f'Schlaf schoen :-) ')
# else:
#     print(f'Arbeiten!.')

# __ 2-nd Variant
isWeekday = bool(int(input(f'Введите 1, если рабочий день, и НЕрабочий = 0: ')))
isVacation = bool(int(input(f'Введите 1, если каникулы, и работа = 0: ')))
if not isWeekday or isVacation:
    print(f'Schlaf schoen :-) ')
else:
    print(f'Arbeiten!.')