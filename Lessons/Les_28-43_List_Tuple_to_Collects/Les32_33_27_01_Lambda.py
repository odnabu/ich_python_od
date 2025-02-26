# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 27.01.25
# Python 32: Вложенные функции. Лямбда-функции.

# ###################################################################################################################
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
print('.' * 120)


# _________________________ Review of previously covered material _________________________

# Хотя кортеж неизменяемый тип данных, но списки внутри кортежа мы можем менять.
# t = ([1,2], [3,4], [5,6])
# t[1].append(0)
# print(t)

#    __  NB! __  Списковые включения с доп циклом for и условием if.
# pairs1 = [(x, y) for x in range(3) for y in range(2)]
# print(f'pairs1 = {pairs1}')
#
# pairs1_txt = [(x, y) for x in range(3) for y in 'range(2)']     # С итерируемым объектом - ТЕКСТОМ.
# print(f'pairs1 = {pairs1_txt}')

# Эквивалент спискового включения выше через вложенные циклы for.
# pairs2 = []
# for x in range(3):
#     for y in range(2):
#         pairs2.append((x, y))
# print(f'pairs1_txt = {pairs2}')
#
# pairs2_txt = []                                                 # С итерируемым объектом - ТЕКСТОМ.
# for x in range(3):
#     for y in 'range(2)':
#         pairs2.append((x, y))
# print(f'pairs2_txt = {pairs2_txt}')

# ___ ТЕРНАРНЫЙ ОПЕРАТОР ___
# Смотри lesson16.md,       ## List comprehension с условием `if-else`


# %%%%%%%%%%%%%%%%%%%%%%%%%%%_____ THEORY - Типы данных _____%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Неизменяемые (immutable) типы данных — это типы данных, такие как числа, строки и кортежи,
# которые передаются в функцию по значению, то есть создается копия значения параметра.

#             "Передача параметров в Python при вызове функции: по ссылке или по значению?"
#              see https://python-school.ru/blog/python/pass-by-assignment/,
# Изменяемые (mutable) типы данных — это типы данных, такие как списки и словари,
# передаются по ссылке, и функция может изменить их содержимое.

# Многие языки программирования предлагают две модели передачи параметров в функции/процедуры:
#   - передача по значению (pass-by-value),
#   - передача по ссылке (pass-by-reference).

#  __ NB! __ При передаче по значению в функцию данные копируются в момент её вызова.
# Здесь важно понять, что данные (значения) именно копируются, это не те же самые значения.
# Поэтому в теле функции с ними можно делать всё что угодно, в т.ч. изменять, и это не отразится
# на исходных данных (тех, которые передали), так как это всего лишь их копии.
def foo(a):
    a = 4
    # return a ** 2
    print(f'Iside foo(a) ---> ', a ** 2)

a = 3
foo(a)                                                     #   --->   16
print(f'\033[31mOUTside\033[m a ---> ', a)                 #   --->   3
print(f'\033[31mOUTside\033[m foo(a) ---> ', foo(a))       #   --->   None

# Функция вызывается, но изменения оказанные на переменную a больше не действую после возврата из функции,
# ведь a всё ещё равна 3. Поэтому может показаться, что используется передача по значению, но это не так. Python не копирует значения параметров при вызове функции.

#       Свойство изменяемости/неимзен. полностью зависит от типа объекта.
#       Иными словами, не/изменяемость является характеристикой типа, а не конкретных объектов.
#       Тип является изменяемым, если содержимое объекта может быть изменено без изменений его идентификатора и типа.
#       Список (list) является изменяемым типом данных.



# def newlist(numbers, num):      # Функции могут влиять на внутренние списки.
#     num += 1
#     numbers.append(num)
#     print(numbers, num)         # k становится [1,2,4], b осталось 4.
#
# k = [1, 2]                      # ССЫЛКА на переменную k НЕ поменялась. Поменялось только содержимое переменной.
# b = 3
# b += 0                          # Переприсваивание данных. __  NB! __ Особенно важно в изменяемых типах данных, --->
# newlist(k, b)                   # ---> потому что ССЫЛКА на объект МЕНЯЕТСЯ!
# print(k, b)                     # k становится [1,2,4], b осталось 3.

