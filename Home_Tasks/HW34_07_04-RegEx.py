# Homework 34, 07.04.25
""" ___ 66-67: Regular Expressions """

# Video Practice 66: _______________________
# Video Lesson 67: ______________________
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
# Напишите функцию extract_emails(text), которая извлекает все адреса электронной почты из заданного текста и
# возвращает их в виде списка.
    # Пример использования:
    #   text = "Contact us at info@example.com or support@example.com for assistance."
    #   emails = extract_emails(text)
    #   print(emails)  # Вывод: ['info@example.com', 'support@example.com']

# # +++++++++++++
# import re
# # +++++++++++++
#
# def extract_emails(text):
#     pattern = r'\b\w+[.]*\w+@[.a-z]+\b'
#     # где: \b\w+[.]*\w+@ - в начале слова до собаки @ могут быть буквы, цифры, нижнее подчеркивание или точка;
#     #       [.a-z]+\b - буквы или точка с любым кол-вом повторений.
#     return re.findall(pattern, text)
#
# text = ("Contact us at info@example.com or support_72@example.com for assistance. "
#         "And another email: olga.dvornik@chmnu.edu.ua")
# emails = extract_emails(text)
# print(emails)



part_2 = '______ Task 2 _____'
""" ______  Task 2  ______________________________________________________________________________________________ """
# Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения заданных ключевых слов в
# тексте, окружая их символами *. Функция должна быть регистронезависимой при поиске ключевых слов.
    # Пример использования:
    #   text = "This is a sample text. We need to highlight Python and programming."
    #   keywords = ["python", "programming"]
    #   highlighted_text = highlight_keywords(text, keywords)
    #   print(highlighted_text)
    #                   # Вывод: "This is a sample text. We need to highlight *Python* and *programming*."

# +++++++++++++
import re
# +++++++++++++
# Testing
# text_t = "This is a sample text. We need to highlight Python and programming."
# ptrn = 'Python'
# hghlt_text = re.sub(ptrn, '***' + ptrn + '***', text_t)
# print(hghlt_text)
# print('=' * 70)


def highlight_keywords(text: str, keywords: list):
    # pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in keywords) + r')\b', re.IGNORECASE)
    pattern = re.compile(r'\b(' + '|'.join(word for word in keywords) + r')\b', re.IGNORECASE)
    # hghltd_txt = pattern.sub(r'*\1*', text)
    hghltd_txt = re.sub(pattern, r'*\1*', text)
    return hghltd_txt

text = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]
highlighted_text = highlight_keywords(text, keywords)
print(highlighted_text)


""" \\\\ __ NB! __ //// """
# # Решение из Python_Summary17-Class_Decor_RegEX-SUM.pdf:
# def highlight_keywords(text, keywords):
#     for k in keywords:
#         # text=re.sub(f"({k})", r'*\1*', text, flags=re.IGNORECASE)
#         text = re.sub(k, '*' + k + '*', text, flags=re.IGNORECASE)
#     return text
#
# text = "This is a sample text. We need to highlight Python and programming."
# keywords = ["python", "programming"]
# print(highlight_keywords(text,keywords))



