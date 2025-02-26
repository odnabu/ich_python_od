# Semenov Artem
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# f = 40; f = '.' * f; print(f) - Filler up to.
# print(f, f'\n...')
# print(' ' * 5, f'...') - Indentation in the output of the result

# 06.01.25
# Python 19: STRINGS --> Format

# ______ Review of previously covered material ______

# __ Task 1 __
# На вход программе подается слово в виде строки. Необходимо прочитать это слово и его первую букву сделать заглавной,
# а остальные - малыми. Результат отобразить на экране.
# phrase = input('Input the phrase: ')
# print(phrase.capitalize())                # Первая буква - заглавная, остальные - маленькие.
# first_letter = phrase[0].upper()
# rest_letters = phrase[1:].lower()
# print(first_letter + rest_letters)

# __ Task 2 __
# На вход программе подается строка. Необходимо прочитать эту строку и определить число вхождений дефисов (-) в ней.
# На экране отобразить полученное число.
# phrase = input('Input the phrase: ')
# count_def = phrase.count('-')
# print(count_def)

# __ Task 3 __
# На вход программе подается строка. Прочитайте эту строку и с помощью метода найдите в ней индекс первого вхождения
# фрагмента "ra". Полученное число (индекс) выведите на экран.
# phrase = input('Input the phrase: ')
# ra_f = phrase.find('ra')
# print(ra_f)
# print(phrase.index('ra'))                 # index выведет ошибку, если НЕ найдет, а find - выведет -1.

# __ Task 4 __
# На вход программе подается строка. Прочитайте ее и замените в ней все двойные дефисы (--)
# и тройные (---) на одинарные (-). Подумайте, в какой последовательности следует выполнять эти замены.
# Результат преобразования выведите на экран.
# phrase = input('Input the phrase: ')        # od --- nabu --- shumer god
# print(phrase.replace('---', '-').replace('--', '-'))

# __ Task 5 __
# На вход программе подаются три целых положительных числа (максимум трехзначные), записанные в одну строчку
# через пробел. Необходимо их прочитать из входного потока. Затем, для двухзначных и однозначных чисел добавить
# слева незначащие нули так, чтобы все числа содержали по три цифры. Вывести на экран полученные числа в столбик
# (каждое с новой строки) в порядке их чтения из входного потока.
# _ 1-st Variant _
# numb_set = input('Input a set of numbers without periods, maximum with three elements, separated by space: ')
# print(numb_set.rjust(3, '0'))
# _ 2-nd Variant _
# a,b,c = map(str, input('Input a set of numbers without periods, \nmaximum with three elements, separated by space: ').split())            # 1 123 35
# print(a.rjust(3,'0'), b.rjust(3,'0'), c.rjust(3,'0'), sep = '\n')
# _ split _ - по умолчанию стоит пробел.
# a = 'Hello'.split()
# print(a)
# b = 'Hello World'.split()
# print(b)
# c = 'H e l l o'.split()
# print(c)
# d = 'Hello+World'.split('+')
# print(d)

# __ Task 6 __
# На вход программе подается строка, состоящая из названий городов, разделенных пробелом.
# Необходимо прочитать эту строку и преобразовать так, чтобы названия городов шли через точку с запятой (без пробелов).
# Результат  (строку) отобразите на экране
# city = input('Enter city names with a periods: ')       # Berlin Dessau Leipzig
# cit_split = city.split()
# print(cit_split)                # Была строка - а стала коллекция.
# print(';'.join(cit_split))      # Теперь из полученной коллекции делаю снова строку с разделителем ";".

# _____________ Formating of STRINGS _____________

# _ NB! _ Спец символы языка Пайтон для строк.
# tex1 = "I'm a programmer"           # Литерал.
# tex2 = 'I\'m a programmer'          # Экранирование спец. символов.
# tex3 = 'I\'m a \tprogrammer'        # Табуляция
# tex4 = 'I\'m a \tprogr\ammer'       # Звуковой сигнал.
# print(tex1,'\n',tex2,'\n',tex3, '\n', tex4)
# For example:
# path = "D:\\Python\\Projects\\ster\\tex1.py"
# print(path)
# text5 = "She said: \"Hello!\""
# print(text5)

# ___ Method FORMAT ___
# __ f'' == ''.format() __
# name = 'Olga'
# age = 48
# print('My name is {0}, I\'m {1} years old and I like programming.'.format(name, age))
# print(f'My name is {name}, I\'m {age} years old and I like programming.')             # ___ The BEST VARIANT ___
# print(f'My name is '+name +'. I\'m ' + str(age) + ' years old and I like programming.')

# ___ f'' == ''.format() ___
# name = 'Max'
# age = 30
# text = f'Ma name is {name} and I\'m {age} years old.'
# print(text)

# ___ Formating of numbers ___
# {:.2f} - спецификатор форматирования, который указывает, как нужно вывести число:, где:
# : - начало спецификатора.
# .2f - формат числа после запятой (с двумя знаками после запятой), а именно:
#       f указывает, что это число должно быть представлено в виде с плавающей точкой (float).
#       .2 указывает на то, что после десятичной точки должно быть ровно 2 знака.
# price = 9.99
# q = 5                # quantity
# total = price * q
# text = 'Total: ${:.2f}'.format(total)
# print(text)
# print("{:b}".format(10))        # Двоичное представление числа.
# print("{:d}".format(42))        # Десятичное представление числа.
# print("{:x}".format(255))       # Шестнацатиричное представление числа.

