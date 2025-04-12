# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 14.02.25
# Python 43: Summary - Dictionaries. Collections.
# ###################################################################################################################
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# -----------------------------------------------------------

print('.' * 145)


# _________________________ Review of Home Works _____________________________________________________________________

# SEE VIDEO!!! and .md.

# ______  Task 1  ____________________________________________________________________________________________________
# ** Чтение JSON-файла с товарами и расчет общей стоимости**
# Задача:
#   - Запросить у пользователя имя JSON-файла с товарами.
#   - Прочитать данные, обработать ошибки (FileNotFoundError, PermissionError, JSONDecodeError).
#   - Посчитать общую стоимость всех товаров (цена × количество). Обработать ошибки валидности данных
# [
# {"name": "яблоко", "price": 50, "quantity": 3},
# {"name": "банан", "price": 30, "quantity": 2},
# {"name": "апельсин", "price": 40, "quantity": 4}
# ]

# import json
#
# with open('products.json', encoding='utf-8') as file:
#     # my_file_json = json.loads(file.read())            # The SAME!
#     my_file_json = json.load(file)                      # The SAME!
# print(type(my_file_json))
# print(my_file_json)

import json
from json import JSONDecodeError

try:
    with open('../Les_44-55_Iterat_Func-program/products.json', encoding='utf-8') as file:
        data_products = json.load(file)
except FileNotFoundError:
    print("File not exists.")
except PermissionError:
    print("Permission denied.")
except JSONDecodeError:
    print("JSON problem")
else:
    sum = 0
    for product in data_products:
        # print(product['price'])
        try:
            sum += product['price']
        except KeyError:
            print("product is not correct - ", product)
        except TypeError:
            print("price is not correct - ", product)
    print(sum)



# ---------------------------------
# import json
# from json import JSONDecodeError
#
# try:
#     with open("products.json", encoding= "utf-8") as my_file:
#         data_products = json.load(my_file)
# except FileNotFoundError:
#     print("вашего файла не существует. возможно я его не вижу, ты не видишь, а он есть")
# except PermissionError:
#     print("у меня прав нет, дай админку")
# except JSONDecodeError:
#     print("Json шалит")
# else:
#     sum = 0
#     for product in data_products:
#         try:
#             sum += product['price']
#         except KeyError:
#             print("продукт не корректен - ", product)
#         except TypeError:
#             print("цена не корректна - ", product)
#     print(sum)