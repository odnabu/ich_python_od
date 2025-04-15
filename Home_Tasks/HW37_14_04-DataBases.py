# Homework 36, 13.04.25
""" ___ 71-72: Data Bases """
from numpy.ma.extras import column_stack

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
# -----------------------------------------------------------
print('.' * 130)


part_1 = '______ Task 1 _____'
""" ______  Task 1  ______________________________________________________________________________________________ """
# В базе данных ich_edit три таблицы:       Базы с большой буквы - ПУСТЫЕ!!!
#   1) users с полями (id, name, age),
#   2) products с полями (pid, prod, quantity),
#   3) sales с полями (sid, id, pid).
# Программа должна запросить у пользователя название таблицы и вывести все ее строки
# или сообщение, что такой таблицы нет.

# +++++++++++++++++++++++
import mysql.connector
# +++++++++++++++++++++++
l = 70
dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database': 'ich_edit',}

# Подключение базы данных ich_edit:
conn = mysql.connector.connect(**dbconfig)
# Создание объекта курсора для выполнения SQL-запросов:
cursor = conn.cursor()
print(f'{'___ Подключение успешно! ':_<{l}}')


try:
    # name_table = input('Enter the name one of table (users, products or sales): ')
    name_table = 'sales'
    # ___ Описание таблицы: __________________
    cursor.execute(f'DESCRIBE {name_table}')
    table_info = cursor.fetchall()
    # print(table_info)
    # ___ Названия заголовков: __________________
    # for item in table_info:                             # Этот вариант НЕудачный, т.к. только для просмотра.
    #     print(item[0])
    column_names = [item[0] for item in table_info]      # Такой вариант лучше - элегантнее и для дальнейшего использования подходит.
    print(f'\tName of columns: {column_names}')
    column_names_iter = map(lambda x: x.lower(), column_names)
    print(f'\tLIST of column names: {list(column_names_iter)}')
    pairs_column_name = zip(column_names, table_info)
    print(list(pairs_column_name))
    d = dict(pairs_column_name)
    print(d)
    print(f'{'':=<{l}}')

    # cursor.execute(f'SELECT * FROM {name_table}')
    # for row in res:
    #     print(row)
except mysql.connector.errors.ProgrammingError as err:
    notice = f'\033[31mERROR\033[m'
    print(f'{'':><{l}}\n'
          f'{notice:15}{err}\nTry another name from the available ones.'
          f'\n{'':><{l}}')

# Закрытие курсора:
cursor.close()
# Закрытие соединения:
conn.close()



part_2 = '______ Task 2 _____'
""" ______  Task 2  ______________________________________________________________________________________________ """
# В базе данных ich_edit три таблицы:
#   1) Users с полями (id, name, age),
#   2) Products с полями (pid, prod, quantity),
#   3) Sales с полями (sid, id, pid).
# Программа должна вывести все имена из таблицы users, дать пользователю выбрать одно
# из них и вывести все покупки этого пользователя.




