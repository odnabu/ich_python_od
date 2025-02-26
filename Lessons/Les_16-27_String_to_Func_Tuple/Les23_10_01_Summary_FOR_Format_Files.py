# Semenov Artem
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 10.01.25
# Python 23: Summary - Loop FOR. Основы работы с файлами

# ###################################################################################################################

# ______ Review of previously covered material ______
# Символьный тип данных - неизменяемый, итерируемый (можно перебирать), индексируемый (последовательность) тип данных.
# создать литерал: ‘_’, ‘’_‘’ , str(_), ‘’’_‘’’’ .
# escape-последовательности: \t табуляция. \n переход на новую с троку.
# метод форматирования строк - format() и f строки.

# _____ Форматирование чисел _____
# print()
# print("1 - The number is: {:d}.".format(123))                     # целочисленные аргументы.
# print("2 - {:5d}.".format(12))                                    # ___ целые числа с минимальной шириной. ___
# print("3 - The float number is: {:f}.".format(123.4567898))       # аргументы с плавающей точкой.
# print("4 - {:8.3f}.".format(12.2346))                             # заполнение для чисел с плавающей точкой.
# print("5 - bin: {0:b}, oct: {0:o}, hex: {0:x}.".format(12))       # восьмеричный, двоичный и шестнадцатеричный формат.

# _____ Динамическое форматирование _____
# string = "{:{fill}{align}{width}}"                                  # динамический шаблон формата строки.
# print(string.format('cat', fill='*', align='^', width=5))     # передача кодов формата в качестве аргументов.
# term = 'Energy'
# print(f'Definition of {term:*^10}.')
# print(f'Definition of {'Force':*^10}.')
# num = "{:{align}{width}.{precision}f}"                              # динамический шаблон формата float.
# print(num.format(123.236, align='>', width=8, precision=2))   # передача кодов формата в качестве аргументов.


# __ Task 1 __
# Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз.
# Программа должна вывести 10 раз текст «Python is awesome!», каждый на отдельной строке.
# text = 'Python is awesome!'
# __ 1-st Variant __
# text = 'Python is awesome!'
# print(f'{text}\n' * 10)
# __ 2-nd Variant __
# text = 'Python is awesome!'
# for i in range(10):
#     print(text)

# __ Task 2 __ Home Task 11, Task 1
# Напишите программу, которая запрашивает у пользователя его имя, возраст и место
# проживания, а затем выводит их в следующем формате:
# "Привет, меня зовут 0. Мне 1} лет. Я живу в 2."
# Вместо 0, 1} и 2} подставьте соответствующие значения. Используйте метод format() для
# форматирования строки. Потом попробуйте использовать f-строку. Выведите результат на
# экран с помощью команды print.
#  ___ Solve Task 1, Home Task 11 from Sasha Golubenko ___
# name = input('Enter your name: ').strip().capitalize()
# age = input('Enter your age: ').strip()
# while True:
#     if not age.isdigit() or int(age) <= 3 or int(age) > 116:
#         print('\033[31mPlease enter a valid age.\033[m')
#         age = input('Enter your age again, please: ').strip()
#     else:
#         break
# city = input('Enter your city: ').strip().capitalize()
# print('_' * 70, '\n1-st Variant:')
# print('     Hello, my name is {}. I\'m {} years old. I\'m living now in {}.'.format(name, age, city))
# print('_' * 70, '\n2-nd Variant:')
# print(f'\n      Hello, my name is {name}. I\'m {age} years old. I\'m living now in {city}.')

# ###################################################################################################################

# ____________ Break, Continue in loop FOR + Список, Коллекция, Кортеж + Работа с файлами ____________
# Additional examples  from teacher Semenov Artem.
# See VIDEO to "Python 23: Summary session 6" from 10.12.25, timestamp: 1:19:15.
# Понятия Список, Коллекция, Кортеж -- смотри пример Example 6, 1-st Var, в частность результат его выполнения.
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
# Где:
# Список - в квадратных скобках ч/з запятую.
# Кортеж - коллекция, которая берется в круглые скобки. По сути кортеж - это набор из разных типов данных,
#          образованный последовательным объединением списков по индексам.
# Коллекции элементов / символов: 1) [ , ] - список - коллекция разнообразных элементов.
#                                 2) ( , ) - кортеж - тоже коллекция разнообразных элементов, только внутри списка.
#                                 3) ' ' or " " - строка - коллекция строчных символов.

