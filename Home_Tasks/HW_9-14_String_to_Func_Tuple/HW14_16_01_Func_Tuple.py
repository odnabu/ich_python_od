# Home Work 14, 16.01.25
# ___ FUNCTIONS ___ +++ ___ Tuple ( КОРТЕЖИ ) ___
# Normal  \033[0;__;__m \033[m    or   BOLD  \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# f = 40; f = '.' * f; print(f) - Filler up to.
# print(f, f'\n...')
# print(' ' * 5, f'...') - Indentation in the output of the result
# while True:
#   ...
#   ask = input("\nDo you want to continue? (y/n): ").lower()
#   if ask == 'n':
#       break
print('.' * 120)

# ___ Task 1 ___
# 1) Напишите программу, которая принимает строку от пользователя и разбивает ее на отдельные слова.
# 2) Затем программа должна объединить слова в обратном порядке с использованием метода join().
# Используйте динамический массив и методы для работы со строками. Выведите результат на экран с помощью команды print.
# __ testing _______________________________________________________________
# str_inp = 'О, сколько нам открытий чудных готовят просвещенья дух...'.split()
# str_list = []
# for word in str_inp:
#     print(word)
#     str_list.append(word)
# print(' '.join(str_list))
# ___________________________________________________________________________

# def reverse_phrase(str_inp):
#     new_list = []
#     print(f'\nSeparated words of set:')
#     for word in str_inp:
#         print(f'{word: ^26}')                # Это НЕ нужно по ТЗ.
#         new_list.append(word)
#     # ' '.join(str_list[::-1])                           # Если делать так, то НЕкрасиво получается.
#     return (#f' ///  Reversed phrase:   {str_inp}.\n'    # Если делать так, то НЕкрасиво получается.
#             f' \\\\  Reversed phrase:   \033[33m{' '.join(new_list[::-1])}\033[m')
#
# phrase_input = input('Enter a string separated by spaces: ').split()
# # #       О, сколько нам открытий чудных готовят просвещенья дух...
# # #       И Опыт, сын ошибок трудных, и Гений, парадоксов друг,
# # #       И Случай - бог-изобретатель. А.С. Пушкин, 1829
# print(reverse_phrase(phrase_input))


# ___ Task 2 ___
# 1) Напишите программу, которая принимает список чисел от пользователя и добавляет каждое число в динамический массив.
# 2) Затем программа должна принимать новое число от пользователя и добавлять его в динамический массив до тех пор,
#    пока пользователь не введет команду "Выход". Используйте метод append() для добавления элементов в
#    динамический массив и условный оператор для проверки команды "Выход".
#    Выведите итоговый динамический массив на экран с помощью команды print.
# ___ Theory ________________________________________________________________________________________________________
#   Статический массив - имеет фиксированный размер, определенный заранее, его размер не может быть изменен.
#                        Ограничены определенным типом данных.
#   Динамический массив - может динамически изменять свой размер во время выполнения программы,
#                         в зависимости от потребностей. Может содержать элементы разных типов данных.
# my_list = [1, 2, 3]
# print(id(my_list))
# my_list[0] = 10
# print(my_list) # [10, 2, 3]
# print(id(my_list))
#   Список - это динамический массив, который хранит ссылки на объекты в куче. Списки являются изменяемыми, что
#            означает, что можно изменять значения элементов списка, а также добавлять, удалять и изменять элементы.
# ___________________________________________________________________________________________________________________

