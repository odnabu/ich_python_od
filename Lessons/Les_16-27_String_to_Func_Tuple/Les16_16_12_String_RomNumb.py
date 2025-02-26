# Semenov Artem
# 16.12.24
# Python 16: STRINGS

# ______ Review of previously covered material ______

# # __ Task 1 __ Таблица умножения.
# N = int(input(f'Enter an integer number less than 10: N = '))
# i = 1
# while i <= 10:
#     numb = N * i
#     print(f'{N} x {i}: {numb}')
#     i += 1

# ______ STRINGS ______ Строки - неизменяемый тип данных.
# s1 = 'Python'
# print(s1)
# s2 = "Python"
# print(s2)
# s3 = Python                   # ERROR
# print(s3)

#  __ In Column __ Введение в столбец:
# text = '''          # ''' ____ ''' __ In Column __
# 123
# Yes
# Gluck
# Freude
# 456'''
# print(text)
# a = ' '
# print(f'a = {a}.')

# num = 10
# # print(str(num) - 4)         # Ошибка типа.
# print(num - 4)                # Ошибки не будет
# print(str(num - 4))
# print(type(num)), print(type(str(num - 4)))

# ____ BACKSLASH ___
# print(f'Dragon\'s mother said "No".')
# print("Dragon's mother said \"No\".")
# print(f'"Khal Drogo\'s favorite word is "athjahakar"."')

# ___ Базовые операции над строками ___
# s1 = 'I love'
# s2 = 'Python language'
# s3 = s1 + ' ' + s2 + '.'        # Concatination.
# print(s3)
# s4 = 5
# # print(s3 + s4)                # ERROR
# print(s3 + 's4')
# print(s3 + "s4")
# print(s3 + str(s4))
# print(s1 * 7)                     # Multiplication
# # print(s3 * 7.5)                 # ERROR
# print(s3 * 7)
# print('h' * 5)                   # Duplicate: "hhhhh"

# ___ Length of the row ___
# a = 'Hello World'
# print(len(a))                      # len - Length of the row.
# b = ''
# print(len(b))

# ___ Operator IN ___
# a ='ab'
# b = "abrakadabra"
# print(a in b)                      # Operator _ in _ - Наличие подстроки a в строке b. TRUE or FALSE.

# ___ Операторы сравнения + Таблица ASCII: ord(), chr() ___
# a = 'hello'
# b = 'Hello'
# c = 'hello '
# print(a == b)
# print(a != b)
# print(a == c)
# __ Кириллица __
# print('Кот' > 'Кит')                  # Лексико-графический порядок сравнения.
# # Все символы закодированы в таблицах, из которых Пайтон (UTF-8) сравнивает символы.
# print('Кот' < 'Кит')
# print(ord('К'))                        # ord - Таблица ASCII.
# print(ord('к'))
# print(ord('о'))                        # Поэтому 'Кот' > 'Кит'
# print(ord('и'))
# __ Latine __
# print(ord('b'))
# print(chr(98))                          # chr - Символ по коду.
# print(chr(1086))

# a = 'Hello Python'                      # Каждый символ имеет свой номер в строке - индекс: from 0 to the end.
# print(a[1])                             # Считает с начала.
# print(a[0])                             # 1-ый номер - 0.
# print(a[-1])                            # Подсчет с КОНЦА, причем не с 0, а с -1.
# print(a[-3])
# print(a[len(a) - 1])                    # Длина строки
# # print(a[-len(a) - 1])                 #  ERROR
# print(a[6])

# ___ СРЕЗ ___
# print(a[0:5])                           # Срез.
# print(a[4:])
# print(a[:5])                            # До 5-го символа, НЕ включая.
# print(a[:])                             # Выведет ВСЮ строку == print(a).
# __ Шаг __
str1 = 'Hello guys. I love Python! It\'s a beautiful day.'
# Цикл ниже - для нумерации символов с выводом в одну строку:
# __________________________________________________________
i = 0
text_in_row = ''
while i < len(str1):
    text_in_row = str(i) + ' - ' + str(str1[i]) + ' \033[1;36;40m|\033[m'
    # print(f'{i} - {txt[i]}'))
    print(f'{text_in_row} ', end='')
    i += 1
# ___________________________________________________________
print('\n ', str1[0:10])          # Start / Stop (not include)
print(' ', str1[0:10:2])         # Start / Stop (not include) / Step=2 - убирает 1 букву.
print(' ', str1[0:10:3])         # Start / Stop (not include) / Step=3 - убирает 2 буквы.
print(' ', str1[0::2])
print(str1)
print(' ', str1[::-1])           # Reverse of the row - обращает строку: с конца на начало.
print(' ', str1[::-2])           # Reverse of the row - обращает строку с шагом 2, т.е. выбрасывает 1 символ: с конца на начало.





