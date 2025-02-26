# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 06.02.25
# Python 38: Dictionaries - Словари.
# ###################################################################################################################
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
print('.' * 145)

# _________________________ Review of previously covered material _________________________
# l = [4, 7, 1, 3, 8]
# print(3 in l)
# s = {4, 7, 1, 3, 8}
# print(3 in s)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%_____  Изменяемые / Неизменяемые МНОЖЕСТВА  _____%%%%%%%%%%%%%%%%%%%%%%%%%%%

# _____ frozenset () _____
# frozenset — это класс, который преобразует строку или последовательность в НЕизменяемое множество.
# my_set = {1, 2, 3}
# my_frozen_set = frozenset({4, 5, 6})
# print(my_set, my_frozen_set, type(my_frozen_set))
# my_set.add(4)                               # Добавление элемента в изменяемое множество
# # my_frozen_set.add(7)                      # Ошибка, нельзя добавить элемент в неизменяемое множество.
# for el in my_frozen_set:
#     print(el)

# Множества поддерживают аналогичный синтаксис для создания множества на основе другого множества
# или итерируемого объекта - Аналог списковых включений для множества.
# my_list = [x for x in range(5)]
# print("list: ", my_list)                       # Выводит {0, 1, 2, 3, 4}
# print("tuple: ", tuple(my_list))               # Выводит {0, 1, 2, 3, 4}
#
# my_set = {x for x in range(5)}
# print("set: ", my_set)                         # Выводит {0, 1, 2, 3, 4}
#
# my_tuple = (x for x in range(5))               # NOT tuple - НЕ кортеж !!!
# print("NOT tuple: ", my_tuple)                 # ERROR !!!!

# list, tuple - ИНДЕКСАЦИЯ!!!
# set - НЕ индексируемый!


# %%%%%%%%%%%%%%%%%%%%%%%%%%%_______    Dictionaries - Словари    _______%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Словари — это ОДНОВРЕМЕННО и упорядоченные (в зависимости от версии Python) и неупорядоченные коллекции
# произвольных объектов с доступом по ключу. Являются изменяемыми структурами данных -
# их элементы могут быть изменены после создания.
# Ключи - неизменяемы объекты, потому ключи - хешируемые данные.

# _____ Элементы словаря _____
# Каждый элемент словаря состоит из пары "ключ: значение".
# Ключи в словаре должны быть уникальными, а значения могут быть любого типа данных.
# Ключ - любой хешируемый объект.
# my_dict = {"names": ["John", "Bob"],
#            "name": "John",
#            "age": 25,
#            "city": "New York",
#            1: "text",
#            (1, 2): "text"}
# # print("dictionary: ", my_dict, sep="\n", end='\n*****')
# print(f'dictionary: {my_dict}', sep="\n", end='\n' + '.'*145)

# _____ Создание словарей _____
# Словари создаются с помощью:
#   - фигурных скобок и перечисления пар "ключ: значение"
#   - с использованием функции dict(), принимающей итерируемый объект, содержащий пары "ключ: значение"
# d = {}              #  __ NB! __  Пустой СЛОВРЬ!
# print(d)
# print(type(d))
#
# my_dict = {"name": "John", "age": 25}
# print(my_dict)
# another_dict = dict([("name", "Jane"), ("age", 30)])
# print(another_dict)

# l = [1, 2, 3]
# list_tuples = [["name", "John"], ["age", 25], ["city", "New York"]]
# print(dict(list_tuples))

# _____ in _____
# in - это оператор, который используется для проверки принадлежности КЛЮЧА словарю.
# Этот оператор проверяет наличие КЛЮЧА в словаре.
# my_dict = {"name": "John", "age": 25}
# print("name" in my_dict)                    # Выводит True
# print("city" in my_dict)                    # Выводит False

# _____ Добавление элементов _____
#   - Для добавления элемента в словарь используют оператор присваивания, указав ключ и значение.
#   - Для удаления элемента из словаря можно использовать оператор del или метод pop(), последний используется для ключей.
# my_dict = {"name": "John", "age": 25}; print(my_dict)
# my_dict["city"] = "New York"; print(my_dict)            # Добавление элемента
# my_dict["age"] = 30; print(my_dict)                     # Изменение элемента по КЛЮЧУ.
# print(my_dict["city"])                                  # Выведение элемента по КЛЮЧУ.
# del my_dict["age"]; print(my_dict)                      # Удаление элемента по КЛЮЧУ.
# my_dict.pop("city"); print(my_dict)                     # Удаление элемента с возвратом значения.

# _____ items() _____
# items() - это метод, который используется для возвращения пар "ключ: значение".
# my_dict = {"name": "John", "age": 25}; print(my_dict)
# print(my_dict.items())

# _____ keys() - values() _____
# keys() - это метод, который используется для возвращения всех ключей.
# values() - это метод, который используется для возвращения всех значений словаря.
# my_dict = {"name": "John", "age": 25}; print(my_dict)
# print(my_dict.keys())
# print(my_dict.values(), '--', type(my_dict.values()))

# my_dict = {"name": "John", "age": 25}; print(my_dict)
# values = my_dict.values()
# print(values, type(values))
# my_dict["new"] = "text"
# print(values)

# my_dict = {"name": "John", "age": 25}; print(my_dict)
# for el in my_dict:
#     print(el)

# t = (1, 2)
# a, b = t; print(a); print(b)
#
# print(my_dict.items())
# for i in my_dict.items():
#     print(f'i --> {i}')
#
# for key, value in my_dict.items():
#     print(f'key - {key}, value - {value}')


# _____ **kwargs _____
# **kwargs - это аргумент, который позволяет передавать произвольное количество именованных аргументов в
# функцию в виде словаря. Этот словарь будет содержать пары "ключ: значение", где ключами являются имена
# аргументов, а значениями - переданные значения.

# _____ Аргумент **kwargs _____ - собирает только в СЛОВАРЬ!!!
# def my_function(**kwargs):
#     # print(type(kwargs))
#     for key, value in kwargs.items():
#         print(key, value)                                   # Выводит имена аргументов и их значения.
# dict_1 = my_function(name="John", age=25, city="New York")
# # dict_2 = my_function(name="Jane", age=30, city="Los Angeles")

def my_function(*args, **kwargs):
    # print(f'\ttype(args) - {type(args)}')
    print(f'\targs = {args}')
    # print(f'\ttype(kwargs) - {type(kwargs)}')
    for key, value in kwargs.items():
        print(f'key = {key}, value = {value}')         # Выводит имена аргументов и их значения.
dict_3 = my_function(name="John", age=25, city="New York")


# _____________________________________    Task 1    _____________________________________

