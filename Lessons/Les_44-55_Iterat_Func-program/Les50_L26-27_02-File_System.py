# Tatiana Kletsovka
# \033[0;fone;__m \033[m   or   \033[1;fone;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################ 
 27.02.25
 Python 50: File System - Работа с файловой системой.
 ################################################################################################################### """
# Video Lesson 50: https://player.vimeo.com/video/1060853210?h=ab29e70def.
# Video Practice __: .
#
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


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%________   Работа с файловой системой   ________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

""" __________ Аргументы командной строки __________ """    # Video 50, 12:50
# — строки, разделенные пробелами, и могут быть доступны программе через специальный объект sys.argv из модуля sys.

""" __ Запуск .py-файла __ """
   # - При запуске .py-файла можно передать аргументы командной строки, которые могут быть использованы программой для
   #   выполнения определенных действий или настроек.
   # - Во время выполнения программы можно получить доступ к переменным окружения, которые предоставляют информацию о
   #   системе или пользователе.

""" __________ Модуль sys __________ """
# — модуль, который предоставляет доступ к некоторым переменным и функциям, связанным с интерпретатором
#   Python и работой программы.

""" ___ sys.argv ___ """        # Video 50, 17:20
# — это атрибут модуля, который представляет список аргументов командной строки, переданных программе при запуске.

# +++++++++++++++++
# import sys                  """ __ NB! __ """  # подгружаем модуль sys.    -->   Video 50, 21:00
# +++++++++++++++++
# args = sys.argv     # После запуска кода ничего НЕ произойдет, НО передастся: ['C:\\Users\\odnab\\PycharmProjects\\PythonProject\\Lessons\\Les50_27_02_File-System..py']
# print(args)

# __ Video 50, 19:40 __ Если работать в ТЕРМИНАЛЕ и ввести команду: {python Lessons/Les50_27_02_File-System.py}, то запустится
# файл со скриптом, и в терминале выведется адрес файла в виде текста. Если теперь в консоли Пайтона
# прописать произвольные аргументы ч/з пробел вот так:
# {python Lessons/Les50_27_02_File-System.py asd reert wew}, |--> то на консоль вернется список с аргументами:
# (.venv) PS C:\Users\odnab\PycharmProjects\PythonProject> python Lessons/Les50_27_02_File-System.py asd reert wew
# Вернет:
# ...................................................................................................................
# ['Lessons/Les50_27_02_File-System.py', 'asd', 'reert', 'wew']
""" +++++++++++++++++++++++++++++++++++++++++++++++++++++++++      Video 50, 23:50  +  __ NB! __ Video 50, 31:10.
    __ NB! __ На GIT и GitHub НЕ отправлять папку (.venv)!
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ """

# __ NB! __ _______________________
#  Stanislav M. 11:14
#  python -m venv .venv  -  запустить в терминале, всё *находясь в главной папке проекта
#  PyCharm не умеет сам активировать?Оо
#  .venv\Scripts\Activate.ps1               # windows
#  .venv\Scripts\Activate                   # linux
#  Yevgeniy G 11:17
#  да так и есть пересоздал проект .venv - теперь есть в терминале.
# _________ _______________________

""" ______  Task 1  ______________________________________________________________________________________________ """
# Video 50, 35:05

# Создайте файл test.py со следующим содержимым:
# +++++++++++++++++
# import sys
# +++++++++++++++++
# print('Список параметров, переданных скрипту')
# print(sys.argv)
# print([arg for arg in sys.argv if arg[0]!='-'])         # Здесь "-" - ФЛАГ! А этой командной строкой (list compehencions) убрали флаги.
# # Запустите файл test.py следующим образом:
# # $ python3 test.py -file test.txt -pi 3.14
# # Здесь из введенных аргументов скрипт выведет элементы БЕЗ флагов.

""" __________ Модуль argparse __________ """       # Video 50, 40:35
 #  — модуль, который предоставляет более удобный и гибкий способ работы с аргументами командной строки.
 # Он позволяет определить ожидаемые аргументы и их типы, задать справку и подсказки для пользователей,
 # обрабатывать аргументы с использованием более сложной логики.
 # Модуль argparse упрощает разработку интерфейса командной строки и повышает читаемость кода.

