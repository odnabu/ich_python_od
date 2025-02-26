# Home Tasks 11, 08.01.25
# ___ STRINGS ___
# Normal  \033[0;__;__m \033[m    or   BOLD  \033[1;__;__m \033[m

# ___ Task 1 ___
# Напишите программу, которая запрашивает у пользователя его имя, возраст и место проживания,
# а затем выводит их в следующем формате: "Привет, меня зовут {0}. Мне {1} лет. Я живу в {2}."
# Вместо {0}, {1} и {2} подставьте соответствующие значения. Используйте метод format() для форматирования строки.
# Потом попробуйте использовать f-строку. Выведите результат на экран с помощью команды print.
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# liv_place = input("Enter your living place: ")
# print(f'Hello, my name is \033[36m{name:<3}\033[m. I\'m \033[36m{age:^3}\033[m years old. I live in \033[35m{liv_place}\033[m now.')

# ___ Task 2 ___
# Напишите программу, которая запрашивает у пользователя два числа и выводит их сумму и произведение в следующем формате:
# "Сумма: {sum:.2f}, Произведение: {product:.2f}"
# Вместо {sum:.2f} и {product:.2f} подставьте соответствующие значения, округленные до двух десятичных знаков.
# Используйте f-строки с использованием форматных спецификаторов для форматирования чисел.
# Выведите результат на экран с помощью команды print.
numb1 = float(input("Enter the 1-st number:  N1 = "))
numb2 = float(input("Enter the 2-nd number:  N2 = "))
# print(f'Summ of numbers: N1 + N2 = {numb1 + numb2}. Product of numbers: N1 * N2 = {numb1 * numb2}.')
sum1 = numb1 + numb2
prod = numb1 * numb2
print(f'Summ of numbers: \033[31mN1 + N2 = {sum1:.2f}\033[m. \nProduct of numbers: \033[33mN1 * N2 = {prod:.2f}\033[m.')






