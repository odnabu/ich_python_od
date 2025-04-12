# Dmitrii Bedov
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 07.04.25
 Deutsch Technikum: Technischer Unterricht 5.
 Бык тупогуб тупогубенький бычок у быка бела губа была тупа.
 ################################################################################################################### """

# Video Lesson 4: ---------------.
# links:
#   - .
#   - .

# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Alt+Enter / Ctrl-Alt+L - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------

print('.' * 120)

""" ______  Task 1  ______________________________________________________________________________________________ """
# DA_Technical_Python_LfS8-04-25.pdf
# Aufgabe 1: Einführung in OOP
# Erstellen Sie eine Klasse Kreis mit dem Attribut Radius und Methoden zur Berechnung des Umfangs und der Fläche
# des Kreises. Das Programm sollte ein Objekt der Klasse erstellen und die Ergebnisse der Berechnungen ausgeben.

# # +++++++++++++++++
# import math
# # +++++++++++++++++
#
# class Kreis:
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def umfang(self):
#         # return round(2 * math.pi * self.radius, 2)
#         return 2 * math.pi * self.radius
#
#     def flaeche(self):
#         return math.pi * self.radius ** 2
#
# kreis = Kreis(3)
# print(f'Der Umfang des Kreises: {kreis.umfang():.2f}')
# print(f'Die Flaeche des Kreises: {kreis.flaeche():.3f}')



""" ______  Task 2  ______________________________________________________________________________________________ """
# DA_Technical_Python_LfS8-04-25.pdf
# Aufgabe 2: Klassenmethoden
# Schreiben Sie eine Klasse Zaehler, die eine Klassenmethode enthält, die die Anzahl der erstellten Objekte dieser
# Klasse zurückgibt. Erstellen Sie mehrere Objekte und überprüfen Sie, ob die Methode die Anzahl korrekt zurückgibt.

# Создайте декоратор, который подсчитывает количество вызовов декорируемой функции. Примените этот декоратор к
# функции, которая выводит приветственное сообщение для пользователя.

# class Zaehler:
#     counter = 0
#
#     def __init__(self):
#         Zaehler.counter += 1
#
#     @classmethod
#     def get_counter(cls):
#         return Zaehler.counter
#
#
# obj_1 = Zaehler()
# obj_2 = Zaehler()
# print(Zaehler.get_counter())
# # print(obj_1.counter)          # Nich richtich!
# # print(obj_2.get_counter())    # Nich richtich!
# # print(obj_2.counter)          # Nich richtich!
# # obj_3 = Zaehler()             # Nich richtich!
# # print(obj_3.counter)          # Nich richtich!


""" ______  Task 3  ______________________________________________________________________________________________ """
# Erstellen Sie einen Dekorator, der die Anzahl der Aufrufe der dekorierten Funktion zählt. Wenden Sie diesen
# Dekorator auf eine Funktion an, die eine Willkommensnachricht für den Benutzer ausgibt.

# Создайте декоратор, который подсчитывает количество вызовов декорируемой функции. Примените этот декоратор к
# функции, которая выводит приветственное сообщение для пользователя.

# Wie man *args und **kwargs in Python-Funktionsaufrufen kombiniert:
# https://labex.io/de/tutorials/python-how-to-combine-args-and-kwargs-in-python-function-calls-417958
# In Python sind *args und **kwargs spezielle Syntaxelemente, die in Funktionsdefinitionen verwendet
# werden, um eine flexible Anzahl von Argumenten zu akzeptieren.
#
# *args
# *args wird verwendet, um eine beliebige Anzahl von positional arguments (positionsbasierte Argumente)
# an eine Funktion zu übergeben.
# Es wird als Tupel innerhalb der Funktion behandelt.
# Beispiel:
#
# python
# def addiere(*args):
#     return sum(args)

# print(addiere(1, 2, 3))        # Ausgabe: 6
# print(addiere(4, 5, 6, 7, 8))  # Ausgabe: 30
# Erklärung:
# Die Funktion addiere nimmt beliebig viele Zahlen entgegen.
# Alle übergebenen Argumente werden in args als Tupel gespeichert (args = (1, 2, 3) im ersten Beispiel).
# Dies ist nützlich, wenn die Anzahl der Argumente nicht im Voraus bekannt ist.
# **kwargs
# **kwargs wird verwendet, um eine beliebige Anzahl von keyword arguments (Schlüssel-Wert-Paare) an eine Funktion zu übergeben.
# Es wird als Dictionary innerhalb der Funktion behandelt.
# Beispiel:
#
# python
# def benutzer_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# benutzer_info(name="Anna", alter=25, beruf="Ingenieurin")

# # Ausgabe:
# # name: Daniela
# # alter: 25
# # beruf: Ingenieurin
# Erklärung:
# Die Funktion benutzer_info akzeptiert beliebige Schlüssel-Wert-Paare.
# Diese werden in kwargs als Dictionary gespeichert (kwargs = {'name': 'Anna', 'alter': 25, 'beruf': 'Ingenieurin'}).
# Kombination von *args und **kwargs
# Man kann beide zusammen verwenden, um sowohl positionsbasierte als auch Schlüssel-Wert-basierte Argumente zu akzeptieren.
#
# Beispiel:
#
# python
# def beispiel_funktion(a, b, *args, **kwargs):
#     print(f"a: {a}, b: {b}")
#     print(f"args: {args}")
#     print(f"kwargs: {kwargs}")
#
# beispiel_funktion(1, 2, 3, 4, x=5, y=6)
# # Ausgabe:
# # a: 1, b: 2
# # args: (3, 4)
# # kwargs: {'x': 5, 'y': 6}
# Erklärung:
# Die ersten beiden Argumente (a, b) sind normale positionsbasierte Argumente.
# Weitere positionsbasierte Argumente (3, 4) werden in args gespeichert.
# Schlüssel-Wert-Paare (x=5, y=6) landen in kwargs.

def decorator(funk):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return funk(*args, **kwargs)
    wrapper.counter = 0
    return wrapper

@decorator
def sag_willkommen():
    print(f'Herzlich willkommen')

sag_willkommen()
sag_willkommen()
sag_willkommen()
print(sag_willkommen.counter)


""" ______  Task 4  ______________________________________________________________________________________________ """
#


""" ______  Task 5  ______________________________________________________________________________________________ """
#


""" ______  Task   ______________________________________________________________________________________________ """
