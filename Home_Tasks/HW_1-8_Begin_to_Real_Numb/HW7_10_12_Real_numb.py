# Home Tasks 7, 10.12.24
# ___ REAL Numbers ___

# ___ Task 1 ___
# Напишите программу, которая запрашивает у пользователя натуральное десятичное число
# и выводит его двоичное представление. Реализуйте алгоритм перевода числа в двоичную систему счисления,
# используя основные концепции представления чисел (подсказка: через деление с остатком).
# Выведите полученное представление числа на экран.
# см. https://younglinux.info/algorithm/binary.
numb = int(input("Enter a real number: "))
binary_numb = bin(numb)
print(f'Binary number by converting with command "bin": {binary_numb}.')
# __ 1-st way __
bin_1 = ''                                          # Для 1-го способа.
i = 4                                                   # Для 2-го способа.
bin_2 = []                                              # Для 2-го способа.
while numb > 0:
    bin_1 = str(numb % 2) + bin_1                   # Для 1-го способа.
    bn = numb % 2                                       # Для 2-го способа.
    print(f'{i} - {bn}')                                # Для 2-го способа.
    i -= 1                                              # Для 2-го способа.
    numb = numb // 2
    bin_2.append(bn)                                    # Для 2-го способа.
bin_list = bin_2                                        # Для 2-го способа.
# print(bin_list)                                       # Для 2-го способа.
bin_list_reverse = list(reversed(bin_list))             # Для 2-го способа.
# print(bin_list_reverse)                               # Для 2-го способа.
print(f'Binary number by 2-st method:', ''.join(map(str, bin_list_reverse)), '.')       # Для 2-го способа.
print(f'Binary number by 1-st method: {bin_1} .')   # Для 1-го способа.
# __ 2-nd way __
# i = 4
# bin_2 = []
# while numb > 0:
#     bn = numb % 2
#     print(f'{i} - {bn}')
#     i -= 1
#     numb = numb // 2
#     bin_2.append(bn)
# print(f'Binary number by 2-st method:', ''.join(reversed(map(str, bin_2))), '.')

# ___ Task 2 ___
# Напишите программу, принимающую число с плавающей точкой и округляющую его до целого числа
# в соответствии с правилами школьной математики. Использовать модуль math и методы из него нельзя.
# Учесть, что программа должна корректно работать с отрицательными числами.
# numb = float(input("Enter a real number: "))
# int_part = int(numb)                # Отделяю целую часть от дробной.
# fract_part = numb - int_part        # Дробная часть = разнице десятичного числа и его целой части.
# if numb > 0:                        # Для положительных чисел.
#     if fract_part >= 0.5:
#         int_part += 1               # Увеличить целую часть на 1, если дробная >= 0.5.
#         print(int_part)             # Вывести целую часть без изменений.
#     else:
#         print(int_part)
# else:                               # Для отрицательных чисел.
#     if fract_part < 0.5:
#         int_part -= 1               # Уменьшить целую часть на 1, если дробная < 0.5.
#         print(int_part)             # Вывести целую часть без изменений.
#     else:
#         print(int_part)             # Вывести целую часть без изменений.
