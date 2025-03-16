# Alexander Mueller
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 06.03.25
 Deutsch Technikum: Technischer Unterricht 1.
 ################################################################################################################### """

# Video Lesson 1: ---------------.
# Video Practice __: wasn't.
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

""" ______  Task 1.1  ______________________________________________________________________________________________ """
# Verwenden Sie collections.Counter, um die Anzahl jedes Zeichens in einer Zeichenkette zu zählen. Schreiben Sie
# eine Funktion count_characters, die eine Zeichenkette annimmt und ein CounterObjekt mit der Anzahl der
# einzelnen Zeichen zurückgibt. Geben Sie anschließend die 3 am häufigsten vorkommenden Zeichen aus.

# +++++++++++++++++++++++++++++++
# from collections import Counter
# +++++++++++++++++++++++++++++++

# def count_characters(word: str):
#     symbol_counter = Counter(word)
#     return symbol_counter.most_common(3)
#
# phrase = "Verwenden Sie collections.Counter, um die Anzahl jedes Zeichens..."
# print(count_characters(phrase))

""" ______  Task 1.2  ______________________________________________________________________________________________ """
# Verwenden Sie collections.deque (очередь), um eine Warteschlange mit fester Länge zu erstellen. Schreiben Sie eine
# Funktion fixed_queue, die eine Liste von Zahlen und die maximale Länge der Warteschlange annimmt, die
# Elemente der Liste zur Warteschlange hinzufügt und den endgültigen Zustand der Warteschlange zurückgibt.

# # +++++++++++++++++++++++++++++++
# from collections import deque
# # +++++++++++++++++++++++++++++++
#
# def fixed_queue(data, max_len):
#     queue = deque(maxlen=max_len)
#     for item in data:
#         queue.append(item)
#     return queue
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# max_length = 3
# print(fixed_queue(numbers, max_length))

""" ______  Task 1.3  ______________________________________________________________________________________________ """
# Verwenden Sie collections.defaultdict, um ein Wörterbuch zu erstellen, bei dem jeder Schlüssel mehrere Werte
# haben kann (zum Beispiel eine Liste). Schreiben Sie eine Funktion group_by_first_letter, die eine Liste von Wörtern
# annimmt und sie nach dem ersten Buchstaben gruppiert, wobei defaultdict verwendet wird.

# ++++++++++++++++++++++++++++++++++
from collections import defaultdict
# ++++++++++++++++++++++++++++++++++

# def group_by_first_letter(words: list) -> dict:
#     words_dict = defaultdict(list)
#     for word in words:
#         words_dict[word[0]].append(word)
#     return words_dict
#
# some_list = ['adf', 'a;lk', 'ydas', 'qwwewr', 'lkj']
# print(group_by_first_letter(some_list))

""" ______  Task 1.4  ______________________________________________________________________________________________ """
# Erstellen Sie ein benanntes Tupel Point mit den Feldern x, y und z. Schreiben Sie eine Funktion calculate_distance,
# die zwei Point-Objekte annimmt und den Abstand zwischen ihnen im dreidimensionalen Raum berechnet.

# ++++++++++++++++++++++++++++++++++
import math
from collections import namedtuple
# ++++++++++++++++++++++++++++++++++

coord_dict = namedtuple('point', ('x', 'y', 'z'))
def calculate_distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2 + (point1.z - point2.z) ** 2)

point1 = coord_dict(12, -5.02, 34)
point2 = coord_dict(45, 15, 23)
print(calculate_distance(point1, point2))

""" ______  Task 2.1  ______________________________________________________________________________________________ """
# Schreiben Sie eine Funktion safe_divide, die zwei Zahlen annimmt und das Ergebnis ihrer Division zurückgibt.
# Wenn die Division nicht möglich ist (Division durch Null), soll die Funktion die Meldung "Cannot divide by zero"
# zurückgeben, ohne die Ausführung des Programms zu unterbrechen.


