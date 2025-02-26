# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 20.01.25
# Python 28: Методы списков, кортежи.

# ###################################################################################################################
print('.' * 120)


# ______ Review of previously covered material ______

# numbs = [1, 2, 3, 4, 5]
# a = [1,2]
# numbs.append(a)             # Добавляет в том виде, в каком был введен, т.е. целая коллекция.
# numbs.extend(a)             # Добавляет элементы в коллекцию, РАЗДЕЛЯЯ их, т.е. по ОТДЕЛЬНОСТИ.
# numbs.extend("Wonder")
# # numbs.extend(5)           # ERROR!!! Число - не итерируемый объект.
# numbs.extend(range(5))      # NB! - итерируемый объект.
# print(numbs)

# []                        # - LIST
# (..., ...)                # - Tuple
# a = (1)                   # NB! - NOT Tuple, because it needs koma!!!


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% _________  Методы списков  __________ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# _____ .insert() _____
# numbs = [1, 2, 3, 4, 5]
# print(numbs[2:])                      # NEW Object! Индексация в срезе даст НЕверный результат! Поэтому в срезах искать НЕЛЬЗЯ!
# print(numbs.index(4))
# numbs.insert(3, "Hi")                 # - BEFORE numbs[3] == 4, ie between 3 snd 4 in list. Вставляется ЦЕЛЫЙ объект.
# print(numbs)
# to_find = 7
# if to_find in numbs:
#     print(numbs.index(to_find,2))
# else:
#     print("Not found")
# ___ NB! ___ СОРТИРОВКА занимает МНОГО места. Поэтому эффективнее использовать _IN_. СМ ВИДЕО!!! с 1:08:00
# result = numbs.index(4)
# numbs.insert(result, "Hi")
# print(numbs)

# _____ .remove() _____
# numbs = [1, 2, 3, 4, 5]
# numbs.remove(3)
# print(numbs)

# if 6 in numbs:
#     print(numbs.remove(6))
# print(numbs)

# if 5 in numbs:
#     print(f'in IF - {numbs.remove(5)}')         # NONE !!! - print выводит ничего, т.е. нужно использовать просто функцию/метод.
# print(f'Behind IF - {numbs}')
# print(print(f'print(print(...)) Behind IF - {numbs}'))           # NONE !!! - print выводит ничего, т.е. нужно использовать просто функцию/метод.
# print(f'print - {[1, 2, 3, 4, 5].remove(5)}')                # NONE !!! - print выводит ничего, т.е. нужно использовать просто функцию/метод.
#
# def fun():
#     return print(f'def - {[1, 2, 3, 4, 5].remove(5)}')
# print(f'print(def()) {fun()}')

# _____ .count() _____
# numbs = [1, 2, 3, 4, 5, 2, 2]
# print(numbs.count(2))

# a = [66, 456, 56, 2, 2, 9, 3]
# a.insert(2,-1)
# a.remove(2)
# print(a, '\n', a.index(-1), '\n', a.count(2))

# _____ .clear() _____
# a = [66, 456, 56, 2, 2, 9, 3]
# a.clear()
# print(a)

# _____ del() _____
#  NB! - В переменных лежат ССЫЛКИ!!!
# my_list = [1, 2, 3, 4]
# my_list2 = my_list
# my_list2.append(5)
# del my_list[2]              # Удаление элемента с индексом 2.
# print(my_list)
# del my_list                 # Удаление списка ЦЕЛИКОМ.
# print(my_list)
# print(my_list2)
# del my_list2[:2]               # - NB! - НЕ включая эдемент с индексом 2!
# print(my_list2)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% _________  Кортежи - TUPLE __________ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Кортежи - НЕизменяемые коллекции, в отличии от списка. Гарантирует неизменяемость списка.
# my_tuple = (1, 2, 3, 4)
# print(my_tuple)
# print(type(my_tuple))
# print(my_tuple.count(2))        # Returns the number of elements with the specified value (с указанным значением).
# my_tuple[0] = "1"               # ERROR

# def return_two():
#     my_tuple = (1, 2, 3, 4)
#     a = my_tuple.index(4)
#     b = my_tuple.index(2)
#     return a, b
# print(return_two())             # Вернет КОРТЕЖ!
# x, y = return_two()
# x, y, z = return_two()          # ERROR !!!

# _____ Operator    *    ______
# Используется для запаковки или раскрытия последовательности: списков, кортежей.
# my_list = [1, 2, 3, 4]
# print('1 | ', my_list, sep='---')           # Тк один элемент, то они НЕ разделяется.
# print('2 | ', my_list, 1, sep='---')
#
# print('3 | ', my_list[0], my_list[1], my_list[2], sep='---')
# print('4 | ', *my_list, 1, sep='---')        #    *   .

