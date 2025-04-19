# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 18.04.25
 Python 77: Revision - SUMMARY 19.
 ################################################################################################################### """

# Video Lesson 77: ------------.
# Video Practice __: wasn't.
# links:
#   - Presentation:
#   - Python RegEx: практическое применение регулярок: https://tproger.ru/translations/regular-expression-python.
#   - Регулярные выражения в Python от простого к сложному: https://habr.com/ru/articles/349860/.
#
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Ctrl+Akt+L / Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Ctrl+Shift + F - Найти по всем файлам.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------

print('.' * 120)

""" ___________________________________  Review of previously covered material  ___________________________________ """

# Video 77,

#########################################
#        if __name__ == "__main__":     #
#            _main()                    #
#########################################


""" \\\\ __ NB! __ \\\\  isinstance(<object>, <type of data>)  -->  ПРОВЕРКА типа данных перед выполнением операций!!! """
# num = 3
# if isinstance(num, int):
#     print(num + 2)


""" __ NB! __  - colorama, tabulate - Пакеты для оформления вывода )) """


""" ------------------- """
"""       Colorama      """
""" ------------------- """
#  — это пакет для Python, который позволяет добавлять цвета и стилизацию текста в терминале.
# После установки пакета Colorama, для того чтобы использовать его в своем Python-скрипте, необходимо
# импортировать модуль с помощью строки from colorama import init, Fore, Back, Style.
# Это позволит вам работать с цветами текста, фоном и стилями.
# Для того чтобы Colorama корректно работала на операционной системе Windows, необходимо вызвать
# функцию init() перед началом использования других функций из пакета.
# ++++++++++++++++++++++++++++++++++++++++++++
from colorama import Fore, Style, Back, init
init()
# ++++++++++++++++++++++++++++++++++++++++++++
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
print(Fore.RED + Style.BRIGHT + ' Красный текст ' + Style.RESET_ALL)
print(Back.BLACK + ' BLACK фон ' + Style.RESET_ALL)
print(Fore.BLACK + Back.YELLOW + ' Black текст на Yellow фоне ' + Style.RESET_ALL)


""" ------------------- """
"""       tabulate      """
""" ------------------- """
#  - Печать таблиц: https://habr.com/ru/articles/709282/
# +++++++++++++++
import tabulate
# +++++++++++++++
data = [
    ['id', 'name', 'number'],
    [0, 'Jeff', 1234],
    [1, 'Bob', 5678],
    [2, 'Bill', 9123]
]
results = tabulate.tabulate(data)
print(results)


""" ------------------- """
"""     prettytable     """
""" ------------------- """
#  - Пакет для красивого оформления и вывода таблиц. Есть поддержка заголовков столбцов,
# импорт из CSV и SQL: https://habr.com/ru/companies/macloud/articles/559042/
# Синтаксис опять же очень простой:

# +++++++++++++++++++++++++++++++++++
from prettytable import PrettyTable
# +++++++++++++++++++++++++++++++++++
x = PrettyTable()
x.title = f'\033[33m Pretty Table \033[m'
# x.start = 0
x.header = True
x.header_style = 'title'
x.align = 'l'
x.vertical_char = ' '     # ⁚ ∘ ∙ • ⁝ ⁘ ⁙ ⁛ ⁞ ◊ ▴ ▲ △ ◇ ◈ ◻ □ ◪ ◩ ∴ ∷ ∵ ⌜ ⌝ ⌞ ⌟ ⌏ ⌎ ⌍ ⌌
x.horizontal_char = f'∙'
# x.horizontal_align_char = '*'
x.junction_char = ':'
# x.top_junction_char = ':'
# x.top_right_junction_char = '⌝'
x.field_names = ["Country", "Capital", "is_russia"]
x.add_row(["Russia", "Moscow", True])
x.add_rows([["Argentina", "Buenos Aires", False], ["Jamaica", "Kingston", False]])
x.add_column("Starts with A", [False, True, False])

print(x)



# Fabulous - вывод текста с тенями или даже картинок - Как-то странно работает или, скорее, НЕ работает.
# К тому же, долго грузилась.
# +++++++++++++++++++++++++++++++++++
# from fabulous import text, image
# +++++++++++++++++++++++++++++++++++
# print(text.Text("Барсук!", color='#ff8c00', shadow=True, skew=5))
# print(image.Image("барсук.png"))



# Библиотека Tkinter - позволяет создавать приложения с графическим интерфейсом.
# https://selectel.ru/blog/tutorials/tkinter-library-in-python/
# +++++++++++++++
# import tkinter
# +++++++++++++++







""" __________ --- __________ """



""" ______  Task 1  ______________________________________________________________________________________________ """
#




