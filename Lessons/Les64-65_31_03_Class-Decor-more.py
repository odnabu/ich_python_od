# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 31.03.25
 Python 64: Classes & Decorators - more.
 ################################################################################################################### """
from abc import abstractmethod

# Video Lesson 64: ------------.
# Video Practice 65: ------------.
# links:
#   - Presentation:
#   -
#
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter / Ctrl+Akt+L- Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------

print('.' * 120)

""" ___________________________________  Review of previously covered material  ___________________________________ """

# Video 64,



""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%_____________   Методы класса и   ____________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
                                                  статические методы                                                """
#

""" __________ Методы класса __________ """
#       ● Определяются с помощью декоратора @classmethod.
#       ● Позволяют работать с атрибутами класса.
#       ● Принимают первым аргументом класс, а не экземпляр класса.
#       ● Позволяют вызывать другие методы класса и выполнять другие операции, связанные с классом.

# ___ EXAMPLE __________________________________________________
# class Person:
#     name = "person"
#
#     def __init__(self):
#         self.name = "name"
#         print(Person.name)
#
#     @classmethod
#     def method(cls):
#         print('method', cls.name)
#
#     def obj_method(self):
#         print('obj method', self.name)
#
#     @staticmethod
#     def static_method():
#         print('static method')
#
# # p = Person()
# # p.method_name()
# Person.method()   # То же самое, что и 2 верхние строки.
# # Person.obj_method()
# Person.static_method()
# ___ END of Example __________________________________________________

""" __________ Статические методы __________ """
#       ● определяются с помощью декоратора @staticmethod.
#       ● Являются простыми функциями внутри класса
#       ● Не принимают дополнительных аргументов (класс или экземпляр класса)
#       ● Используются для группировки связанных операций, которые не требуют доступа к атрибутам класса или экземпляра.


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%______________     Защищенные и     _____________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
                                                   приватные атрибуты                                                """
# Video 64, 40:00

""" __________ Защищенные атрибуты __________ """
#       ● Предназначены для внутреннего использования внутри класса и его наследников.
#       ● Для обозначения: нотация с 1-ным подчеркиванием _ .

""" __________ Приватные атрибуты __________ """
#       ● Предназначены для полной инкапсуляции и не предназначены для доступа извне класса.
#       ● Для обозначения: нотация с 2-ным подчеркиванием __ .

# ___ EXAMPLE __________________________________________________
# class MyClass:
#     def __init__(self):
#         self._protected_attr = "Protected attribute"
#         self.__private_attr = "Private attribute"
#
# obj = MyClass()
# print(obj._protected_attr)          # Protected attribute.
# print(obj._MyClass__private_attr)   # Private attribute.
# ___ END of Example __________________________________________________


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%______________     Полиморфизм и     _____________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
                                                       наследование                                                """
# Video 64, 53:00

""" __________ Полиморфизм __________ """
# — позволяет объектам различных классов иметь одинаковый интерфейс, то есть поддерживать одни и те же методы или
# операции. Это дает возможность обрабатывать объекты разных классов с использованием общих функций и методов,
# что упрощает и унифицирует код.

""" __________ Наследование __________ """
# — позволяет создавать новые классы на основе уже существующих.

# ___ EXAMPLE __________________________________________________
# class Shape:
#     def area(self):
#         raise NotImplementedError("Method 'area' must be implemented")
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# shapes = [Rectangle(5, 10), Circle(3)]
# for shape in shapes:
#     print(shape.area())
# ___ END of Example __________________________________________________

""" __________ Базовый класс (родительский класс) __________ """
#  — это класс, от которого наследуется новый класс.

""" __________ Производный класс (дочерний класс) __________ """
#  — это класс, класс, который наследует базовый класс.

""" __________ Наследование в Python __________ """
#   ● Проблема ромбовидного наследования: производный класс наследует от нескольких классов, которые
#     имеют общего предка.
#   ● Решение проблемы: MRO (Method Resolution Order) - порядок разрешения методов.

# ___ EXAMPLE __________________________________________________
# class A:
#     def method(self):
#         print("A method")
#
# class B(A):
#     pass                        # Перейдет к С.
#     # def method(self):
#     #     print("B method")
#
# # class C(A):                   # Если С наследуется от А, то печатается С.
# class C:    #(A):               # А если как в этой строке, то будет напечатан А.
#     def method(self):
#         print("C method")
#
# class D(B, C):
#     pass
#
# obj = D()
# obj.method()        # B method
# print(D.__mro__)
# ___ END of Example __________________________________________________


""" ___ Создание пользовательских исключений ___ """
# Для создания пользовательского исключения необходимо определить новый класс, наследующийся от
# класса Exception или его подклассов.


""" ______  Task 1  ______________________________________________________________________________________________ """
# Video 65.
# Создать систему наследования для геометрических фигур: фигура, прямоугольник, квадрат, круг (можно добавить
# и другие плоские фигуры - например, параллелограмм, треугольник, прямоугольный треугольник).
# У всего определить площадь и периметр, а также __str__ (дополнительно можно добавить __repr__).
# Важно: где-то нужно переопределять методы, а площадь абстрактной фигуры не определена.
# Добавить метод, который выводит сообщение "Class: <class_name>".

# ++++++++++++++++++++++++++++++++++++
from abc import ABC, abstractmethod
import math
# ++++++++++++++++++++++++++++++++++++

class Figures(ABC):

    def class_name(self):
        return f'Class: {self.__class__.__name__}'

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Rectangle(Figures):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle with width {self.width} and height {self.height})'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

class Triangle(Figures):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt( p * (p - self.a) * (p - self.b) * (p - self.c) )

class Circle(Figures):
    pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'Circle with radius {self.radius}'

    def __repr__(self):
        return f'Circle with radius {self.radius}'

    def perimeter(self):
        return 2 * self.pi + self.radius

    def area(self):
        return self.pi * self.radius ** 2

figures_list  = [Rectangle(4, 5), Triangle(7, 8, 3), Circle(6)]
for figure in figures_list:
    print(f'--- {figure.class_name():-<30}')
    print(figure.perimeter())
    print(figure.area())
    print(figure)

print(figures_list)
