# ___ Part 1 ___
# a = 7.5; b = 8
# d = 'Hello world'
# # print(type(a), type(b))
# print(int(a), float(b))
# print(d, type(d)) # String
# print(id(a)) # Адрес ячейки, где находится a
# print(id(b))
# print(id(d))
# b = a
# print(id(b))
#
# ___ Part 2 ___
# width = float(input("Enter Width: "))
# height = float(input("Enter Height: "))
# Area = (width * height)
# Perimeter = (width + height) * 2
# print("The Area is: ", Area)
# print("The Perimeter is: ", Perimeter)
# print("Area = ", Area)
# print("Perimeter = ", Perimeter)
# name = input("Enter your name: ")
# print(name, "'s ", "Perimeter = ", Perimeter)
#
# ___ Part 3 ___
space = " "
text1 = '-чному числу '
text2 = 'соответствует '
text3 = '-ичное число '
print('\n', 'Binary and Decimal:')
# Binary to Decimal
binary_number = '0b10101' # 2-чное число
decimal_number = int(binary_number, 2) # Команда перевода в 10-чное
print(space, "2"+text1, binary_number, text2, "10"+text3, decimal_number)
print(f'*** 2{text1} {binary_number: ^5} {text2} 10{text3} {decimal_number}') # https://younglinux.info/python/input :
# "_>5" - on the left, "_<5" - on the right, "_^5" - middle
#
# Decimal to Binary
decimal_number = 21 # 10-чное число
binary_number = bin(decimal_number) # Команда перевода в 2-чное
print(space, "10"+text1, decimal_number, text2, "2"+text3, binary_number)
#
print("\n", "Octal and Decimal:")
# Octal to Decimal
octal_number = '0o751' # 8-ичное число
decimal_number = int(octal_number, 8) # Команда перевода в десятичное
print(space, "8"+text1, octal_number, text2, "10"+text3, decimal_number)
#
# Decimal to Octal
decimal_number = 489 # 10-чное число
octal_number = oct(decimal_number) # Команда перевода в 8-чное
print(space, "10"+text1, decimal_number, text2, "8"+text3, octal_number)
#
print("\n", "Hexadecimal and Decimal:")
# Hexadecimal to Decimal
hex_number = 'A3' # 16-ичное число
decimal_number = int(hex_number, 16) # Команда перевода в десятичное
print(space, "16"+text1, hex_number, text2, "10"+text3, decimal_number)
#
# Decimal to Hexadecimal
decimal_number = 21 # 10-чное число
hex_number = hex(decimal_number) # Команда перевода в 16-чное
print(space, "10"+text1, decimal_number, text2, "16"+text3, hex_number)
