# Homework 35, 07.04.25
""" ___ 68-69: Networks """

# Video Practice 68: _______________________
# Video Lesson 69: ______________________
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
# Напишите функцию get_response(url), которая отправляет GET-запрос по заданному URL-адресу и возвращает объект
# ответа. Затем выведите следующую информацию об ответе:
# - Код состояния (status code)
# - Текст ответа (response text)
# - Заголовки ответа (response headers)
    # Пример использования:
    # url = "https://api.example.com"
    # response = get_response(url)
    # print("Status Code:", response.status_code)
    # print("Response Text:", response.text)
    # print("Response Headers:", response.headers)

# # +++++++++++++++
# import requests
# # +++++++++++++++
# # url = "https://example.com"
# # print(requests.get(url))
#
# def get_response(url_: str):
#     return requests.get(url_)
#
# try:
#     # url_full = "https://api.example.com"
#     # response = get_response(url_full)
#     # Как я поняла из информации по ошибке: socket.getaddrinfo(host, port, family, socket.SOCK_STREAM) - адрес НЕверно введен,
#     # потому что хоста api.example.com НЕ существует, то есть поддомена api для домена example.com НЕ существует.
#
#     url_act = "https://example.com"
#     response = get_response(url_act)
#     print("Status Code:", response.status_code)         # Код состояния ответа (status code).
#     print("Response Text:", response.text)              # Текст ответа (response text) - данные, полученные от сервера.
#     print("Response Headers:", response.headers)        # Заголовки ответа (response headers).
# except requests.exceptions.ConnectionError as e:
#     notice = f"\033[31mERROR\033[m: "
#     print(notice, e)


part_2 = '______ Task 2 _____'
""" ______  Task 2  ______________________________________________________________________________________________ """
# Напишите функцию find_common_words(url_list), которая принимает список URL-адресов и возвращает список наиболее
# часто встречающихся слов на веб-страницах.
#   ++ 1) Для каждого URL-адреса функция должна получить содержимое страницы с помощью запроса GET (requests.get()) и
#      использовать регулярные выражения для извлечения слов.
#   2) Затем функция должна подсчитать количество вхождений каждого слова и вернуть наиболее часто встречающиеся
#      слова в порядке убывания частоты.

# ++++++++++++++++++++++++++++++++++++
import requests
import re
from collections import Counter         # Класс Counter() модуля collections - https://docs-python.ru/standart-library/modul-collections-python/klass-counter-modulja-collections/
# ++++++++++++++++++++++++++++++++++++

def find_common_words(url_list):
    l = 80
    # only_words = []             # for 1-st Variant ///
    sep_word = []               # for 2-nd Variant ///
    for url in url_list:
        response = requests.get(url)
        print(f'\033[40;33m{'... get(url) ':.<{l}}\033[m')
        print(response.text)
        # ____ 1-st Variant ___________________________________
        # for word in response.text.split():
        #     res_sub_1 = re.sub(r'\s*\W+', ' ', word)       # \s≈[ \f\n\r\t\v] --> https://habr.com/ru/articles/349860/
        #     for w in res_sub_1.split():
        #         res_sub_2 = re.sub(r'\s*\W+', ' ', w)
        #         # if res_sub_2 != '0':                    # -------- NOT in lms ---------------
        #         #     print(res_sub_2)                    # -------- NOT in lms ---------------
        #         #     only_words.append(res_sub_2)        # -------- NOT in lms ---------------
        #         print(res_sub_2)
        #         only_words.append(res_sub_2)
        # print(only_words, '\n', len(only_words))          # Checking.
        # ____ 2-nd Variant ___________________________________
        for word in response.text.split('<>/= '):
            res_sub_1 = re.sub(r'\s*\W+', ' ', word)
            sep_word = res_sub_1.split()
            # print(sep_word, '\n', len(sep_word))          # Checking.
    print(f'\033[40;33m{'--- Words Counter ':-<{l}}\033[m')
    # count_word = Counter(only_words)            # for 1-st Variant /// See HW21_11_02_Collection.py
    count_word = Counter(sep_word)                # for 2-nd Variant /// See HW21_11_02_Collection.py
    # -------- NOT in lms ---------------
    # print(count_word)
    # all_pairs = []                                      # Новая коробка для хранения пар из Counter().
    # for k, v in count_word.items():                     # Разбираю словарь на ключи и значения и -->
    #     pair = (k, v)                                   #  --> собираю в пару.
    #     all_pairs.append(pair)                          # Пару кладу в новую коробку для пар.
    # # all_pairs.sort(key=lambda x: x[1], reverse=True)        # Сортируем по всем вторым (с индексом [1]) элементам кортежей.
    # all_pairs.sort(key=lambda x: -x[1])                 # так ЛУЧШЕ!!! сортировать по всем вторым элементам кортежей (с индексом [1]), НО во ОБРАТНОМ порядке (-x[1]).
    # return print(all_pairs)                                    # count_word.most_common
    return count_word.most_common(3)

urls = ['https://example.com', 'https://www.iana.org/help/example-domains']       # 'https://www.iana.org/help/example-domains'
# urls = ['https://example.com']
responses = find_common_words(urls)
res = [f'{k} --> {v} times' for k, v in responses]
print(f'3 most common words in all url\'s:\n{res}.')
