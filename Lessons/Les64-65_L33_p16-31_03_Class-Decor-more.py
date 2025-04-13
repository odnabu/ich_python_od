# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 31.03.25
 Python 64: Classes & Decorators - more.
 ################################################################################################################### """

# Video Lesson 64: https://player.vimeo.com/video/1070968789?h=ce1a048823.
# Video Practice 65: https://player.vimeo.com/video/1070993158?h=ef72e3eff4.
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
#       ● Определяются с помощью декоратора @classmethod. - see detailed in https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/dekorator-classmethod/
#       ● Позволяют работать с атрибутами класса.
#       ● Принимают первым аргументом класс, а не экземпляр класса.
#       ● Позволяют вызывать другие методы класса и выполнять другие операции, связанные с классом.

# ___ EXAMPLE __________________________________________________
# class Person:
#     name = f'\033[32mStatic attribute - Person\033[m'      # Статический АТРИБУТ класса.  Смотри здесь:
#                                             # https://highload.tech/kak-sozdavat-klassy-v-python-so-znaniem-dela-razbiraem-na-primerah/
#     def __init__(self):
#         self.name = "NAME"                  # Атрибут name — динамический.
#         print(Person.name)
#
#     # ВСТРОЕННЫЙ Декоратор метода -- преобразует обычный метод в метод класса в данном классе:
#     @classmethod                  # See here https://sky.pro/media/osnovy-raboty-s-classmethod-i-staticmethod-v-python/
#     def method(cls):              # Первым аргументом метода всегда является сам класс (обычно обозначается как cls),
#                                   # а не экземпляр класса (self).
#         print(f'\033[40;1;35m@classmethod: Method -->\033[m', cls.name)     # cls.name - выведет имя класса, точнее то,
#                                                                             # что стоит в статическом АРГУМЕНТЕ.
#
#     def obj_method(self):
#         print('obj method', self.name)
#
#     # Статический метод не получает НЕявный первый аргумент self класса: https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/dekorator-staticmethod/
#     # Проще говоря, декоратор @staticmethod превращает метод, определенный внутри класса, в обычную функцию,
#     # которая не имеет доступа к экземпляру класса self, поэтому ее можно вызывать без создания экземпляра класса.
#     # Следовательно, статический метод может быть вызван либо в классе C.f(), либо в экземпляре класса C().f().
#     @staticmethod
#     def static_method():
#         print('- Static method -')
#     # Метод  изменяет значение статического поля, относящегося ко всему классу. То есть, его задача —
#     # выполнить действие, а не вернуть результат.
#     """ __ NB! __"""  # Если метод выполняет только действие, возвращаемое значение не требуется.
#     # +++ Еще здесь хороший вопрос: "Суть метода @classmethod, @staticmethod, @property".
#     # https://ru.stackoverflow.com/questions/1389201/%D0%A1%D1%83%D1%82%D1%8C-%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D0%B0-classmethod-staticmethod-property
#
#
#
# p = Person()        # Выводит статический АТРИБУТ класса. See link above.
# # p.method()        # Можно применять к ЭКЗЕМПЛЯРУ класса, а можно и к самому классу, т.к. тогда вызывается @classmethod -->
# Person.method()     # --> результат будет как после выполнения строки выше.
# # Person.obj_method()
# Person.static_method()
# ___ END of Example __________________________________________________

""" __________ Статические методы __________ """        # Смотри пример выше /\.
# +++ https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/dekorator-staticmethod/
# +++ Что такое статический метод в классах Python и зачем нужен:
#     https://docs-python.ru/tutorial/klassy-jazyke-python/takoe-staticheskij-metod-klassah-zachem-nuzhen/
#       ● определяются с помощью декоратора @staticmethod.
#       ● Являются простыми функциями внутри класса
#       ● Не принимают дополнительных аргументов (класс или экземпляр класса)
#       ● Используются для группировки связанных операций, которые не требуют доступа к атрибутам класса или экземпляра.

# ___ EXAMPLE __________________________________________________

# ___ END of Example __________________________________________________


# FACIT, see here: https://stepik.org/lesson/794698/step/1?discussion=8506060&unit=797450
# 1) методы класса - это методы, к которым используется декоратор @classmethod, они работают только с атрибутами
#    самого класса через параметр cls. Они не имеют доступа к атрибутам экземпляра класса.
# 2) методы экземпляра класса - это методы, которые работают с атрибутами экземпляра класса через параметр self.
#    Также у них есть доступ к атрибутам класса, к которым следует обращаться также через self. В методах экземпляра класса можно вызывать статические методы и методы класса (через self).
# 3) статические методы - это методы, к которым используется декоратор @staticmethod, у которых нет доступа к
#    атрибутам экземпляра класса, формально могут "видеть" атрибуты класса через имя самого класса, но это не
#    рекомендуется делать. Это методы, которые выполняют "сервисную" функцию для данного класса (например,
#    всякие вычисления). У них нет параметра self и cls. Вызывать эти методы вне класса можно через имя класса.



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
#   операции. Это дает возможность обрабатывать объекты разных классов с использованием общих функций и методов,
#   что упрощает и унифицирует код.

""" __________ Наследование __________ """
# — позволяет создавать новые классы на основе уже существующих.

