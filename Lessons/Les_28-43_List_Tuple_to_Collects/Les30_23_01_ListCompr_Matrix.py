# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 23.01.25
# Python 30: Представления списков.

# ###################################################################################################################
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
print('.' * 120)


# ______ Review of previously covered material ______
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(numbers)
# print(*numbers)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% _________  THEORY - Представления списков  __________ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# _____ Списковые включения (List comprehensions) _____
# List comprehension (лист генератор) - новый СПИСОК на основе существующего списка или другой итерируемой последовательности.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared_numb = [x ** 2 for x in numbers]          #  \\\  List comprehensions  ///
# print(squared_numb)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]         # Эквивалент того, что выше через цикл for.
# squared_numb = []
# for numb in numbers:
#     squared_numb.append(numb ** 2)
# print(numbers)
# print(squared_numb)

# __   NB!  __  Списковые включения автоматически АППЕНДЯТ (.append) или включают, те его не нужно вставлять!
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)
# print([numb ** 2 for numb in numbers])            #   \\\  List comprehensions  ///

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)
# squared_numb = [numb ** 2 for numb in numbers]
# print(squared_numb)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)
# squared_numb = [print(numb ** 2) for numb in numbers]         # Возвратит _НИЧЕГО_ (None), так как что
# print(squared_numb)                                           # print(print(...)) ВСЕГДА возвращает _НИЧЕГО_ (None).

# numbs = 6, 7, 8, 9
# print('Print Tuple: ', numbs)                                         # Возвратит _НИЧЕГО_ (None), так как что
# print(print('print(print( ... )) of Tuple: ', numbs))                 # print(print(...)) ВСЕГДА возвращает _НИЧЕГО_ (None).

#    NB!   Списковые включения можно делать с ОДНИМ и не больше условием if.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)
# squared_numb = [numb ** 2 for numb in numbers if numb > 5]
# print(squared_numb)


# _____ Вложенные списки (LIST) / кортежи (TUPLE) _____
# Для иерархических структур.
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print('\nPrint Matrix: ', matrix)
# print(matrix[1])
# print(matrix[1][2])
# print([4, 5, 6][0])
# print([4, 5, 6][2])

# matrix_str = "Python"
# print(matrix_str[2])

# matrix_q = [
#     [1, 2, 3],
#     "Python",
#     [7, 8, 9]
# ]
# print(matrix_q[1][2])

# numbers = (1, 2, [3, 4], 5, 6, [[7, 8], [9, 10]])
# print(len(numbers))
# for el in numbers:
#     print(el)


# _____ СТЕК (STACK) - Last-in, First-out _____
# Стек (STACK) - структура данных, работающая по принципу последний вошел - первый вышел.
# Стел (STACK) - это паттерн, ко которому .... ???????????????????????
# stack = []
# # Добавление элементов в стек:
# stack.append(1)                 # Добавление элемента в очередь.
# stack.append(3)
# top_element = stack.pop()       # Извлечение верхнего элемента из списка.
# print(top_element)
# print(stack)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new = [20, 30]
# numbers.append(new)
# new.pop()
# numbers.pop()
# print(new)
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]       # __  NB! __ В памяти Python лежит не список из объектов, а список из ССЫЛОК на объекты!
# new = [20, 30]
# numbers.append(new)
# print(numbers)
# new.pop()
# print(new)
# print(numbers)


# _____ Очередь (QUEUE)_____
# deque - очередь, причем двусторонняя коллекция, потому что можно как слева положить (.append()), так и справа .appendleft().
# from collections import deque
# queue = deque()
# queue.append(1)                  # Добавление элемента в очередь.
# queue.append(2)
# queue.append(3)
# first_elem = queue.popleft()     # Извлечение первого элемента из очереди.
# print(first_elem)                # 1
# print(queue)


# _____ Сортировка (SORT)_____
# Список меняется, при этом не получается новый список, он просто МЕНЯЕТСЯ.
# my_list = [4, 1, 2, 3]
# print(my_list)
# my_list.sort()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)


# _____ FUNCTION _____
# def say_hi(name):
#     print(f'Hello, {name}.')
#
# say_hi('Michael')
# say_hi('Michael', "!")                    # ERROR !

# def say_hi(name, symbol):
#     print(f'Hello, {name}{symbol}.')
#
# say_hi('Michael')
# say_hi('Michael', "!!!")                  # ERROR !

# def say_hi(name, symbol="!"):
#     print(f'Hello, {name}{symbol}.')
#
# say_hi('Michael')
# say_hi('Michael', "!!!")        # NOT error !
# say_hi('Michael', ".")