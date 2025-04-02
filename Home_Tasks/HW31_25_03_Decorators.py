# Home Work 31, 25.03.25
""" ___ 60-61: Decorators ___ """

# Video Lesson 60: ______________________
# Video Practice 61: _______________________
# Normal  \033[0;__;__m \033[m    or   BOLD  \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ############################################################################################################### """
# f = 40; f = '.' * f; print(f) - Filler up to.
# print(f, f'\n...')
# print(' ' * 5, f'...') - Indentation in the output of the result
# while True:                      # __ NB! __ See HW14_16_01_Func_Tuple.py, Task 2, "___ Clear code..."
#   ...
#   ask = input("\nDo you want to continue? (y/n): ").lower()
#   if ask == 'n':
#   # if user_n == 'Stop'.lower():
#       break
# def input_numb_list():            #  __ NB! __ See HW16_23_01_List_Matrix.py
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# print(f'\tName: {p.name:<10}')
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------
print('.' * 130)

part_1 = '______ Task 1 _____'
""" ______  Task 1  ______________________________________________________________________________________________ """
# Напишите декоратор validate_args, который будет проверять типы аргументов функции и выводить сообщение об ошибке,
# если переданы аргументы неправильного типа. Декоратор должен принимать ожидаемые типы аргументов
# в качестве параметров.
    # Пример использования:
    # @validate_args(int, str)
    # def greet(age, name):
    #     print(f"Привет, {name}! Тебе {age} лет.")
    # greet(25, "Анна")         # Все аргументы имеют правильные типы
    # greet("25", "Анна")       # Возникнет исключение TypeError
#
    # Ожидаемый вывод:
    # Привет, Анна! Тебе 25 лет.
    # TypeError: Аргумент 25 имеет неправильный тип <class 'str'>. Ожидается <class 'int'>.

# %%%%%%%%%%%%%%%___________ Немного теории по Декораторам, но с другой точки зрения ___________%%%%%%%%%%%%%%%
# Смотри статью по ссылке: https://pythonworld.ru/osnovy/dekoratory.html
# Декораторы — это, по сути, "обёртки", которые дают возможность изменить поведение функции, не изменяя её код.

