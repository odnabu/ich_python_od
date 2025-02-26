# Home Tasks 9, 16.12.24
# ___ STRINGS ___

# ___ Task 1 ___
# Напишите программу, которая запрашивает у пользователя строку и определяет, является ли она панграммой.
# Панграмма - это фраза, содержащая все буквы алфавита. Программа должна игнорировать регистр букв и
# пробелы при проверке панграммы. Выведите соответствующее сообщение на экран с помощью команды print.
# Решить задачу для латиницы.
# frase = str(input(f'Enter a frase: '))             # "The quick brown fox jumps over the lazy dog"
# alphabet = str('abcdefghijklmnopqrstuvwxyz')       # set of 26 letters
# # print(alphabet)
# # print(len(alphabet), type(alphabet))
# i = 0                                               # The number of letter in an Alphabet
# # __________________________
# # while i < len(alphabet):
# #     print(alphabet[i])
# #     i += 1
# # __________________________
# sum = 0
# while i < len(alphabet):
#     if alphabet[i] in frase:
#         sum += 1
#     i += 1
# if sum == len(alphabet):
#     print(f'"{frase}" - is a PANGRAM!')
# else:
#     print(f'"{frase}" is just a common frase.')


# ___ Task 2 ___
# Напишите программу, которая запрашивает у пользователя строку и выводит на экран количество
# гласных и согласных букв в ней. Используйте функцию len() для подсчета количества букв.
# Выведите результат на экран с помощью команды print. Решить задачу для латиницы.
frase = str(input(f'Enter a frase: '))        # Hello World
vowel = 'aeiou'                               # 5 vowel letters
consonant = 'bcdfghjklmnpqrstvxz'             # 19 consonant letters
other = 'wy'                                  # Y and W, which may function as either type.
# print(len(vowel), len(consonant), len(other))
i, j, k = 0, 0, 0
# j = 0
# k = 0
sum_v, sum_c, sum_wy = 0, 0, 0
# sum_c = 0
# sum_wy = 0
while i < len(vowel):
    if vowel[i] in frase.lower():
        sum_v += 1
    while j < len(consonant):
        if consonant[j] in frase.lower():
            sum_c += 1
        while k < len(other):
            if other[k] in frase.lower():
                sum_wy += 1
            k += 1
        j += 1
    i += 1
print(f'The number of:\n   - Vowels: {sum_v},\n   - Consonants: {sum_c},\n'
      f'   - Y and W, which may function as either type: {sum_wy}.')

# ______________________________________________
# i = 0
# sum_v = 0
# while i < len(vowel):
#     if vowel[i] in frase.lower():
#         sum_v += 1
#     i += 1
# print(f'The quantity of:\n   Vowels: {sum_v}.')

# print(consonant[0])
# j = 0                                   # Hello World
# sum_c = 0
# while j < len(consonant):
#     if consonant[j] in frase.lower():
#         sum_c += 1
#     j += 1
# print(f'The quantity of:\n   Consonants: {sum_c}.')
# ______________________________________________



