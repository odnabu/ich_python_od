# Homework 38, 13.04.25
""" ___ 1-76: REVISION + Data Bases """

# Video Practice 76: _______________________
# Video Lesson __: was'nt
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
# 1) Вывести список таблиц в базе данных.
# 2) Предоставить пользователю выбрать таблицу из предложенных.
# 3) Ввести список полей выбранной таблицы.
# 4) Позволить искать значение по определенному полю.
# 5) При вводе искомого значения добавить возможность выбора знака - найти записи, в которых выбранное поле больше, меньше или равно введенному значению.


# +++++++++++++++++++++++
import mysql.connector
# +++++++++++++++++++++++
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
    # ___ 1) Список таблиц в БД ich_edit: ___________________________
    print(f'{'___ List of tables in DB "ish_edit" ':_<{l}}')
    cursor.execute('SHOW TABLES')
    table_list = cursor.fetchall()
    # print(table_list)
    # for index, table in enumerate(table_list, start=1):
    #     print(f'{index} - {table[0]}')
    # ___ 2) Выбор пользователем таблицы: ____________________________
    print(f'{'___ Choosing the table ':_<{l}}')
    # user_table = input('Enter the table name from the list above: ')
    user_table = 'Denis_logs'; print(user_table)
    # ___ 3) Список полей таблицы: ___________________________________
    print(f'{'___ Field HEADERS in selected table ':_<{l}}')
    # ___ Названия заголовков: _______________________________________
    cursor.execute(f'SHOW COLUMNS FROM {user_table}')
    columns_info = cursor.fetchall()
    column_title = [field[0] for field in columns_info]
    # print(column_title)
    t_0 = 4; t_s = 8; t_b = 17
    # column_names_str = f'{'':{t}}'.join(column_title)
    column_names_str = ''
    for i in column_title:
        c_title = str(i).strip('()')
        if len(str(i)) > t_0:
            # column_names_str += f'{str(i).strip('()'):{len(str(i))+5}}'
            column_names_str += f'\033[40;36m{c_title:{t_b}}\033[m'
        else:
            column_names_str += f'\033[40;36m{c_title:{t_s}}\033[m'
    print(f'\t{column_names_str}')
    # for index, field in enumerate(cursor.fetchall(), start=1):
    #     print(f'{index} - {field[0]}')
    # ___ Содержимое колонок: ________________________________________
    # print(f'{'___ List of field CONTENTS in selected table ':_<{l}}')
    cursor.execute(f'SELECT * FROM {user_table} LIMIT 1')
    table_content = cursor.fetchall()
    # table_content = cursor.fetchmany(10)
    # print(table_content)
    # --------------------------
    for row in table_content:
        row_string = ''
        for i in row:
            c_title = str(i).strip('()')
            if len(str(i)) > t_0:
                row_string += f'{c_title:{t_b}}'
                # row_string += f'{str(i).strip('()'):{len(str(i))+5}}'
            else:
                row_string += f'{c_title:{t_s}}'
        print(f'\t{row_string}')
    # ___ 4) Поиск значения по определенному полю: ___________________
    print(f'{'___ Searching value ':_<{l}}')


except mysql.connector.errors.ProgrammingError as err:
    notice = f'\033[31mERROR\033[m'
    print(f'{'':><{l}}\n'
          f'{notice:15}{err}\nTry another name.'
          f'\n{'':><{l}}')
finally:
    # Закрытие курсора:
    cursor.close()
    # Закрытие соединения:
    conn.close()



