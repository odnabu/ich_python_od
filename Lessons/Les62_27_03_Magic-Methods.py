# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 27.03.25
 Python 62: Магические методы в Python.
 ################################################################################################################### """

# Video Lesson 62: https://player.vimeo.com/video/1069918814?h=ea3f3f7663.
# Video Practice __: wasn't.
# links:
#   - Presentation: "Python_32_M.pptx-Magic_Methods.pdf".
#   -

# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------

print('.' * 120)

""" ___________________________________  Review of previously covered material  ___________________________________ """



""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%__________   Магические методы классов   _________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """
# — это специальные методы с особым именем, начинающимся и заканчивающимся на два подчеркивания (__) -
#   __init__, __add__, __eq__, и т.д.

#   ● Магические методы позволяют определить поведение объектов при выполнении определенных операций, таких как
#     математические операции.
#   ● Методы математических операций определяют поведение объекта при выполнении арифметических операций:
#       ○ сложение (__add__)
#       ○ вычитание (__sub__)
#       ○ умножение (__mul__)
#       ○ деление (__div__) и другие.
# ___ EXAMPLE _____________________________________________________________________________________
#  Video 62, 27:00

# class Money:
#     def __init__(self, amount, currency):
#         self.amount = amount
#         self.currency = currency
#
#     def __add__(self, other):
#         if self.currency == other.currency:
#             return Money(self.amount + other.amount, self.currency)
#
#     def __str__(self):
#         return f"{self.amount} {self.currency}"
#
# m1 = Money(100, "eur")
# m2 = Money(230, "eur")
# print(m1 + m2)
# ___ END of Example _____________________________________________________________________________________


""" __________ Декоратор @functools.total_ordering __________ """
# — декоратор, который позволяет автоматически генерировать недостающие методы сравнения (__lt__, __le__,
#   __gt__, __ge__) на основе метода __eq__ и одного из методов __lt__ или __gt__.

# See Video 62, _______

# +++++++++++++++++++++++++++++++++++++++
from functools import total_ordering
# import functools
# +++++++++++++++++++++++++++++++++++++++

@total_ordering
# @functools.total_ordering
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price        # and self.name.lower() == other.name.lower()

    # def __ne__(self, other):
    #     return self.price != other.price

    # def __lt__(self, other):
    #     return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    # def __le__(self, other):
    #     return self.price <= other.price

    # def __ge__(self, other):
    #     return self.price >= other.price

    def __bool__(self):
        return bool(self.price)

    def __hash__(self):
        return hash((self.name, self.price))  # Используем кортеж

p1 = Product("Apple", 2)
p2 = Product("Banana", 0)
p3 = Product("Melon", 3)
print(f'{p1.name} - {p1.price}\n'
      f'{p2.name} - {p2.price}\n'
      f'{'-' * 30}')

print(f'{'p1 < p2':<10}', p1 < p2)
print(f'{'p1 <= p2':<10}', p1 <= p2)
print(f'{'p1 > p2':<10}', p1 > p2)
print(f'{'p1 >= p2':<10}', p1 >= p2)
print(f'{'p1 == p2':<10}', p1 == p2)
print(f'{'p1 != p2':<10}', p1 != p2)
print()
print(f'{'bool(p1)':<10}', bool(p1))
print(f'{'bool(p2)':<10}', bool(p2))

# Если в классе определен __eq__, а __hash__ не переопределен, то Python автоматически делает __hash__ = None.
s = {p1, p2}
print(s)


l = [1, 2, 3]
print(len(l))
print(l.__len__())




""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%__________   Использование методов   _________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

""" ___ Методы __len__, __hash__, __bool__  ___ """
#   ● Метод __len__ - определяет поведение объекта при вызове встроенной функции len() и возвращает
#     размер или длину объекта.
#   ● Метод __hash__ - Определяет хэш-значение объекта, которое используется, например, при добавлении
#     объекта в множество или использовании в качестве ключа в словаре.
#   ● Метод __bool__ - Определяет логическое значение объекта при вызове встроенной функции bool().


""" ___  __getitem__  ___ """   # Video 62, 1:00:05
# — метод, который позволяет получить значение по ключу.

#   ///   See Example Video 62, 1:02:00    ///
# class MyList:
#     def __init__(self, data):
#         self.data = data  # Внутренний список
#
#     def __getitem__(self, index):
#         print(f"Получаем элемент {index}")
#         return self.data[index]  # Просто берем из списка
#
#     def __setitem__(self, index, value):
#         if value >= 0:
#             print(f"Устанавливаем {value} в позицию {index}")
#             self.data[index] = value  # Изменяем список
#         else:
#             print("Значение не может быть отрицательным")
#
#     def __str__(self):
#         return str(self.data)
#
# ml = MyList([10, 20, 30])
# print(ml)
# print(ml[1])            # Вызывает __getitem__ → Получаем 20
# ml[1] = 99              # Вызывает __setitem__ → Меняем на 99
# print(ml)               # [10, 99, 30]
# ml[1] = -5              # Вызывает __setitem__
# print(ml.data)          # [10, 99, 30]

""" ___  __setitem__  ___ """
# — метод, который присвоить значение по ключу.

# ___ EXAMPLE _____________________________________________________________________________________
# class Money:

#     # дополнительные методы класса
#     def __getitem__(self,index):
#         if index==self.currency:
#             return self.amount
#         else:
#             return -1
#
#     def __setitem__(self,index,amount):
#         if index==self.currency:
#             self.amount=amount
#         else:
#     print("Валюта не совпадает")
# ___ END of Example _____________________________________________________________________________________

""" ___  __delitem__  ___ """
# — метод, который определяет поведение при удалении элемента по ключу.

""" ___  __call__  ___ """
# — метод, который позволяет вызывать экземпляр класса как функцию.

# ___ EXAMPLE _____________________________________________________________________________________
# class CallableClass:
#     # Логика вызова класса:
#     def __call__(self, *args, ** kwargs):
#
# obj = CallableClass()
# obj()                   # Вызов класса как функции
# ___ END of Example _____________________________________________________________________________________

# Объясните, что происходит в этом фрагменте кода:
# class Test:
#     def __call__(self, message):
#         print(message)
#         return True
#
# test = Test()
# test("Hello World ---> ")

""" ___  __iter__  ___ """
# — метод, который определяет, как объект должен быть перебираемым, и возвращает итератор.

""" ___  __next__  ___ """
# — метод, который определяет логику получения следующего элемента из итератора.


""" __________ Добавление семантики итератора __________ """

# ___ EXAMPLE _____________________________________________________________________________________

# ___ 1-st - THEORY _____________________
# class MyIterator:
#     def __iter__(self):
#         return self
#
#     def +_next__(self):
#         # Логика получения следующего элемента.
#         # Если достигнут конец итерации, вызывается исключение StopIteration
#         raise StopIteration
#
# obj = MyIterator()
# for item in obj:
#     # Логика перебора элементов
#     pass

# ___ 2-nd - Example _____________________
# class MyIterator:
#     def __init__(self):
#         self.i = 0
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i < 100:
#             self.i += 10
#             return self.i
#         else:
#             raise StopIteration
#
# obj = MyIterator()
# for item in obj:
#     print(item)
# ___ END of Example _____________________________________________________________________________________

""" ___  __dict__  ___ """
# — метод, который возвращает словарь, содержащий атрибуты объекта.

# class MyClass:
#     def __init__(self):
#         self.x = 1
#         self.y = 2
#
# obj = MyClass()
# print(obj.__dict__)         # {x': 1, 'y': 2}

""" __________ Добавление методов в класс __________ """

# class MyClass:
#     def __init__(self, x):
#         self.x = x
#
#     def __str__(self):
#         return f"MyClass with x = {self.x}"
#
# obj = MyClass(10)
# print(obj)          # MyClass with x = 10



# ___ EXAMPLE _____________________________________________________________________________________

# ___ END of Example _____________________________________________________________________________________



""" ______  Task 1  ______________________________________________________________________________________________ """
# ### 🔹 **1. Класс "Инвентарь" (`__getitem__`, `__setitem__`)**
# **Задача:** Реализуйте класс `Inventory`, который хранит предметы (словарь `{"название": количество}`) и
# поддерживает обращение через `[]`.
    # **Пример работы:**
    # ```python
    # inv = Inventory()
    # inv["зелье"] = 3 # Установить количество
    # print(inv["зелье"]) # 3
    #
    # inv["зелье"] = 2 # Увеличить количество
    # print(inv["зелье"]) # 5
    #
    # print(inv["меч"]) # 0 (если предмета нет)
    # ```
#
    # **Требования:**
    # - `__getitem__` должен возвращать количество предмета (если нет — `0`).
    # - `__setitem__` должен **увеличивать** количество предмета, если он уже есть в инвентаре.

# class Inventory:
#     # В принципе можно обойтись без метода __init__. Но, он нужен, чтобы складывать куда-то значения.
#     # И это будет пустой словарь:
#     def __init__(self):
#         self.items = {}
#
#     def __getitem__(self, item):
#         return self.items.get(item, 0)     # Если объект есть вернет объект, если нет, то вернет 0.
#
#     def __setitem__(self, key, value):
#         self.items[key] = self.items.get(key, 0) + value
#
#
#
# inv = Inventory()
# print(inv["зелье"])     # 0
# inv["зелье"] = 3        # Установить количество
# print(inv["зелье"])     # 3
# inv["зелье"] = 2        # Увеличить количество
# print(inv["зелье"])     # 5
# print(inv["меч"])       # 0 (если предмета нет)

