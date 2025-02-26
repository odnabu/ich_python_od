# Semenov Artem
# 13.12.24
# Python 15: Summary - REAL NUMBERS

# ______ Review of previously covered material ______

# __ Task 1 __
# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите индекс наибольшего элемента последовательности. Нумерация элементов начинается с нуля.
# index = 1
# max_value = 0
# max_index = 0
# while True:
#     num = int(input(f'Enter a number: {index} - '))
#     # print(f'tne {index} number is {num}.')
#     if num == 0:
#         break
#     if max_value < num:
#         max_value = num
#         max_index = index
#     index += 1
# print(f'Index of the MAX number is: {max_index}.')


# ______ REAL NUMBERS ______
# Напишите программу, которая запрашивает у пользователя натуральное десятичное число и
# выводит его двоичное представление. Реализуйте алгоритм перевода числа в двоичную систему
# счисления, используя основные концепции представления чисел (подсказка: через деление с
# остатком). Выведите полученное представление числа на экран.
N = int(input(f'Enter a natural number: '))
binary_numb = bin(N)
bin_N = ''
while N > 0:
    x = N % 2
    print(f'{x}')
    bin_N += str(x) + binary_numb   # Так как bin_N = bin_N + x.
    N = N // 2
print(bin_N)


