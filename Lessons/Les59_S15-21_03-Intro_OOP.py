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
        -- PRIVATE_variable -->   СОВСЕМ ЗАКРЫТО! чисто для внутренней реализации. ВНЕ класса НЕ вызывать:   self.__name = 
        -- PRIVATE_method   -->   СОВСЕМ ЗАКРЫТО! чисто для внутренней реализации. ВНЕ класса НЕ вызывать:   .__method =   
        -- protected_variable     Просто закрыто, точнее ограничен доступ. ВНЕ класса НЕ вызывать:           self._name = 
        -- protected_method       Просто закрыто, точнее ограничен доступ. ВНЕ класса НЕ вызывать:           ._method = """


""" ______  Task 1  ______________________________________________________________________________________________ """
# See details about condition i file Lessons/lesson30_tasks.md .

# Разработайте класс `Student`, который использует инкапсуляцию для хранения информации о студенте.
# #### **Требования**:
# 1. **Приватные атрибуты**:
#    - `__name` (имя студента, строка)
#    - `__age` (возраст, целое число)
#    - `__grades` (список оценок, список чисел от 1 до 5)

class Student:
    # 2.1 - Конструктор `__init__(name, age)`, принимает имя и возраст, а список оценок создаёт пустым:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__grades = []

    # 2.2 - getter for Name and Age:
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # 2.3 - Сеттер для `_age`, который не позволяет установить возраст меньше 16 лет:
    def set_age(self, age):
        if age < 16:
            print(ValueError('Age must be at least 16.'))
        else:
            self.__age = age

    # 2.4 - Метод, который добавляет оценку (только если она от 1 до 5):
    def add_grade(self, grade):
        if grade in range(1, 6):
            # if 1 <= grade <= 5:
            return  self.__grades.append(grade)
        else:
            print(ValueError('Grade must be between 1 and 5.'))

    # 2.5 - Метод, который возвращает средний балл (или `None`, если оценок нет):
    def get_average_grade(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)

    # Дополнительно. Реализуйте метод `__str__()`, который возвращает строку с данными студента.
        # (See theory https://sky.pro/media/raznicza-mezhdu-__str__-i-__repr__-v-python/)
        # при попытке преобразовать объект класса Student в строку, будет получено представление объекта student_1:
    def __str__(self):
        return f'Student: {self.__name}, age: {self.__age}, grades: {self.__grades}.'
        # при вызове repr() для объекта класса Student, будет получено представление объекта в виде,
        # который может быть использован для воссоздания объекта:
    def __repr__(self):
        return f"Student(name={self.__name!r}, age={self.__age!r}, grades={self.__grades!r}))"

    # Ful INFO about Student:
    def get_students_info(self):
        return (f'\t{'Student:':<15} {self.__name}\n'
                f'\t{'Age:':<15} {self.__age}\n'
                f'\t{'Average grade:':<15} \033[31m{round(sum(self.__grades) / len(self.__grades), 2)}\033[m\n')


student_1 = Student('Bob', 18)
# print(student_1.get_average_grade())          # This is for understanding, why NONE appears.
student_1.add_grade(-3)
student_1.add_grade(4)
student_1.add_grade(1)
student_1.add_grade(5)

student_2 = Student('Diane', 16)
student_2.add_grade(3)
student_2.add_grade(5)
student_2.add_grade(3)

print(f'{'__ 2.5 get_av_grade __':_<80}', end='\n')
print(student_1.get_average_grade())

print(f'{'__ 2.2 get name & age __':_<80}', end='\n')
print(student_1.get_name())
print(student_1.get_age())

print(f'{'__ 2.3 not set age < 16 __':_<80}', end='\n')
student_1.set_age(15)

# Дополнительно. Реализуйте метод `__str__()`
print(f'\n{'__ Дополнительно методы __str__(),  __repr__  __':_<80}', end='\n')
print(student_1)
print(repr(student_1))
print(f'{'___   __str__   ':_<80}\n',
      student_1.__str__())
print(f'{'___  __repr__   ':_<80}\n',
      student_1.__repr__())

# Ful INFO about Student:
print(f'\n{'__ Full student\'s info: __':_<80}', end='\n')
print(student_1.get_students_info())
print(student_2.get_students_info())

# print(dir(student_1))

# ВОПРОС: имеет ли смысл делать в классе обработку ошибок?
