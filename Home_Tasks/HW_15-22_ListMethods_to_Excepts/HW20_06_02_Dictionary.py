# Home Work 20, 06.02.25
# ___ 38: Dictionaries. ___
# Normal  \033[0;__;__m \033[m    or   BOLD  \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# f = 40; f = '.' * f; print(f) - Filler up to.
# print(f, f'\n...')
# print(' ' * 5, f'...') - Indentation in the output of the result
# while True:
#   ...
#   ask = input("\nDo you want to continue? (y/n): ").lower()
#   if ask == 'n':
#       break
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# -----------------------------------------------------------
print('.' * 140)
part_1 = '______ Задачник Python_TfS38 _____'
# ______ Задачник Python_TfS38 _____  Task 1  _____________________________________
# Создание и вывод словаря:
# Описание: Создайте словарь с ключами "name", "age", "city" и соответствующими значениями. Выведите словарь.

# __-st Variant __
# another_dict = dict([("name", "Jane"), ("age", 30)])
# print(another_dict)

# __ 2-nd Variant __
# def input_dictionary(**kwargs):
#     return kwargs
#
# my_dict_1 = input_dictionary(year=2025, month="January", day=9)
# print(my_dict_1)

# ______ Задачник Python_TfS38 _____  Task 2  _____________________________________
# Доступ к элементам:
# Описание: Дан словарь person из предыдущей задачи. Получите и выведите значение по ключу "age".

# person = input_dictionary(name="Olga", age=48, city="Dessau-Rosslau")
# print(person, '\n', '.' * 80)
# print(person["age"], '\n', '.' * 80)            # выведите значение по ключу "age".

# ______ Задачник Python_TfS38 _____  Task 3  _____________________________________
# Изменение элементов:
# Описание: Измените значение "city" в словаре person на "Boston" и выведите обновленный словарь.
# person["city"] = "Nazare"
# print(person, '\n', '.' * 80)

# ______ Задачник Python_TfS38 _____  Task 4  _____________________________________
# Добавление новых пар ключ-значение:
# Описание: Добавьте новую пару ключ-значение "hobby": "painting" в словарь person и выведите словарь.
# person["Country"] = "Portugal"
# print(person, '\n', '.' * 80)

# ______ Задачник Python_TfS38 _____  Task 5  _____________________________________
# Удаление элементов:
# Описание: Удалите из словаря person ключ "hobby" и выведите результат.
# del person["Country"]
# print(person, '\n', '.' * 80)

# ______ Задачник Python_TfS38 _____  Task 6  _____________________________________
# Проверка наличия ключа:
# Описание: Проверьте, существует ли ключ "email" в словаре person. Выведите соответствующее сообщение.
# print("email" in person, '\n', '.' * 80)

# ______ Задачник Python_TfS38 _____  Task 7  _____________________________________
# Итерация по ключам:
# Описание: Итерируйте по всем ключам словаря person и выведите их.
# def iterate_keys(dictionary):
#     for el in dictionary:
#         return dictionary.keys()
#
# keys_pairs = iterate_keys(person)
# print("Итерация по ключам --> ", keys_pairs, '\n', '.' * 80)

# ______ Задачник Python_TfS38 _____  Task 8  _____________________________________
# Итерация по значениям:
# Описание: Итерируйте по всем значениям словаря person и выведите их.
# def iterate_values(dictionary):
#     for el in dictionary:
#         return dictionary.values()
#
# values_pers = iterate_values(person)
# print(values_pers, '\n', '.' * 80)

# ______ Задачник Python_TfS38 _____  Task 9  _____________________________________
# Итерация по парам ключ-значение:
# Описание: Итерируйте по парам ключ-значение словаря person и выведите их в формате "ключ: значение".
# def iterate_pairs(dictionary):
#     for el in dictionary:
#         return dictionary.items()
#
# pares = iterate_pairs(person)
# print(pares, '\n', '.' * 80)

