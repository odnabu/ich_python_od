# Semenov Artem

# ______ Review of previously covered material ______
# a = 5
# b = 4.5
# c = 'Python'
# print(type(a), type(b), type(c))
# print(id(a), id(b), id(c))

# name = input("Enter your name: ")
# age = float(input("Enter your age: "))
# print(f'The next year, {name} your age is {age+1} years old.')

# decimal_numb = int(input('Enter decimal number: '))
# binary_numb = bin(decimal_numb)
# print(binary_numb)
# print(oct(decimal_numb))
# print(hex(decimal_numb))

# binary_numb = input('Enter a binary number: ') # 0b1010
# print(f'{int(binary_numb, 2)}')
# oct_numb = input('Enter octal number: ') #0o12
# print(f'{int(oct_numb, 8)}')
# hex_numb = input('Enter hexal number: ') # 0xa
# print(f'{int(hex_numb, 16)}')

# ______ Part 1 ______
# x = 5
# y = 2
# print(x + y)
# print(x * y)
# print(x / y)
# print(x // y) # Целочисленное деление - //
# print(x % y) # Остаток от деления. Но выводится не дробная часть, а часть от целого.
# # Например, 7/2 = 3,5, 7-2*3 = 1, где 1 - остаток от деления.
# print(x ** y) # Возведение в степень
# print(x ** 0.5) # Извлечение корня квадратного
# print(8 ** 1/3) # Извлечение корня любой степени

# ______ Part 2 ______ Вещественные числа
# a = 3.14
# b = -0.0001
# c = 2.0
# print(type(c))

# a = 0.1 + 0.2 # Проблема записи битовых чисел в Пайтоне
# # приводит к НЕПРАВИЛЬНЫМ вычислениям. А float хранится в памяти с погрешностью.
# print(a)

# z1 = 1.5e3
# z2 = 1.5e30
# z3 = 1.5e-3
# print(z1, z2, z3)

# a = 0.1 + 0.2 # Проблема записи битовых чисел в Пайтоне
# # приводит к НЕПРАВИЛЬНЫМ вычислениям. А float хранится в памяти с погрешностью.
# b = 0.3
# print(a == b)

# n = int(input('Enter number of students: '))
# k = int(input('Enter number of apples: '))
# apple_per_student = k // n
# rest_of_apples = k % n
# print(f'Apples per student: {apple_per_student}, Rest of apples: {rest_of_apples}.')

# ______ Part 3 ______ Битовые Операции
# x = 10 # 1010 in binary
# y = 5 # 0101 in binary
# print(x & y) # Побитовое И
# print(x | y) # Побитовое ИЛИ - OR
# print(x ^ y) # Побитовое XOR
# print(x << 1) # Сдвиг влево
# print(x >> 1) # Сдвиг вправо

# ______ Part 4 ______ Встроенные математические функции
# a = -25
# print(abs(a))
# print(pow(2, 12)) # 2 ** 12
# print(round(5.1258937, 3))
# b = (1, 5, -8, 15, 25, 0, a)
# print(max(b))
# print(min(b))
# print(sum(b))

# d = 5
# # d = d + 2
# d += 2 # d = d + 2
# # d -= 2
# # d *= 2
# # d /=2
# print(d)