# Home Work 15, 22.01.25
# ___ Methods of lists ___ + ___ Tuple ( КОРТЕЖИ ) ___
# Normal  \033[0;__;__m \033[m    or   BOLD  \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# f = 40; f = '.' * f; print(f) - Filler up to.
# print(f, f'\n...')
# print(' ' * 5, f'...') - Indentation in the output of the result
# while True:
#   ...
#   ask = input("\nDo you want to continue? (y/n): ").lower()
#   if ask == 'n':
#       break
print('.' * 120)

# _____________________________________    Task 1    _____________________________________
# Напишите функцию, которая принимает список кортежей от пользователя, где каждый кортеж
# содержит информацию о студенте (имя, возраст, средний балл). Программа должна вывести на экран
# имена студентов, чей средний балл выше заданного значения. Используйте методы кортежей и циклы
# для обработки данных. Выведите итоговый список на экран с помощью команды print.
#
# Пример списка кортежей:
# [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
#
# Пример вывода:
#
# Введите пороговое значение среднего балла: 90
# Студенты со средним баллом выше 90 : ['Charlie']
# __ See Les-28, subsect. Functions with operator * : def sum_elements1(name, *elements): ...
# __ + Les-28, Task 1: tuple(str).

# tuple_my = "Alice", 20, 90
# print(tuple(tuple_my))

# __ Разбор задачи на составляющие:
# students_list = [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
# student1 = students_list[0]         # Извлекаю ВСЕ данные (в кортеже) на конкретного студента: ("Alice", 20, 90).
# print(student1)
# stud1_name = student1[0]            # Извлекаю конкретные данные (имя) первого студента (0) из списка: "Alice".
# print(stud1_name)

# __ Проверка использования оператора *:
# sts_list_sep = (*students_list)
# print(*sts_list_sep)

# print(*students_list)             # Лучше использовать в def.

# __ Averaged point:
# points = []
# for n in students_list:
#     # print(n[2])
#     points.append(n[2])
#     sum_points = sum(points)
# # print(points, len(points))
# average_point = sum_points / len(students_list)
# print(f'The averaged point: ', average_point)

# __ Averaged point + Names:
# points = []
# names = []
# for n in students_list:
#     # print(n[2])
#     points.append(n[2])
#     sum_points = sum(points)
#     average_point = sum_points / len(students_list)
#     if n[2] >= average_point:
#         names.append(n[0])
# # average_point = sum_points / len(students_list)
# print(f'The averaged point: ', average_point)
# print(f'Студенты со средним баллом выше: ', names)

# ___ CLEAR CODE for ICH by the Task ___
# def print_best_list(stds_list, limit_value):
#     names = []
#     for n in stds_list:
#         if n[2] > limit_value:
#             names.append(n[0])
#     return print(f'Пороговое значение среднего балла: \033[33m{limit_value}\033[m.'
#                  f'\nСтуденты со средним баллом выше \033[31m{limit_value}\033[m: {names}.')
#
# students_list = [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
# limit_value = 90
# print_best_list(students_list, limit_value)


# _____________________________________    Task 2    _____________________________________
# Напишите программу, которая принимает строку от пользователя и разбивает ее на отдельные слова.
# Затем программа должна создать новый кортеж, содержащий длину каждого слова в исходной строке.
# Используйте методы строк и кортежей для обработки данных.
#
# Пример вывода:
#
# Введите предложение: Программирование это интересно и полезно
# Длины слов в предложении: (15, 3, 8, 2, 6)

# phrase = "Программирование это интересно и полезно"
# print(f'Consists phrase "{phrase.isalpha()}" only letters: \033[36m{phrase.isalpha()}\033[m.',
#       f'\nConsists "{phrase.split()[0]}" only letters: \033[36m{phrase[0].isalpha()}\033[m.')
# print(f'Number of elements in phrase with split() = {len(phrase.split())}.')
# print(f'Number of letters in 1-st word with split() = {len(phrase.split()[0])}.')
# print('.' * 20)


# ___ CLEAR CODE for ICH by the Task ___
def prin_len_words(phrase):
    length = []
    for n in phrase.split():
        if n.isalpha() is True:
            length.append(len(n))
    return tuple(length)

sentence = "Программирование .- это интересно и полезно"
print(f'Предложение: \033[36m{sentence}\033[m.\nДлины слов в предложении: {prin_len_words(sentence)}.')