# user_numb_list = input('Enter a list of numbers separated by space: ').split()
# if str(user_numb_list).count(' ') == 0 or user_numb_list.count(',') > 0:
#     print('\033[31mInvalid input :(\033[m')
# else:
#     print(user_numb_list)
#
# #  ho = [1, 2, 3]
# # print(id(ho))   # Функция id() возвращает уникальный идентификатор переданного ей в качестве аргумента объекта.
#                 # Этот идентификатор является адресом в памяти, по которому расположен сам объект.
#                 # При каждом запуске программы этот идентификатор создается заново и будет для одного и того же объекта
#                 # разным, за исключением случаев, когда у объектов есть свой постоянный уникальный id, как, например,
#                 # у целых чисел от -5 до 256 - для них id будет одним и тем же при каждом вызове функции id().
#
# print('Enter a list of numbers separated by Enter.\nTo end the list print "stop".  ')
# dynamic_list = []
# # space1 = 0           # Переменная для подсчета количества пробелов в user_numbers.
# while True:
#     user_n = input('Enter a number: ')
#     user_n = user_n.strip('/+*\\')
#     # space1 = user_numbers.count(' ')          # 1-method) Подсчет количества пробелов в user_numbers.
#     space2 = user_n.count(' ')                  # 2-method) Подсчет количества пробелов в user_numbers.
#     komm = user_n.count(',')
#     if user_n == 'Stop'.lower():
#         break
#     # ________________________________________________________________________________________________________________
#     # lst = [int(x) if x.isdigit() else float(x) for x in li]     # https://stackoverflow.com/questions/74665788/how-to-convert-string-to-number-in-python
#     # for i in user_numbers:                      # 3-method) Цикл подсчета количества пробелов в user_numbers.
#     #     if i.isspace():                         # i.isspace() for i in user_numbers       https://letpy.com/handbook/string-methods/isalpha/
#     #         space = 1
#     # ________________________________________________________________________________________________________________
#
#     if user_n.isdigit():                  # OR .isnumeric().
#         # int(user_n)                     # НЕ буду пока преобразовывать.
#         dynamic_list.append(user_n)
#     elif user_n.isalpha() or space2 > 0 or komm > 0 or user_n == '':               # (space == 1):
#     # (user_n[i].isspace() for i in user_n)
#         print('\033[31mInvalid input :(\033[m Enter a number without spaces or another symbols:')
#     else:
#         # float(user_n)                   # НЕ буду пока преобразовывать.
#         dynamic_list.append(user_n)
# # result = user_numb_list.extend(dynamic_list)      # IT DOESN'T WORK
# # print(result, type(result))                       # IT DOESN'T WORK
# print(user_numb_list + dynamic_list)
# print(dynamic_list.append('10'))


# test_set = input('Enter a list of numbers: ')         # Тестовый цикл для проверки наличия пробелов при введении чисел.
# print(test_set)
# for i in test_set:
#     if i.isspace():
#         space = 1
# if space == 1:
#     print('\033[31mInvalid input :(\033[m')

# ___ Clear code for ICH by my understanding ___
# def input_numb_list():
#     user_numb_list = input('Enter a list of numbers separated by space: ').split()
#     if str(user_numb_list).count(' ') == 0 or user_numb_list.count(',') > 0:
#         print('\033[31mInvalid input :(\033[m')
#     else:
#         print(f'Your 1-st list:\t{user_numb_list}.')
#     return user_numb_list
#
# l1 = input_numb_list()
#
# def input_numbs():
#     print('Enter a list of numbers separated by Enter. To end the list print "stop".  ')
#     dynamic_list = []
#     while True:
#         user_n = input('Enter a number: ')
#         user_n = user_n.strip('/+*\\ ,')
#         space2 = user_n.count(' ')                  # 2-method) Подсчет количества пробелов в user_numbers.
#         komm = user_n.count(',')
#         if user_n == 'Stop'.lower():
#             break
#         if user_n.isdigit():                  # OR .isnumeric().
#             dynamic_list.append(user_n)
#         elif user_n.isalpha() or user_n == '' or space2 > 0 or komm > 0 :
#             print('\033[31mInvalid input :(\033[m Enter a number without spaces or another symbols:')
#         else:
#             dynamic_list.append(user_n)
#     print(f'Your 2-nd list:\t{dynamic_list}.')
#     return dynamic_list
#
# l2 = input_numbs()
#
# print(l1 + l2)


# ___ CLEAR CODE for ICH by the TASK ___
#
# __ 1-st Variant - EXTENDED __
# def input_numbs():
#     print('Enter a list of numbers separated by Enter. To end the list print "stop".  ')
#     dynamic_list = []
#     while True:
#         user_n = input('Enter a number: ')
#         user_n = user_n.strip('/+*\\ ,')      # Убираю случайные символы.
#         if user_n == 'Stop'.lower():
#             break
#         if user_n.isdigit():                  # OR .isnumeric().
#             dynamic_list.append(int(user_n))
#         elif user_n.isalpha() or user_n == '':
#             print('\033[31mInvalid input :(\033[m Enter a number without spaces or another symbols:')
#         else:
#             dynamic_list.append(float(user_n))
#     print(f'Your list of numbers:\t{dynamic_list}.')
#     return dynamic_list
#
# l2 = input_numbs()
#
# __ 2-nd Variant - SIMPLE __
# def input_numbs():
#     print('Enter a list of integer numbers separated by Enter. To end the list print "stop".  ')
#     dynamic_list = []
#     while True:
#         user_n = input('Enter an integer number: ')
#         if user_n == 'Stop'.lower():
#             break
#         user_n = int(user_n)
#         dynamic_list.append(user_n)
#     print(f'Your list of integer numbers: \t{dynamic_list}.')
#     return dynamic_list
#
# input_numbs()

# _____ Проверка, является ли список динамическим. _____
# Для этого попробую разными способами добавить элемент в список.
# Как добавить элемент в список: https://sky.pro/wiki/python/kak-dobavit-element-v-spisok-v-python/.



