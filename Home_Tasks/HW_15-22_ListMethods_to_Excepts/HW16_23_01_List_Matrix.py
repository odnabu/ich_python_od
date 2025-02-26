# Home Work 16, 23.01.25
# ___ 30: Представления списков & Tuple ( КОРТЕЖИ ) ___
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
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
print('.' * 120)

# _____________________________________    Task 1    _____________________________________
# Напишите программу, которая принимает матрицу (вложенный список) от пользователя и находит сумму всех элементов
# в матрице. Используйте вложенные списки и циклы для обхода элементов матрицы.
# Пример матрицы: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# Пример вывода:
# Сумма элементов в матрице: 45

# __ 1-st Variant __ Python
# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# def sum_matrx_elms(matrix):
#     sum_all = []
#     for el in matrix:
#         a = sum(el)
#         sum_all.append(a)
#     return sum(sum_all)
#
# print(f'Sum of elements in a matrix: {sum_matrx_elms(m)}.')

# __ 2-nd Variant __ Classical
# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # print(len(m))
# # print(len(m[0]))
# def sum_matx_el(s):
#     i = 0
#     sum_el = []
#     while i <= len(m) - 1:
#         sum_el.append(sum(m[i]))
#         s = sum(sum_el)
#         # print(s)
#         i += 1
#     return s
#     # print(f'Sum of elements in a matrix: {s}.')
#
# print(f'Sum of elements in a matrix: {sum_matx_el(m)}.')

# _____________________________________    Task 2    _____________________________________
# Напишите программу, которая принимает список чисел от пользователя и сортирует его в порядке убывания,
# используя метод sort() и параметр reverse=True. Выведите отсортированный список на экран.
#
# Пример вывода:
# Введите список чисел, разделенных пробелами: 5 2 8 1 3
# Отсортированный список чисел: [8, 5, 3, 2, 1]

def input_numb_list():
    numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
    return numb_list

l1 = input_numb_list()

def sorting(some_list):
    some_list.sort(reverse=True)
    return some_list

print(f'Sorted list of numbers: {sorting(l1)}.')