# _____________________________________ NB!
# numbers = [1, 2]
# print(f'1-st value of \033[33mnumbers\033[m =', numbers)
# print(f'\tid(\033[33mnumbers\033[m): ', id(numbers))              # Адрес в памяти со ссылкой на ЗНАЧЕНИЕ переменной numbers.
#
# new_numbers = numbers           # Теперь ДОСТУП к содержимому (ЗНАЧЕНИЕ), на которое ссылается numbers, ТАК же получает и другая переменная - new_numbers.
# new_numbers.append(3)           # Если к содержимому (ЗНАЧЕНИЮ) по ссылке в new_numbers (которая получила тот же адрес в памяти, что и numbers) что-то добавить, то это добавиться и в numbers.
# print(f'Value of \033[33mnumbers\033[m AFTER \033[36mnew_numbers\033[m.append(3) =', numbers)      # Т.е. в обоих переменных хранится ссылка на ячейку в памяти, где лежит 1 общее значение ???
# print(f'\tid(\033[33mnumbers\033[m): ', id(numbers))          #  __ NB! __ НЕТ ли здесь КОНФЛИКТА ?
#
# print(f'Value of \033[36mnew_numbers\033[m AFTER append(3) =', new_numbers)
# print(f'\tid(\033[36mnew_numbers\033[m): ', id(new_numbers))
#
# # Если теперь выполнить переприсваивание для переменной numbers (изменение значения, т.е. изменение ссылки numbers
# numbers = [1, 2, 8]             # --> на другую - где лежит новое значение) то значение new_numbers НЕ поменяется! т.к. она продолжает оставаться ссылкой на значение "[1, 2, 3]".
# print(f'2-nd value of \033[33mnumbers\033[m =', numbers)
# print(f'\tid(\033[33mnumbers\033[m): ', id(numbers))          # Адрес в памяти со ссылкой на НОВОЕ значение переменной numbers.
# print(f'NEW Value of \033[36mnew_numbers\033[m AFTER "\033[33mnumbers\033[m={numbers}": ==> ', new_numbers)
# print(f'\tid(\033[36mnew_numbers\033[m): ', id(new_numbers))

# _____________________________________ NB!

# def my_function(*args):
#     for arg in args:
#         print(arg)
# my_function(1, 2, 3) # Выводит 1, 2, 3


# _____________________________________    Example 1    _____________________________________
# Напишите функцию, которая принимает произвольное количество аргументов и находит минимальное число среди них.
# Пример ввода: 3 10 22 -3 0
# Пример вывода: -3
# def find_min(*args):                              # ОДНО и ТО ЖЕ! только имя разное (args): Shift + F6.
#     return min(args)
# print(find_min(3, 10, 22, -3, 0))
#
# def find_min(*numbers):                           # ОДНО и ТО ЖЕ! только имя разное (numbers): Shift + F6.
#     return min(numbers)
# print(find_min(3, 10, 22, -3, 0))


# %%%%%%%%%%%%%%%%%%%%%%%%%%%_____ THEORY - Вложенные функции _____%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Вложенные функции — это функции, определенные внутри других функций.
# Они могут использоваться для организации кода, скрытия реализации или создания замыканий.
# def outer_function():
#     def inner_function():
#         print("Inner function")
#     inner_function()
# outer_function()                  # Выводит "Inner function".

# Ключевое слово nonlocal — это ключевое слово, которое используется во вложенных функциях для объявления переменной,
# которая является не локальной, но и не глобальной. Оно позволяет обращаться к переменной из внешней
# функции, которая находится на один уровень выше.

# Глобальная и локальная область видимости. Переменные в Build-in области - встроенные функции, такие как print.

# 1) Local.
# 2) Enclosed.                      # Замкнутая область видимости - переменная замкнута между двумя функциями.
# 3) Global.
# 4) Build-in.

