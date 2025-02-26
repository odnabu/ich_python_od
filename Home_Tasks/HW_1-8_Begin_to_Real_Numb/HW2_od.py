# Home_Tasks 2, 19.11.24: Home task
#
# Part 1
f_name = input('Enter your name: ') # First/Given Name
s_name = input('Enter your family name: ') # Second/Family Name
age = input('How old are you? ') # Age
print(f'\n Hallo, {f_name} {s_name}! You are {age: ^4} years old.')
#
# Part 2: Binary to Decimal
space = " "
text1 = '-чному числу '
text2 = 'соответствует '
text3 = '-ичное число '
print('\n', 'Binary to Decimal:')
# Binary to Decimal
binary_number = '1100110' # 2-чное число
decimal_number = int(binary_number, 2) # Команда перевода в 10-чное
print(f'  2{text1} {binary_number: ^5} {text2} 10{text3} {decimal_number}')
#
# Part 3: Decimal to Binary
decimal_number = 127 # 10-чное число
binary_number = bin(decimal_number) # Команда перевода в 2-чное
print(space, "10"+text1, decimal_number, text2, "2"+text3, binary_number)