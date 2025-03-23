# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 21.03.25
 Python 59: SUMMARY - Intro OOP. Methods of Class.
 ################################################################################################################### """

# Video Lesson __: wasn't.
# Video Practice 59: -----------.
# links:
#   - Presentation: https://lms.itcareerhub.de/pluginfile.php/7892/mod_resource/content/1/Python_29_M.pptx.pdf
#   - Классы в Python: https://python-scripts.com/python-class.
#   - Как создавать классы в Python: https://highload.tech/kak-sozdavat-klassy-v-python-so-znaniem-dela-razbiraem-na-primerah/.

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

""" ___________________________________  Review of previously covered material  ___________________________________ """

""" ______ HW ---, Task --- ______ """



""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%________________   ИНКАПСУЛЯЦИЯ   _______________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

# AGAIN!!! See Video 59, 35:00
# По сути ИНКАПСУЛЯЦИЯ - ограничение доступа к полю (переменной) и методу.
""" __ NB! __ 
            -- PRIVATE_variable -->     СОВСЕМ ЗАКРЫТО! чисто для внутренней реализации:   self.__name = 
            -- PRIVATE_method   -->     СОВСЕМ ЗАКРЫТО! чисто для внутренней реализации:   .__method =   
            -- protected_variable       Просто закрыто,точнее ограничен доступ:            self._name = 
            -- protected_method         Просто закрыто,точнее ограничен доступ:            ._method = """


""" ______  Task 1  ______________________________________________________________________________________________ """
# See details about condition i file Lessons/lesson30_tasks.md .

# Разработайте класс `Student`, который использует инкапсуляцию для хранения информации о студенте.
# #### **Требования**:
# 1. **Приватные атрибуты**:
#    - `__name` (имя студента, строка)
#    - `__age` (возраст, целое число)
#    - `__grades` (список оценок, список чисел от 1 до 5)

class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__grades = []

    def get_average_grade(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)

    def add_grade(self, grade):
        if grade in range(1, 6):
        # if 1 <= grade <= 5:
            return  self.__grades.append(grade)


student = Student('Bob', 18)
print(student.get_average_grade())
student.add_grade(-3)
student.add_grade(4)
student.add_grade(5)
print(student.get_average_grade())