# ______ Задачник Python_TfS38 _____  Task 10  _____________________________________
# Создание словаря из списков:
# Описание: Даны два списка: keys = ["a", "b", "c"] и values = [1, 2, 3]. Создайте словарь,
# используя эти списки, где элементы первого списка будут ключами, а второго — значениями.
# def make_dictionary(list1, list2):
#     return dict(zip(list1, list2))          # Функция zip() используется для совмещения двух и более списков в один.
#                                             # возвращает итератор кортежей.
# keys = ["a", "b", "c"]                      # https://sky.pro/media/rabota-s-funkcziej-zip-v-python/
# values = [1, 2, 3]
# new_dict = make_dictionary(keys, values)
# print(new_dict, '\n', '.' * 80)

# Также функция zip() может быть использована для «расстегивания» списка кортежей обратно в отдельные списки.
# Для этого используется оператор «*». Он позволяет преобразовать список в набор аргументов для функции.
# https://sky.pro/media/rabota-s-funkcziej-zip-v-python/
# keys_for_unzip = list(new_dict.keys())
# values_for_unzip = list(new_dict.values())
# pairs_for_unzip = list(new_dict.items())
# #
# keys, values = zip(*pairs_for_unzip)
# print(f'keys --> {list(keys)} \nvalues -->  {list(values)}', '\n', '.' * 80)

# Another Variant for unpacking dictionary to list of tuples:
# https://pythonturbo.ru/preobrazovanie-slovarya-v-spisok-kortezhej-v-python/
# print("The Dictionary is:", new_dict)
# myList = []
# for k in new_dict:                              # k - key
#     value = new_dict[k]
#     myTuple = (k, value)
#     myList.append(myTuple)
# print("The list of tuples is: ", myList, '\n', '.' * 80)

# ______ Задачник Python_TfS38 _____  Task 11  _____________________________________
# Удаление элемента и возврат его значения:
# Описание: Удалите из словаря person ключ "age" и верните его значение. Если ключ отсутствует, верните "Key not found".
# print(person)
# del person["age"]
# print(f'del person["age"] --> ', person, '\n', '.' * 80)

# ______ Задачник Python_TfS38 _____  Task 12  _____________________________________
# Получение значения по ключу:          __ NB! __ See Les40
# Описание: Получите значение по ключу "name" из словаря person, используя метод get().
# Если ключ отсутствует, верните "Unknown".
# print(f'Method .get("name") --> ', person.get("name"), person, '\n', '.' * 80)

# ______ Задачник Python_TfS38 _____  Task 13  _____________________________________
# Очистка словаря:
# Описание: Очистите словарь person, удалив из него все элементы.
# person.clear()
# print(person)

# ______ Задачник Python_TfS38 _____  Task 14  _____________________________________
# Копирование словаря:
# Описание: Создайте полную копию словаря person в новую переменную person_copy и выведите её.
# person_copy = person.copy()
# print(f'person_copy --> {person_copy}', '\n', '.' * 80)

# ______ Задачник Python_TfS38 _____  Task 15  _____________________________________
# Вложенные словари:
# Описание: Создайте словарь company, содержащий информацию о двух сотрудниках. Ключами будут их имена, а значениями —
# словари с ключами "age" и "department". Выведите информацию о возрасте второго сотрудника.
# company = {
# "John": {"age": 29, "department": "Sales"},
# "Doe": {"age": 34, "department": "Marketing"}
# }
# print(company["Doe"]["age"], '\n', '\\' * 80)
print(' ' * 140)

part_2 = '______ Task 1 _____'
# ______  Task 1  ____________________________________________________________________________________________________
# Напишите функцию merge_dicts, которая принимает произвольное количество словарей в качестве аргументов
# и возвращает новый словарь, объединяющий все входные словари. Если ключи повторяются, значения должны быть
# объединены в список. Функция должна использовать аргумент **kwargs для принятия произвольного числа аргументов словаря.
# Пример ввода:
# {'a': 1, 'b': 2}
# {'b': 3, 'c': 4}
# {'c': 5, 'd': 6}
# Пример вывода:
# {'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]}
# dict_1 = {'a': 1, 'b': 2}
# dict_2 = {'b': 3, 'c': 4}
# dict_3 = {'c': 5, 'd': 6}

