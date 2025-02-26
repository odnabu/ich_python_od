# Home Work 21, 11.02.25
# ___ 40: Collection. ___
# Normal  \033[0;__;__m \033[m    or   BOLD  \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
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
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# -----------------------------------------------------------
print('.' * 140)

part_1 = '______ Task 1 _____'
# ______  Task 1  ____________________________________________________________________________________________________
# Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте и выводит на экран
# наиболее часто встречающиеся слова. Для решения задачи используйте класс Counter из модуля collections.
# Создайте функцию count_words, которая принимает текст в качестве аргумента и возвращает словарь с
# количеством вхождений каждого слова. Выведите наиболее часто встречающиеся слова и их количество.
#   Пример вывода:
# Введенный текст: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
# sed: 2
# Lorem: 1
phrase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est!.. Sed sed lacinia est!'

from collections import Counter

# w_count = Counter(list(phrase.split()))
# print(w_count)

# See Les40_10_02_Collection.py, Task 3 with "# __ NB! __ Phrase without any signs."
def count_words(text, numb_of_most_pop):
    only_letters = []
    for s in text:                                      # Достаю только буквы и пробелы (т.е. без знаков препинания).
        if s.isalpha() or s.isspace():
            only_letters.append(s)
    new_text = ''.join(only_letters)                    # Снова возвращаю строку - соединяю последовательно буквы с пробелами и -->
    new_text = list(new_text.lower().split())           # --> преобразую в список с маленькими буквами.
    c_w = Counter(new_text)
    all_pairs = []                                      # Новая коробка для хранения пар из Counter().
    for k, v in c_w.items():                            # Разбираю словарь на ключи и значения и -->
        pair = (k, v)                                   #  --> собираю в пару.
        all_pairs.append(pair)                          # Пару кладу в новую коробку для пар.
    # all_pairs.sort(key=lambda x: x[1], reverse=True)        # Сортируем по всем вторым (с индексом [1]) элементам кортежей.
    all_pairs.sort(key=lambda x: -x[1])                 # так ЛУЧШЕ!!! сортировать по всем вторым элементам кортежей (с индексом [1]), НО во ОБРАТНОМ порядке (-x[1]).
    first_max = []                                      # Новая коробка для первых 3-х самых популярных.
    for i in range(numb_of_most_pop):
        first_max.append(all_pairs[i])
    return first_max                                    # c_w.most_common(3)

res = count_words(phrase, 3)
# print(res)
# print(f'Введенный текст: {phrase} \n{res[0][0]}: {res[0][1]} \n{res[1][0]}: {res[1][1]} \n{res[2][0]}: {res[2][1]}')
output = "\n".join([f"{item[0]}: {item[1]}." for item in res])   # Попросила Копилот преобразовать простыню кода в компактную запись ч/з (list comprehension)
print(f'Введенный текст: {phrase} \n{output}', '\n', '.' * 80)

# ______  Task 2  ____________________________________________________________________________________________________
# Напишите программу, которая создает именованный кортеж Person для хранения информации о человеке,
# включающий поля name, age и city. Создайте список объектов Person и выведите информацию о каждом человеке на экран.
#   Пример вывода:
# Name: Alice, Age: 25, City: New York
# Name: Bob, Age: 30, City: London
# Name: Carol, Age: 35, City: Paris

# See "... именованные кортежи в Python", https://sky.pro/media/kak-sozdat-i-ispolzovat-imenovannye-kortezhi-v-python/
from collections import namedtuple
def create_person(name, age, city):
    person = namedtuple('Person', ['name', 'age', 'city'])
    return person(name, age, city)

pers1 = create_person('Alice', 25, 'New York')
pers2 = create_person('Bob', 30, 'London')
pers3 = create_person('Carol', 35, 'Paris')

def print_person(*person):
    for p in person:
        print(f'\tName: {p.name:<10} Age: {p.age:<10} City: {p.city:<10}')

# print_person(pers1, pers2, pers3)

# ---------------------------------------------- NOT WORKS !   See HW14_16_01_Func_Tuple.py, Task 2, "___ Clear code..."
# def input_numb_list(*person):
#     while True:
#         list_of_persons = []
#         person = input('Enter a list of data separated by space. \nTo end the list print "stop" :  ').split()
#         # ------------------------------------------
#         # person = [d for d in input('Enter a list of data separated by space. \nTo end the list print "stop" :  ').split()]
#         # name, age, city = person_data[0], person_data[1], person_data[2]
#         # Person = namedtuple("Person", "name age city")
#         list_of_persons.append(person)
#         # ------------------------------------------
#         if person == 'Stop'.lower():
#             break
#         return list_of_persons
#
# l_p = input_numb_list()
#
# def create_person(**kwargs):
#     person = namedtuple('Person', ['name', 'age', 'city'])
#     return person(kwargs)
# ---------------------------------------------- NOT WORKS !!!!!!


# ______  Task 3  ____________________________________________________________________________________________________
# Напишите программу, которая принимает словарь от пользователя и ключ, и возвращает значение для указанного ключа
# с использованием метода get или setdefault. Создайте функцию get_value_from_dict, которая принимает словарь и
# ключ в качестве аргументов, и возвращает значение для указанного ключа, используя метод get или setdefault
# в зависимости от выбранного варианта. Выведите полученное значение на экран.
#   Пример словаря:
# my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
#   Пример вывода:
# Введите ключ для поиска: banana
# Использовать метод get (y/n)? y
# Значение для ключа 'banana': 6

my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
# test_key = 'banana'

# print(".get(\"apple\")     --> ", my_dict.get("apple"))                         # Выводит 5.
# print(".get(\"grape\")     --> ", my_dict.get("grape"))                         # Выводит None.
# print(".get(\"grape\") + 0 --> ", my_dict.get("grape", 0), '\n', '.' * 55)      # Выводит 0, так как ключа "grape" нет в словаре.

# print(".setdefault(\"apple\", 10) --> ", my_dict.setdefault("apple", 10))       # Т.к. ключ существует, возвращает соответствующее значение 5.
# print(".setdefault(\"grape\", 10) --> ", my_dict.setdefault("grape", 15))       # Выводит 15 и ДОБАВЛЯЕТ новую пару ключ-значение.
# print(my_dict, '\n', '.' * 55)                                                  # Выводит {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 15}

def input_test_key(some_key):
    some_key = input("Enter a key for searching: ")
    return some_key

def get_value_from_dict(dictionary, some_key):
    ask = input("To use method .get() enter \"g\". To use method .setdefault() enter \"s\": ").lower()
    if ask == 'g':
        return dictionary.get(some_key)
    else:
        return dictionary.setdefault(some_key)

def print_value(input_key, input_res):
    if input_res is not None:
        print(f'Value for key {input_key}: \033[36m{input_res}\033[m.')
    else:
        print(f'Value for key {input_key}: \033[1;31m{input_res}\033[m.')

# test_key = input_test_key(my_dict)
# res = get_value_from_dict(my_dict, test_key)
# print_value(test_key, res)



