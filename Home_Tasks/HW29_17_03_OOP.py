# Home Work 29, 17.03.25
""" ___ 56-57: OOP ___ """

# Video Lesson 56: ______________________
# Video Practice 57: _______________________
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
# Создайте класс Rectangle для представления прямоугольника. Класс должен иметь атрибуты width (ширина) и
# height (высота), а также метод calculate_area(), который вычисляет площадь прямоугольника.
# Затем создайте экземпляр класса Rectangle с заданными значениями ширины и высоты и выведите его площадь.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height         # Тут ЛУЧШЕ делать return, т.к. производится РАСЧЕТ, который потом
                                                # может понадобится.
        # print(f'For Rectangle with width = {self.width} and height = {self.height} is '
        #       f'\n\tAREA = {self.width * self.height}')

rectangle = Rectangle(8, 7)
rectangle.calculate_area()                  # Если в методе нт print, то здесь уже результат НЕ выведется.
print(f'For Rectangle with width = {rectangle.width} and height = {rectangle.height} is '
              f'\n\tAREA = {rectangle.calculate_area()}')


""" ______  Task 2  ______________________________________________________________________________________________ """
# Создайте класс Student для представления студента. Класс должен иметь атрибуты name (имя) и age (возраст),
# а также метод display_info(), который выводит информацию о студенте. Затем создайте экземпляр класса Student с
# заданным именем и возрастом и вызовите метод display_info().

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f'Student\'s Name: {self.name}, Age: {self.age}.')

student_1 = Student('Olga', 49)
student_1.display_info()
