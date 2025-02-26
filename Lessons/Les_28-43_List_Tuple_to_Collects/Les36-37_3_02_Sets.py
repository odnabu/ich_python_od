# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 03.02.25
# Python 36: Sets - Множества.
# ###################################################################################################################
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
print('.' * 145)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%_____  Хэш - hash   _____%%%%%%%%%%%%%%%%%%%%%%%%%%%

# _____ Хэш - hash.  Хэш-таблица _____
# Хэш — это числовое значение, которое вычисляется для данных с помощью хэш-функции.
# Хэш-таблица — это структура данных, которая использует хэши для эффективного хранения и поиска элементов.
# Хешируемые элементы - неизменяемы объекты:
# hash — это встроенная функция, которая возвращает хэш-значение для объекта. Хэшируемыми типами данных в
# Python являются неизменяемые объекты, такие как строки, числа и кортежи.
# Это нужно: помогает искать определенные объекты в структуре данных, которая работает по другой логике - Video 0:30:00.

# hash_value = hash("hello")
# print(hash_value)               # Выводит целочисленное значение хэша.

# print(hash("Hello"))
# print(hash("Hello"))
# print(hash(100))

# print(hash(1), hash(1.0), hash(0), hash(True), hash(False), hash(-2))            # 1, 1, 0, 1, 0, -2
# print(hash('1'), hash("string"), hash((1, 2, 3)))                                # Everyone is different.


# %%%%%%%%%%%%%%%%%%%%%%%%%%%_____  Множество - set   _____%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Множество — это абстрактная структура данных, которая представляет собой
# неупорядоченную коллекцию уникальных элементов, причем таких которые можно хешировать.

# __  NB!  __ Основное свойство множества - Уникальность элементов. В множестве НЕ может быть повторяющихся элементов.

# s1 = {"Python", "C", "C++", "Java"}
# s2 = {"a": 1, "b": 2, "c": 3}
# print(f'{s1},\n{s2}')

# _____ Операции из теории множеств _____

# __  NB! __ Над множествами можно производить операции с помощью:
#       - операторов (<>|==^),
#       - методов (.intersection()).

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# intersection = set1.intersection(set2)                      # Пересечение (intersection).
# union = set1.union(set2)                                    # Объединение (union).
# difference = set1.difference(set2)                          # Разность (difference).
# symmetric_difference = set1.symmetric_difference(set2)
# print(intersection)                                         # Выводит {2, 3}.
# print(union)                                                # Выводит {1, 2, 3, 4}.
# print(difference)                                           # Выводит {1}.
# print(symmetric_difference)                                 # Выводит {1, 4}.


# set3 = {1, 2, (5, 8)}
# set4 = {1, 2, (5, [9, 23])}
# print(hash([9, 23]))
# print(hash((9, 23)))

# _____ Работа с множествами _____

# Создать множество в Python можно:
#   - перечислив элементы в фигурных скобках.
#   - с использованием функции set().
# set2 = {2, 3, 4}
# print(type(set2))
# set3 = {}                   # Может быть только пустым СЛОВАРЕМ.
# print(type(set3))
# set_num = set()             # ТОЛЬКО так можно создать пустое множество.
# print(type(set_num))

# Размер множества можно получить: с помощью функции len()
# my_set = {1, 2, 3}
# empty_set = set()
# print(len(my_set))          # Выводит размер множества
# print(2 in my_set)          # Выводит True, так как элемент 2 содержится во множестве

# Для проверки наличия элемента в множестве: можно использовать оператор in.
# print({3} in set2)          # НЕ СРАБОТАЕТ, тк можно сравнивать только 2 разных объекта.

# set2_2 = {2, {3}, 4}        # ERROR  -  unhashable type: 'set'.
# print(type(set2_2))

# _____ Добавление/удаление элемента во множество _____
# Добавить элемент в множество:  с помощью функции add.
# Удалить элемент с помощью функций remove, discard.
# Очистить множество с помощью функции clear.
# my_set = {1, 2, 3}
# my_set.add(4)                     # {1, 2, 3, 4}
# my_set.remove(2)                  # {1,3,4}
# my_set.discard(5)                 # ничего не изменится
# my_set.clear()                    # Очищает множество и выдает ПУСТОЕ множество.
# print(my_set)                     # Выводит результат.

# _____ Сравнение множеств _____
# Множества можно сравнить с помощью операторов (<>|==^) или с помощью методов (.intersection()) на:
#   - равенство (==)
#   - неравенство (!=)
#   - подмножество (<=, <)
#   - надмножество (>=, >)
#   - .issubset()
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1 == set2)             # Выводит False
# print(set1 < set2)              # Выводит False, set1 не является подмножеством set2

# set3 = {2, 3, 4}
# print(set2.issubset(set3))

# set1 = {2, 3, 4, 1}
# set2 = {4, 3, 3}
# print(set1 > set2)
# print(set1 < set2)

# _____ Итерирование по множеству с помощью цикла for _____
# Перебрать множество, чтобы выполнить определенные действия для каждого элемента множества: с помощью цикла for.

# flag = True                       ??????????????????????????????????
# for i in set1:
#     print(i)
#     if i not in set2:

