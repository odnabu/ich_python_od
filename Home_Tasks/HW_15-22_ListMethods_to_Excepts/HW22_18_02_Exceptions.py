""""""
""""
 Home Work 22, 18.02.25
 ___ 42: Exceptions. ___
 Video Lesson 42: https://player.vimeo.com/video/1056392539?h=d82ccb0b86
 Normal  \033[0;__;__m \033[m    or   BOLD  \033[1;__;__m \033[m
 print('#' * 115)      # Для разделения блоков на листе с кодом:
 ###################################################################################################################
 f = 40; f = '.' * f; print(f) - Filler up to.
 print(f, f'\n...')
 print(' ' * 5, f'...') - Indentation in the output of the result
 while True:                      # __ NB! __ See HW14_16_01_Func_Tuple.py, Task 2, "___ Clear code..."
   ...
   ask = input("\nDo you want to continue? (y/n): ").lower()
   if ask == 'n':
   # if user_n == 'Stop'.lower():
       break
 def input_numb_list():            #  __ NB! __ See HW16_23_01_List_Matrix.py
     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
     return numb_list
 ------------------------ SHORTCUTS ------------------------
 Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
 Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
 Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
 Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
 ----------------------------------------------------------- """
print('.' * 140)


part_1 = '______ Task 1 _____'
# Исключения - see https://tatyderb.gitbooks.io/python-express-course/content/chapter_exception/3_tree.html

""" ______  Task 1  ______________________________________________________________________________________________ """
# Напишите программу, которая открывает файл, считывает из него два числа и выполняет операцию их деления.
# Если число отрицательное, выбросите исключение ValueError с сообщением "Число должно быть положительным".
# Обработайте исключение и выведите соответствующее сообщение.

# See file Les29_21_01_Files_Tanya_Kletsovka2.py

# __ 1-st Variant __
# try:
#     file = open(r'C:\Users\odnab\PycharmProjects\PythonProject\Lessons\data_22_t1.txt')
# except FileNotFoundError as e:
#     print("Проблема с открыванием файла: ", e)
# else:
#     data = file.readlines()
#     try:
#         for el in data:
#             el = el.strip().split()
#             dev = int(el[0]) / int(el[1])
#             if dev < 0:
#                 raise ValueError("Число должно быть положительным.")
#             else:
#                 print(dev)
#     except ValueError as e:
#         notice = f"\033[31m{e}\033[m"
#         print(notice)

# __ 2-nd Variant __
# --------------- testing:
# file = open(r'C:\Users\odnab\PycharmProjects\PythonProject\Lessons\data_22_t1.txt', 'r')
# data = file.readlines()
# for el in data:
#     el = el.strip().split()
#     for i in range(len(el)):
#         el[i] = int(el[i])
#     print(el)
# ------------------------

# # Функция открывания файла, преобразования строк в числа и возвращение их списком:
# def read_numbers_from_file(file_path):
#     file = open(file_path, 'r')
#     data = file.readlines()
#     for el in data:
#         el = el.strip().split()
#         for i in range(len(el)):          # 2 числа.
#             el[i] = int(el[i])
#     return el
#
# numbers = read_numbers_from_file(r'C:\Users\odnab\PycharmProjects\PythonProject\Lessons\data_22_t1.txt')
# # print(numbers[0], numbers[1])
# # print(type(numbers[0]), type(numbers[1]))
#
# def divide_numbers(n1, n2):
#     if n1 < 0 or n2 < 0:
#         raise ValueError("Число должно быть положительным.")
#     return n1 / n2
#
# # print(divide_numbers(numbers[0], numbers[1]))
#
# file_path = r'C:\Users\odnab\PycharmProjects\PythonProject\Lessons\data_22_t1.txt'      # Абсолютный путь к файлу data_22_t1.txt.
# try:
#     numbers = read_numbers_from_file(file_path)
#     dev = divide_numbers(numbers[0], numbers[1])
#     print(f"Результат деления: {dev}")
# except FileNotFoundError:
#     print("Файл не найден")
# except ValueError as e:
#     notice = f"\033[31m{e}\033[m"
#     print(f"Ошибка: {notice}")



part_2 = '______ Task 2 _____'
""" ______  Task 2  _______________________________________________________________________________________________ """
# Напишите программу, которая открывает файл (1), считывает его содержимое (2) и выполняет операции над числами в файле (3).
# Обработайте возможные исключения при открытии файла (FileNotFoundError) и при выполнении операций над числами
# (ValueError, ZeroDivisionError). Используйте конструкцию try-except-finally для обработки исключений и
# закрытия файла в блоке finally.

 # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ___ NB! ___ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 # Link to HW 22, that wasn't graded: https://lms.itcareerhub.de/mod/assign/view.php?id=6183
 # 2. Тут сложно ориентироваться и не хватает обработки ошибок. Например read_numbers_from_file может вызвать
 # FileNotFoundError, int(el[i]) может вызвать ValueError. Попробуй сделать всё одной функцией, учитывая все ошибки,
 # а после разбить на отдельные.
 # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# --------------- testing:
# file = open(r'C:\Users\odnab\PycharmProjects\PythonProject\Lessons\data_22_t2.txt', 'r')
# lines = [line.rstrip() for line in file]
# # print(lines)
# # print(lines[0])
# # elems = lines[0].split()
# # print(elems)
#
# output_list = []
# for item in lines:
#     for num in item.split():
#         if '.' in num:
#             output_list.append(float(num))
#         else:
#             output_list.append(int(num))
# # print(output_list)
#
# for i, v in enumerate(output_list, start=1):
#     print(i, v)                         # Выводит индекс и значение

