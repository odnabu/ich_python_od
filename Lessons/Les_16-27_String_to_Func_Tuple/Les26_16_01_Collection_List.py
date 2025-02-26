# Semenov Artem
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 16.01.25
# Python 26: Базовые коллекции. Списки.

# ###################################################################################################################
print('.' * 120)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% _________  Коллекции и списки  __________ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Коллекции и списки - сохраняются в динамических массивах ????

# list_city = ['London', 'Berlin', 'Paris']
# list_numb1 = [1, 2, 3, 4, 5]
# list_numb2 = [0.1, -23, 0.0005669, 400, 5]
# list_various = [1, 'ads', [list_city, list_numb1], True, list_city]
# print(list_city[0])
# print(list_various[4])
# print(list_numb1[1:4])
# print(list_city[::-1])
# print(list_various[::-1])

# list_city[0] = 'Dessau'
# print(list_city)

# ___ Empty LIST __
# a = []
# b = list()
# print(a, '\n', b)

# Преобразование коллекции в список:
# a = list('Dessau')
# print(f'String (or Tuple) to list: {a}.')
# print(['Dessau'])                             # Так преобразование не осуществить.

# print(len(list_numb1))
# print(max(list_numb1))
# print(min(list_numb1))
# print(sum(list_numb1))
# print(sorted(list_numb2, reverse=True))        # Работает только с ОДНИМ типом данных.
# print(sorted(list_city, reverse=True))         # Работает только с ОДНИМ типом данных.
# s = 'Dessau'
# print(sorted(s, reverse=False))                # Работает только с ОДНИМ типом данных.


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% _________  Separating row to symbols  __________ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# ___ 1-st Method ___
# numbers = input('Enter numbers with a space: ').split()
# print(numbers)
# for i in numbers:
#     i = int(i)
#     print(i)

# ___ 2-nd Method ___
# numbers = input('Enter numbers with a space: ').split()
# numb_int = []
# numb_int2 = []
# print(numbers)
# for i in numbers:
#     i = int(i)
#     numb_int.append(i)
#     numb_int2.append(i ** 2)
# print(numb_int, '\n', numb_int)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% _________  JOIN symbols to row  __________ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# my_list = ["apple", "banana", "cherry"]
# result = ' *Fruit* '.join(my_list)            # join Связывает список в строку чз разделитель ' Fruits '.
# print(result)
#
# my_list1 = [1, 2, 3, 4, 5]                  # Позволяет добавлять все элементы одного списку к другому списку.
# my_list.extend(my_list1)
# print(my_list)

