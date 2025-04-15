# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 15.04.25
 Python 75: Работа с базами данных из интерфейса Python - Practice 19.
 ################################################################################################################### """

# Video Lesson 75: ------------.
# Video Practice __: wasn't
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

# Video 75,

""" \\\\ __ NB! __ \\\\  isinstance(<object>, <type of data>)  -->  ПРОВЕРКА типа данных перед выполнением операций!!! """
# num = 3
# if isinstance(num, int):
#     print(num + 2)

""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%______________   ---   _____________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

# Video 75, ___

""" __ ПОДЛЮЧЕНИЕ  ich_edit __ """
# dbconfig = {'host': 'ich-edit.edu.itcareerhub.de',
#             'user': 'ich1',
#             'password': 'ich1_password_ilovedbs',
#             'database': 'ich_edit'}
# connection = mysql.connector.connect(**dbconfig)

""" ___ Библиотека, с которой лучше работать pymysql. ___"""
# Сначала нужно установить через pip.
# import pymysql



""" ___ --- ___ """

""" __________ --- __________ """
#       ●
# ___ EXAMPLE __________________________________________________
# ___ END of Example __________________________________________________




""" ______  Task 1  ______________________________________________________________________________________________ """
# Link to JSON and XML Weather API and Geolocation Developer API:  https://www.weatherapi.com/
# https://www.weatherapi.com/api-explorer.aspx
# API Key: 4e4e4bfc8ea74640b8f105454251504
# Nazaré, Portugal -->
# http://api.weatherapi.com/v1/current.json?key=4e4e4bfc8ea74640b8f105454251504&q=Nazaré, Portugal&aqi=no

# # +++++++++++++++++
# import requests
# # +++++++++++++++++
#
# # weather = requests.get('http://api.weatherapi.com/v1/current.json?key=4e4e4bfc8ea74640b8f105454251504&q=Nazaré, Portugal&aqi=no')
# # ? - разделяет параметры и непосредственно адрес сайта.
# city = 'Nazaré, Portugal'        # 'Nazaré, Portugal'
# # city = input('Enter city: ')        # 'Nazaré, Portugal'
# dictionary = {'key': '4e4e4bfc8ea74640b8f105454251504',
#               'q': city,
#               'aqi': 'no'}
# weather_1 = requests.get('http://api.weatherapi.com/v1/current.json', params=dictionary)
# # print(weather_1.json())
#
# # Проверка статуса и только потом печать:
# if weather_1.status_code == 200:
#     # weather_data = weather_1.json()
#     # print(weather_data.get('current').get('temp_c'))
#     weather_data = weather_1.json()['current']  #
#     print(f'Temperature in C:  {weather_data['temp_c']}')


""" ______  Task 2  ______________________________________________________________________________________________ """
# Задача: скачать к себе на компьютер 100 последних фотографий со страницы Explore | Flickr.
# Разобьем задачу на две части:
# 1. Вывести URL всех картинок. Пример URL
# https://live.staticflickr.com/65535/53534030316_e8e655393a_w.jpg
# 2. Скачать каждую картинку по ее URL и сохранить ее на диске.
# Первая задача - обязательная, вторая - опциональная.
# При использовании нужно использовать библиотеки BeautifulSoap и requests, пройденное по теме работы с файлами для
# сохранения картинок в файл. Вам также пригодятся лямбда-функции и работа со списками.
# Учтите, что на страничке по ссылке выше выводится много картинок и нам нужны не все. Нужные
# нам имеют аттрибут loading="lazy". Отфильтруйте ненужные картинки и скачивайте только нужные.

# +++++++++++++++++++++++++++++++
import requests
from bs4 import BeautifulSoup       # для работы с текстом на сайте.
import os                           # для создания папки.
# +++++++++++++++++++++++++++++++

url = 'https://www.flickr.com/explore/'
response = requests.get(url)
# print(response.text)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')    # Так как тип теговый, то текст можно спарсить. А ЖСОН - нет.
    images = soup.find_all('img', loading="lazy")           # loading - именованый параметр.
    # print(images)
    img_urls = []
    for tag in images:
        # img_urls.append(tag.get('src'))    #   OR    img_urls.append(tag['src'])  -  как просто по ключу обратиться
        url1 = 'https:' + tag.get('src')
        img_urls.append(url1)
    print(img_urls)
    os.makedirs('les75_imgs', exist_ok=True)
    for index, img_url in enumerate(img_urls, 1):
        img_resp = requests.get(img_url)
        if img_resp.status_code == 200:
            with open(f'les75_imgs/image_{index}.jpg', 'wb') as file:
                file.write(img_resp.content)            # content - потому что в бинарном формате.