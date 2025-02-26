# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 10.02.25
# Python 40: Modul - Collections.
# ###################################################################################################################
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
print('.' * 145)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%_______________    Modul - Collections    _______________%%%%%%%%%%%%%%%%%%%%%%%%%%%

# _____ get() _____
# get — это метод, который позволяет получить значение по ключу key.
#   - Если ключ существует в словаре, метод вернет соответствующее значение.
#   - В противном случае, если был предоставлен необязательный аргумент default, то он будет возвращен вместо None.
# my_dict = {"apple": 5, "banana": 2, "orange": 8}
# print(my_dict.get("apple"))                         # Выводит 5.
# print(my_dict.get("grape"))                         # Выводит None.
# print(my_dict.get("grape", 0))                      # Выводит 0, так как ключа "grape" нет в словаре.
# print(my_dict.get("apple", 15))
# print(my_dict)

# _____ setdefault() _____
# setdefault — это метод, который пытается получить значение по ключу key.
#   - Если ключ существует, метод вернет соответствующее значение.
#   - Если ключа нет в словаре, метод добавит в словарь новую пару ключ-значение с ключом key и значением default,
#     если аргумент default был предоставлен.
# my_dict = {"apple": 5, "banana": 2, "orange": 8}
# print(my_dict.setdefault("apple", 10))              # Т.к. ключ существует, возвращает соответствующее значение 5.
# print(my_dict.setdefault("grape", 15))              # Выводит 15 и ДОБАВЛЯЕТ новую пару ключ-значение.
# print(my_dict)                                      # Выводит {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 15}

# courses = {}
# students = [('Math', 'Alice'), ('Math', 'Bob'), ('Physics', 'Charlie')]
# for course, student in students:
#     courses.setdefault(course, []).append(student)
# print(courses)  # {'Math': ['Alice', 'Bob'], 'Physics': ['Charlie']}

# _____ Класс OrderedDict. _____
# OrderedDict — это класс, представляющий словарь, который запоминает порядок вставки элементов.
# Гарантирует, что элементы будут возвращаться в том же порядке, в котором они были добавлены.

# from collections import OrderedDict

# ordered_dict = OrderedDict()
# ordered_dict["apple"] = 5
# ordered_dict["banana"] = 2
# ordered_dict["orange"] = 8
# print(ordered_dict)

# _____ pop(), popitem() _____
# print(ordered_dict.pop("apple"))              # Вырезает по ключу пару и возвращает удаленную пару.
# print(ordered_dict)
# print(ordered_dict.popitem())                 # Вырезает последнюю пару с одной из сторон и возвращает удаленную пару.
# print(ordered_dict)
# print(ordered_dict.popitem(last=False))       # Вырезает последнюю пару с одной из сторон и возвращает удаленную пару.
# print(ordered_dict)

# _____ move_to_end() _____
# print(ordered_dict.move_to_end("banana"))                     # Перемещает пару в конец словаря.
# print(ordered_dict)
# print(ordered_dict.move_to_end("banana", last=False))         # Перемещает пару в начало словаря.
# print(ordered_dict)


# _____ Понятие LRU-кэша - Least Recently Used _____
# LRU-кэш — это механизм кэширования, который хранит ограниченное количество элементов и автоматически удаляет самый
# давно неиспользованный элемент при превышении лимита размера.
# Для реализации LRU-кэша можно использовать словарь (dict).
# При каждом обращении к элементу кэша, его ключ и значение обновляются.
# При превышении лимита размера, можно удалить элемент с самым старым использованием,
# то есть самый первый добавленный элемент.

# from collections import OrderedDict

# def lru_cache(capacity, cache, key, value):
#     if key in cache:
#     # Если ключ уже существует, обновляем значение и перемещаем элемент в конец словаря.
#         cache.pop(key)
#     elif len(cache) >= capacity:
#     # Если кеш переполнен, удаляем первый элемент (самый старый)
#         cache.popitem(last=False)
#     cache[key] = value
# capacity = 3
# cache = OrderedDict()
#
# lru_cache(capacity, cache, "key1", "value1")
# lru_cache(capacity, cache, "key2", "value2")
# lru_cache(capacity, cache, "key3", "value3")
# print(cache) # Выводит OrderedDict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])

# lru_cache(capacity, cache, "key2", "new_value2") # Обновлāем значение "key2"
# print(cache) # Выводит OrderedDict([('key1', 'value1'), ('key3', 'value3'), ('key2', 'new_value2')])
# lru_cache(capacity, cache, "key4", "value4") # Кÿш переполнен, удалāем "key1"
# print(cache) # Выводит OrderedDict([('key3', 'value3'), ('key2', 'new_value2'), ('key4', 'value4')])