# ___ Example 1 ___
# Найти первое число, которое делится на 5.
# numbers = [1, 8, 11, 22, 35, 40]
# for num in numbers:
#     if num % 5 == 0:
#         print(f"Нашли число, делящееся на 5: {num}")
#         break  # Прерываем цикл после нахождения первого подходящего числа

# ___ Example 2 ___
# Пропустить все отрицательные числа.
# numbers = [5, -1, 3, -7, 8]
# for num in numbers:
#     if num < 0:
#         continue  # Пропускаем итерацию для отрицательных чисел
#     print(f"Положительное число: {num}")

# ___ Example 3 ___
# Проверка на наличие четного числа.
# numbers = [1, 3, 5, 7]
# for num in numbers:
#     if num % 2 == 0:
#         print(f"Нашли четное число: {num}")
#         break
# else:
#     print("Четных чисел нет")

# ___ Example 5 ___
# Поиск первого четного числа, игнорируя отрицательные.
# numbers = [-3, -2, -1, 1, 3, 4, 7]
# for num in numbers:
#     if num < 0:
#         continue  # Игнорируем отрицательные числа
#     if num % 2 == 0:
#         print(f"Нашли четное число: {num}")
#         break
# else:
#     print("Четных чисел не найдено")

# ___ Example 6 ___ Function zip()
# Синтаксис:
# zip(iterable1, iterable2, ..., iterableN)
# iterable1, iterable2, ..., iterableN - одна или несколько итерируемых последовательностей.
# Возвращает итератор, который при каждом обращении выдает кортеж, содержащий элементы из каждой последовательности.
# Если последовательности разной длины, функция останавливается на самой короткой.
# __ 1-st Variant __
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# zipped = zip(names, ages)
# print(list(zipped))
# __ 2-nd Variant __ with loop FOR
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# for name, age in zip(names, ages):
#     print(f'{name} is {age} years old.')
# __ 3-d Variant __
# Если две коллекции, из которых одна короткая, другая длинная.
# Т.е. функция прерывается по короткому списку.
# short = [1, 2]
# long = [10, 20, 30]
# zipped = zip(short, long)
# print(list(zipped))


# ___ Example 7 ___ Работа с файлами - Менеджер контекста.
# with open('example_Shakespeare.txt', 'r', encoding='cp1251') as file:
#     content = file.read()
#     print(content)
# with open('example_Shakespeare.txt', 'w', encoding='cp1251') as file:
#     file.write("Кто предает себя же самого –")
# with open('example_Shakespeare.txt', 'a', encoding='cp1251') as file:
#     file.write("\nНе любит в этом мире никого!")

# ___ Example 8 ___ Работа с файлами - Менеджер контекста.
# with open("input.txt", "r", encoding="cp1251") as infile:
# # Считываем все строки из файла:
# lines = infile.readlines()
# # Объединяем строки, разделяя их пробелами, чтобы получить весь текст:
# full_text = " ".join(lines)
# # Разделяем текст на отдельные слова:
# words = full_text.split()
# # Переворачиваем список слов:
# words.reverse()
# # Открываем файл output.txt для записи:
# with open("output.txt", "w", encoding="cp1251") as outfile:
#     # Записываем каждое слово на новой строке
#     for word in words:
#         outfile.write(word + "\n")


# ###################################################################################################################

# file_path = input("Введите полный путь к файлу: ") # 'C:\Documents\Files\Hello.txt'
# with open(file_path, 'r', encoding='cp1251') as file:
#     content = file.read()
#     print(content)

# with open('example.txt', 'a+', encoding='cp1251') as file:
#     file.write("\nAppending new text.")
#     file.seek(0)
#     content = file.read()
#     print(content)






