# Home Tasks 6, 03.12.24
# ___ Loop WHILE ___
import time
import random

# _NB!_ Home Task: задача с ограничением количества введений пароля.

# ___ Task 1 ___ Угадайте число.
# start_time = time.time()
# print('\nLet\'s play! Guess the number between 1 and 100. Enter a number:')
# rand_numb = random.randint(1, 100)    # Генерация ЦЕЛЫХ чисел.
# while True:
#     user_numb = int(input(f'  n = '))
#     if rand_numb > user_numb:
#         print(f'The guessed number is higher, try another one: ')
#     elif rand_numb < user_numb:
#         print(f'The guessed number is smaller, try another one: ')
#     else:
#         print(f'Congratulations! You guessed the number. It\'s  {rand_numb}!')
#         break
# end_time = time.time()
# game_time = end_time - start_time
# print(f'Game id over! Your total play time is {round(game_time, 2)} sec.\nCome next time!')

# ___ Task 2 ___ Fibonacci sequence.
fib = []        # Задаем список, куда соберутся все числа, созданные циклом while.
# Введем вручную два числа, которые позволят определить первый элемент последовательности (ряда Фибоначчи):
f_i_minus_2 = -1        # F(i-2)
f_i_minus_1 = 1         # F(i-1)
n = int(input("\nEnter a number of numbers in Fibonacci sequence:\nn = "))  # Количество чисел в последовательности.
i = 0       # Введем число, с которого начнется нумерация первого числа в последовательности, т.е.: i=i+1.
            # Тогда для первого числа в ряду номер будет i=0+1 = 1.
while i < n:
    f_i = f_i_minus_2 + f_i_minus_1   # Задаем сумму, которая определяет каждый член ряда.
    f_i_minus_2 = f_i_minus_1         # Перезаписываем значение для следующего "ПЕРЕДпредыдущего" F(i-2) члена.
    f_i_minus_1 = f_i                 # Перезаписываем значение для следующего "предыдущего" F(i-1) члена ряда.
    fib.append(f_i)                   # Накапливаем все члены ряда Фибоначчи, созданные циклом while.
                                      # .append(f_i) - Добавляет элемент в конец списка -->
                                      # Отсюда: https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html
    i += 1                            # Для 1-го числа в ряду i=0+1 = 1 etc.
    # print(f_i, end=', ')            # Выводим числа через запятую в одну строку с помощью опции end=', ' в команде print.
    # print(f'{i} Fibonacci number = {f_i}.')    # В столбец.
print(f'The first {i} Fibonacci numbers: ', ', '.join(map(str, fib)), '.')       # join(map(str, fib)) --> отсюда:
                                            # https://sky.pro/wiki/python/pechat-spiska-bez-skobok-v-odnu-stroku-na-python/

# ___ Task 3 ___ Prime numbers.
# From here: https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-10-uslovnyy-cikl-while-2022-12-22
print('\nLet\'s check if the number is Prime.')
while True:
    n = int(input("Enter an integer positive number: n = "))
    cond_f = False
    n_list = []
    i = 2
    while i < n:
        if n % i == 0:
            cond_f = True
            # print(f'{n} devices to {i}')
            n_list.append(i)
        i += 1
    if cond_f:
        print(f'\n  {n} is not prime.')
        print(f'The prime divisors of {n}: ', ', '.join(map(str, n_list)), '.')
    else:
        print(f'\n  {n} is a PRIME NUMBER.')
    ask = input("\nDo you want to continue? (y/n): ").lower()
    if ask == 'n':
        break
