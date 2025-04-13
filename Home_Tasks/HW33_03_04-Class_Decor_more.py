# Homework 33, 03.04.25
""" ___ 64-65: Magic Methods +++ Classes & Decorators - more """

# Video Practice 64: _______________________
# Video Lesson 65: ______________________
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
# Реализуйте класс Employee, представляющий сотрудника компании.
# Класс должен иметь статическое поле company с названием компании, а также методы:
#   +++ - __init__(self, name, position): конструктор, принимающий имя и должность сотрудника,
#   +++ - get_info(self): метод, возвращающий информацию о сотруднике в виде строки (имя, должность, название компании),
#   - set_company(cls, name): метод класса для изменения названия компании.
# Пример использования:
    # employee1 = Employee("John", "Manager")
    # employee2 = Employee("Alice", "Developer")
    # print(employee1.get_info())
# Вывод:
        # """
        # Name: John
        # Position: Manager
        # Company: ABC Company
        # """
    # Employee.set_company("XYZ Company")
    # print(employee2.get_info())
# Вывод:
        # """
        # Name: Alice
        # Position: Developer
        # Company: XYZ Company
        # """


class Employee:
    company = 'OD Inc.'

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        l = '10'
        return f'{'Name:':{l}} {self.name} \n{'Position:':{l}} {self.position} \n{'Company:':{l}} {Employee.company}'

    @classmethod
    def set_company(cls, company):
        cls.company = company           # Изменение статического поля класса напрямую.
    #  Объясни, пожалуйста, почему в этой части скрипта нет return в конце метода.
    # Оля, ты совершенно права — в методе set_company действительно нет return, и это абсолютно нормально.
    # Метод set_company изменяет значение статического поля company, относящегося ко всему классу Employee.
    # То есть, его задача — выполнить действие, а не вернуть результат.
    """ __ NB! __"""  # Если метод выполняет только действие, возвращаемое значение не требуется.
    #     В Python, если в методе или функции нет явного return, то он автоматически возвращает None.
    #     Это нормально для методов, которые изменяют состояние, но не должны возвращать никакого значения.
    # Почему здесь не нужен return:
    #   - Метод изменяет значение cls.company, и этого достаточно для выполнения его задачи.
    #   - Вызов метода делается ради изменения состояния, а не получения результата.


employee1 = Employee("John", "Manager")
employee2 = Employee("Alice", "Developer")
print('=' * 40, f'\n{employee1.get_info()}')
print('=' * 40, f'\n{employee2.get_info()}')

Employee.set_company("XYZ Company")
print('=' * 40, f'\n{employee2.get_info()}')



part_2 = '______ Task 2 _____'
""" ______  Task 2  ______________________________________________________________________________________________ """
# Реализуйте абстрактный базовый класс Shape (фигура), а от него унаследуйте классы Rectangle (прямоугольник) и
# Circle (круг). Класс Shape должен иметь абстрактный метод area, который должен быть реализован в каждом
# дочернем классе. Классы Rectangle и Circle также должны иметь метод perimeter для расчета периметра.
# Выведите площадь и периметр прямоугольника и круга на экран.
    # Пример использования:
    # rectangle = Rectangle(5, 3)
    # circle = Circle(2)
    # print(f"Rectangle area: {rectangle.area()}")              # Вывод: Rectangle area: 15
    # print(f"Rectangle perimeter: {rectangle.perimeter()}")    # Вывод: Rectangle perimeter: 16
    # print(f"Circle area: {circle.area()}")                    # Вывод: Circle area: 12.566370614359172
    # print(f"Circle perimeter: {circle.perimeter()}")          # Вывод: Circle perimeter: 12.566370614359172

# +++++++++++++++++++++++++++++++++++
from abc import ABC, abstractmethod
import  math
# +++++++++++++++++++++++++++++++++++

class Shape(ABC):
    pi = math.pi

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def area(self):
        return self.side_1 * self.side_2

    def perimeter(self):
        return 2 * (self.side_1 + self.side_2)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius ** 2

    def perimeter(self):
        return 2 * self.pi * self.radius


rectangle = Rectangle(5, 3)
circle = Circle(2)
print(f"Rectangle area: {rectangle.area()}")              # Вывод: Rectangle area: 15
print(f"Rectangle perimeter: {rectangle.perimeter()}")    # Вывод: Rectangle perimeter: 16
print(f"Circle area: {circle.area()}")                    # Вывод: Circle area: 12.566370614359172
print(f"Circle perimeter: {circle.perimeter()}")          # Вывод: Circle perimeter: 12.566370614359172