# _______ EXAMPLES _________
# def updateOrder(OrderedDict,key):           # ??????????????????????????????
#     if key in OrderedDict:
#         value=OrderedDict.pop(key)
#         OrderedDict[key] = value

# _____ Класс defaultdict _____
# defaultdict — это класс, представляющий словарь, который автоматически создает значения для несуществующих
# ключей при первом обращении.

# from collections import defaultdict, OrderedDict

# ___ for int():
# my_dict = defaultdict(int)
# print(my_dict)
# my_dict["apple"] = 5
# print(my_dict)
# print(my_dict["apple"])           # Выводит 5
# print(my_dict["banana"])          # Выводит 0, так как ключа "banana" нет, но defaultdict автоматически создал его со значением 0

# ___ for list():
# my_dict = defaultdict(list)
# print(my_dict)
# my_dict["apple"] = [1, 2]
# print(my_dict)
# # print(my_dict["apple"])         # Выводит [1, 2]
# # print(my_dict)
# # print(my_dict["banana"])        # Выводит 0, так как клĀча "banana" нет, но defaultdict автоматически создал его со значением 0
# # print(my_dict)
# print(my_dict["kiwi"].append(1))
# print(my_dict)

# _______ EXAMPLES _________
# В аквариуме три рыбки, и их названия, виды и резервуары указываются в этих трех кортежах.
# Нужно организовать инвентарный список по резервуарам и получить список рыб, присутствующих в каждом резервуаре.
# Используйте defaultdict для группировки рыб по резервуарам.

# from collections import defaultdict

# fish_inventory = [
#     ("Sammy", "shark", "tank-a"),
#     ("Jamie", "cuttlefish", "tank-b"),
#     ("Mary", "squid", "tank-a"),
# ]
# tanks = defaultdict(list)
# for name, fish, tank in fish_inventory:
#     # tanks[tank] = (name, fish)              # Doesn't work :(
#     tanks[tank].append((name, fish))          # It WORKS :)
# print(tanks)

# _____ Класс Counter _____
# counter — это класс, который предоставляет удобную структуру для подсчета элементов в итерируемом объекте.

# from collections import Counter

# my_list = [1, 2, 3, 1, 2, 3, 1, 2, 4, 5, 4, 3, "hello", "a", "b", "a", "a"]
# my_counter = Counter(my_list)
# print(my_counter)                               # Выводит Counter({1: 3, 2: 3, 3: 3, 4: 2, 5: 1})
# print(my_counter[1])                            # Выводит 3, так как элемент "1" встречается 3 раза в списке.
#
# print(list("hello"))
# print(Counter("hello"))


# _____ Именованные кортежи - namedtuple _____
# Именованные кортежи namedtuple — это кортежи, которые представляют удобную структуру для создания
# простых классов без методов, которые используются только для хранения данных.

# from collections import namedtuple

# # Создаем именованный кортеж с именами полей 'name' и 'age'
# Person = namedtuple('Person', ['name', 'age'])
# person1 = Person(name='Alice', age=30)
# print(person1[0])
# print(person1.name)
# print(person1.age)

# _______ EXAMPLES _________

# from collections import namedtuple

# Person = namedtuple("Person", ["name", "age", "city"])      # the SAME!
# Person = namedtuple("Person", "name age city")              # the SAME!
# # person1 = ('Alice', 30)                        # Базовый кортеж.
# # person2 = ('Bob', 35)                        # Базовый кортеж.
# person1 = Person("Alice", 30, "New York")
# person2 = Person("Bob", 25, "San Francisco")
# name, age, city = person1
# print(name, age, city)
# print(person1.name)
# print(person1.age)
# print(person2.name)
# print(person2.age)



# %%%%%%%%%%%%%%%%%%%%%%%%%%%__________  Введение в сериализацию/десериализацию  __________%%%%%%%%%%%%%%%%%%%%%%%%%%%

# _____ JSON _____
# json — это модуль, который предоставляет функции для сериализации и десериализации данных в формате JSON.

# import json

