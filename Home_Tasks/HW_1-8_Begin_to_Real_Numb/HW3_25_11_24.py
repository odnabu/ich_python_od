# Home Tasks 3, 25.11.24

# ___ Task 1 ___ Простой калькулятор.
a = int(input('Enter 1st integer number: '))
b = int(input('Enter 2nd integer number: '))
print(f'Sum = {a + b}.') # Сумма.
print(f'Difference = {a - b}.') # Разность
print(f'Product = {a * b}.') # Произведение
print(f'Quotient = {a / b}.') # Частное
print(f'Remainder from dividing = {a // b}.') # Остаток от деления первого числа на второе
print(f'Raising a number (a) to a power (b) = {a ** b}.') # 1-е число в степень 2-го числа

# ___ Task 2 ___ Problem 1: Circus.
import math # Библиотека math
R = float(input('Enter the radius of the circus arena R = '))
print(f'The circumference of the arena L = {2 * math.pi * R} m.') # Длина окружности арены
print(f'The area of the arena A = {math.pi * R ** 2} sq.m.') # Площадь окружности арены

# ___ Task 3 ___ Problem 2: Map.
x1 = float(input('Enter the X-coordinate of the 1st point x1 = '))
y1 = float(input('Enter the Y-coordinate of the 1st point y1 = '))
x2 = float(input('Enter the X-coordinate of the 2nd point x2 = '))
y2 = float(input('Enter the Y-coordinate of the 2nd point y2 = '))
print(f'The distance between two points d = {((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5} a.u.') #
