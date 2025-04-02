# Home Work 30, 21.03.25
""" ___ 56-59: OOP ___ """

# Video Lesson 58: ______________________
# Video Practice 59: _______________________
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
# Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------
print('.' * 130)

part_1 = '______ Task 1 _____'
""" ______  Task 1  ______________________________________________________________________________________________ """
# Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота) со значениями по умолчанию, а также методы
# calculate_area() для вычисления площади прямоугольника и calculate_perimeter() для вычисления периметра прямоугольника.
# Переопределить методы __str__, __repr__.
# Затем создайте экземпляр класса Rectangle и выведите информацию о нем, его площадь и периметр.

class Rectangle:
    # атрибуты width (ширина) и height (высота) со значениями по умолчанию:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # метод calculate_area() для вычисления площади:
    def area(self):
        return self.width * self.height

    # метод calculate_perimeter() для вычисления периметра:
    def perimeter(self):
        return 2 * (self.width + self.height)

    # Переопределить методы __str__, __repr__:
    def __str__(self):
        return f'Rectangle: width={self.width}  and  height={self.height}.'

    def __repr__(self):
        return f'Rectangle(width={self.width!r}, height={self.height!r})'

# rectangle_1 = Rectangle(7, 9)
# print(f'{'__ rectangle_1 __':_<50}', end='\n')
# print(rectangle_1)
# print(repr(rectangle_1))
# print(f'\n{'__ Area & Perimeter __':_<50}', end='\n')
# print(f'{'Area =':>15} {rectangle_1.area()}')
# print(f'{'Perimeter =':>15} {rectangle_1.perimeter()}\n')



""" ______  Task 2  ______________________________________________________________________________________________ """
# Создайте класс BankAccount для представления банковского счета. Класс должен иметь атрибуты account_number
# (номер счета) и balance (баланс), а также методы deposit() для внесения денег на счет и withdraw() для
# снятия денег со счета. Затем создайте экземпляр класса BankAccount, внесите на счет некоторую сумму и
# снимите часть денег. Выведите оставшийся баланс. Не забудьте предусмотреть вариант, при котором при снятии баланс
# может стать меньше нуля. В этом случае уходить в минус не будем, вместо чего будем возвращать сообщение
# "Недостаточно средств на счете".

class BankAccount:
    # атрибуты account_number (номер счета) и balance (баланс):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance

    # метод deposit() для внесения денег на счет:
    def deposit(self, amount):
        self._balance += amount

    # метод withdraw() для снятия денег со счета:
    def withdraw(self, amount):
        if amount >= self._balance:
            print(ValueError(f'\033[31mНедостаточно средств на счете.\033[m'))
            # raise ValueError(f'\033[31mНедостаточно средств на счете.\033[m')
        else:
            self._balance -= amount

    def __str__(self):
        return f'Balance of account {self.account_number} now is \033[32m{self._balance:,}\033[m.'

    def __repr__(self):
        return f'Bank Account(account_number={self.account_number!r}, balance={self._balance!r})'


# %%%%%%%%%%%%%%%%________  Модуль datetime в Python: Дата и Время  ________%%%%%%%%%%%%%%%%
# See link: https://highload.tech/modul-datetime-v-python/

# +++++++++++++++
import datetime
# +++++++++++++++
# # print(dir(datetime))                         # __ NB! __ ALL information about library datetime.
# print(f'{'__ ALL fields and methods in library datetime __':_<60}', end='\n')
# # __ NB! __ ALL information about library datetime in SEPARAT ROW.
# [print(f'{index} - {item}') for index, item in enumerate(dir(datetime))]     # enumerate() - https://highload.tech/for-list-iterate-range-python/
# print(f'{'-' * 60}', end='\n\n')

print(f'{'__ Library  DateTime __':_<60}', end='\n')
datetime_now = datetime.datetime.now()
print(f'{'Full format:':>20} {datetime_now}')
print(f'{'Day:':>20} {datetime_now.strftime('%d')}')
# ++++++++++++++++++++++++++
from datetime import date
# ++++++++++++++++++++++++++
datetime_today = date.today()
print(datetime_today)


# Вывод чисел с разделителями тысяч в Python: https://sky.pro/media/vyvod-chisel-s-razdelitelyami-tysyach-v-python/
# +++ https://ru.stackoverflow.com/questions/1281983/python-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4-%D1%87%D0%B8%D1%81%D0%BB%D0%B0-%D1%81-%D1%80%D0%B0%D0%B7%D0%B1%D0%B8%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC-%D0%BD%D0%B0-%D1%82%D1%80%D0%B8%D0%B0%D0%B4%D1%8B

print(f'\n{'__ Current Balance __':_<60}', end='\n')
deposit_23_03_25 = BankAccount(1234567890, 800_000)
print(deposit_23_03_25)
print(f'\033[31m{'__repr__':<10}\033[m', repr(deposit_23_03_25))

print(f'\n{'__ Deposit __':_<60}', end='\n')
try:
    pass
except NameError:
    pass

amount_d = 300_000
deposit_23_03_25.deposit(amount_d)
print(f'You\'ve deposit \033[33m{amount_d:,}\033[m to account.\n{deposit_23_03_25}')

print(f'\n{'__ Withdraw __':_<60}', end='\n')
amount_w = 100_000
deposit_23_03_25.withdraw(amount_w)
print(f'You withdraw \033[34m{amount_w:,}\033[m to account.\n{deposit_23_03_25}')