# __ Example with Operator * __
# def sum_elements1(a, b):
#     print(sum([a, b]))
# sum_elements1(1, 2)
#
# def sum_elements1(a, b, c):
#     print(sum([a, b, c]))
# sum_elements1(1, 2, 3)

# _____ Functions _____
# def sum_elements1(*elements):            # * - позволяет получить ЛЮБОЕ кол-во чисел.
#     print(type(elements))                # * - триггер на запаковку.
#     print(sum(elements))
# sum_elements1(1, 2, 3)
# sum_elements1(1, 2, 3, 4, 5, 6)

# def sum_elements1(*elements):            # * - позволяет получить ЛЮБОЕ кол-во чисел.
#     print(type(elements))                # * - триггер на запаковку.
#     print(elements)
# sum_elements1([3], 1, 2, 3, 4, 5, 6)

# def sum_elements1(name, *elements):            # * - позволяет получить ЛЮБОЕ кол-во чисел.
#     print(type(elements))                      # * - триггер на запаковку.
#     print(name)
#     print(elements)
# sum_elements1("Anna", 1, 2, 3, 4, 5, 6)
# #

# def sum_elements1(name, *args):                 # * - позволяет получить ЛЮБОЕ кол-во чисел.
#     print(type(args))                           # -- ARGS --.
#     print(name)
#     print(args)
# sum_elements1("Anna", 1, 2, 3, 4, 5, 6)

# print ОЖИДАЕТ ARGS, поэтому print(print(...)) - выдаст НИЧТО!

# _____ LOOPS _____
# my_list = [1, 2, 3]
# for item in my_list:
#     print(item)

# my_list = [1, [2, 4], 3]
# for item in my_list:
#     print(item)

# _____ LOOPS  +  enumerate() _____
# my_list = [1, [2, 4], 3]
# for item in enumerate(my_list):         # enumerate() - пакует в КОРТЕЖИ! - это распаковка.
#     print(item)

# my_list = [1, [2, 4], 3]
# for i, item in enumerate(my_list):         # enumerate() - пакует в КОРТЕЖИ! - это распаковка.
#     print(i, item)

# t = 1, 2, 3                                 # TUPLE
# print(type(t))


# __ Task 1 __
# str = "Hello World!"
# print(tuple(str))                      # Преобразовать в кортеж.
# print(*tuple(str),  sep='_')           # Преобразовать в кортеж c разделителем - 1-st way.
# print("_".join(tuple(str)))            # Преобразовать в кортеж c разделителем - 2-nd way.

# __ Task 2 __
# Дан массив целых чисел длины 1 и более. Написать функцию, которая возвращает массив длины 2,
# состоящих из первого и последнего элемента входного массива. {1, 2, 3} -> {1, 3}, {7, 4, 6, 2} -> {7, 2}.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def return_set(numbers):
#     return [numbers[0], numbers[-1]]            # or list(numbers[0], numbers[-1])
# print(return_set(numbers))

# __ Task 3 __
# Дан список покупок. Найдите какой по счету (начиная с единицы) товар с названием "Milk".
# Если товара нет, выведите сообщение об отсутствии.
# products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]
# prod_name = 'Butter'    # 'Bier'
# if prod_name in products:
#     print(f'The supple {prod_name} is in \033[1;31m{products.index(prod_name) + 1}\033[m position in the list.')
# else:
#     print(f'{prod_name} is not in List of products/supplies.')

# __ Task 4 __
# Дан текст. Программа должна:
# 1. Разбить текст на слова.
# 2. Создать список уникальных слов в алфавитном порядке (не учитывая регистр).
# 3. Вывести количество уникальных слов.
#
# **Данные:**
# text = "Python is a great programming language. Python is popular and powerful."
# **Пример вывода:**
# Количество уникальных слов: 9
# Уникальные слова: ['a', 'and', 'great', 'is', 'language', 'popular', 'powerful', 'programming', 'python']

# def count_unique(text):
#     # pass
#     split_text = text.replace('.', '').replace(',', '').lower().split()
#     print(split_text)
#     list_unique = []
#     for word in split_text:
#         # if list_unique.count(word) == 0:          # 1-st Variant
#         if word not in list_unique:                 # 2-nd Variant
#             list_unique.append(word)
#     print(list_unique)
#
# count_unique('Python is a great programming language. Python is popular and powerful.')