# my_set = {1, 2, 3}
# for item in my_set:
#     print(item)             # Выводит каждый элемент множества.

# ___ Симметричная разница ___
# set1 = {2, 3, 4, 1}
# set2 = {4, 3, 3}
# print(set1.symmetric_difference(set2))
# print(set1.symmetric_difference_update(set2))
# print(set1 ^ set2)
# print(set1)


# _____________________________________    Task 1    _____________________________________
# Дан массив. Дать ответ на вопрос есть ли в нём два элемента с суммой ноль.
#       - Решить с двумя вложенными циклами.
#       - Решить с помощью множеств.
# l1 = [1, -8, -5, 4, 7, 3, -4, -1, 9]
# l2 = [1, -8, -5, 4, 7, 3, 9]
# def is_paar_sum_null(mas):
#     new_mas = set()
#     for i in mas:
#         if -i in mas:
#             return True
#         new_mas.add(i)
#     return False
# result1 = is_sum_null(l1)
# result2 = is_sum_null(l2)
# print(result1, result2)

# _____________________________________    Task 2    _____________________________________
# Напишите программу, которая принимает два списка и возвращает список, содержащий только
# уникальные элементы из обоих списков.
# Создайте функцию unique_elements, которая принимает два списка в качестве аргументов и
# возвращает список уникальных элементов. Используйте множества для фильтрации дубликатов. Выведите результат на экран.
# Примеры списков:
# 1, 2, 3, 4, 5
# 4, 5, 6, 7, 8
# Пример вывода:
# Уникальные элементы: 1, 2, 3, 4, 5, 6, 7, 8

# __ 1-st Variant __
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# def check_unique(list1, list2):
#     new_mas = list(set(list1).union(set(list2)))        # -- // --
#     # new_mas = list(set(list1) | set(list2))           # The SAME to -- // --
#     new_mas.sort()                                      # Sorting.
#     return new_mas
#
# print(check_unique(list1, list2))

# __ 2-nd Variant __
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# def check_unique(list1, list2):
#     new_mas = list(set(list1).union(set(list2)))        # -- // --
#     # new_mas = list(set(list1) | set(list2))           # The SAME to -- // --
#     new_mas.sort()                                      # Sorting.
#     return new_mas
#
# print(check_unique(list1, list2))

# __ 3-d Variant __
# a = {1, 2, 3, 4, 5, 9}
# b = {4, 5, 6, 7, 8}
# def unique_elements(a,b):
#     res = a.union(b)
#     return list(sorted(res))
#
# total = unique_elements(a,b)
# print(total)

# __ 4-th Variant __
# list1 = ['3, 4, 5']
# list2 = ['4, 5, 6']
# print(set(list1 + list2))
# def get_uniq_elements(list1, list2):
#     return list(set(list1 + list2))
# result = get_uniq_elements(list1, list2)
# print("Uniq data:", result)

# __ 5-th Variant __
# list1 = ['3', '4', '5']
# list2 = ['4', '5', '6']
# print(set(list1 + list2))
# def get_uniq_elements(list1, list2):
#     return sorted(list(set(list1 + list2)))
# result = get_uniq_elements(list1, list2)
# print("Uniq data:", result)


# _____________________________________    Task 3    _____________________________________
# Оригинальный список с вложенными списками:
# original_list = [[1, 2, 3], 'Hi', 10, [4, 5, 6], [7, 8, 9]]
# original_list = [[[[[[1, 0], 0], 0], 0], 2, 3], 'Hi', 10, [4, 5, 6], [7, 8, 9]]
# print(f'\t\t\t{original_list}')
# # копия списка:
# deep_copied_list = original_list.copy()
# # Изменим элемент в оригинальном списке:
# original_list[0][0] = 99
# # Выводим результаты:
# print("Оригинальный список:", original_list)
# print("Глубокая копия:", deep_copied_list)

# __ 1-st STEP - Функция для глубокой копии:
def deep_copy(list1):
    result = []
    for i in list1:
        # if type(i) == list:                   # -- // --
        if isinstance(i, list):                 # The SAME to -- // --
            result.append(deep_copy(i))
        else:
            result.append(i)
    # print(list1 is result)
    return result

# Оригинальный список с вложенными списками:
original_list = [[1, 2, 3], 'Hi', 10, [4, 5, 6], [7, 8, 9]]
print(f'{str(original_list).rjust(70, ' ')}')
# копия списка, который имеет ссылки на такие же объекты, НО по другим адресам,
# чтобы не менялся original_list, если мы будем менять, например, элемент в [1, 2, 3]:
deep_copied_list = deep_copy(original_list)                 # Здесь ставим ДЕБАГ и смотрим, как работает цикл.
print('----------------------------')
# print(id(original_list))
# print(id(deep_copied_list))
# print('----------------------------')
# print(id(original_list[0]))
# print(id(deep_copied_list[0]))

# Изменим элемент в оригинальном списке:
original_list[0][0] = 99
# Выводим результаты:
print(f'Оригинальный список: {str(original_list).rjust(50, ' ')}')
print(f'Глубокая копия: {str(deep_copy(original_list)).rjust(55, ' ')}')



