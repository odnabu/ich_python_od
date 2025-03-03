# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# 21.02.25
# Python 46: Generators.
# ###################################################################################################################
# Video Lesson 46: https://player.vimeo.com/video/1058931605?h=5fb2fe93cb
# Video Practice __: wasn't.

# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# -----------------------------------------------------------

print('.' * 145)


# _________________________ Review of previously covered material _________________________




# %%%%%%%%%%%%%%%%%%%%%%%%%%%_____________   Generators   ______________%%%%%%%%%%%%%%%%%%%%%%%%%%%

# __________ Генераторы __________
# - функции или выражения, которые возвращают последовательность значений по одному за раз, во время итерации.
#       ● Вместо того чтобы возвращать все значения сразу, генераторы создают итератор, который
#         возвращает следующий элемент при каждом вызове метода __next__() или при использовании цикла for.
#       ● Генераторы используются для эффективной работы с большими объемами данных или бесконечными
#         последовательностями.
# def my_generator():
#  yield 1
#  yield 2
#  yield 3
# for item in my_generator():
#  print(item)

# __________ throw и close в генераторах __________   Video 46, 25:30
#       ● Генераторы могут использовать методы throw и close для взаимодействия с внешним кодом.
#       ● Это может быть полезным для корректной очистки ресурсов или для управления выполнением генератора.

# ___ Method  throw ___   Video 46, 25:30 +++ 28:00
# — метод, который позволяет вызвать исключение внутри генератора.

# ___ Method  close ___  Video 46, 26:30
# — метод, который приводит к завершению генератора, вызывая исключение GeneratorExit*.

# def my_generator():
#     try:
#         yield 1
#         yield 2
#         yield 3
#     except ValueError:          # Video 46, 34:50   |=> Генератор всегда либо что-то возвращает, либо завершается
#         yield None              # Video 46, 34:50       выполнение генератора, либо в результате ValueError направить
#                                 #  программу по другому пути. Т.е. можно И данные отправлять В функцию, которые будут
#                                 #  в генераторе обрабатываться, ТАКЖЕ можно регулировать работу с ошибками.
#     except GeneratorExit:
#         # Код для очистки ресурсов:
#         pass
#
# gen = my_generator()
# print(next(gen))                        # Выводит 1
# +++++++++++++++++++++++++++++
#  next(gen) === den.__next__           # __ NB! __ THE SAME!!!
# +++++++++++++++++++++++++++++
# gen.close()             # НО, если закрыть генератор .close(), то ТОГДА вызывается GeneratorExit. Video 46, 30:30
# if next(gen) < 3:                       # Video 46, 29:30
#     print(gen.throw(ValueError("Enough")))       # .throw - означает бросить в генератор исключение ValueError("Enough"),
                                                 # при этом к ValueError исключение GeneratorExit НИКАКОГО отношения НЕ имеет.

# ___ BIG EXAMPLE ___
#   Video 46, 35:35
# ___________________

# print("34234")
# print(next(gen))

# ___ GeneratorExit ___
# def my_generator():
#     try:
#         yield 1
#         yield 2
#         yield 3
#     except ValueError:
#         yield None
#     except GeneratorExit:                 # GeneratorExit - вызывается для очистки ресурсов. Video 46, 39:00
#         # Код для очистки ресурсов:
#         pass
#
# gen = my_generator()            # Video 46, 36:00
# print(next(gen))                # Выводит 1
# if next(gen) < 3:
#     print(gen.throw(ValueError("Enough")))
# # gen.close()                             # метод .close() вызывает GeneratorExit внутри генератора и тем прекращает его работу.
                                            # После метода .close() команда next(gen) уже НЕ будет работать. Video 46, 43:35.


# __________ Генератор с бесконечным циклом внутри __________  Video 46, 52:00
# — он позволяет создавать последовательности, которые не имеют конечного количества элементов.
# Генератор может генерировать бесконечную последовательность чисел Фибоначчи или бесконечный поток данных.

# ___ Генератор с бесконечным циклом внутри ___

# __ 1 - Fibonacci __
# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fib_gen = fibonacci_generator()
# for i in range(10):
#     print(next(fib_gen))
# fib_gen.close()

# __ 2 - Pattern __
# def my_generator(pattern=None):
#     if pattern is None:
#         pattern = ['>-<', '-*-', '>*<']
#     while True:
#         for i in pattern:
#             yield i
#
# gen = my_generator(['>---<', '-***-', '>***<'])
# for i in range(4):
#     print(gen.__next__())
# print("-")
# for i in range(4):
#     print(gen.__next__())

# __________ Инструкции next и send __________  Video 46, 59:20
#   ● send — метод, который передает значение внутрь генератора и одновременно возвращает следующее значение из
#            генератора.
#   ● next — метод, который также возвращает следующее значение, но не принимает никаких аргументов.

# __ 1-st Example __
# -- see this example in "Python Tutor: Visualize Code":
# https://pythontutor.com/render.html#code=def%20my_generator%28%29%3A%0A%20%20%20%20received_value%20%3D%20yield%201%0A%20%20%20%20yield%20received_value%20%2B%201%0Agen%20%3D%20my_generator%28%29%0Aprint%28gen.__next__%28%29%29%0Aprint%28gen.send%2810%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false
# def my_generator():
#     received_value = yield 1
#     yield received_value + 1
#
# gen = my_generator()
# print(next(gen))          # Выводит 1
# print(gen.send(10))       # Выводит 11

# __ 2-nd Example __
# def my_generator():
#     received_value = yield 1
#     yield received_value + 1

# gen = my_generator()
# # print(next(gen))                  # THE SAME! Выводит 1
# print(gen.__next__())             # THE SAME! Выводит 1
# print(gen.send(10))

# __ 3-d Example __
# def test():
#     s = 0
#     while True:
#         x = yield s
#         s += x
# t = test()
# print(next(t))
# print(t.send(111))
# print(t.send(123))

# __ 4-th Example __
# def my_generator():
#     value = yield
#     if value > 0:
#         yield value * 2
#     else:
#         yield value * 3
# gen = my_generator()
# next(gen)
# print(gen.send(5))            # Выводит 10
# print(gen.send(-2))           # Выводит -6

# __ 5-th Example __
def show_letters(some_str):
    yield from (letter for letter in some_str if letter.isalpha())
random_str = show_letters('A!sdf 09 _ w')
print(next(random_str))
print(next(random_str))

# ______  Task 1  ____________________________________________________________________________________________________
# Напишите генератор, который принимает на вход поток элементов и выдает только уникальные
# элементы, сохраняя их порядок встречаемости (для уже повторяющихся элементов не выдает ничего)