# Декомпозирую задачу.
# 1) сначала разделяю словари на составляющие:
#       - разделяю каждый словарь на ключи и значения - вложенными циклами: сначала иду по словарям, затем по их элементам.

# Выделяю ключи:
# def separate_keys(*dictionary):
#     d_keys = []
#     for d in dictionary:
#         for el in d:
#             d.keys()
#         d_keys.append(d.keys())
#     return d_keys
#
# print(separate_keys(dict_1, dict_2, dict_3), '\n', '.' * 80)

# Выделяю ключи и значения:
# def separate_key_val(*dictionary):
#     d_keys = []
#     d_values = []
#     for d in dictionary:
        # -------------------------
    #     pairs = list(d.items())
    #     keys, values = zip(*pairs)            # Выдаёт списки кортежей по каждому словарю.
    #     d_keys.append(keys)
    #     d_values.append(values)
    # return d_keys, d_values
        # -------------------------
    #     for el in d:
    #         d_values.append(d[el])            # Доступ по ключам к ЗНАЧЕНИЯм.
    # return d_values
    # -------------------------
    #     for k in d.keys():                    # --- !!! --- Получение отдельных списков с ключами и значениями.
    #         d_keys.append(k)
    #     for v in d.values():
    #         d_values.append(v)
    # return d_keys, d_values
#     # -------------------------
#
# print(separate_key_val(dict_1, dict_2, dict_3), '\n', '.' * 80)

# Выделяю уникальные ключи --- !!! --- :
# def separate_key_val(*dictionary):
#     d_keys = []
#     for d in dictionary:
#         for k in d.keys():
#             if k not in d_keys:
#                 d_keys.append(k)
#     return d_keys
#
# print(separate_key_val(dict_1, dict_2, dict_3), '\n', '.' * 80)

# Выделяю и проверяю значения по каждому словарю:
# def separate_key_val(*dictionary):
#     d_values = []
#     for d in dictionary:
#         val = []
#         for k in d.values():
#             val.append(k)
#         d_values.append(val)
#     return d_values
#
# print(separate_key_val(dict_1, dict_2, dict_3), '\n', '.' * 80)

# Выделяю уникальные ключи: Doesn't work to the End!
# 1) создаю новый словарь.
# 2) создаю список для значений.
# 3) для каждого словаря в списке выделяю ключи и значения с помощью метода .items().
# 4)
# def separate_key_val(*dictionary):
#     new_dict = {}
#     for d in dictionary:
#         # for k, v in d.items():
#         #     if k in new_dict:
#         #         v_list.append(v)
#         #         new_dict[k] = v_list
#         #     else:
#         #         new_dict[k] = v
#         # -----------------------------
#         sep_k_v = d.items()
#         for k, v in sep_k_v:
#             v_list = [v]
#             if k not in new_dict:
#                 new_dict[k] = v_list
#             else:
#                 v_list.append(v)
#                 new_dict[k] = v_list
#     return new_dict
#
# print(separate_key_val(dict_1, dict_2, dict_3), '\n', '.' * 80)


# ___ 1-st part of the Solution ___ it WORKS!!!!
# def separate_key_val(*dictionary):
#     d_keys = []
#     d_values = []
#     for d in dictionary:
#         for k in d.keys():                  # --- !!! --- Получение отдельных списков с ключами и значениями.
#             d_keys.append(k)
#         for v in d.values():
#             d_values.append(v)
#     return d_keys, d_values
#
# lists_k_v = separate_key_val(dict_1, dict_2, dict_3)
# # print(lists_k_v[0], '\n', lists_k_v[1])
# print(lists_k_v, '\n', '.' * 80)

