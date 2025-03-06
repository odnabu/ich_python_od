# Home Work 23, 20.02.25
# ___ 44: Iterators & Generators. ___
# Video Lesson 44: https://player.vimeo.com/video/1057453688?h=eff2771473
# Video Practice 45: https://player.vimeo.com/video/1057479599?h=def68827de
# Normal  \033[0;__;__m \033[m    or   BOLD  \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
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
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# -----------------------------------------------------------
print('.' * 130)


part_1 = '______ Task 1 _____'
# ______  Task 1  ____________________________________________________________________________________________________
# Напишите программу, которая генерирует и выводит квадраты чисел от 1 до N с использованием генераторного выражения.
# Реализуйте функцию generate_squares, которая принимает число N в качестве аргумента и использует
# генераторное выражение для генерации квадратов чисел. Затем выведите квадраты чисел на экран.
# Пример работы программы:
# 1
# 4
# 9
# 16
# 25

def generate_squares(numb):
    # squared_numb = (numb ** 2 for numb in range(1, numb + 1))
    # return squared_numb
    yield from (numb ** 2 for numb in range(1, numb + 1))

n = 5
for item in generate_squares(n):
    # print(f'\t{item}')
    print(f'\tSquared element - {item}')


part_2 = '______ Task 2 _____'
# ______  Task 2  ____________________________________________________________________________________________________
# Напишите генератор, который будет генерировать бесконечную последовательность Фибоначчи.
# Каждый раз, когда генератор вызывается, он должен возвращать следующее число последовательности.
# Напишите программу, которая будет использовать этот генератор для вывода первых N чисел Фибоначчи.
# Пример вывода:
# Введите количество чисел Фибоначчи: 10
# Первые 10 чисел Фибоначчи:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

# All solution see here: https://habr.com/ru/articles/337314/

# ______ Yield ______
# Для начало напишем простой генератор не используя объект-генератор. Это генератор чисел Фибоначчи:
# class FibonacciGenerator:
#     def __init__(self):
#         self.prev = 0
#         self.cur = 1
#
#     def __next__(self):
#         result = self.prev
#         self.prev, self.cur = self.cur, self.prev + self.cur
#         return result
#
#     def __iter__(self):
#         return self
#
# for i in FibonacciGenerator():
#     print(i)
#     if i > 100:
#         break

# Но используя ключевое слово yield можно сильно упростить реализацию:
# def fibonacci():
#     prev, cur = 0, 1
#     while True:
#         yield prev
#         prev, cur = cur, prev + cur
#
# for i in fibonacci():
#     print(i)
#     if i > 100:
#         break


# ______ Clear code for lms: ______
# def fibonacci(numb):
#     prev, cur = 0, 1
#     while cur <= numb:
#         yield prev
#         prev, cur = cur, prev + cur
#
# # numb = int(input("Enter a number of numbers in a sequence: "))
# numb = 5
# print(f'Введите количество чисел Фибоначчи: {numb}', end='.\n')
# print(f'Первые {numb} чисел Фибоначчи: ')
# for item in fibonacci(numb):
#     print(item)







