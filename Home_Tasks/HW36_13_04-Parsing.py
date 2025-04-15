# Homework 36, 13.04.25
""" ___ 70: Parsing """

# Video Practice 70: _______________________
# Video Lesson __: wasn't
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
# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы, использует библиотеку
# BeautifulSoup для парсинга HTML и выводит список всех ссылок на странице.


# What are some popular websites with minimal content? -->
# https://www.quora.com/What-are-some-popular-websites-with-minimal-content

# Сохраняю URL в переменную:
# url = 'https://htwins.net/'      # Full URL:  url = 'https://htwins.net/scale2/'     # Выдало 406 на page.status_code.
# requests/src/requests/status_codes.py --> https://github.com/psf/requests/blob/main/src/requests/status_codes.py

# # +++++++++++++++++++++++++++++
# from bs4 import BeautifulSoup
# import requests
# # +++++++++++++++++++++++++++++

# def get_all_links(url):
#
#     list_all_links = []
#     # Отправляю GET()-запрос на сайт и сохраняю полученное в переменную 'page':
#     page = requests.get(url, headers={"User-Agent": "XY"})      # 406 --> The default Python User-Agent
#     # 'python-requests/2.21.0' was being probably blocked
#     # by the hosting company:
#     # https://stackoverflow.com/questions/56101612/python-requests-http-response-406
#     # Проверяю подключение:
#     print(f'Status code: {page.status_code}')         # Если выдало 200, смотрю дальше.
#     # Просмотрю все данные веб-страницы:
#     # print(page.text)
#     # print(f'\033[40;33m{'':=<90}\033[m')
#     soup = BeautifulSoup(page.content, 'html.parser')
#     links = soup.find_all('a')
#     for link in links:
#         list_all_links.append(link.get('href'))
#     # print(link['href'])
#     return list_all_links
#
#
# # url= 'https://lovelycharts.com/'
# url = 'https://htwins.net/scale2/'
# print(get_all_links(url))


part_2 = '______ Task 2 _____'
""" ______  Task 2  ______________________________________________________________________________________________ """
# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и уровень заголовков, а затем
# использует библиотеку Beautiful Soup для парсинга HTML и извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.)
# с их текстом.

# +++++++++++++++++++++++++++++
from bs4 import BeautifulSoup
import requests
# +++++++++++++++++++++++++++++

def get_headers(url: str, headers: tuple) -> str:
    l = 45          # Length of the horizontal separator line.
    page = requests.get(url)
    result = []  # Список для хранения заголовков, если их нужно где-то дальше использовать.
    if page.status_code != 200:
        print(f'Status code: {page.status_code}')
        page = requests.get(url, headers={"User-Agent": "XY"})
    soup = BeautifulSoup(page.text, 'html.parser')
    print(f'{'____ Result of parsing: ':_<{l}}')
    for header in headers:
        h = soup.find(header)
        # print(f'{header}: {h.text}')
        if h is None:
            print(f'{header}: The header {header} was not found.')
        elif h.text == '':
            # raise AttributeError(f'{header}: The header {header} is empty.')
            print(f'{header}: The header {header} is empty.')
        else:
            print(f'{header}: {h.text}')
            result.append(f'{h.text.strip()}')  # Добавляю текст заголовка.
    print(f'{'____ Text of headers were found: ':_<{l}}')
    return ''.join(result)         # Возвращаю результат в виде строки для дальнейшего использования.


# try:
#     url = 'https://htwins.net/scale2/'       # __ NB! __  - Выводит статус 406, который говорит об ограниченном доступе к сайту.
#     headers = 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
#     # print(get_headers(url, headers))
#     get_headers(url, headers)
# except AttributeError as e:
#     print(e)

url = 'https://htwins.net/scale2/'
headers = 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
# get_headers(url, headers)
headers = get_headers(url, headers)
print(headers)
print(headers + ' --> FOR CKECKING!')
