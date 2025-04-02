# Dmitrii Bedov
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 31.03.25
 Deutsch Technikum: Technischer Unterricht 4.
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
# Les02 (Technischer Unterricht 5) -->
# Aufgabe 5: Schleife while Schreiben Sie ein Programm, das eine Zahl vom Benutzer abfragt und alle ihre Teiler
# unter Verwendung einer while-Schleife ausgibt.

# zahl = int(input('Geben Sie bitte eine Zahl ein: '))
# teiler = 1
# while teiler <= zahl:
#     if zahl % teiler == 0:
#         print(teiler)
#     teiler += 1

""" ______  Task 2  ______________________________________________________________________________________________ """
# Les02 (Technischer Unterricht 5) -->
# Aufgabe 6: Einführung in Zeichenketten Erstellen Sie ein Programm, das eine Zeichenkette vom Benutzer entgegen
# nimmt und eine Zeichenkette zurückgibt, bei der sich Groß- und Kleinbuchstaben abwechseln (zum Beispiel
# "Hallo" → "HaLlO").

phrase = 'Geben  Sie ein Satz ein: '
print(phrase)
wechselnde_zeichenkette = ''
# print([letter for letter in phrase])
for index, letter in enumerate(phrase):
    if index % 2 == 0:
        wechselnde_zeichenkette += letter.upper()
        # print(wechselnde_zeichenkette)
    else:
        wechselnde_zeichenkette += letter.lower()

print(wechselnde_zeichenkette)





""" ______  Task 3  ______________________________________________________________________________________________ """
#


""" ______  Task 4  ______________________________________________________________________________________________ """
# Les03 - Aufgabe 4: Generatoren
# Erstellen Sie einen Generator zur Berechnung der unendlichen Fibonacci-Folge. Das Programm soll die ersten
# 10 Zahlen dieser Folge mit dem Generator ausgeben.

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


""" ______  Task 5  ______________________________________________________________________________________________ """
# Les03 - Aufgabe 5: Arbeit mit dem Dateisystem
# Erstellen Sie ein Programm, das eine Textdatei mit dem Namen und dem Alter des Benutzers, die über die Tastatur
# eingegeben wurden, erstellt. Anschließend soll das Programm diese Datei lesen und die Daten im Format
# "Name: <Name>, Alter: <Alter>" ausgeben.


""" ______  Task   ______________________________________________________________________________________________ """