# __ only [[1], [2, 3], [4, 5], [6]] as a result of function: __
# def make_list_v(lis1, lis2):
#     all_dict = {}
#     for key, value in zip(lis1, lis2):
#         if key in all_dict:
#             all_dict[key].append(value)
#         else:
#             all_dict[key] = [value]
#     list_values = list(all_dict.values())
#     return list_values
#
# list_k = lists_k_v[0]
# list_v = lists_k_v[1]
# print(make_list_v(list_k, list_v), '\n', '.' * 80)

# ___ 2-nd part of the Solution ___  it WORKS!!!!
# def make_list_v(lis1, lis2):
#     all_dict = {}
#     for key, value in zip(lis1, lis2):
#         if key in all_dict:
#             all_dict[key].append(value)
#         else:
#             all_dict[key] = [value]
#     return all_dict
#
# list_k = lists_k_v[0]
# list_v = lists_k_v[1]
# print(make_list_v(list_k, list_v), '\n', '.' * 80)

# print(dict_1, dict_2, dict_3, sep='\n')
# print('.' * 30)

# print(dict_1['a'], [dict_1['a']])
# d_list = [dict_1['a']]                # Преобразовать в список значение, полученное обращением по ключу.
# print(type(d_list))
# d_list.append(2)
# print(d_list, '\n', '.' * 80)

# ______________________ CLEAR CODE for lms + mz Comments ______________________
# def separate_key_val(*dictionary):
#     dict_new = []                                 # Новая коробка (список, который станет новым словарем), куда буду складывать результаты обработки входящих словарей.
#     new_pair = []                                 # Новая пара "ключ + значение" в новом словаре.
#     for d in dictionary:
#         for k, v in d.items():                    # Для пар: "ключ + значение" в данном словаре.
#             if k not in new_pair:                     # Если ключа ещё нет в новой паре, то -->
#                 new_pair = [k, [v]]                       # --> то новой парой становится пара с текущим ключом и преобразованным в список значением.
#                 dict_new.append(new_pair)                 # Список новых пар в новой коробке (списке).
#             elif k in new_pair:                       # Если ключ уже есть в новой паре, то -->
#                 # print(f'new_pair = {new_pair}, new_pair[1] = {new_pair[1]}')
#                 v_list = new_pair[1]                      # --> то 2-му элементу в уже существующей паре даю отдельное имя, чтобы использовать его дальше.
#                 # print(f'v = {v}, v_list = new_pair[1] = {new_pair[1]}, v_list.append(v) = {v_list.append(v)}')
#                 v_list.append(v)                          # Присоединяю ко 2-му значению ещё одно.
#                 new_pair = [k, v_list]                    # Обновляю новую пару.
#                 dict_new.append(new_pair)                 # Присоединяю обновленную пару в новую коробку.
#     res = dict(dict_new)                          # Преобразование списка с помощью dict() в словарь.
#     return res
#
# # lists_k_v = separate_key_val(dict_1, dict_2)
# lists_k_v = separate_key_val(dict_1, dict_2, dict_3)
# print(lists_k_v, '\n', '.' * 80)

# ______________________ CLEAR CODE for lms ______________________
# dict_1 = {'a': 1, 'b': 2}
# dict_2 = {'b': 3, 'c': 4}
# dict_3 = {'c': 5, 'd': 6}
#
# def separate_key_val(*dictionary):
#     dict_new = []
#     new_pair = []
#     for d in dictionary:
#         for k, v in d.items():
#             if k not in new_pair:
#                 new_pair = [k, [v]]
#                 dict_new.append(new_pair)
#             elif k in new_pair:
#                 v_list = new_pair[1]
#                 v_list.append(v)
#                 new_pair = [k, v_list]
#                 dict_new.append(new_pair)
#     res = dict(dict_new)
#     return res
#
# lists_k_v = separate_key_val(dict_1, dict_2, dict_3)
# print(lists_k_v, '\n', '.' * 80)

