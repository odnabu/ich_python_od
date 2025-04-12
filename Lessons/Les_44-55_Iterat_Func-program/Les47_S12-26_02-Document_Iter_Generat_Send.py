# Tatiana Kletsovka
#  \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
#  print('#' * 115)      # Для разделения блоков на листе с кодом:
 """ #################################################################################################################
 26.02.25
 Python 47: SUMMARY: Iterators. Generators + yield + send + close.
 ################################################################################################################## """
 # Video Lesson 50: .
 # Video Practice -- : --
 #
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


# ______________________________________  Review of previously covered material  ______________________________________


# %%%%%%%%%%%%%%%%%%%%%%%%%%%__________________     Documentation    __________________%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Video 47, 14:00.

# help(str)       # class - Video 47, 27:00.
# help(min)       # function - Video 47, 28:00.
# help()              # with searching in console - Video 47, 29:00.


# %%%%%%%%%%%%%%%%%%%%%%%%%%%_______________    Home Work 24, 24.02.25    _______________%%%%%%%%%%%%%%%%%%%%%%%%%%%

# __ Task 2 __ Video 47, 34:00
# start=1, step=2 --> Аргументы по умолчанию:
# def sum_of_elements(start=1, step=2):
#     while True:
#         # yield start
#         # start += step
#         start += step           # Если сделать так, то 1-ый элемент не будет выводится, а выведется -->
#         yield start             # --> следующий элемент как сумма 1-го и шага.
#
# f_num = 5
# step_num = 2
# gen = sum_of_elements(start=f_num, step=step_num)
# for _ in range(5):              # Можно реализовать с бесконечным циклом while.
#     print(next(gen))

""" Stanislav M. 13:33
С None всё прям интересно, нашел своё изыскание на эту тему:

value = None
if value == True:
    print("None is != True")
elif value == False:
    print("None is != False")
elif value == None:
    print('В контексте булей, None воспринимается falsy.') """


# ______  Task 1  ____________________________________________________________________________________________________
# Напишите генератор, в который передаются строки разной длины и который возвращает строки фиксированной
# длины 7 символов. Если длина переданной строки больше 7 символов, то возвращаются первые 7 символов.
# Если длина переданной строки меньше 7 символов, то недостающие символы присоединяются к строке слева в
# виде нулей (“abcdˮ → “000abcdˮ).

def return_seven_symbols():
    # yield None                  # None можно НЕ писать. Этот None просто для читабельности.
    #                             # yield ПРИНИМАЕТ от next(gen) запрос, ОТДАЕТ None и ЖДЕТ что придет от gen.send("abcd").
    # Потому лучше сделать так:
    string: str = yield              # :str - аннотация типа строки, чтобы появились методы.
    while True:
        print(string)
        if len(string) >= 7:
            string = yield string[:7]
            print(f'\033[34m{string}\033[m')
        else:
            string = yield string.rjust(7, "0")     # Или таким образом - ч/з    : str и .rjust()
            # string = yield "0" * (7 - len(string)) + string       # Или так - ч/з    "0" * (7 - len(string)) + string
            print(f'\033[31m{string}\033[m')

gen = return_seven_symbols()
next(gen)                           # next(gen) - перенаправляет на первый yield в функции.
print(gen.send("sdd"))
print(gen.send("abcdabcdabcdabcd"))
print(gen.send("123456756984644654"))