# +++++++++++++++++
# import argparse
# +++++++++++++++++
# parser = argparse.ArgumentParser()        # Сначала оздаем парсер в который будем добавлять аргументы, т.е.
                                            # создаем объект, который будет хранить информацию, (Video 50, 41:29).
# parser.add_argument('--input', help='Path to input file')
# parser.add_argument('--output', help='Path to output file')
# args = parser.parse_args()                # Затем флаги считываются (Video 50, 42:20), и здесь к парсеру обращаемся
                                            # и просим распарсить аргументы, которые в свою очередь складываем в args.
# print(args.input)
# print(args.output)

# Oleksii Starodubov 11:35
# напишем баш скрипт и в кронтаб закинем. пусть проверяет:)

# (.venv) PS C:\Users\odnab\PycharmProjects\PythonProject> python Lessons/Les50_27_02_File-System.py --output names_1.txt


""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%________   Файловая система компьютера   ________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

# — это организация и структурирование файлов и папок на диске.
#   ● В операционных системах существует иерархическая структура каталогов, начиная от корневого
#     каталога, который содержит все остальные каталоги и файлы.
#   ● Работа с файловой системой позволяет программам выполнять операции чтения, записи, создания,
#     перемещения и удаления файлов и папок.

""" __________ Модуль os и его подмодуль - метод os.path __________ """

""" ______ os ______ """
 # — это модуль, который предоставляет функции для работы с операционной системой, включая файловую систему.
 #   - os.chdir() - Позволяет изменить текущее местоположение (перейти в...) рабочий каталог.
 #   - os.getcwd() - Возвращает текущий рабочий каталог.
 #   - os.listdir() - Возвращает список файлов и папок в указанном каталоге.
 #   - os.mkdir() - Создает новый каталог.
 #   - os.makedirs() - Создает новый каталог вместе со всеми промежуточным и каталогами.
 #   - os.walk() - Рекурсивно перебирает все файлы и папки в указанном каталоге.

# __ NB! __ Video 50, 1:10:00
# +++++++++++++++++
# import os
# +++++++++++++++++
# # os.chdir('/path/to/directory')
# current_dir = os.getcwd()
# print(f'current_dir \033[32m--> {current_dir}\033[m')
# files = os.listdir(current_dir)
# os.mkdir('new_directory')
# os.makedirs('new_directory/sub_directory')
# for dirpath, dirnames, filenames in os.walk(current_dir):    # Пройтись по директориям рекурсивно. Video 50, 1:18:00
#     for filename in filenames:
#         print(os.path.join(dirpath, filename))

# Video 51, 20:00:
# for dirpath, dirnames, filenames in os.walk("."):
#     for filename in filenames:
#         print(os.path.join(dirpath, "new", filename))
#     for dirname in dirnames:
#         print(os.path.join(dirpath, "new", dirname))
#
# print()

""" ______ os.path ______ """
# see https://lms.itcareerhub.de/pluginfile.php/7880/mod_resource/content/1/Python_26_M.pptx.pdf , Slide 36.
#  — модуль, который предоставляет функции для работы с путями файлов и каталогов.
#  Он предоставляет кроссплатформенные методы для создания, обработки и проверки путей.
#   - os.path.join() - Объединяет компоненты пути в единый путь.
#   - os.path.abspath() - Возвращает абсолютный путь.
#   - os.path.exists() - Проверяет существование файла или каталога.
#   - os.path.isdir() - Проверяет, является ли путь каталогом.
#   - os.path.isfile() - Проверяет, является ли путь файлом.

