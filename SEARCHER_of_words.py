# -----------------------------------------     Words SEARCHER     ----------------------------------------------------
# Поиск слова в файле: See https://ru.stackoverflow.com/questions/274131/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA-%D1%81%D0%BB%D0%BE%D0%B2%D0%B0-%D0%B2-%D1%84%D0%B0%D0%B9%D0%BB%D0%B5
# + https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-15-metody-raboty-s-faylami-i-faylovoy-sistemoy-2023-02-06

# ++++++++++++++++++++++++
import os
import re
# ++++++++++++++++++++++++

def find_word_in_files(word, directory):
    # Список файлов, содержащих указанное слово:
    found_files = []
    # Обходим все файлы и поддиректории:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):    # Проверяем, является ли файл Python-скриптом
                file_path = os.path.join(root, file)
                try:
                    # Открываем файл для чтения:
                    with open(file_path, 'r', encoding="utf-8") as f:
                        content = f.read()
                        # Проверяем наличие слова в содержимом файла:
                            # See "Python RegEx: ...  --> https://tproger.ru/translations/regular-expression-python
                            # re.match()
                            # re.search()
                            # re.findall()
                            # re.split()
                            # re.sub()
                            # re.compile())"
                        if re.search(rf"\b{word}*", content):       # \b - начало слова, * - любой символ после начала.
                            found_files.append(file_path)
                except Exception as e:
                    # Игнорируем ошибки (например, при открытии бинарных файлов):
                    print(f"Не удалось открыть файл: {file_path}. Ошибка: {e}")
    # Вывод результата:
    if found_files:
        print(f"Слово начинающееся с \033[33m'{word}'\033[m \033[32mнайдено\033[m в следующих файлах:")
        for found_file in found_files:
            print(f'{' ' * 5}', found_file)
    else:
        print(f"Слово начинающееся с \033[33m'{word}'\033[m \033[31mНЕ найдено\033[m ни в одном файле в папке {directory}.")

# Пример вызова функции.
    # Слово для поиска:
search_word = "Fibonacci"
    # Путь к одной директории проекта:
project_directory_H = r'Home_Tasks'
find_word_in_files(search_word, project_directory_H)
    # Путь к другой директории проекта:
project_directory_L = r'Lessons'
find_word_in_files(search_word, project_directory_L)
# -------------------------------------------------------------------------------------------------------------------