part_3 = '______ Task 2 _____'
# ______  Task 2  ____________________________________________________________________________________________________
# Напишите программу, которая принимает строку от пользователя и подсчитывает количество уникальных
# символов в этой строке. Создайте функцию count_unique_chars, которая принимает строку и возвращает количество
# уникальных символов. Выведите результат на экран.
# Пример вывода:
# Введите строку: hello
# Количество уникальных символов: 4

# quote_phsy = ('-1- Anything we practice, we become better at. Edith Eger, The Choice: Embrace the Possible.'
#           '-2- Whatever you practice, you become better at. Edith Eger, The Gift: 14 Lessons to Save Your Life.')
# phrase = 'hello'

# __ 1-st Variant __ - set()        https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
# def count_unique_symb1(str):
#     # res = ''.join(set(str))
#     res = set(str)
#     # print(res)
#     return len(res)
#
# print(f'Number of unique simbols1 = {count_unique_symb1(phrase)}')

# __ 2-nd Variant __ - loop for        https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
# def count_unique_symb2(str):
#     output = set()
#     for s in str:
#         output.add(s)
#     # print(output)
#     return len(output)
#
# print(f'Number of unique simbols2 = {count_unique_symb2(phrase)}', '\n', '.' * 80)

# __ 3-d Variant __ - loop for        https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
# def count_unique_symb3(str):
#     output = set()
#     unique = [s for s in str if s not in output and (output.add(s) or True)]
#     return len(unique)
#
# print(f'Number of unique simbols3 = {count_unique_symb3(phrase)}', '\n', '.' * 80)



part_4 = '______ Task 3 _____'
# ______  Task 3  ____________________________________________________________________________________________________
# Напишите программу, которая создает словарь, содержащий информацию о студентах и их оценках.
# Ключами словаря являются имена студентов, а значениями - списки оценок. Создайте функцию calculate_average_grade,
# которая принимает словарь с оценками студентов и вычисляет средний балл для каждого студента.
# Функция должна возвращать новый словарь, в котором ключами являются имена студентов, а значениями - их средний балл.
# Выведите результат на экран.
# Пример словаря с оценками:

# grades = {
#     'Alice': [85, 90, 92],
#     'Bob': [78, 80, 84],
#     'Carol': [92, 88, 95]
# }

# Пример вывода:
# {'Alice': 89.0, 'Bob': 80.66666666666667, 'Carol': 91.66666666666667}

# __ 1-st Part of Solution __
# Ввод вручную элементов записи с именем и оценками студента - See HW16_23_01_List_Matrix.py
# def input_table_of_grade():
#     while True:
#         name = input("Enter the student's name: ")
#         grades_list = [int(g) for g in input('Enter a list of grades separated by space: ').split()]
#         record = {name: grades_list}
#         ask = input("\nDo you want to continue? (y/n): ").lower()
#         if ask == 'n':
#             break
#     return record

# names_grades = input_table_of_grade()
# print(names_grades)

# __ 2-nd Part of Solution __ 1-st Variant -- WORKS!
# def calculate_average_grade(dictionary):
#     student = []
#     for key, value in dictionary.items():
#         sum = 0
#         for v in value:
#             sum += v
#         avg_grade = sum / len(value)
#         student.append([key, avg_grade])
#     result = dict(student)
#     return result
# #
# avg_res = calculate_average_grade(grades)
# print(avg_res)

# __ 2-nd Part of Solution __ 2-nd Variant -- WORKS!
# def calculate_average_grade(dictionary):
#     student = ()
#     for key, value in dictionary.items():
#         avg_grade = sum(value) / len(value)
#         student += ((key, avg_grade),)              #  __ NB! __ Добавить ЗАПЯТУЮ после первого элемента в кортеже! -->
#     result = dict(student)                          # --> see https://sky.pro/wiki/python/dobavlenie-elementov-v-kortezh-python-reshenie-oshibki-unicode/
#     return result
#
# avg_res = calculate_average_grade(grades)
# print(avg_res)

