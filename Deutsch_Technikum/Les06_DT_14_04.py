# Dmitrii Bedov
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 14.04.25
 Deutsch Technikum: Technischer Unterricht 6.
 Бык тупогуб тупогубенький бычок у быка бела губа была тупа.
 ################################################################################################################### """

# Video Lesson 6: ---------------.
# links:
#   - .
#   - .

# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter / Ctrl-Alt+L - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------

print('.' * 120)

# Eine REST-API (Representational State Transfer Application Programming Interface) ist eine Schnittstelle,
# die den Prinzipien des REST-Architekturstils folgt. Sie ermöglicht die Kommunikation zwischen verschiedenen
# Softwareanwendungen, unabhängig von Betriebssystemen oder Plattformen, und wird häufig für Webservices genutz.

# https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html

# GET: Abrufen von Daten.
# POST: Senden neuer Daten.
# PUT: Aktualisieren bestehender Daten.
# DELETE: Löschen von Daten

""" ______  Task 1  ______________________________________________________________________________________________ """
# Aufgabe 1: Schreiben Sie ein Python-Programm, das zufällige Fakten über Katzen ausgibt.
# Maksym Poliakov 14:59
# import  requests
#
# url = 'https://catfact.ninja/fact'
# reqt = requests.get(url)
# dict_tmp  = reqt.json()
#
# for key , value in dict_tmp.items() :
#     print(f'{key} \n случайный текст {value}')

# # Stanislav M. 15:05
# import requests
# import json
#
# def get_response(url):
#     if requests.get(url) == 200:
#         return requests.get(url)
#
#
# url = 'https://catfact.ninja/fact'
# response = get_response(url)
# print(json.loads(response.text)['fact'])



""" ______  Task 2  ______________________________________________________________________________________________ """
# Aufgabe 2: Schreiben Sie ein Python-Programm, das Informationen über einen Film anhand des Titels abruft,
# unter Verwendung der API von The Movie Database (TMDB).
# API-Schlüssel - b210cb1e2063d6493cb6ca95b379ecef

# https://www.themoviedb.org/

# https://api.themoviedb.org/3/search/movie?api_key=b210cb1e2063d6493cb6ca95b379ecef&query=Inception
# https://api.themoviedb.org/3/search/movie?api_key=b210cb1e2063d6493cb6ca95b379ecef&query=MIB


""" ______  Task 3  ______________________________________________________________________________________________ """
#


""" ______  Task 4  ______________________________________________________________________________________________ """
#


""" ______  Task 5  ______________________________________________________________________________________________ """
#


""" ______  Task   ______________________________________________________________________________________________ """
