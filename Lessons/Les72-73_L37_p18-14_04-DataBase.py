# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 14.04.25
 Python 72-73: Работа с базами данных из интерфейса Python - Lecture 37, Practice 18.
 ################################################################################################################### """

# Video Lesson 72: ------------.
# Video Practice 73: ------------.
# links:
#   - Presentation:
#   -
#   -
#
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Ctrl+Akt+L / Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Ctrl+Shift + F - Найти по всем файлам.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------

print('.' * 120)

""" ___________________________________  ---  ___________________________________ """

# Video 72,

""" \\\\ __ NB! __ \\\\  isinstance(<object>, <type of data>)  -->  ПРОВЕРКА типа данных перед выполнением операций!!! """
# num = 3
# if isinstance(num, int):
#     print(num + 2)

""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%______________   Подключение к   _____________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """
"""                                                  базе данных                                                  """
# Video 72, ___

""" __________ Библиотека sqlite3 __________ """         # Video 72, 19:00
# — это библиотека, которая предоставляет возможность взаимодействия с базой данных SQLite из Python.

""" __________ Подключение к СУБД MySQL __________ """          # Video 72, 17:00
# Для работы с другими базами данных, необходимо установить соответствующую библиотеку, например,
# psycopg2 для PostgreSQL или mysql-connector-python для MySQL.
        # pip install mysql-connector-python            # Video 72, 22:00 --> pip - пакетный менеджер.
# Для подключения к базе данных нужно:
#       ● импортировать установленный модуль,
#       ● создать переменную-словарь для описания конфигурации подключения,
#       ● установить соединение.
# Базовый порт на подключение к MySQL - 3306.


# ___ EXAMPLE __________________________________________________
# # ++++++++++++++++++++++
# import mysql.connector
# # ++++++++++++++++++++++
# dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
#     'user': 'ich1',
#     'password': 'password',
#     'database': 'hr'}
# connection = mysql.connector.connect(**dbconfig)
# ___ END of Example __________________________________________________


""" __________ Работа с базой данных __________ """

""" ___ Курсор (cursor) ___ """
# — объект, с помощью которого выполняются операции с базой данных. Он представляет собой интерфейс для отправки
#   запросов и получения результатов.
""" __ NB! __ """    # Запоминает ответ запроса, чтобы потом с ним работать.

""" ___ Создание курсора ___ """
# Курсор создается из соединения (connection) с помощью метода cursor():
# cursor = connection.cursor()

""" ___ Закрытие курсора ___ """
# По завершению работы с БД курсор и соединение нужно __ЗАКРЫВАТЬ__, чтобы избежать непредвиденных ошибок и снижения
# производительности:
# Закрытие курсора:
# cursor.close()
# Закрытие соединения:
# connection.close()

""" ___ execute ___ """
# — метод, который используется для выполнения команд SQL. Он принимает строку с SQL-запросом в качестве аргумента.
# Пример использования:
# cursor.execute("SELECT * FROM users")


""" __________ fetchone, fetchall, fetchmany __________ """
# — методы, которые могут использоваться для извлечения данных из результата запроса.
# --- Даёт доступ к ИТЕРАТОРУ в cursor.
# Пример использования:
# cursor.execute("SELECT * FROM users")
# result = cursor.fetchall()
# for row in result:
#   print(row)
""" __ NB! __ """    # print(*emp, sep='\n')


""" ___ fetchall ___ """
# — метод, который возвращает все строки результата в виде списка, где каждая строка представлена кортежем или списком.
""" __ NB! __ """     # Освобождает курсор. --> Oleksii Starodubov 10:01
# fetch - команда собаке типа "апорт" или "принеси". Вот и здесь даем команду принести полученную информацию ))

""" ___ fetchone ___ """        # Video 72, 1:18:00.
# — метод, который возвращает ОДНУ строку результата.
# emp1 = cursor.fetchone()
# print(emp1)
# cercor.reset()

""" ___ fetchmany ___ """        # Video 73, 14:00. (10:54 ->)
# emp = cursor.fetchmany(3)      # Выведет только 3 элемента, даже если будет всего 2 или 1 объект.


""" ___ Метод execute ___ """
# Может принимать параметры, которые могут быть переданы в SQL-запрос с использованием специального синтаксиса.
# name = "John"
# age = 25
# cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
""" __ NB! __ """    # %s - плейсхолдер строка - String.         Video 73, 26:00. (10:54 --> 11:21... )

""" ___ executemany ___ """         # Video 73, 38:00. (11:32... )
# — это метод, который позволяет выполнить несколько операций с разными значениями параметров.
# Он принимает два аргумента: строку с SQL-запросом и последовательность кортежей или списков, содержащих
# значения параметров.
# Пример использования:
# data = [("John", 25), ("Alice", 30), ("Bob", 35)]
# cursor.executemany("INSERT INTO users (name, age) VALUES (%s, %s)", data)

""" ___ Метод commit ___ """
# — метод, который применяется после выполнения операций, которые изменяют данные в базе данных, чтобы сохранить
#   изменения. Он вызывается на объекте соединения (connection).
# После вызова commit, изменения будут фиксированы в базе данных.
# connection.commit()       # СОХРАНИТЬ изменения, внесенные в БД.


""" __________ Параметры с именованными заполнителями __________ """
# Вместо плейсхолдеров %s можно использовать имена, которые будут заменены соответствующими значениями при
# выполнении запроса.
# data = {"name": "John", "age": 25}
# cursor.execute("INSERT INTO users (name, age) VALUES (%(name)s, %(age)s)", data)

""" __________ Транзакция __________ """
# — это логическая группа операций, которые должны быть выполнены все или ни одна. Для выполнения транзакций можно
#   использовать методы commit и rollback:

#       ● Если все операции в транзакции прошли успешно, вызов commit фиксирует изменения.
#       ● В случае возникновения ошибки или отката транзакции вызывается метод rollback, который отменяет
#         все выполненные операции.

# try:
#   connection = mysql.connector.connect(**dbconfig)
#   cursor = connection.cursor()
#   # Выполнение операций в рамках транзакции
#   connection.commit()
# except:
#   connection.rollback()
# Finally:
#   cursor.close()
#   connection.close()

""" ___ Блок try-except ___ """
# — блок, который можно использовать для обработки ошибок, связанных с базой данных. В случае возникновения
#   исключения, можно обработать ошибку.

# try:
#     cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("John", 25))
#     connection.commit()
# except mysql.connector.Error as e:
#     print("Ошибка базы данных:", e)
#     connection.rollback()


""" __________ Разделение логики работы с базой данных __________ """

# def insert_user(cursor, name, age):
#     cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
# def get_users(cursor):
#     cursor.execute("SELECT * FROM users")
#     return cursor.fetchall()




""" ___ --- ___ """

""" __________ --- __________ """
#       ●
# ___ EXAMPLE __________________________________________________
# ___ END of Example __________________________________________________





""" ______  Task 1  ______________________________________________________________________________________________ """
# Практическое задание 1
# Написать программу, которая запрашивает у пользователя возраст и выводит все строки таблицы users ('database': 'social_media'),
# где возраст больше указанного.

# # +++++++++++++++++++++++++
# import mysql.connector
# # +++++++++++++++++++++++++
#
# dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
# 'user': 'ich1',
# 'password': 'password',
# 'database': 'social_media',
# }
#
# # Подключение базы данных hr:
# conn = mysql.connector.connect(**dbconfig)
#
# # Создание объекта курсора для выполнения SQL-запросов:
# cursor = conn.cursor()
# print('Подключение успешно!')
#
# ratting = input('Enter Text: ')
# # cursor.execute("SELECT * FROM user WHERE rating > %s", (ratting,))      # Instead  * --> rating
# cursor.execute("SELECT last_name, rating FROM user WHERE rating > %s", (ratting,))      # Instead  * --> last_name, rating
# print(*cursor.fetchall(), sep='\n')
#
# # Закрытие курсора:
# cursor.close()
# # Закрытие соединения:
# conn.close()


""" ______  Task 2  ______________________________________________________________________________________________ """
# Практическое задание 2
# В базе данных ich_edit три таблицы:
#   1) Users с полями (id, name, age),
#   2) Products с полями (pid, prod, quantity)
#   3) Sales с полями (sid, id, pid).
# Программа должна вывести все покупки каждого пользователя.

# +++++++++++++++++++++++++
import mysql.connector
# +++++++++++++++++++++++++

dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
'user': 'ich1',
'password': 'password',
'database': 'ich_edit',
}

# Подключение базы данных ich_edit:
conn = mysql.connector.connect(**dbconfig)
# Создание объекта курсора для выполнения SQL-запросов:
cursor = conn.cursor()
print('Подключение успешно!')

# print(f'{'___ ALL Tables in database ich_edit: ':_<80}')
# cursor.execute('SHOW TABLES')
# for i in cursor.fetchall():
#     print(i[0])

print(f'{'___ DESCRIBE table users in database ich_edit: ':_<80}')
tab = 'users'
cursor.execute(f"DESCRIBE {tab}")
res = cursor.fetchall()
for el in res:
    print(el)

print('=' * 80)
print(f'{'___ QUERY: ':_<80}')
query = '''SELECT * FROM users
            INNER JOIN sales ON users.id = sales.id
            INNER JOIN product ON product.pid = sales.pid
           WHERE name = 'John' '''      # INNER JOIN - чтобы отсеять повторения.

cursor.execute(query)
for row in cursor.fetchall():
    print(row)


# Закрытие курсора:
cursor.close()
# Закрытие соединения:
conn.close()


# _______________ FOR Home Work _____________________________________
# cursor.execute('SHOW TABLES')
# # for i in cursor.fetchall():
# #     print(i[0])

# cursor.execute(f"describe <table name>")
# res = cursor.fetchall()
# for el in res:
#     print(el)

