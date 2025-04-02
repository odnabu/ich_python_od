# Dmitrii Bedov
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 24.03.25
 Deutsch Technikum: Technischer Unterricht 3.
 Бык тупогуб тупогубенький бычок у быка бела губа была тупа.
 ################################################################################################################### """
# Video Lesson 3: ---------------.
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
# Aufgabe 1: Wörterbücher:
# Schreiben Sie ein Programm, das eine Zeichenkette vom Benutzer abfragt. Das Programm
# soll die Häufigkeit jedes Zeichens in der Zeichenkette zählen und die Ergebnisse in einem
# Wörterbuch speichern, wobei der Schlüssel das Zeichen und der Wert die Häufigkeit
# seines Vorkommens ist.

# # ___ 0 Variant - my ___
# # +++++++++++++++++++++++++++++++++++
# from collections import Counter
# # +++++++++++++++++++++++++++++++++++
# zeichenkette_von_benutzer = 'Бык тупогуб тупогубенький бычок у быка бела губа была тупа'
# value_counts = Counter(zeichenkette_von_benutzer)
# # value_counts = Counter(zeichenkette_von_benutzer.split())
# print(f'{'My Variant: ':<15} {dict(value_counts.most_common())}')

# # ___ 1-st Variant from Vadim ___
# def zeihne_kette(text):
#     result = {}
#     # Die Schleife - cycle. Die FOR-Schleife.
#     for zeichnen in text:
#         if zeichnen not in result:
#             result[zeichnen] = 1
#         else:
#             result[zeichnen] += 1
#     return result
#
# print(f'{'Vadim: ':<15} {zeihne_kette(zeichenkette_von_benutzer)}')

# # ___ 2-nd Variant from Golubenko ___
# def count_chars(text):
#     return {char: text.count(char) for char in set(text)}
#
# print(f'{'Golubenko: ':<15} {count_chars(zeichenkette_von_benutzer)}')


""" ______  Task 2  ______________________________________________________________________________________________ """
# Aufgabe 2: Ausnahmen: Fehlerbehandlung:
# Erstellen Sie ein Programm, das zwei Zahlen vom Benutzer annimmt und eine Division
# durchführt. Wenn der Benutzer Null als Divisor eingibt, sollte das Programm eine
# Fehlermeldung ausgeben und um die Eingabe eines anderen Divisors bitten.

# var1 = int(input('Geben Sie eine Zahl ein: '))
# var2 = int(input('Geben Sie die zweite Zahl ein: '))
#
# try:
#     result = var1 / var2
#     print(result)
# except ZeroDivisionError as e:
#     print(e)

""" ______  Task 3  ______________________________________________________________________________________________ """
# Aufgabe 3: Iteratoren, Iterierbare Objekte und Generatoren:
# Schreiben Sie einen Generator, der vom Benutzer Anfangs- und Endwerte annimmt und
# nur gerade Zahlen im angegebenen Bereich generiert. Verwenden Sie diesen Generator,
# um alle geraden Zahlen vom Anfangs- bis zum Endwert auszugeben.



""" ______  Task 6  ______________________________________________________________________________________________ """
# Aufgabe 6: Einführung in funktionale Programmierung
# Schreiben Sie eine Funktion, die eine Liste von Zeichenketten entgegennimmt und nur diejenigen Zeichenketten
# zurückgibt, die mehr als 5 Zeichen enthalten. Verwenden Sie dafür die Funktion Filter.

def filter_length_str(list):
    return [word for word in list if len(word) > 5]
    # return list(filter(lambda s:

beispiel_liste = ["Python", "ist", "eine", "großartige", "Programmiersprache"]
print(filter_length_str(beispiel_liste))