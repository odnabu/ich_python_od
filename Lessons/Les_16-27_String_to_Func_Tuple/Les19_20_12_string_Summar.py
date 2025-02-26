# Semenov Artem
# 20.12.24
# Python 19: STRINGS - Summary Session.
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
import math

# ______ Review of previously covered material ______
# a = 2
# b = float(a)
# c = str(a)
# print(a, b + a)
# print(c + str(a))

# __ Task 1 __
# Написать программу, которая по данному радиусу вычисляет: длину окружности, площадь круга, объем шара.
import math
r = float(input('Enter a radius: r = '))
length = round(2 * r * math.pi, 2)
area = round(math.pi * r ** 2, 2)
voluem = round(4 / 3 * math.pi * r ** 3, 2)
print(f'\033[31m Length = {length} \033[m,\n\033[35m Area = {area} \033[m,\n\033[36m Voluem = {voluem} \033[m.')