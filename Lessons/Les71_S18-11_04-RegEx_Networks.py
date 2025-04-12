# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 11.04.25
 Python 71: Regular Expressions. Networks - SUMMARY 18.
 ################################################################################################################### """

# Video Lesson 71: ------------.
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

# Video 71,

""" \\\\ __ NB! __ \\\\  isinstance(<object>, <type of data>)  -->  ПРОВЕРКА типа данных перед выполнением операций!!! """
# num = 3
# if isinstance(num, int):
#     print(num + 2)


""" ////  __ NB! __  ////       ___  HT 34, task 2  ___   """     # See 1:04:00.
# ++++++++++++++
import re
# ++++++++++++++
# Решение от teacher - Тани Клецовки.

# def highlight_keywords(text, keywords):
#     for word in keywords:           # ({word}) - это 1-я группа,  (and) - 2-я группа.
#         pattern = rf'\b({word})\b (and)'  # r'\b(python)\b'    /// можно вместо  (and) поставить (w+).
#         text = re.sub(pattern, r'-\2- *\1*', text, flags=re.IGNORECASE)  # '*\1*' = '*python*' = '*Python*'
#     return text
#
#
# text = "This is a sample text. We need to highlight Python and programming WOW."
# keywords = ["python", "programming"]
# print(highlight_keywords(text, keywords))


""" __________ Change DATE with RegEx __________ """
# DATE - найти и изменить вывод даты:
text = "Dates: 03.06.2025, 05/02/2024"
# yyyy-mm-dd

pattern = r'.+: (\d{2})[./-](\d{2})[./-](\d{4})'
matches = re.findall(pattern, text)
print(matches)
new_text = re.sub(pattern, r'\3-\2-\1', text)
print(new_text)



""" ______  Task 1  ______________________________________________________________________________________________ """
#