# Пакет inspect позволяет получить информацию об объектах, таких как модули, классы, методы, функции, объекты кода и т.д.
# Смотри здесь: https://digitology.tech/docs/python_3/library/inspect.html.
# # ++++++++++++++
# import inspect
# # ++++++++++++++
# # Задаю имя параметрического декоратора и переменные:
# # def validate_args(type1, type2):
# def validate_args(*types):
#     """
#     Декоратор, который проверяет типы аргументов функции и выводит сообщение об ошибке,
#     если переданы аргументы неправильного типа.
#     """
#     # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой - func,
#     # получая возможность исполнять произвольный код до и после неё.
#     def decorator(func):
#         # Позиционные аргументы (*args) +++ Именованные аргументы (**kwargs) --->
#         # - https://sky.pro/wiki/python/rabota-s-argumentami-v-python-args-i-kwargs/
#         def wrapper(*args, **kwargs):
#             # Оборачиваю в рамку для понимания происходящего, для чего перед выводом функции (сверху) добавлю линию '%':
#             print('%' * 60)
#             # ---- 1-st Variant - SIMPLE --------------------------
#            # if type(args[0]) != type1 and type(args[1]) != type2:
#            #     print(f'\033[31m{' ERROR':<10}\033[0m Argument \033[36m{args[0]}\033[m should be {type1}\n'
#            #           f'{' ':<10} and Argument \033[36m{args[1]}\033[m should be {type2}!')
#            # elif type(args[0]) != type1:
#            #     print(f'\033[31mERROR\033[0m: should be {type1}!')
#            # elif type(args[1]) != type2:
#            #     print(f'\033[31mERROR\033[0m: should be {type2}!')
#            # else:
#            #     # Верни саму функцию:
#            #     func(*args, **kwargs)
#            # -----------------------------------------------------
#            #
#            # ---- 2-nd Variant -------------------------------------
#            # try:
#            #     signature = inspect.signature(func)
#            #     # print(signature)
#            #     func_args = [param.name for param in signature.parameters.values()]
#            #     # print(func_args[0], func_args[1])
#            #     # print(type(args[0]) == type1)   ===   # print(isinstance(args[0], type1))
#            #     if type(args[0]) != type1 and type(args[1]) != type2:
#            #         raise TypeError(f'Arguments {args[0]} and {args[1]} have a wrong type:\n'
#            #                         f'{' ':<10}{type(args[0])} and {type(args[0])} respectively.\n'
#            #                         f'{' ':<10}\033[34m{func_args[0]}\033[m - Should be {type1},\n'
#            #                         f'{' ':<10}\033[34m{func_args[1]}\033[m - Should be {type2}.')
#            #     elif type(args[0]) != type1:
#            #         raise TypeError(f'Argument {args[0]} has a wrong type: {type(args[0])}.\n'
#            #                         f'\t\t\033[34m{func_args[0]}\033[m - Should be {type1}.')
#            #     elif type(args[1]) != type2:
#            #         raise TypeError(f'Argument {args[1]} has a wrong type: {type(args[1])}.\n'
#            #                         f'\t\t\033[34m{func_args[1]}\033[m - Should be {type2}.')
#            #     else:
#            #         # Верни саму функцию:
#            #         return func(*args, **kwargs)
#            # except TypeError as e:
#            #     print(f'\033[31m{' ERROR':<10}\033[0m{e}')
#            # -----------------------------------------------------
#             """ ---- 3-d Variant - COMPLETE ------------------------------------- """
#             # See SUMMARY with Home Works: https://colab.research.google.com/drive/1cYvBwl54vdc6dcfrcPuHjI1ERkiV1xKh#scrollTo=P7Zcj5Y4OOtK
#             # try:
#             # Для выведения на экран имен аргументов внутри функции func из пакета анализа inspect пользуюсь методом .parameters.values():
#             signature_of_func = inspect.signature(func)
#             func_args = [param.name for param in signature_of_func.parameters.values()]        # Имена аргументов в функции func --> For testing.
#             # -------------------------------------------------------------------------------------------------
#             # Список для хранения ошибок:
#             errors = []
#             # Функция zip() - итератор, используется для совмещения двух и более списков в один. Возвращает
#             # итератор кортежей: https://sky.pro/media/rabota-s-funkcziej-zip-v-python/.
#             for item, (arg, expected_type) in enumerate(zip(args, types)):
#                 # Проверить, является ли объект экземпляром указанного класса, смотри ссылку: https://sky.pro/media/raznicza-mezhdu-funkcziyami-type-i-isinstance-v-python/
#                 # print([isinstance(arg, types) for arg in zip(args, types)])       # For testing.
#                 if not isinstance(arg, expected_type):
#                     # Индекс определенного элемента в списке, например, index = fruits.index("cherry") -->
#                     # https://sky.pro/media/nahozhdenie-indeksa-elementa-v-spiske-python/
#                     # print(args.index(arg), func_args[args.index(arg)])
#                     errors.append(f'Argument {arg} have a wrong type: {type(arg)}\n'
#                                     f'{' ':<10}{func_args[item]} --> Should be {expected_type}.\n')
#             # Вывод всех ошибок, если они есть:
#             if errors:
#                 er = f'\033[31m{" ERROR":<10}\033[0m'
#                 print(er + er.join(errors))
#                 # print(f'\033[31m{" ERROR":<10}\033[0m' + "\n".join(errors))
#                 return
#
#             # Если ошибок нет, верни саму функцию:
#             return func(*args, **kwargs)
#
#         # except TypeError as e:
#         #     print(f'\033[31m{' ERROR':<10}\033[0m{e}')
#         # -----------------------------------------------------
#
#         # И ещё одну линию '-' после:
#         print('-' * 60)
#         # Возвращаю функцию из "обёртки" - wrapper:
#         return wrapper
#     return decorator
#
# # Теперь вызываю функцию, которуЮ возвращает декоратор, т.е. вызываю её "обёртку", передаю ей аргументы, а она
# # в свою очередь передаёт их декорируемой функции greet():
#
# @validate_args(int, str)
# def greet(age, name):
#     print(f"Привет, {name}! Тебе {age} лет.")
#
# greet(25, "Анна-correct")
# greet('25', ["Анна-error"])
# # greet(25, ["Анна-error"])



