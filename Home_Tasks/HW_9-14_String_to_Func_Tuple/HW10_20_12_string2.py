# Home Tasks 10, 20.12.24
# ___ STRINGS ___
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m

# ___ Task 1 ___
# Напишите программу, которая запрашивает у пользователя строку и преобразует ее,
# удаляя все гласные буквы из строки. Используйте метод replace() для замены гласных букв
# на пустую строку. Выведите преобразованную строку на экран с помощью команды print.
# __ 1-st Var __ (exactly by Home Task)
# frase = input(f'Enter a phrase: ')             # Hello World
# vowel = 'aeiouy'                               # 5 vowel letters + y
# # print(frase.replace(frase[1], ''))
# frase_new = ''
# i = 0
# while i < len(frase):
#     if frase[i] not in vowel:
#         frase_new += frase[i]
#     else:
#         frase_new += frase[i].replace(frase[i], '')
#     # print(frase_new)
#     i += 1
# print(f'Frase after replacing: {frase_new}.')

# __ 2-nd Var __ FINAL CODE (with colors)
# frase = input(f'Enter a phrase: ')              # Hello World
# vowel = 'aeiouy '                               # 5 vowel letters + y + Space
# # print(frase.replace(frase[1], ''))
# frase_new = ''
# i = 0
# while i < len(frase):
#     if frase[i] not in vowel:
#         frase_new += f'\033[1;36;40m {frase[i]} \033[m'
#     else:
#         frase_new += frase[i].replace(frase[i], '\033[0;30m.\033[m')      # There is Into 1 point (dot).
#     # print(frase_new)
#     i += 1
# print(f'Frase after replacing: {frase_new}.')


# ___ Task 2 ___
# Напишите программу, которая запрашивает у пользователя строку и определяет, содержит ли она
# только уникальные символы. Если все символы в строке уникальны, выведите соответствующее сообщение на экран.
# В противном случае выведите сообщение о том, какие символы повторяются. Не используйте множества и
# подобные структуры данных, которые мы пока не изучали, для проверки уникальности символов.
#  (a in b)

# __ 1-st part __ Подсчет количества раз, которое встречается каждая буква во фразе.
# frase = input(f'Enter a phrase: ')            # Hello World
# print(f'Total number of simbols is: {len(frase)}.')
# i = 0
# while i < len(frase):
#     n_rep = frase.count(frase[i])
#     print(f'{frase[i]} - {n_rep} times.')
#     i += 1

# __ 2-nd part __ Печать в список всех (включая дубликаты) повторяющихся букв и их количество.
# frase = input(f'Enter a phrase: ')            # Hello World
# print(f'Total number of simbols is: {len(frase)}.')
# i = 0
# not_uniq_list = ''
# while i < len(frase):
#     n_rep = frase.count(frase[i])
#     if n_rep != 1:
#         not_uniq_list += frase[i]
#         print(f'{frase[i]} - {n_rep} times.')
#     i += 1
# print(not_uniq_list)

# __ 3-nd part __ Список символов, которые хотя бы 1 раз входят во фразу.
# frase = input(f'Enter a phrase: ')              # Hello World
# print(f'Total number of simbols is: {len(frase)}.')
# i = 0
# list_i = ''
# # print(frase.find(frase[3]))                   # Поиск первого вхождения символа в строку и определение его номера.
# while i < len(frase):                           # Перебираю каждый символ во фразе по номеру от 0 до последнего.
#     s_find = frase.find(frase[i])               # Ищу первое вхождение символа и определяю его номер.
#     if frase.count(frase[i]) >= 1 and frase[i] not in list_i:    # Если количество вхождений символа .count во -->
#         list_i += frase[s_find]                 # --> фразу >= 1 и ЭТОГО символа ещё нет в новом списке, то добавляю его.
#     i += 1                                      # Перехожу к следующему символу.
# print(f'The list of symbols in frase: "{list_i}".')