# ------------------------

# ------------------------ Рабочий старый код:
# # Функция открывания файла, преобразования строк в числа и возвращение их списком:
# def get_numbers_from_file(file):
#     file = open(file, 'r')
#     if not file:
#         raise FileNotFoundError("Неверное имя файла.")
#     lines = [line.rstrip() for line in file]
#     output_list = []
#     for item in lines:
#         for num in item.split():
#             if '.' in num:
#                 output_list.append(float(num))
#             else:
#                 output_list.append(int(num))
#     return output_list
#
# numbers = get_numbers_from_file(r'data_22_t2.txt')
# # # print(numbers)
# ------------------------


# -1- Функция открывания файла:
import os      # Подключение модуля os для работы с файлами.

def validate_file_name(file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError("Невозможно открыть файл")
    else:
        return file_name

# -2- Функция считывания данных из файла (преобразование строковых данных в числа), и возвращение их списком:
def get_numbers(file_name):
    lines = [line.rstrip() for line in file_name]
    output_list = []
    for item in lines:
        for num in item.split():
            if '.' in num:
                output_list.append(float(num))
            else:
                output_list.append(int(num))
    return output_list

# Функция для ВИЗУАЛИЗАЦИИ данных, которая сопоставляет индексы чисел из списка самим числам - просто для визуализации.
def indexing_numbers(list_numb):
    for i, v in enumerate(list_numb, start=1):
        print(f'{i}  {v}')

# Функция, которая возвращает пару чисел с выбранными индексами:
# __ 1-st Variant - с ручным вводом индексов чисел в консоли:
def select_numbers():
        indx1 = int(input("Введите индекс 1-го числа: "))
        indx2 = int(input("Введите индекс 2-го числа: "))
        return numbers[indx1-1], numbers[indx2-1]

# __ 2-nd Variant - с вводом индексов чисел в коде ниже - см. строку с командой # pair_numb = select_numbers(1, 4):
# def select_numbers(indx1, indx2):
#         return numbers[indx1-1], numbers[indx2-1]

# Простой Калькулятор с элементарными арифметическими действиями над числами:
def math_operations(pair):                      # 1-st Variant - Для ручного ввода знака арифмет. операции в консоли.
# def math_operations(pair, math_operat):       # 2-nd Variant - Для ввода знака арифмет. операции в коде.
    math_operat = input("Введите один из знаков арифметической операции  +  -  *  / : ")
    n1, n2 = pair[0], pair[1]
    if math_operat == '+':
        result = n2 + n1
        math_operat = "сложения"
        sign_math_operat = '+'
    elif math_operat == '-':
        result = n1 - n2
        math_operat = "вычитания"
        sign_math_operat = '-'
    elif math_operat == '*':
        result = n1 * n2
        math_operat = "умножения"
        sign_math_operat = '*'
    elif math_operat == '/':
        result = n1 / n2
        math_operat = "деления"
        sign_math_operat = '/'
    else:
        raise TypeError("Введен недопустимый оператор")
    return result, math_operat, sign_math_operat


# # file_path = r'C:\Users\odnab\PycharmProjects\PythonProject\Lessons\data_22_t1.txt'  # Абсолютный путь к файлу data_22_t1.txt.

file = None     # None - для случаев, когда файл еще не существует, например, еще не создан лог-фал.
                # В случае, если не указать file = None, ошибка НЕ словится - программа ПРЕРВЕТСЯ и следующая программа НЕ запустится!
                # Также можно открывать файл с _with open_ - так ошибка в случае несуществующего файла не возникнет!
                # Video 47 from 26.02.25, 51:00.
try:
    file_name = validate_file_name('data_22_t2.txt')
    if file_name:
        file = open(file_name, 'r')
        numbers = get_numbers(file)
    print(f"Числа из файла {file_name} и соответствующие им индексы: ")
    indexing_numbers(numbers)
    pair_numb = select_numbers()                                    # for __ 1-st Variant
    # pair_numb = select_numbers(1, 4)                              # for __ 2-nd Variant
    res, operation, symbol = math_operations(pair_numb)             # 1-st Var - Для ручного ввода знака арифмет. операции в консоли.
    # res, operation, symbol = math_operations(pair_numb, '/')      # 2-nd Var - Для ввода знака арифмет. операции в коде.
except FileNotFoundError as e_fnf:
    notice_v = f"\033[31m{e_fnf}\033[m"
    print(f"{notice_v}: возможно ошибка в имени или адресе файла.")
except ValueError as e_v:
    notice_v = f"\033[31m{e_v}\033[m"
    print(f"Ошибка в файле, вероятно нечисловое значение: {notice_v}")
except NameError as e_n:
    print("Индекс может быть только целым числом: ", e_n)
except IndexError as e_indx:
    print("Индекс одного из чисел вне диапазона: ", e_indx)
except TypeError as e_t:
    notice_t = f"\033[31m{e_t}\033[m"
    print(f"Ошибка введения арифметической операции: {notice_t}.")
except ZeroDivisionError as e_0:
    notice_0 = f"\033[31m{e_0}\033[m"
    print(f"Ошибка деления на ноль: {notice_0}.")
else:
    print(f"Для пары чисел {pair_numb} результат операции {operation}: "
          f"\033[1;34m{pair_numb[0]} {symbol} {pair_numb[1]} = {res}\033[m")
finally:
    if file:
        file.close()
    print('Файл закрыт.')