# # +++++++++++++++++
# import os
# # +++++++++++++++++
# path = os.path.join('/path/to', 'products.txt')
# print(f'{path} \033[32m--> .path.join\033[m')
# absolute_path_correct = os.path.abspath(os.getcwd())
# print(f'{absolute_path_correct} \033[32m--> .path.abspath(os.getcwd()\033[m')
# absolute_path = os.path.abspath(path)
# print(absolute_path)
# exists = os.path.exists(absolute_path_correct)
# print(exists)
# exists = os.path.exists(absolute_path)
# print(exists)
# is_directory = os.path.isdir(absolute_path_correct)
# is_file = os.path.isfile(absolute_path_correct)
# print(is_file)
# print(is_directory)

# # +++++++++++++++++
# import os
# # +++++++++++++++++path1 = "folder1"
# path1 = "folder1"
# path2 = "folder2"
# path3 = "products.txt"
# result1 = os.path.join(path1, path2, path3)
# result2 = "/".join([path1, path2, path3])
# print(result1, result2, sep='\n')

# print(type(os.path.join))           # <class 'function'>

""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%____________   Рекурсивные функции   ___________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """

# — функции, которые позволяют обрабатывать все файлы и папки внутри заданного каталога, включая вложенные каталоги.
#     ● Рекурсивные функции для выполнения операций, которые требуют обхода всей структуры каталогов, например,
#       для поиска файлов определенного типа или копирования файлов в другое место.
#     ● Рекурсивные функции можно реализовать с использованием циклов или рекурсии, вызывая себя для
#       каждого вложенного каталога.

# +++++++++++++++++
# import os
# +++++++++++++++++
# def process_directory(directory):
#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)
#         if os.path.isfile(file_path):
#             # Обработка файла:
#             print(file_path)
#         elif os.path.isdir(file_path):
#             # Рекурсивный вызов для вложенного каталога:
#             process_directory(file_path)
#
# start_directory = '/path/to/start_directory'
# process_directory(start_directory)


""" %%%%%%%%%%%%%%%%%%____________   Поиск файла, определение его абсолютного пути   ___________%%%%%%%%%%%%%%%%%% """

""" ПРИМЕР от Копилот """   #  который включает поиск файла, определение его абсолютного пути,
# замену бэкслешей (\) на слеши (/), а также открытие файла по абсолютному пути.
# Для этого используется модуль os, который предоставляет функции для работы с файловой системой.

# +++++++++++++++
import os
# +++++++++++++++

# Имя файла, который нужно найти:
file_name = "products.txt"
# file_name = "example_Shakespeare.txt"

# ___   -1- Поиск файла:   ___
# Используется os.walk, чтобы рекурсивно обходить текущую директорию и её поддиректории. По умолчанию "." -
# что значит искать в текущей директории и её поддиректориях. -->
# - Я же ставлю "..", чтобы искал от директории на уровень выше, т.е. в папке с проектом PythonProject.
# Если файл с именем file_name найден, его абсолютный путь возвращается с помощью os.path.join.

# Функция поиска файла:
def find_file(file_name, search_directory):
    for root, dirs, files in os.walk(search_directory):
        if file_name in files:
            # Возвращаю абсолютный путь к файлу:
            return os.path.join(root, file_name)
    return None

# Поиск файла в директории на уровень выше (".."), т.е. в папке с проектом PythonProject и поддиректориях:
# directory_path = r'C:\Users\odnab\PycharmProjects\PythonProject'
directory_path = '../..'
file_path = find_file(file_name, directory_path)

# ___   -2- Замена слешей:  +++   -3- Открытие файла:   ___
# - Метод replace("\\", "/") заменяет все бэкслеши на обычные слеши для работы в ОС Windows.
# - Используем with open() для безопасного открытия файла по найденному пути.
#   В случае ошибки (например, отсутствия прав) генерируется исключение, и выводится соответствующее сообщение.

if file_path:
    # # Преобразуем путь: заменяем бэкслеши (\) на слеши (/):
    # file_path = file_path.replace("\\", "/")
    print(f"\033[33mФайл найден, адрес:\033[m  {file_path}")
    # Открываю файл для чтения:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Содержимое файла:")
            # print(content)
    except Exception as e:
        print(f"Ошибка при открытии файла: {e}")
else:
    print(f"Файл \033[34m'{file_name}'\033[m \033[31mне найден\033[m.")



