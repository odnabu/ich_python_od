# pip install mysql-connector-python

import mysql.connector

dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
             'user': 'ich1',
             'password': 'password',
             # 'database': 'hr',              # <<<<< !!! >>>>>
             'database': 'ich_edit',
             # 'port': 3306
            }
conn = mysql.connector.connect(**dbconfig)
# conn = mysql.connector.connect(
#     host='ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
#     user='ich1',
#     password='password',
#     database='hr'
# )

# # Подключение к базе данных
# conn = mysql.connector.connect(
#     host='ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',  # Адрес сервера
#     user='ich1',
#     password='password',
#     database='hr'
# )

# # Подключение к базе данных
# conn = mysql.connector.connect(
#     host='mysql.itcareerhub.de',  # Адрес сервера
#     user='ich1',
#     password='ich1_password_ilovedbs',
#     database='290724_test'
# )

# Создание объекта курсора для выполнения SQL-запросов:
cursor = conn.cursor()

# query = "SELECT * FROM employees"
# Пример запроса
# cursor.execute(query)
# emp = cursor.fetchall()
cursor.execute("SELECT * FROM sales")
# cursor.execute("SELECT * FROM employees")
# cursor.execute("SELECT * FROM employees where employee_id = 103")
# cursor.execute("SELECT * FROM employees where employee_id = %s", (103,))

# query_emp = "SELECT * FROM employees where employee_id = %s or last_name = %s"
# person = (103, "King")
# cursor.execute(query_emp, person)
# person = (104, "Hunold")
# cursor.execute(query_emp, person)
# cursor.execute("SELECT * FROM employees where employee_id = %(id)s", {'id': 103})

# cursor.execute("SELECT * FROM employees "
#                "where employee_id = %(id)s or last_name = %(ln)s",
#                {"ln": "King", 'id': 103})        # <<<<< !!! >>>>>

# print(type(cursor))
# emp = cursor.fetchone()
# emp = cursor.fetchall()
# print(emp)

l = 70

print(f'{'___ Content of table sales.ich_edit on ICH connection: ':_<{l}}')
# emps = cursor.fetchmany(3)        # <<<<< !!! >>>>>
emps = cursor.fetchall()
# print(emps)
# for emp in emps:
#     print(f'\t{emp}')
print("-----------------------")
cursor.reset()


""" ____ Добавить ЗАГОЛОВКИ к выводу содержимого таблицы: ___ """

print(f'{'___ Table INFO: ':_<{l}}')
# cursor.execute("DESCRIBE employees")
cursor.execute("DESCRIBE sales")
table_info = cursor.fetchall()
# print(f'\t{table_info}')

print(f'{'___ Name of columns in list - 1-st Variant: ':_<{l}}')
table_names = [el[0] for el in table_info]
# print(f'\t{table_names}')

print(f'{'___ Name of columns in list - 2-nd Variant: ':_<{l}}')
table_names_iter = map(lambda l: l[0], table_info)
# for r in table_names_iter:      # separate in each row.
#     print(f'\t{r}')
# print(f'\t{list(table_names_iter)}')    # LIST view.

print(f'{'___ Column names & Values: ':_<{l}}')
t = 5
column_names_str = f'{'':{t}}'.join(table_names_iter)
print(f'\t{column_names_str}')
# print(f'\t{''.join(table_names)}')
# print(*emps, sep='\n')
# for emp in emps:
#     print(f'\t{emp}')       # 	(1, 1, 6)
for emp in emps:
    e = f'{'':{t+2}}'.join(str(emp).strip('()').split(', '))
    print(f'\t {e}')


print(f'{'___ CONCATENATE column names with values: ':_<{l}}')
pairs = zip(table_names, emps)
# print(list(pairs))
# print(emps)
# print([item for item in emps])
# # ____ It's look the best the Variant for dictionary:
pairs_each_row = [dict(zip(table_names, item)) for item in emps]    # [{'sid': 1, 'pid': 1, 'id': 6}, ...]
print(pairs_each_row)

# for r in pairs:
#     print(r)
d = dict(pairs)       # То же самое, что и в 2-х строках выше, только в виде словаря.
# for k, v in d.items():
#     for item in v:
        # print(d)



# print(*emps, sep='\n')
# emp = cursor.fetchall()
# print()



# # print(emp[0:2])
#
# # for table in cursor.fetchall():
# #     print(table)
#
# cursor.execute('SHOW TABLES')
# # for i in cursor.fetchall():
# #     print(i[0])
#
# for i, *_ in cursor.fetchall():
#     print(i)

# tab = input("Choose table: ")
# cursor.execute(f"describe {tab}")
# res = cursor.fetchall()
# for el in res:
#     print(el)
#
# cursor.execute(f"SELECT * FROM {tab}")
# res = cursor.fetchall()
# for el in res:
#     print(el[1])

# Закрытие курсора
cursor.close()
# Закрытие соединения
conn.close()
