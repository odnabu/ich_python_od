# Homework 36, 13.04.25
""" ___ 71-72: Data Bases """

# Video Practice 71-72: _______________________
# Video Lesson 73: _______________________
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
# print(f'\tName: {p.name:<10}')
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Ctrl+Alt+L - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------++-
print('.' * 130)


part_1 = '______ Task 1 _____'
""" ______  Task 1  ______________________________________________________________________________________________ """
# В базе данных ich_edit три таблицы:       Базы с большой буквы - ПУСТЫЕ!!!
#   1) users с полями (id, name, age),
#   2) products с полями (pid, prod, quantity),
#   3) sales с полями (sid, id, pid).
# Программа должна запросить у пользователя название таблицы и вывести все ее строки
# или сообщение, что такой таблицы нет.


# # +++++++++++++++++++++++
# import mysql.connector
# # +++++++++++++++++++++++
# dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
#             'user': 'ich1',
#             'password': 'password',
#             'database': 'ich_edit',}
#
# # Подключение базы данных ich_edit:
# conn = mysql.connector.connect(**dbconfig)
# # Создание объекта курсора для выполнения SQL-запросов:
# cursor = conn.cursor()
# l = 60
# print(f'{'___ Подключение успешно! ':_<{l}}')
#
#
# try:
#     # name_table = input('Enter the name one of table (users, products or sales): ')
#     name_table = 'sales'
#     # ___ Содержимое таблицы: ___________________________________
#     cursor.execute(f'SELECT * FROM {name_table}')
#     table_content = cursor.fetchall()
#     # for row in table_content:
#     #     print(row, '   -->   ',len(row))
#     # === HEADERS of COLUMN =====================================
#     # ___ Описание таблицы: _____________________________________
#     # print(f'{'___ Table INFO: ':_<{l}}')
#     cursor.execute(f'DESCRIBE {name_table}')
#     table_info = cursor.fetchall()
#     # print(table_info)
#     # ___ Названия заголовков & колонки таблицы: __________________
#     table_names = [el[0] for el in table_info]
#     print(f'{'___ Column names & Values: ':_<{l}}')
#     t = 5
#     column_names_str = f'{'':{t}}'.join(table_names)
#     print(f'\t{column_names_str}')
#     for row in table_content:
#         e = f'{'':{t + 2}}'.join(str(row).strip('()').split(', '))
#         print(f'\t {e}')
#     # ___ Для дальнейшего использования в виде СЛОВАРЯ: ___________
#     print(f'\n{'___ CONCATENATE column Names with Values: ':_<{l}}')
#     pairs_each_row = [dict(zip(table_names, item)) for item in table_content]
#     # print(pairs_each_row)
#     for item in pairs_each_row:
#         print(f'\t{item}')
#     print(f'{'':=<{l}}')
#
# except mysql.connector.errors.ProgrammingError as err:
#     notice = f'\033[31mERROR\033[m'
#     print(f'{'':><{l}}\n'
#           f'{notice:15}{err}\nTry another name from the available ones.'
#           f'\n{'':><{l}}')
# finally:
#     # Закрытие курсора:
#     cursor.close()
#     # Закрытие соединения:
#     conn.close()



part_2 = '______ Task 2 _____'
""" ______  Task 2  ______________________________________________________________________________________________ """
# В базе данных ich_edit три таблицы:
#   1) users с полями (id, name, age),
#   2) products с полями (pid, prod, quantity),
#   3) sales с полями (sid, id, pid).
# Программа должна вывести все имена из таблицы users, дать пользователю выбрать одно
# из них и вывести все покупки этого пользователя.

# ++++++++++++++++++++++
import mysql.connector
# ++++++++++++++++++++++

dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database': 'ich_edit',}

# Подключение базы данных ich_edit:
conn = mysql.connector.connect(**dbconfig)
# Создание объекта курсора для выполнения SQL-запросов:
cursor = conn.cursor()
l = 60
print(f'{'___ Подключение успешно! ':_<{l}}')


try:
    t_users = 'users'
    t_sales = 'sales'
    t_product = 'product'
    # ___ Список имен в БД users: ____________________________
    # cursor.execute(f'SELECT COUNT(*) FROM {name_table}')      # Кол-во записей в БД.
    cursor.execute(f'SELECT name FROM {t_users} '
                   f'GROUP BY name ORDER BY name ASC ')         # LIMIT 5 - для удобства отработки кода.
    list_tables = cursor.fetchall()
    print(f'\n{'___ NAMES in DB ' + t_users + ': ':_<{l}}')
    for index, name in enumerate(list_tables):
        print(f'\t{index} - {name[0]}')
    # ___ Ввод пользователем имени клиента: __________________
    # user_name = input('Choose one of the NAME from the list above: ')
    user_name = '_John'
    print(f'\n{'___ List of ' + user_name + ' purchases: ':_<{l}}')
    # ___ ЗАПРОС _____________________________________________
    query = (f'SELECT * FROM {t_users} '
             f'     INNER JOIN {t_sales} ON {t_users}.id = {t_sales}.id  '
             f'     INNER JOIN {t_product} ON {t_product}.pid = {t_sales}.pid '
             f'WHERE name = \'{user_name}\' ')
    cursor.execute(query)           # Выполнение запроса.
    f_all = cursor.fetchall()       # Выведение результата на экран.
    # print(f_all)      # [(7, 'John', 25, 4, 1, 7, 1, 'first', 20), ...]
    # ___ Проверка, НЕ является результат cursor.fetchall() пустым списком:
    if f_all:
        for row in f_all:
            print(f'\t{row}')
    else:
        print(f'\tClient {user_name} did\'nt make any purchases.')

except mysql.connector.errors.ProgrammingError as err:
    notice = f'\033[31mERROR\033[m'
    print(f'{'':><{l}}\n'
          f'{notice:15}{err}\nTry another name from the available ones.'
          f'\n{'':><{l}}')
finally:
    # Закрытие курсора:
    cursor.close()
    # Закрытие соединения:
    conn.close()