# ___
# price = 9.99
# q = 5                # quantity
# total = price * q
# text = f'Total: ${total:.2f}.'
# print(text)

# ___ Выравнивание ___
# >: выравнивание вправо.
# <: выравнивание влево.
# ^: выравнивание по центру.
# text = "|{:>10}|{:^10}|{:<10}|".format("право", "центр", "лево") print(text)

# ___ Позиционные аргументы ___
# name = 'Max'
# age = 30
# text = f'My name is {name:>10} and I\'m {age:=^10} years old.'
# print(text)
# # text2 = f'My name is {name:-10} and I\'m {age:=^10} years old.'     # ! ERROR
# # print(text2)
# text3 = f'Ma name is {name:*>30} and I\'m {age:*^10} years old.'
# print(text3)
# print(f'{'Hello':*<10}')

# __ Task 1 __
# На вход приходят имя-фамилия-пол-возраст. Программа выводит приветственную строку, в которую вставлены имя-фамилия
# и пишет дополнительно что средний возраст всех людей твоего пола среди встреченных ранее – такой-то.
# Реализовать без хранения списков или иных массивов в памяти.
# total_age = 0
# count_m = 0
# count_f = 0
# while count_m <= 3 or count_f <= 3:
#     name = input('Enter your name: ')
#     last_name = input('Enter your last name: ')
#     gender = input('Enter your gender: ')
#     age = int(input('Enter your age: '))
#     print(f'Hello, {name} {last_name}!')
#     if gender == 'm':
#         total_age += age
#         count_m += 1
#         average_age = total_age / count_m
#         print(f'Average age from all respondents your gender ({gender}) is {average_age:.1f} years old.')
#     elif gender == 'f':
#         total_age += age
#         count_f += 1
#         average_age = total_age / count_f
#         print(f'Average age from all respondents your gender ({gender}) is {average_age:.1f} years old.')
    # ask = input('Do you want to continue? (y/n): ')
    # if ask == 'n':
    #     break

# ______________________ Sasha Golub Var ____________________________
# total_age = 0
# count_man = 0
# count_woman = 0
# while count_man <= 3 or count_woman <= 3:
#     name = input("Enter your name: ")
#     last_name = input("Enter your second name: ")
#     gender = input("Enter your gender: ")
#     age = int(input("Enter your age: "))
#     print(f"Hello, {name} {last_name}!")
#     if gender == 'male':
#         total_age += age
#         count_man += 1
#         average_age = total_age / count_man
#         print(f"Average age from all respondents your gender is {average_age:.1f} years old.")
#     elif gender == 'female':
#         total_age += age
#         count_woman += 1
#         average_age = total_age / count_woman
#         print(f"Average age from all respondents your gender is {average_age:.1f} years old.")
#     ask = input("Do you want to continue? (yes/no): ")
#     if ask == 'no':
#         break
# __________________________________________________

# __ Task 2 __
# Напишите программу, которая выводит на экран следующий текст, используя строковые литералы и экранирование символов:
# print("Hello\tWorld!\nHow are you?")

# __ Task 3 __ -------------------------- HOME TASK --------------------------
# Приходит текст из 5 строк, надо:
#   1) сделать так, чтобы все предложения начинались с большой буквы.
#   2) не было подряд несколько пробелов, запятых, многоточий и т.п.
#   3) Строка не должна начинаться с пробелов, допустима только табуляция (отступ).
#   4) Не забывайте, что точка не всегда значит конец предложения! Например, и т.д. и т.п.
# text = """   это пример текста. с несколькими строками! он начинается с пробелов?
# и т.д. есть лишние пробелы. и даже многоточия..."""
# text = " ".join("""   это пример текста. с несколькими строками! он начинается с пробелов?
# и т.д. есть лишние пробелы. и даже многоточия...""".split())
# formated_text = text.split(". ")
# print(formated_text)
# i = 0
# while i < len(formated_text):
#     formated_text[i] = formated_text[i].capitalize()
#     i += 1
# print(formated_text)

# __ Task 4 __
# Вывести 3-ий символ строки.
# text = input("Enter a string: ")
# print(text[2])          # 3-ий символ
# print(text[:2])         # Срез с начала
# print(text[-2])         # Предпоследний
# print(text[::-1])       # Срез с конца
# print(text[0:5])        # Срез не включая последний.

# __ Task 5 __
# Вывести всю строку, кроме последних 2 символов.
# text = input("Enter a string: ")
# print(text[0:-2])

# __ Task 6 __
# выведите все символы с четными индексами (считая, что индексация начинается с 0,
# поэтому символы выводятся начиная с первого).
text = input("Enter a string: ")
print('Even indexes: ', text[:-1:2])          # 0123456
print('Even indexes: ', text[::2])
# выведите все символы с HEчетными индексами
print('Odd indexes: ', text[1::2])          # 0123456
print(len(text))