# ==== for lms ===============================================================================
# Пакет inspect позволяет получить информацию об объектах, таких как модули, классы, методы, функции, объекты кода и т.д.
# ++++++++++++++
import inspect
# ++++++++++++++
def validate_args(*types):
    """
    Декоратор, который проверяет типы аргументов функции и выводит сообщение об ошибке,
    если переданы аргументы неправильного типа.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('>' * 60)
            signature_of_func = inspect.signature(func)
            func_args = [param.name for param in signature_of_func.parameters.values()]
            # Список для хранения ошибок:
            errors = []
            for item, (arg, expected_type) in enumerate(zip(args, types)):
                if not isinstance(arg, expected_type):
                    errors.append(f'Argument {arg} have a wrong type: {type(arg)}\n'
                                    f'{' ':<10}{func_args[item]} --> Should be {expected_type}.')
            # Вывод всех ошибок, если они есть:
            if errors:
                er = f'\n\033[31m{" ERROR":<10}\033[0m'
                print(er + er.join(errors))
                print('-' * 60)
                return

            # Если ошибок нет, верни саму функцию:
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_args(int, str)
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет.")

greet(25, "Анна-correct")
greet('25', ["Анна-error"])


""" ______  Task 2  ______________________________________________________________________________________________ """
# Напишите декоратор log_args, который будет записывать аргументы и результаты вызовов функции в лог-файл.
# Каждый вызов функции должен быть записан на новой строке в формате "Аргументы: <аргументы>,
# Результат: <результат>". Используйте модуль logging для записи в лог-файл.
#     Пример использования:
#     @log_args
#     def add(a, b):
#         return a + b
#     add(2, 3)
#     add(5, 7)
#
#     Ожидаемый вывод в файле log.txt:
#     Аргументы: 2, 3, Результат: 5
#     Аргументы: 5, 7, Результат: 12
#
# Убедитесь, что перед запуском кода у вас создан файл log.txt в той же директории, где находится скрипт Python.

# See:  - Модуль logging: https://sky.pro/media/kak-rabotat-s-modulem-logging-v-python/
#       - Логирование в Python: https://habr.com/ru/companies/wunderfund/articles/683880/
#       - logging — Logging facility for Python: https://docs.python.org/3/library/logging.html

# # +++++++++++++++++++++++++++
# import logging
# # +++++++++++++++++++++++++++
# # Настройка записи логов:
# FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
# logging.basicConfig(filename='log.txt', format=FORMAT, level=logging.INFO)
#
# def log_args(func):
#     """
#     Декоратор, который записывает аргументы и результаты вызовов функции в лог-файл.
#     """
#     def wrapper(*args, **kwargs):
#         # Позиционные аргументы (*args) +++ Именованные аргументы (**kwargs) --->
#         # - https://sky.pro/wiki/python/rabota-s-argumentami-v-python-args-i-kwargs/
#         # Оборачиваю в рамку для понимания происходящего, для чего перед выводом функции (сверху) добавлю линию '%':
#         print('%' * 60)
#
#         # Вызываю функцию, введенную мной после декоратора и получаю из нее результат:
#         result = func(*args, **kwargs)
#         print(result)
#         # Забираю аргументы и результат для записи в лог-файл:
#         args_str = ", ".join(map(str, args))
#         # -------- То что в 2 строках ниже - НЕ обязательно  -------------------------------------------
#         # kwargs_str = ", ".join(f'{k}={v}' for k, v in kwargs.items())
#         # logging.info(f'Arguments: {args_str}{', ' + kwargs_str if kwargs else ''}, Result: {result}')
#         # -----------------------------------------------------------------------------------------------
#         logging.info(f'Arguments: {args_str}. Result: {result}')
#         return result
#
#         # И ещё одну линию '-' после:
#         print('-' * 60)
#     # Возвращаю декорированную функцию из "обёртки" - wrapper:
#     return wrapper
#
# @log_args
# def add(a, b):
#     return a + b
#
# add(2, 3)
# add(5, 7)


