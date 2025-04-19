# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 17.04.25
 Python 76: Revision - SUMMARY 19.
 ################################################################################################################### """

# Video Lesson 76: ------------.
# Video Practice __: wasn't.
# links:
#   - Presentation:
#   - Python RegEx: практическое применение регулярок: https://tproger.ru/translations/regular-expression-python.
#   - Регулярные выражения в Python от простого к сложному: https://habr.com/ru/articles/349860/.
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

""" ___________________________________  Review of previously covered material  ___________________________________ """

# Video 76,

""" \\\\ __ NB! __ \\\\  isinstance(<object>, <type of data>)  -->  ПРОВЕРКА типа данных перед выполнением операций!!! """
# num = 3
# if isinstance(num, int):
#     print(num + 2)



""" __________ --- __________ """



""" ______  Task 1  ______________________________________________________________________________________________ """
# Задача: порекомендовать фильмы в определенной категории.
# Напишите программу, которая запрашивают информацию у пользователя, делает запросы в базу
# данных и выводит результат. Работаем с базой данных фильмов Sakila.

# 1. При запуске программы выводится список категорий (номер и название категории).
# 2. Пользователь может ввести номер категории.
# 3. Программа выводит все фильмы в данной категории, но не более 10 фильмов. О фильме выводится следующая информация:
#    название, год выпуска, описание. Опционально - список актеров.
# 4. * Поменяйте программу так, чтобы на шаге 1 пользователь мог выбрать поиск по категории или по имени актера.
#      - Если выбирается поиск по категории, то выводится список категории и уже описанный поиск по категории.
#      - Если выбирается поиск по актеру, то сначала пользователь вводит имя пользователя и делается поиск по базе актеров.
#      - Если указанный пользователем актер существует, то можно выбрать имя из предложенных вариантов и найти все фильмы
#        с участием этого актера. В запросе для поиска по указанному имени актера можно пользоваться select/like чтобы
#        убедиться, что актер(ы) с таким или похожим именем существуют в базе, прежде чем искать фильмы по имени актера.

# +++++++++++++++++++++++
import mysql.connector
# +++++++++++++++++++++++
dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database': 'sakila',}

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

cursor.execute('''SELECT actor_id, first_name, last_name FROM actor''')
actors = cursor.fetchall()
# print(actors)
for index, name in enumerate(actors, start=1):
    print(f'{index} - {name[1]} {name[2]}')


choose_actor_numb = int(input('Enter the number of actor in list above: '))
chosen_actor = actors[choose_actor_numb - 1]
print(f'Name of chosen actor: {chosen_actor}')

cursor.execute('''  SELECT title, release_year, length, rating FROM actor 
                                INNER JOIN film_actor ON film_actor.actor_id = actor.actor_id
                                INNER JOIN film ON film.film_id = film_actor.film_id
                            WHERE actor.actor_id = %s ''', (chosen_actor[0],))
film_to_act = cursor.fetchmany(10)
for index, film in enumerate(film_to_act, start=1):
    print(f'{index} - {film}')


cursor.reset()
cursor.close()
conn.close()