# __ 4-th part __
# frase = input(f'Enter a phrase: ')              # Hello World
# print(f'Total number of simbols is: {len(frase)}.')
# i = 0
# list_i = ''
# # print(frase.find(frase[3]))                   # Поиск первого вхождения символа в строку и определение его номера.
# while i < len(frase):                           # Перебираю каждый символ во фразе по номеру от 0 до последнего.
#     s_find = frase.find(frase[i])               # Ищу первое вхождение символа и определяю его номер.
#     if frase.count(frase[i]) >= 1 and frase[i] not in list_i:    # Если количество вхождений символа .count во -->
#         list_i += frase[s_find]                 # --> фразу >= 1 и ЭТОГО символа ещё нет в новом списке, то добавляю его.
#     i += 1                                      # Перехожу к следующему символу.
# # print(f'The list of symbols in frase: "{list_i}".')
# k = 0                               # Запускаю подсчет количеств вхождений каждого символа из списка list_i во фразу.
# total_sum = 0                       # Для подсчёта общего кол-ва вхождений всех символов во фразу.
# while k < len(list_i):              # Перебираю каждый символ из нового списка.
#     if list_i[k] in frase:          # Если символ из списка есть во фразе, то ...
#         s_num = frase.count(list_i[k])          # ... считаю сколько раз этот символ входит во фразу.
#     # print(f'{list_i[k]} - {s_num} times.')    # Вывожу на печать результат подсчета для КАЖДОГО символа из списка во фразе.
#         if s_num != 1:                                  # Если вхождений символа будет больше 1, то -->
#             print(f'{list_i[k]} - {s_num} times.')      # --> вывести на экран кол-во вхождений.
#     total_sum += s_num                          # Подсчитаю общее кол-во вхождений всех символов из списка во фразу, по сути это len(frase).
#     k += 1
# # print(f'Total times: {total_sum}.')
# if total_sum == len(list_i):        # Сравниваю длину списка (куда входят символы, которые встречаются хотя бы 1 раз во фразе) -->
#     print('The phrase contains only unique symbols.')       # --> с общим кол-вом вхождений символов во фразу total_sum, причем total_sum == len(frase).
# else:
#     print('The phrase does NOT contain only unique symbols.')

# __ 5-th part __________________ OPTIMISED FINAL CODE __________________
# Идея такая:
#   1) сначала создать список со всеми символами, которые хотя бы один раз входят во фразу (уникальные символы);
#   2) проверять каждый символ из списка и считать кол-во его вхождений.
# frase = input(f'Enter a phrase: ')              # Hello World
# # print(f'Total number of simbols is: {len(frase)}.')
# i = 0
# list_i = ''                                     # Для списка уникальных символов.
# while i < len(frase):                           # Перебираю каждый символ во фразе по номеру от 0 до последнего.
#     s_find = frase.find(frase[i])               # Ищу первое вхождение символа и определяю его номер.
#     if frase.count(frase[i]) >= 1 and frase[i] not in list_i:    # Если количество вхождений символа .count во -->
#         list_i += frase[s_find]                 # --> фразу >= 1 и ЭТОГО символа ещё нет в новом списке, то добавляю его.
#     i += 1                                      # Перехожу к следующему символу.
# # print(f'The list of symbols in frase: "{list_i}".')
# if len(frase) == len(list_i):        # Сравниваю длину списка (куда входят символы, которые встречаются хотя бы 1 раз во фразе) -->
#     print('The phrase contains only unique symbols.')       # --> с общим кол-вом вхождений символов во фразу len(frase).
# else:
#     print('The phrase does \033[0;31m NOT\033[m contain only unique symbols:')
# k = 0                               # Запускаю подсчет количества вхождений каждого символа из списка уникальных символов list_i во фразу.
# list_rep = ''                       # Инициализация списка повторяющихся символов.
# while k < len(list_i):              # Перебираю каждый символ из списка уникальных символов.
#     s_num = frase.count(list_i[k])          # ... считаю сколько раз этот символ входит во фразу.
#     if s_num != 1:                  # Если вхождений символа будет больше 1, то вывести на экран кол-во вхождений.
#         list_rep += f'\'\033[1;31m{list_i[k]}\033[m\'' + ', '       # Формирую список повторяющихся символов в апострофах.
#         # print(f'{list_i[k]} - {s_num} times.')      # Вывожу на экран количество повторений символов из списка list_rep.
#     k += 1
# print(f'the symbols: {list_rep} are repeating.')

# ___ Task 3 ___
# Напишите программу, которая запрашивает у пользователя строку и выравнивает ее по центру с заданной шириной.
# Если строка не может быть выровнена по центру из-за нечетной ширины, она должна быть выровнена смещением вправо.
# Используйте методы center() и rjust() для выравнивания строки.
frase = input(f'Enter a phrase: ')                  # Hello World
w = int(input('Enter a width for phrase: '))        # 16
# print(f'Total number of simbols in phrase is: {len(frase)}.')
# print(f'For comparison:\n.{frase.center(w, '+')}.')         # Возвращает отцентрированную строку, по краям которой стоит символ fill (пробел по умолчанию)
if len(frase) % 2 != 0:
    neven_len_st = frase.rjust(len(frase) + 1, '*')
    # print(f'.\033[36m{neven_len_st.center(w, '_')}\033[m.')
    neven_len_ = frase.rjust(len(frase) + 1, ' ')
    print(f'In accordance with the technical specifications,'
          f'\nwhen the numbers of symbols is \033[1;36mODD\033[m:\n.\033[1;36m{neven_len_.center(16)}\033[m.')
else:
    even_len = frase.ljust(len(frase))
    # print(f'.\033[33m{even_len.center(w, '_')}\033[m.')
    print(f'In accordance with the technical specifications,'
          f'\nwhen the number of symbols is \033[1;33mEVEN\033[m:\n.\033[1;33m{even_len.center(16)}\033[m.')