# def outer_function():
#     x = 1
#     print(id(x))
#     def inner_function():
#         nonlocal x                 # Перенаправление действия в другую часть памяти - выход не предыдущий уровень.
#         x = 2
#         print(id(x))
#     inner_function()
#     print(x)                       # Выводит 2, потому что изменяет переменную x, переприсваивает значение.
#     print(id(x))
# outer_function()

# len = 5
# print(len("Some text"))             #   ERROR! Так как одна область видимости.

# -------------------------------------  :-)  :-)  :-)  :-)  :-)
# Что такое функция и что такое вложенные функции на примере сравнения с микроволновкой :D
# food = 'пельмехи'
#
# def microwave(food2warm, speed):
#     food2warm = food2warm + ' тёплые'
#
#     def wattage_600():
#         nonlocal food2warm
#         food2warm = food2warm + ' (готово за минуту)'
#         return food2warm
#
#     def wattage_100():
#         nonlocal food2warm
#         food2warm = food2warm + ' (готово за вечность)'
#         return food2warm
#
#     if speed == 'быстро':
#         return wattage_600()
#     elif speed == 'медленно':
#         return wattage_100()
#
#
# print(microwave(food, 'быстро'))
# print(microwave(food, 'медленно'))
# -------------------------------------  :-)  :-)  :-)  :-)  :-)

# _____________________________________    Example 2    _____________________________________
# def say_hi():
#     print('hi')
# say_hi()
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
# print(square(4)) # Выведет: 16 (4^2)
# print(cube(4)) # Выведет: 64 (4^3)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%_____ THEORY - Лямбда функции _____%%%%%%%%%%%%%%%%%%%%%%%%%%%
# "Синтаксический сахар":
#       - списковые включения,
#       - тернарный оператор.

# \\ Лямбда-функции // — это компактный способ определения функции в одной строке.
# Они могут быть использованы там, где требуется передать функцию в качестве аргумента
# или создать простую функцию без необходимости определения отдельной функции.
#  __ NB! __ Принимает любое кол-во аргументов, но возвращает только одно действие.

# def add(x, y):                      # ОДНО и ТО ЖЕ!
#     return x + y
# result = add(2, 3)
# print(result)

# add = lambda x, y: x + y            #   \\\ LAMBDA /// - ОДНО и ТО ЖЕ c def add...!   x, y - ARGUMENTS. : ___ - ACTION.
# result = add(2, 3)
# print(result)                       # Выводит 5.

# print((lambda x, y: x + y)(2, 3))

#   __  NB!  __ Передача функции по ссылке:
# def square(x):
#     return x ** 2
# def apply_function(func, value):
#     return func(value)
# result = apply_function(square, 5)     # Вызов функции square в apply_function, в которую (в square) нужно подставить 5.
# print(result)

# def apply_function(func, value):
#     return func(value)
# result = apply_function(lambda x: x * x, 5)
# print(result)

# words = ["First day", "6 day 2", "day 3", "day 0", "1 monday", "tuesday"]
# #  [0]      f            6           d       d          1          t
# #  [2]      r            d           y       y          m          e
# words.sort(key=lambda word: word[0])        # Сортировка по 1-ым символам / буквам в данном элементе (word) списка words.
# print(words)
# words.sort(key=lambda word: word[2])        # Сортировка по 3-им символам / буквам в данном элементе (word) списка words.
# print(words)

# _____ Встроенные методы: sorted() и reversed() _____
# Встроенные методы - это встроенные функции, которые могут быть использованы
# для сортировки и обращения последовательностей соответственно. Они возвращают новые отсортированные или
# обращенные последовательности, не изменяя исходную последовательность.

# ______ Сортировка и порядок сортировки - sorted _______
# words = ['mango', 'grape', 'apple', 'strawberry', 'banana', 'pineapple', 'kiwi', 'blueberry']
# print('id(words - orig) =', id(words))
# result = sorted(words)          # sorted сначала сделает копию списка, а потом отсортирует его.
# print(result)
# print('id(result - sorted) =', id(result))
# words.sort()
# print(words)
# print('id(words.sort()) =', id(words))
#
# result2 = sorted(words, key=len)          # sorted - сортировка по длине слов, НЕ учитывается сортировка по алфавиту.
# print('id(result2 - sorted) =', id(result2))

