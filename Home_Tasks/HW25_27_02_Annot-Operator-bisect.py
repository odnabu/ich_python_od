# Home Work 26, 24.02.25
""" ___ 48-49: Annotations. Operators. bisect ___ """
import os
from sys import exec_prefix

# Video Lesson 48: ______________________
# Video Practice 49: _______________________
# Normal  \033[0;__;__m \033[m    or   BOLD  \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ############################################################################################################### """
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
print('.' * 130)


part_1 = '______ Task 1 _____'
""" ______  Task 1  ______________________________________________________________________________________________ """
# Напишите функцию find_longest_word, которая будет принимать список слов и возвращать самое длинное слово из списка.
# Аннотируйте типы аргументов и возвращаемого значения функции.
# Пример вызова функции и ожидаемого вывода:
# words = ["apple", "banana", "cherry", "dragonfruit"]
# result = find_longest_word(words)
# print(result)         # Ожидаемый вывод: "dragonfruit"

# def find_longest_word(list_words: list) -> str:
#     return max(list_words)
#
# words = ["apple", "banana", "cherry", "dragonfruit"]
# result = find_longest_word(words)
# print(f'The longest word is \033[35m{result}\033[m.')


part_2 = '______ Task 2 _____'
""" ______  Task 2  ______________________________________________________________________________________________ """
# Напишите программу, которая будет считывать данные о продуктах из файла и использовать аннотации типов для
# аргументов и возвращаемых значений функций. Создайте текстовый файл "products.txt", в котором каждая строка будет
# содержать информацию о продукте в формате "название, цена, количество". Например:
# Apple, 1.50, 10
# Banana, 0.75, 15
#
# В программе определите функцию calculate_total_price, которая будет принимать список продуктов и
# возвращать общую стоимость. Продумайте, какая аннотация должна быть у аргумента!
# Считайте данные из файла, разделите строки на составляющие и создайте список продуктов.
# Затем вызовите функцию calculate_total_price с этим списком и выведите результат.

# +++++++++++++++++++++++++++++++++
from typing import Union
import os                               # Подключение модуля os для работы с файлами.
# +++++++++++++++++++++++++++++++++

# ___ 1-st Variant - Simple. ___
def calculate_total_price(file: Union[str, float, int]) -> float:
    file = open(file)                                                 # Можно вынести за функцию.
    total = 0
    for line in file:
        line = line.rstrip().split(', ')
        total += float(line[1]) * int(line[2])
    # print(f'The total price is \033[35m{total:.2f}\033[m.')
    return total

result = calculate_total_price("products.txt")
print(f'The total price is \033[35m{result:.2f}\033[m.')


# # ___ 2-nd Variant: step by step with Technical specifications. ___

# # -1- Функция проверки существования файла:
# def validate_file_name(file_name: str) -> str:
#     if not os.path.exists(file_name):
#         raise FileNotFoundError("Невозможно открыть файл")
#     else:
#         return file_name
#
# # -2- Функция считывания данных из файла (преобразование строковых данных в числа), и возвращение их списком:
# from typing import Generator, List, Tuple
#
# # Генератор чтения данных из файла:
# def get_data_list(file) -> Generator[Tuple[str, float, int], None, None]:
#     for line in file:
#         name, price, amount = line.strip().split(', ')
#         yield name, float(price), int(amount)           # Построчно отдает данные.
#
# # Генератор подсчета общей стоимости:
# def calculate_total_price(products: List[Tuple[str, float, int]]) -> Generator[float, None, None]:
#     for name, price, amount in products:
#         yield price * amount
#         # print(total_price)
#
#
# file = None
# try:
#     f_name = validate_file_name("products.txt")
#     if f_name:
#         file = open(f_name, 'r')
#         products_list = list(get_data_list(file))           #
#         for index, product in enumerate(products_list, start = 1):
#             print(f'{index:>3}. {product[0]}')
#         total_price = sum(calculate_total_price(products_list))
#         print(f'{'-' * 30}\nThe total price is \033[35m{total_price:>7.2f}\033[m')
# except FileNotFoundError as e_fnf:
#     notice_fnf = f"\033[31m{e_fnf}\033[m"
#     print(f"{notice_fnf}: возможно ошибка в имени или адресе файла.")
# except ValueError as e_v:
#     notice_v = f"\033[31m{e_v}\033[m"
#     print(f"Ошибка в файле, возможно неверный формат данных: {notice_v}")
# finally:
#     if file:
#         file.close()
#     print('Файл закрыт.')


""" __ NB! ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Начиная с этого дз мы потихоньку отказываемся от формата ожидаемого ввода-вывода. 
# Потому что в реальных задачах обычно этого нет. Нужно самому придумывать даже самые простые тестовые данные, 
# содержимое тестовых файлов и т.п. В случае с классами (будут чуть позже) особенно.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ """




