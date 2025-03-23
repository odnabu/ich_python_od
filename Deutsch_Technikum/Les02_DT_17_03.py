# Dmitrii Bedov
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 17.03.25
 Deutsch Technikum: Technischer Unterricht 2.
 ################################################################################################################### """
# Video Lesson 2: ---------------.
# links:
#   - .
#   - .

# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------

print('.' * 120)

""" ______  Task 1  ______________________________________________________________________________________________ """
# Aufgabe 1. Grundlegende Sammlungen. Listen.
# Schreiben Sie ein Programm, das eine Liste von Zahlen vom Benutzer annimmt und dann Folgendes ausgibt:
#   1. Eine Liste aller einzigartigen Zahlen in der Reihenfolge ihres Auftretens.
#   2. Die Anzahl der Elemente in der ursprünglichen Liste und die Anzahl der einzigartigen Elemente.

# numb_list = [n for n in range(5)]
# print(numb_list)

list1 = [1, 3, 5, 5, 9, 2, 7, 3, 2, 3]
list2 = []
for num in list1:
    if num not in list2:
        list2.append(num)

# print(list2)
# print(len(list1))
# print(len(list2))

""" ______  Task 2  ______________________________________________________________________________________________ """
# Aufgabe 2: Listenmethoden, Tupel.
# Schreiben Sie ein Programm, das fünf Zahlen vom Benutzer annimmt, sie zu einer Liste
# hinzufügt und anschließend ein Tupel mit den einzigartigen Werten aus der Liste erstellt
# und das Tupel ausgibt.

def input_numbs_tuple():
    numb_list = [int(x) for x in input(f'Geben Sie 5 Zahlen durch Leerzeichen getrennt ein: ').split()]
    print(tuple(numb_list))

input_numbs_tuple()

# ---- from Golubenko --------------------------- Video 2, 41:30
# def unique_tuple():
#     numbers = {int(input(f'{i + 1}. Zahl: ')) for i in range(5)}
#     print(tuple(numbers))
#
# unique_tuple()
# ---------------------------------------------------------------

""" ______  Task 3  ______________________________________________________________________________________________ """
# Aufgabe 3: Listenverständnis.
# Erstellen Sie eine Liste von Zahlen von 1 bis 20 mithilfe eines Listen-Komprehensionsausdrucks und
# geben Sie eine neue Liste aus, die nur die geraden Zahlen aus dieser Liste enthält, wobei diese im
# Quadrat dargestellt werden.

# erstellen - создавать.
# die Variable.
# присвоить переменной значение - einer Variable einen Wert zuweisen.
# In range - im Bereich.
# Wir verwenden hier die range-Funktion.

# ___ 1-st Variant ___
list3 = [n for n in range(1, 21, 1)]        # Klamern AUF, Klamern ZU.
# print(list3)
for num in list3:
    if num % 2 != 0:                        # Für ungerade Zahlen.
        list3.remove(num)

list4 = []
for num in list3:
    list4.append(num ** 2)
# print(f'Gerade Zahlen - 1 Variant: {list4}')

# ___ 2-nd Variant __
gerade_zahlen = [n ** 2 for n in list3 if n % 2 == 0]
# print(f'Gerade Zahlen - 2 Variant: {gerade_zahlen}')

# ___ 3-d Variant ___
def squared_even_numb(numb_list):
    for num in numb_list:
        if num % 2 == 0:
            yield num ** 2

gen = squared_even_numb(list3)
# print(f'Gerade Zahlen - 3 Variant: {list(gen)}')

# ___ 4-th Variant ___
even_num_list = list(num ** 2 for num in filter(lambda num: num % 2 == 0, list3))
# print(even_num_list)

""" ______  Task 4  ______________________________________________________________________________________________ """
# Aufgabe 4: Verschachtelte Funktionen. Lambda-Funktionen.
# Schreiben Sie eine Funktion, die eine Liste von zweistelligen Zahlen entgegennimmt und
# eine neue Liste zurückgibt, die nach der zweiten Ziffer sortiert ist. Verwenden Sie eine
# Lambda-Funktion innerhalb der Hauptfunktion, um diese Aufgabe auszuführen.

# +++++++++++++++++++++++++++++++
import random
# +++++++++++++++++++++++++++++++
n_start, n_end, number_of = 13, 21, 10
list_random_numb = [random.randint(n_start, n_end) for _ in range(number_of)]
# print(f'List of random numbers:  {list_random_numb}')