# ___ EXAMPLE __________________________________________________
# class Shape:
#     name = "shape"
#
#     def area(self):
#         print("Method 'area' must be implemented")
#         # raise NotImplementedError("Method 'area' must be implemented")
#
#
# class Rectangle(Shape):
#     name = "rect"
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     # def area(self):
#     #     return 3.14 * self.radius ** 2
#
# shapes = [Rectangle(5, 10), Circle(3)]
# for shape in shapes:
#     print(shape.area())
#     print(shape.name)
# ___ END of Example __________________________________________________

""" __________ Базовый класс (родительский класс) __________ """
#  — это класс, от которого наследуется новый класс.

""" __________ Производный класс (дочерний класс) __________ """
#  — это класс, класс, который наследует базовый класс.

""" __________ Наследование в Python __________ """
#   ● Проблема ромбовидного наследования: производный класс наследует от нескольких классов, которые
#     имеют общего предка.
""" __ NB! __  -->  """
#   ● Решение проблемы: MRO (Method Resolution Order) - порядок разрешения методов. Например:
    # obj = D()
    # obj.method()
    # D.__mro__

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
# obj.method()                      # B method
# print(D.__mro__)
# ___ END of Example __________________________________________________


""" ___ Создание пользовательских исключений ___ """
# Для создания пользовательского исключения необходимо определить новый класс, наследующийся от
# класса Exception или его подклассов.

# class CustomException(Exception):
#     pass
#
# try:
#     raise CustomException("This is a custom exception")
# except CustomException as e:
#     print(e)            # This is a custom exception

""" __________ Вызов конструктора текущего класса __________ """
# Создание подкласса с расширенным       |           Вызов конструктора текущего класса
# функционалом, но с сохранением         | --->      вместо конструктора родительского
# базового состояния                     |           класса

# class MyBaseClass:
#     def __init__(self, x):
#         self.x = x * 3              # Здесь не просто определю переменную, а перенормирую ее: * 3.
#
#
# class MySubClass(MyBaseClass):
#     def __init__(self, x, y):
#         # super().__init__(x)         # Здесь вызовется х * 3.
#         super().__init__(x + 3)       # А здесь сначала к х прибавится 3, а только потом умножится на 3.
#         self.y = y
#
#
# obj = MySubClass(1, 2)
# print(obj.x)        # 3
# print(obj.y)        # 2

""" ______  Task 1  ______________________________________________________________________________________________ """
# Объясните, что происходит в этом фрагменте кода и какой будет вывод:

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         print("The animal makes a sound.")
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#         print(f'super() from Dog(Animal) --> {super()}')
#
#     def make_sound(self):
#         print(f'super() from make_sound() --> {super()}')
#         super().make_sound()
#
#     print("The dog barks.")
#
#
# my_dog = Dog("Buddy")
# my_dog.make_sound()         # "The animal makes a sound."


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%____________   Абстрактные классы   ___________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

# — механизм для определения интерфейсов, которые должны быть реализованы в производных классах.
#   Абстрактные классы не могут быть инициализированы напрямую, служат ТОЛЬКО ДЛЯ наследования.

""" __________ Модуль abc (Abstract Base Classes) __________ """
# — базовый класс ABC и декораторы для определения абстрактных методов и свойств.

# +++++++++++++++++++++++++++++++++++++
from abc import ABC, abstractmethod
# +++++++++++++++++++++++++++++++++++++

# class BaseShape:
class BaseShape(ABC):
    @abstractmethod
    def area(self):
        pass

    def area2(self):
        pass

class Circle(BaseShape):
    def __init__(self, radius):
        self.radius = radius
        print("Inside Circle __init__")

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(BaseShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f'circle.area():  {circle.area()}')
print(f'rectangle.area(): {rectangle.area()}')

# print(BaseShape())
print(Circle(5))
print(Rectangle(3, 4))



""" ______  Task 2  ______________________________________________________________________________________________ """
# Video 65.
# Создать систему наследования для геометрических фигур: фигура, прямоугольник, квадрат, круг (можно добавить
# и другие плоские фигуры - например, параллелограмм, треугольник, прямоугольный треугольник).
# У всего определить площадь и периметр, а также __str__ (дополнительно можно добавить __repr__).
# Важно: где-то нужно переопределять методы, а площадь абстрактной фигуры не определена.
# Добавить метод, который выводит сообщение "Class: <class_name>".

# # ++++++++++++++++++++++++++++++++++++
# from abc import ABC, abstractmethod
# import math
# # ++++++++++++++++++++++++++++++++++++
#
# class Figures(ABC):
#
#     def class_name(self):
#         return f'Class: {self.__class__.__name__}'
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class Rectangle(Figures):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f'Rectangle with width {self.width} and height {self.height})'
#
#     def __repr__(self):
#         return f'Rectangle({self.width}, {self.height})'
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         return self.width * self.height
#
# class Triangle(Figures):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#     def area(self):
#         p = self.perimeter() / 2
#         return math.sqrt( p * (p - self.a) * (p - self.b) * (p - self.c) )
#
# class Circle(Figures):
#     pi = math.pi
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __str__(self):
#         return f'Circle with radius {self.radius}'
#
#     def __repr__(self):
#         return f'Circle with radius {self.radius}'
#
#     def perimeter(self):
#         return 2 * self.pi + self.radius
#
#     def area(self):
#         return self.pi * self.radius ** 2
#
# figures_list  = [Rectangle(4, 5), Triangle(7, 8, 3), Circle(6)]
# for figure in figures_list:
#     print(f'--- {figure.class_name():-<30}')
#     print(figure.perimeter())
#     print(figure.area())
#     print(figure)
#
# print(figures_list)