# words = ['mango', 'grape', 'apple', 'strawberry', 'banana', 'pineapple', 'kiwi', 'blueberry']
# result = sorted(words, key=lambda x: (len(x), x))
# print(result)

# _____ Компаратор в сортировке. _____
# Зачем нужны лямбда-функции? - Компаратор в сортировке.
# Лямбда-функции могут использоваться в сортировке для определения порядка сортировки элементов.
# def last_char_len(s):
#     return s[-1]
# words = ['mango', 'grape', 'apple', 'strawberry', 'banana', 'pineapple', 'kiwi', 'blueberry']
# result = last_char_len(words)
# print(result)

# _____ Сортировка по последнему символу _____
# words = ['mango', 'grape', 'apple', 'strawberry', 'banana', 'pineapple', 'kiwi', 'blueberry']
# result = sorted(words, key=lambda s: s[-1])
# print(result)

#  _____ Обратная к сортировке  - reversed _____
# обращение последовательностей.
# my_list = [3, 1, 2]
# sorted_list = sorted(my_list)
# reversed_list = list(reversed(my_list))
# print(sorted_list)                          # Выводит [1, 2, 3]
# print(reversed_list)                        # Выводит [2, 1, 3]



# _____________________________________    Task 1    _____________________________________
# Дано предложение из слов, разделенных пробелами.
# Написать функцию transform(), которая принимает такое предложение и возвращает аналогичное,
# но где все слова длины 3 в этом предложении - заглавными буквами.
# Пример: “The quick brown fox jumps over the lazy dog” -> “THE quick brown FOX jumps over THE lazy DOG”.

# ___ Через функцию: ___
# def transform(phrase):
#     words = phrase.split()
#     new_words = []
#     for word in words:
#         if len(word) == 3:
#             new_words.append(f'\033[31m{word.upper()}\033[m')
#         else:
#             new_words.append(word)
#     return ' '.join(new_words)
#
# sentence = "The quick brown fox jumps over the lazy dog."
# print(transform(sentence))

# __ Через списковые включения: ___
# def transform(phrase):
#     words = phrase.split()
#     new_words = [f'\033[31m{word.upper()}\033[m' if len(word) == 3 else word for word in words]
#     return ' '.join(new_words)
#
# sentence = "The quick brown fox jumps over the lazy dog."
# print(transform(sentence))

# _____________________________________    Task 2    _____________________________________
# Изменим условие 1 задачи: нужно, чтобы функция из примера 1 могла также менять слова
# длины 4 на написанные маленькими буквами.
# В общем виде, нужно, чтобы функции можно было дать условие, которому соответствует
# указанное действие.
# Например, все слова длины 4 хотим заменить на звездочки. А слова длины 2 - на черточки.
# Каждое выполнение функции - одно условие и одно действие.

# __ Через списковые включения: ___

# __ 1-st part __
# def transform(phrase, length_word):
#     words = phrase.split()
#     new_words = [f'\033[31m{word.upper()}\033[m' if len(word) == length_word else word for word in words]
#     return ' '.join(new_words)
#
# sentence = "The quick brown fox jumps over the lazy dog."
# print(transform(sentence, 3))
# print(transform(sentence, 4))

# -- 2-nd part --
# def transform(phrase, condition):
#     words = phrase.lower().split()
#     # condition = lambda word: len(word) == 3
#     new_words = [f'\033[31m{word.upper()}\033[m' if condition(word) else word for word in words]
#     return ' '.join(new_words)
#
# sentence = "The quick brown fox jumps over the lazy dog."
# print(transform(sentence, lambda word: len(word) == 5))
# print(transform(sentence, lambda word: word[0] == 't'))
# # print(transform(sentence, 4))


