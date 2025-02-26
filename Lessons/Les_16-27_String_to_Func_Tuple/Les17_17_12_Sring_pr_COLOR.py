# Semenov Artem
# 17.12.24
# Python 17: STRINGS - Practice

# ______ Review of previously covered material ______

# __ Task 1 __
# Дана строка с именем, например, “Иван”. Написать программу, которая печатает приветствие, например, “Привет, Иван!”.
# name = str(input("What is your name?\n  "))
# ___ Другим цветом ___
# print(f'\033[34mHi {name}!\033[m')          # ASCII-codes 30 - 37
# print(f'\033[31mHi {name}!\033[m')
        # Черный: \030[31m
        # Красный: \033[31m
        # Зеленый: \033[32m
        # Желтый: \033[33m
        # Синий: \033[34m
        # Фиолетовый: \033[35m
        # Голубой: \033[36m
        # Серый: \033[37m
# print("\033[1;32;40mЖирный зелёный текст на чёрном фоне\033[0m")        # ____ NB! ____

# __ показывает все возможные цвета и символы __
# вроде бы как цветов много, но не особо, не RGB. всего 8 цветов + и + их вариации
# n = 0
# str = ""
# cwet = "31"
#
# while n < 10000:
#     str += chr(n)
#     n+= 1
#     cwet = f"{n // 200 % 50 + 29}"
#     if not(n % 200):
#         print(f"\033[{cwet}m{cwet}")
#         print(f"\033[{cwet}m{str}")
#         str = ""

# __ Task 2 __
# Веб-страницы состоят из строк типа "<i>Yay</i>" - выводит текст Yay # курсивом.
# В этом примере, строка-тег “i” означает <i> и </i>, которые окружают слово Yay. Нам дана строка-тэг и текст.
# Написать программу, которая выводит тег вокруг данного текста, например,  "<i>Yay</i>".
# Например, ('i', 'Hello') → '<i>Hello</i>'.
# text = input('Enter some text: ')
# modified_string = "<i>" + text + "</i>"
# print(modified_string)

# __ Task 3 __
# Дана строка. Написать программу, которая создает строку из трех копий последних двух символов данной строки.
# Данная строка должна быть длиной минимум 2. (('Hello') → 'lololo'), ('ab') → 'ababab'.
# __ 1-st Var __
# text = input('Enter some text: ')
# new_text = ''
# a = text[-2:] * 3
# print(a)
# __ 2-nd Var __
# text = input('Enter some text: ')
# new_text = ''
# if len(text) > 2:
#     a = text[-2:] * 3
#     print(a)
# else:
#     print('Text must be longer than 2 characters.')

# __ Task 4 __
# Дана строка, написать программу, которая печатает строку без первого и последнего символа от данной строки,
# например, “Иван” - “ва”. “Python” -> “ytho”.
# text = input('Enter some text: ')
# print(text[1:-1])

# __ Task 5 __
# Даны две строки разной длины (одна может быть пустой). Написать программу, которая печатает строку вида
# короткая+длинная+короткая, где короткая строка снаружи длинной. Например, 'Hello', 'hi' → 'hiHellohi'.
# text_1 = input('Enter some 1-st text: ')
# text_2 = input('Enter some 2-nd text: ')
# if len(text_1) > len(text_2):
#     print(text_1, text_2, text_1, sep='*')           # sep='' - разделитель.
# else:
#     print(text_2, text_1, text_2, sep='_')

# __ Task 6 __
# Написать программу, которая печатает True, если слова “cat” и “dog” встречаются в строке одинаковое количество раз
# (и напечатать false - если разное количество раз). 'catdog' → True, 'catcat' → False, '1cat1cadodog' → True.
# text = input('Enter some text: ')          # catdogcat  catdogcatcatdogcat
# c = text.count('cat')
# d = text.count('dog')
# print(text)
# print(f'cat = {c}')
# print(f'dog = {d}')
# __ 1st Var __
# if c == d:
#     print('True')
# else:
#     print('False')
# __ 2-nd Var __
# print(c == d)             # условие внутри принта. Результат - булевое значение True or False.

# __ Task 7 __
# Задача 6, только без count.
# text = input('Enter some text: ')          # catdogcatdog catdogcat  catdogcatcatdogcat
# work_text = str(text)
# cat_int = 0
# dog_int = 0
# i = 0
# while i <= len(work_text) - 3:
#     if work_text[i:i+3] == 'cat':
#         cat_int += 1
#     if work_text[i:i+3] == 'dog':
#         dog_int += 1
#     i += 1
# print(cat_int == dog_int, f', слова “cat” и “dog” встречаются в строке одинаковое количество раз:\n  cat_int = {cat_int}, dog_int = {dog_int}')

# __ Task 8 __
# Написать программу, которая печатает количество вхождений данной подстроки в строку.
# Например, для подстроки hi, 'abc hi ho' → 1, для подстроки “well”,  'ABCwell well') → 2.
text = input('Enter some text: ')               # Some frase from cheking this frase
text_in = input('Enter subtext: ')              # as
coint_txt_in = 0
i = 0
n = 0
while i + len(text_in) <= len(text):
    if text[i:i + len(text_in)] == text_in:
        n += 1
    i += 1
print(f'The number of {coint_txt_in} in Text = {n}.')
