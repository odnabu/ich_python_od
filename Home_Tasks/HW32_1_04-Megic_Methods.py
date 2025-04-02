# Home Work 32, 01.04.25
""" ___ 62-63: Magic Methods ___ """

# Video Lesson 62: ______________________
# Video Practice 63: _______________________
# Normal  \033[0;__;__m \033[m    or   BOLD  \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ############################################################################################################### """
# f = 40; f = '.' * f; print(f) - Filler up to.
# print(f, f'\n...')
# print(' ' * 5, f'...') - Indentation in the output of the result
# while True:                      # __ NB! __ See HW14_16_01_Func_Tuple.py, Task 2, "___ Clear code..."
#   ...
#   ask = input("\nDo you want to continue? (y/n): ").lower()
#   if ask == 'n':
#   # if user_n == 'Stop'.lower():
#       break
# def input_numb_list():            #  __ NB! __ See HW16_23_01_List_Matrix.py
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# print(f'\tName: {p.name:<10}')
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Ctrl+Alt+L - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------
print('.' * 130)

part_1 = '______ Task 1 _____'
""" ______  Task 1  ______________________________________________________________________________________________ """
# Реализовать класс Counter, который представляет счетчик. Класс должен поддерживать следующие операции:
#   - Увеличение значения счетчика на заданное число (оператор +=).
#   - Уменьшение значения счетчика на заданное число (оператор -=).
#   - Преобразование счетчика в строку (метод __str__).
#   - Получение текущего значения счетчика (метод __int__).
# Пример использования:
# counter = Counter(5)
# counter += 3
# print(counter)        # Вывод: 8
# counter -= 2
# print(int(counter))   # Вывод: 6

# class Counter:
#     def __init__(self, start_n):
#         self.start_n = start_n
#
#     def __add__(self, next_n):
#         return Counter(self.start_n + next_n)
#
#     def __sub__(self, next_n):
#         return Counter(self.start_n - next_n)
#
#     def __str__(self):
#         return f'{self.start_n}'
#
#     def __int__(self):
#         return self.start_n
#
# try:
#     a = 5
#     # method_add = Counter.__add__.__name__
#     # if method_add == "__add__":
#     #     display_name = "+"
#     # else:
#     #     display_name = method_add
#     counter = Counter(5)
#     print(f'{'Start Number :':<18} {counter}')
#     counter += 3
#     print(f'{'Next Value "+" :':<18} {counter}')
#     # print(f'{a} + {counter} = {a + counter}')
#     counter -= 2
#     print(f'{'Next Value "-" :':<18} {counter}')
#     # print(f'{a} + {counter} = {a - counter}')
#     counter += 4
#     print(f'{'Next Value "+" :':<18}', int(counter))
#     print(f'a * {int(counter)} = {a} * {int(counter)} = {a * int(counter)}')
# except TypeError as e:
#     notice = f'\033[31m{'ERROR:':<8}\033[m'
#     print(f'{notice}{e}')



""" ______  Task 2  ______________________________________________________________________________________________ """
# Реализовать класс Email, представляющий электронное письмо. Класс должен поддерживать следующие операции:
#   - Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
#   - Преобразование письма в строку (метод __str__)
#   - Получение длины текста письма (метод __len__)
#   - Получение хеш-значения письма (метод __hash__)
#   - Проверка наличия текста в письме (метод __bool__)
# Пример использования:
#   email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
#   email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
#   email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")
# print(email1)  # Вывод:
    # """
    # From: john@example.com
    # To: jane@example.com
    # Subject: Meeting
    # Hi Jane, let's have a meeting tomorrow.
    # """
# print(len(email2))        # Вывод: 24
# print(hash(email3))       # Вывод: -920444056
# print(bool(email1))       # Вывод: True
# print(email2 > email3)    # Вывод: True

class Email:


    def __init__(self, name, email):
        self.name = name
        self.email = email
