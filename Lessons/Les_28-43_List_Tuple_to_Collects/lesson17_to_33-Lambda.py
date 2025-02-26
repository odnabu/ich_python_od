# t = ([1, 2], [3, 4], [5, 6])
# t[1].append(0)
# print(t)

#
# # List comprehension
# pairs = [(x, y) for x in range(3) for y in 'ab']
# print(pairs)
#
# # Эквивалент с циклом for
# pairs = []
# for x in range(3):
#     for y in 'ab':
#         pairs.append((x, y))
#
# print(pairs)

# # List comprehension
# words = ["cat", "elephant", "dog", "bird"]
# modified_words = [word if len(word) > 3 else word.capitalize() for word in words]
#
# print(modified_words)
#
# # Эквивалент с циклом for
# words = ["cat", "elephant", "dog", "bird"]
# modified_words = []
# for word in words:
#     if len(word) > 3:
#         modified_words.append(word)
#     else:
#         modified_words.append(word.capitalize())
#
# print(modified_words)

# def newlist(numbers, num):
#     # numbers = k
#     # num = 3
#     num += 1
#     # numbers = [1, 2]
#     numbers.append(num)
#     print(numbers, num)
#
# k = [1, 2]
# b = 3
# # b += 1
# newlist(k, b)
#
# print(k, b)


# numbers = [1, 2]
# print(numbers)
# new_numbers = numbers
# new_numbers.append(3)
# print(numbers)
# print(new_numbers)
# print(id(numbers))
# print(id(new_numbers))

# def my_function(*args):
#     print(args)
#     for arg in args:
#         print(arg)
# my_function(1, 2, 3)


# Напишите функцию, которая принимает произвольное количество аргументов и находит
# минимальное число среди них.
# Пример ввода: 3 10 22 -3 0
# Пример ввода: 3 10 2 0
# Пример вывода: -3


# def find_min(*numbers):
#     return min(numbers)
#
# print(find_min(3, 10, 22, -3, 0))
#
# a = 5
# def outer_function():
#     def inner_function():
#         print("Inner function")
#     # inner_function()
#
# outer_function()

# Local
# Enclosed
# Global
# Build-in

# len = 5
# print(len("sdafsd"))
# def outer_function():
#     x = 1
#     print(id(x))
#     def inner_function():
#         nonlocal x
#         x = 2
#         print(id(x))
#     inner_function()
#     print(x)
# outer_function()


# def say_hi():
#     print("hi")
#
# say = say_hi
# say()
# print(say)
# print(say_hi)

# def power(exponent):
#     def raise_to_power(base):
#         return base ** exponent
#     return raise_to_power
#
# square = power(2)
# print(square)
# cube = power(3)
# print(cube)
#
# print(square(4))  # Выведет: 16 (4^2)
# print(cube(4))    # Выведет: 64 (4^3)

# def add(x, y):
#     return x + y
# result = add(2, 3)
# print(result)
#
#
# add = lambda x, y: x + y
# print(add(2, 3))
#
# # print((lambda x, y: x + y)(2, 3))

# square = lambda x: x ** 2
# print(square(4))
# print(square(5))



# def square(x):
#     return x * x
# # print(square(5))
#
# def apply_function(func, value):
#     return func(value)
#
# result = apply_function(square, 5)
# # result = apply_function(lambda x: x * x, 5)
# print(result)

# words = ['mango', 'grape', 'apple', 'strawberry', 'banana', 'pineapple', 'kiwi', 'blueberry']
# result = sorted(words)
# print(result)
# words.sort()
# print(words)

# words = ['mango', 'grape', 'apple', 'strawberry', 'banana', 'pineapple', 'kiwi', 'blueberry']
# # Сортировка по длине слов
# result = sorted(words, key=len)
# print(result)

# def last_char_len(s):
#     return s[-1]
#
# words = ['mango', 'grape', 'apple', 'strawberry', 'banana', 'pineapple', 'kiwi', 'blueberry']
# # Сортировка по последнему символу
# result = sorted(words, key=last_char_len)
# print(result)


# words = ['mango', 'grape', 'apple', 'strawberry', 'banana', 'pineapple', 'kiwi', 'blueberry']
# # Сортировка по последнему символу
# result = sorted(words, key=lambda s: s[-1])
# print(result)

# words = ['mango', 'grape', 'apple', 'strawberry', 'banana', 'pineapple', 'kiwi', 'blueberry']
# # print(sorted(words))
# # print(words)
#
# print(list(reversed(words)))
# print(words)


words = ['mango', 'grape', 'apple', 'Strawberry', 'Banana', 'pineapple', 'kiwi', 'blueberry']
# Сортировка по первому символу (игнорируя регистр) и по последнему символу
result = sorted(words, key=lambda x: (len(x), x))
print(result)
