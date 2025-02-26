# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 24.01.25
# Python 31: Summary - Представления списков, Matrix.

# ###################################################################################################################
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
print('.' * 120)


# _________________________ Review of previously covered material _________________________

# %%%%%%%%%%%%%%%%%%%%%%%%%%%_____ Home Work 15, 22.01.25 _____%%%%%%%%%%%%%%%%%%%%%%%%%%%

# _____________________________________    Task 1    _____________________________________
# ___ BETTER Variant ___
# def find_best_list(stds_list, limit_value):         #   NB!  the NAME of function!
#     names = []
#     for n in stds_list:
#         if n[2] > limit_value:
#             names.append(n[0])
#     return names                                    # It's better WITHOUT _print_ or _f''_. ONLY result of function.
#
# sts_list = [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
# limit_mark = 90
# print(f'Пороговое значение среднего балла: \033[33m{limit_mark}\033[m.'
#       f'\nСтуденты со средним баллом выше \033[31m{limit_mark}\033[m: {find_best_list(sts_list, limit_mark)}')
# result_now = find_best_list(sts_list, limit_mark)   # For using in another tasks.
# print(result_now)

# import ast                                      # Very interesting!
# chitalka = input('Enter a TUPLE: ')             # see ~ 1:00:00. !!!!!!!!!!!!!!!!
# sr = input(f'{chitalka}: ')
# HOHo = ast.literal_eval(chitalka)


# _____________________________________    Task 2    _____________________________________
# def count_letters_in_words(phrase):         #   NB!  the NAME should be clear.
#     length = []
#     for n in phrase.split():
#         if n.isalpha() is True:
#             length.append(len(n))
#     return tuple(length)
#
# sentence = "Программирование .- это интересно и полезно"
# print(f'Предложение: \033[36m{sentence}\033[m.\nДлины слов в предложении: {count_letters_in_words(sentence)}.')


# %%%%%%%%%%%%%%%%%%%%%%%%%%%_____ Home Work 15, 22.01.25 _____%%%%%%%%%%%%%%%%%%%%%%%%%%%

# _____________________________________    Task 1    _____________________________________
# __ ANOTHER Variant fo 1-st Variant __ Python __
# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# def sum_matrx_elms(matrix):
#     sum_all = 0
#     for row in matrix:
#         for num in row:
#             # num = int(num)
#             sum_all += num
#     return sum_all
#
# print(f'Sum of elements in a matrix: {sum_matrx_elms(m)}.')

# _____________________________________    Task 2    _____________________________________

# ___ BETTER Variant ___
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
#
# l1 = input_numb_list()
#
# def sorting(some_list):
#     some_list.sort(reverse=True)
#     # return some_list                          # RETURN не нужен, те выше в строке уже лежит ссылка на объект с функцией.
#
# sorting(l1)                                     # Отрабатываем сначала функцию ...
# print(f'Sorted list of numbers: {l1}.')         # ... и возвращаем внутреннюю функцию из sorting, в которую подставили l1.