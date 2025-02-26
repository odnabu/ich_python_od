# Semenov Artem
# 28.11.24
# Python 5: Практикум Python

# ___ Task 1 ___
# print('Hello World!')

# ___ Task 2 ___
# name=input('What is your name?')
# print(f'Hello {name}')
# print('Hello', name)

# ___ Task 4 ___
# print(f'3 ^ 5 = {3 ** 5}')
# print(f'3 ^ 5 = {pow(3, 5)}')
# print(f'3 sqrt 5 = {3 ** (1/5)}')
# print(f'3 ^ 5 = {pow(3, 1/5)}')
# print(f'3 // 5 = {3 // 5}')
# print(f'8 // 5 = {8 // 5}')
# print(f'12 // 5 = {12 // 5}')
# print(f'8 / -4 = {8 / -4}')

# ___ Task 5 ___
# x = 0.1; y = 0.2; z = 0.3
# print(f'Task 4: x + y + z = {x + y + z}')   # 0.6000000000000001
# print(f'Task 4: x + y + z = {round(x + y + z, 11)}')

# from decimal import Decimal
# Определяем числа с помощью Decimal
# x = Decimal('0.1')
# y = Decimal('0.2')
# z = Decimal('0.3')
# print(f'Task 4: x + y + z = {x + y + z}')  # Вывод: 0.6

# ___ Task 6 ___
# time_hour = 9; time_minute = 45
# time_duration_sec = time_hour * 60 * 60 + time_minute * 60
# print(f'\nКоличество секунд, прошедшее с полуночи {time_duration_sec}')

# ___ Task 7 ___
# time_hour = 10; time_minute = 3
# time_duration_sec = time_hour * 60 * 60 + time_minute * 60
# print(f'\nКоличество секунд, прошедшее с полуночи {time_duration_sec}')

# ___ Task 8 ___
# time_hour = int(input('Введите часы: '))
# time_minute = int(input('Введите минуты: '))
# time_duration_sec = time_hour * 60 * 60 + time_minute * 60
# print(f'\nКоличество секунд, прошедшее с полуночи {time_duration_sec}')

# -- map - функция-генератор.
# ____ time = map(int, input('Введите время (часы, минуты через пробел): ').split())
# ____ print(time)

# hours, minutes = map(int, input('Введите время (часы минуты через :): ').split(':'))
# time_duration_sec = hours * 60 * 60 + minutes * 60
# print(f'{hours}:{minutes}, {time_duration_sec}')

# ___ Task 9 ___
# Выделите строки, которые одинаковы в решениях задачи 6, 7 и 8 и строки, которые
# отличаются --- дублирование кода.

# ___ Task 10, 11 ___
a = float(input('Введите длину 1 катета с точностью до сантиметра: '))
b = float(input('Введите длину 2 катета с точностью до сантиметра: '))
hypoten = (a ** 2 + b ** 2) ** (1/2)
print(f'\nДлина гипотенузы = {round(hypoten, 2)}')

# ___ Task 12 ___
print(f'\n10+3*(7-3)/2 = {10 + 3*(7-3)/2}')
