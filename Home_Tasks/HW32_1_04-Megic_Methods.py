# Home Work 32, 01.04.25
""" ___ 62-63: Magic Methods ___ """

# Video Practice 63: _______________________
# Video Lesson 62: ______________________
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
#     # def __init__(self, start_n, name):
#     def __init__(self, start_n):
#         self.start_n = start_n
#         # self.name = name
#
#     def __add__(self, next_n):
#         return Counter(self.start_n + next_n)       # ПЕРЕОПРЕДЕЛЕНИЕ метода на новое поведение.
#
#     def __sub__(self, next_n):
#         return Counter(self.start_n - next_n)
#
#     def __str__(self):
#         return f'{self.start_n}'
#
#     def __int__(self):
#         return int(self.start_n)        # здесь ОБЯЗАТЕЛЬНО НУЖНО int( ), тогда нужно добавить raise<TupeOfError>
#
# try:
#     a = 5
#     # method_add = Counter.__add__.__name__
#     # if method_add == "__add__":
#     #     display_name = "+"
#     # else:
#     #     display_name = method_add
#     counter = Counter(5)
#     # counter = Counter(5, 'positive counter')
#     print(type(counter))
#     print(f'{'Start Number :':<18} {counter}')
#     counter += 3
#     print(f'{'Next Value "+" :':<18} {counter}')
#     print(counter.__int__())
#     print(type(counter.__int__()))
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


part_2 = '______ Task 2 _____'
""" ______  Task 2  ______________________________________________________________________________________________ """
# Реализовать класс Email, представляющий электронное письмо. Класс должен поддерживать следующие операции:
#   +- Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
#   +- Преобразование письма в строку (метод __str__)
#   +- Получение длины текста письма (метод __len__)
#   +- Получение хеш-значения письма (метод __hash__)
#   - Проверка наличия текста в письме (метод __bool__)
# Пример использования:
#   email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
#   email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
#   email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")
# print(email1)
    # Вывод:
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

# # ++++++++++++++++++++++++++++
# import functools
# from datetime import datetime
# # ++++++++++++++++++++++++++++
#
# @functools.total_ordering
class Email:

    def __init__(self, from_mail: str, to_mail: str, subject: str, message: str, date_mail: str) -> None:
        self.from_mail = from_mail
        self.to_mail = to_mail
        self.subject = subject
        self.message = message
        self.date_mail = date_mail
        # self.date_mail = datetime.strptime(date_mail, "%Y-%m-%d")

    # Design of the letter text:
    def __str__(self):
        return (f'\033[34m{'"' * 3}{'  Email  ':"<48}\033[m\n'
                f'|\t{'From:':<10}{self.from_mail:<20}{'':>16}|\n'
                f'|\t{'To:':<10}{self.to_mail:<20}{'':>16}|\n'
                f'|\t{'Subject:':<10}{self.subject:<20}{'':>16}|\n'
                f'|{'|':>50}\n'
                f'|  \x1B[3m{self.message:<40}\x1B[0m{'':<7}|\n'
                f'|{self.date_mail:>47}{'|':>3}\n'
                f'\033[34m{'"' * 51}\033[m')

    # Comparison of Dates (операторы <, >, <=, >=, ==, !=):
    def __lt__(self, other):
        return True if self.date_mail < other.date_mail else False

    def __gt__(self, other):
        return True if self.date_mail > other.date_mail else False

    def __lte__(self, other):
        return True if self.date_mail <= other.date_mail else False

    def __gte__(self, other):
        return True if self.date_mail >= other.date_mail else False

    def __eq__(self, other):
        # return True if self.date_mail == other.date_mail else False
        return True if self.date_mail == other.date_mail else False

    def __ne__(self, other):
        return True if self.date_mail != other.date_mail else False

    # Получение длины текста письма (метод __len__):
    def __len__(self):
        return len(self.message)

    # Получение хеш-значения письма (метод __hash__):
    def __hash__(self):
        return hash((self.from_mail, self.to_mail, self.subject, self.message))

    # Проверка наличия текста в письме (метод __bool__):
    def __bool__(self):
        return True if len(self.message) > 0 else False

# ______ Print Email ______
email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")
print(email2)

# Количество повторений символа для разделителей:
rep = 51

# Функция для вывода имен переменных, использованных в выражении.
# Пример отсюда: https://ru.stackoverflow.com/questions/1549255/%D0%9A%D0%B0%D0%BA-%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE-%D0%B2%D1%8B%D0%B2%D0%B5%D1%81%D1%82%D0%B8-%D0%BD%D0%B0-%D1%8D%D0%BA%D1%80%D0%B0%D0%BD-%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9.
def get_var_name(var):
    variables = globals()
    for name, value in variables.items():
        if value is var:
            return name
    return None

# print(get_var_name(email_1st))

# ______ Date ______
email_1st = email1
email_2nd = email2
# print(f'Dates: \t{get_var_name(email_1st)} - {email_1st.date_mail}, '
#       f'\t{get_var_name(email_2nd)} - {email_2nd.date_mail}.\n{'-' * rep}')

# ___ Comparison of emails dates (operators <, >, <=, >=, ==, !=) ___
# date_compare = email_1st.date_mail < email_2nd.date_mail
# date_compare = email_1st.date_mail > email_2nd.date_mail
# date_compare = email_1st.date_mail <= email_2nd.date_mail
# date_compare = email_1st.date_mail >= email_2nd.date_mail
date_compare = email_1st.date_mail == email_2nd.date_mail
# date_compare = email_1st.date_mail != email_2nd.date_mail
date_result = f'\033[32m{date_compare}\033[m' if date_compare is True else f'\033[31m{date_compare}\033[m'
print(date_result, f'-->  Result of checking email dates:\n'
                    f'\t{get_var_name(email_1st):>10}: {email_1st.date_mail}, '
                    f'{get_var_name(email_2nd):>10}: {email_2nd.date_mail}.\n{'-' * rep}')

# ___ len() ___
print(f'Email contains {len(email_1st.message)} symbols.')

# ___ hash() ___
print(hash(email_1st))

# ___ bool() ___
print(bool(email_1st), f'--> email contains text.')