# __ Сериализация Python-объекта в JSON-строку:
# data = {"name": "John", "age": 25, "city": "New York"}
# print(type(data), data)
# json_str = json.dumps(data)
# print(type(json_str), json_str)           # Выводит '{"name": "John", "age": 25, "city": "New York"}'
# -----------------
# data = {"name": "John", "age": 25, "city": "New York", "hobby":("hiking", "swimming")}
# data = {"name": "John", "age": 25, "city": "New York", "hobby":("hiking", "swimming"), "country": None, "is_active": True}
#
# print(type(data), data)
# json_str = json.dumps(data)
# print(type(json_str), json_str)             # Выводит <class 'str'> {"name": "John", "age": 25, "city": "New York", "hobby": ["hiking", "swimming"]}
# print(json_str, '\n', '.' * 140)
# -----------------
# __ Десериализация JSON-строки в Python-объект:
# json_str = '{"name": "John", "age": 25, "city": "New York", "hobby": ["hiking", "swimming"], "country": null, "is_active": true} '
# data = json.loads(json_str)
# print(type(data), data)
# print(data["name"])                                 # Выводит 'John


# _____________________________________    Task 1    _____________________________________
# Дана строка. Посчитайте в ней частоту встречаемости всех букв. Считаем, что в строке могут быть пробельные символы.
# user_str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.'

# from collections import Counter

# def count_letters(text):
#     # if text.isalpha():
#         # --------------------------------
#         # new_text = str(text)
#         # my_count = Counter(new_text)
#         # return my_count
#         # --------------------------------
#     x = Counter(text)
#     for el in list(x.keys()):
#         if not (el == ' ' or el.isalpha() or el.isspace()):
#             x.pop(el)
#         else:
#             continue
#     return x
#
# print(count_letters(user_str), '\n', '.' * 145)

# _____________________________________    Task 2    _____________________________________
# Реализуйте функцию, которая принимает словарь задач с категориями и группирует задачи по их категориям.
#   Данные:
# tasks = {
# "task1": "работа",
# "task2": "учёба",
# "task3": "развлечения",
# "task4": "работа",
# "task5": "учёба"
# }
#   Вывод:
# {
# 'работа': ['task1', 'task4'],
# 'учёба': ['task2', 'task5'],
# 'развлечения': ['task3']
# }

# from collections import defaultdict

# def group_by_tasks(tasks):
#     groups = defaultdict(list)
#     for key, value in tasks.items():
#         groups[value].append(key)
#     return groups
#
# print(group_by_tasks(tasks))

# _____________________________________    Task 3    _____________________________________
# Дан текст.
# Необходимо посчитать сколько раз встретилось каждое слово и вывести в топ слов, упорядоченный сначала по
# убыванию встречаемости, а при равенстве частот в соответствии с упорядочиванием в лексикографическом порядке.
# Решить задачу с помощью использования изученных классов.
# text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est!'

# __ NB! __ Phrase without any signs.
# print(text[0].isalpha())
# only_letters = []
# for s in text.lower():
#     if s.isalpha() or s.isspace():
#         only_letters.append(s)
# print(only_letters)
# print(''.join(only_letters))

# from collections import Counter

# __ Простое решение:
# clean_text = text.replace(',', '').replace('.', '').replace('!', '').lower().split()
# print("clean_text = ", clean_text, '\n', '.' * 145)
# my_counter = Counter(clean_text)
# print("my_counter = ", my_counter, '\n', '.' * 145)
# sorted_counter_x0 = sorted(my_counter.items(), key=lambda x: x[0])
# sorted_counter_x1 = sorted(my_counter.items(), key=lambda x: -x[1])
# sorted_counter = sorted(my_counter.items(), key=lambda x: (-x[1], x[0]))        # ????????????????????? (-x[1], x[0])
# print("sorted_counter_x0 = ", sorted_counter_x0, '\n', '.' * 145)
# print("sorted_counter_x1 = ", sorted_counter_x1, '\n', '.' * 145)
# print("sorted_counter = ", sorted_counter, '\n', '.' * 145)

# __ В виде функции:
# def count_words(text):
#     clean_text = text.replace(',', '').replace('.', '').lower().split()
#     my_counter = Counter(clean_text)
#     sorted_counter = sorted(my_counter.items(), key=lambda x: (-x[1], x[0]))
#     return sorted_counter
#
# print(count_words(text))

# __ Вот перебор строки с исключением в одну запись:
# def count_words(text):
#     clean_text = [word.strip('.,!?') for word in text.lower().split()]
#     my_counter = Counter(clean_text)
#     sorted_counter = sorted(my_counter.items(), key=lambda x: (-x[1], x[0]))
#     return sorted_counter
#
#
# print(count_words(text))



