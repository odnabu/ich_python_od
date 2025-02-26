# Home Work 18, 30.01.25
# ___ 34: Recursion. ___
# Normal  \033[0;__;__m \033[m    or   BOLD  \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
# ###################################################################################################################
# f = 40; f = '.' * f; print(f) - Filler up to.
# print(f, f'\n...')
# print(' ' * 5, f'...') - Indentation in the output of the result
# while True:
#   ...
#   ask = input("\nDo you want to continue? (y/n): ").lower()
#   if ask == 'n':
#       break
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
print('.' * 140)


# _____________________________________    Task 1    _____________________________________
# Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.
# Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
# Создайте функцию anagrams, которая принимает список слов в качестве аргумента и возвращает список анаграмм.
# Используйте множества и сортировку букв в слове для проверки на анаграмму. Выведите результат на экран.
#
# Пример переданного списка слов:
# ['cat', 'dog', 'tac', 'god', 'act']
# Пример вывода:
# Анаграммы: ['dog', 'god'], ['cat', 'tac', 'act']

# list_words = ['cat', 'dog', 'tac', 'god', 'act']
# print(list_words[0])


# word_1 = list_words[0]
# print(word_1, ''.join(sorted(word_1)), word_1[1:] + word_1[0])

# ---------------------------------------------------------- НЕ ПОДХОДИТ, тк НЕ все возможные комбинации.
# Цикл для всех возможных перестановок букв в одном слове:
# all_var = []
# for l in word_1:
#     repl = word_1.replace(l, '')
#     # print(repl)
#     a = l.join(repl)
#     # print(a)
#     all_var.append(a)
#
# print(all_var)

# Функция для всех возможных перестановок букв в одном слове:
# def all_var_comb(word):
#     all_var = []
#     for l in word:
#         repl = word.replace(l, '')
#         # print(repl)
#         a = l.join(repl)
#         # print(a)
#         all_var.append(a)
#     return all_var
# res = all_var_comb(word_1)
# print(res)

# all_l = set(list_words)
# b = set(res)
# # print(all_l, b)
# anagr_1 = b.intersection(all_l)
# print(anagr_1)
# ----------------------------------------------------------


# ---------------------------------------------------------- Copilot - НЕ ПОДХОДИТ, тк избыточно для решения ДЗ.
# # Программа всех возможных перестановок букв в слове:
# def all_permutations(word):
#     # Базовый случай: если длина слова равна 1, возвращаем слово
#     if len(word) <= 1:
#         return [word]
#     # Результирующий список для хранения перестановок
#     perms = []
#     # Перебираем каждую букву в слове
#     for i, char in enumerate(word):
#         # Получаем оставшиеся буквы после удаления текущей
#         # print(word[:i], word[i + 1:])
#         remaining = word[:i] + word[i + 1:]
#         # Рекурсивно получаем все перестановки оставшихся букв
#         for perm in all_permutations(remaining):
#             perms.append(char + perm)
#     # Удаление дубликатов путем преобразования в множество и обратно в список:
#     unique_perms = list(set(perms))
#     return unique_perms
# # Пример использования функции
# word = "cat"
# perms = all_permutations(word)
# # # Выводим результат:
# # print("Все возможные перестановки букв в слове: ", perms)
# ----------------------------------------------------------



# ---------------------------------------------------------- Copilot - Code with loop WHILE
# def anagrams(words):
#     anagram_groups = []
#     while words:
#         w = words.pop(0)
#         group = [w]
#         sorted_word = ''.join(sorted(w))
#         for other_word in words[:]:
#             if ''.join(sorted(other_word)) == sorted_word:
#                 group.append(other_word)
#                 words.remove(other_word)
#         if len(group) > 1:
#             anagram_groups.append(group)
#     return anagram_groups
# # Пример использования функции:
# words = ['cat', 'dog', 'tac', 'god', 'act']
# # print(words.pop(0))
# anagram_groups = anagrams(words)
# # Выводим результат
# print("Анаграммы:", anagram_groups)
# ----------------------------------------------------------


# ---------------------------------------------------------- Copilot + I - ALL Code with loop FOR
# def anagrams(words):
#     align_res = 70
#     anagram_groups = []
#     for w in words:
#         print(f'\n\033[31m{'*'*140}\033[m\n',
#               f'\n-1.1- Возьмем 1-е (или следующее) слово из списка: '.ljust(align_res, ' '), f'\033[31m    -->  w = {w}\033[m')
#         group = []
#         print(f'\t-1.2- Новый список, куда будут складывается слова одной группы:'.ljust(align_res, ' '), 'group --> ', group)
#         sorted_word = ''.join(sorted(w))
#         print(f'\t-1.3- Отсортируем взятое в 1.1 слово w = "\033[31m{w}\033[m":'.ljust(align_res+8, ' '), 'sorted_word --> ', sorted_word)
#         for other_word in words[:]:
#             print(f'\t(2.1) Теперь берем каждое слово из списка (начиная с 1-го):'.ljust(align_res, ' '), 'other_word -->', other_word)
#             other_word_sorted = ''.join(sorted(other_word))
#             print(f'\t(2.2) ... и отсортируем в нем буквы:'.ljust(align_res, ' '), 'other_word_sorted -->',  other_word_sorted)
#             if other_word_sorted == sorted_word:
#                 group.append(other_word)
#                 print(f'\t\t[3] Если отсортированное слово совпадает с 1-ым сортированным \n',
#                       f'\t\t\tто \033[33m кладем\033[m его в группу: '.ljust(align_res+1, ' '),
#                       f'\033[33m group.append(other_word) --> {group}\033[m')
#                 words.remove(other_word)
#                 print(f'\t\t--4 Далее проверенное слово "\033[31m{other_word}\033[m" удаляем из списка,\n',
#                       f'\t\t\tчтобы следующее сделать первым:'.ljust(align_res-7, ' '), f'\033[37m remove(other_word) --> {words}\033[m')
#             new_group = list(set(group))
#             print(f'\t\t/5.1/ С помощью set() удалим дубликаты из получившегося списка\n',
#                   f'\t\t/5.2/ и \033[36m проверим\033[m содержимое группы после пп. 1.1-4:'.ljust(align_res+4, ' '), f'\033[36m new_group --> {new_group}\033[m')
#         if len(new_group) > 1:
#             # print(f'\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
#             anagram_groups.append(new_group)
#     return anagram_groups
#
# words = ['cat', 'cta', 'dog', 'tac', 'god', 'act', 'cta', 'cta', 'xyz', 'zxy', 'yzx']
# anagram_groups = anagrams(words)
# print(f'\nАнаграммы: ', anagram_groups)
# ----------------------------------------------------------


# _________________ CLEAR Code with loop FOR for LMS-platform _________________
# ИДЕЯ:
#   1) взять 1-ое слово из списка list_words и получить его отсортированный в алфавитном порядке вариант.                |->  ''.join(sorted(w)).
#      Дальше проверять все слова списка (начиная с самого 1-ого слова) -->
#   2) взять следующее (2-е) слово из списка, получить его отсортированный вариант и ...                                 |->   other_word
#      ... сравнить его с отсортированным вариантом первого слова.                                                       |->   ''.join(sorted(other_word)) == sorted_word
#   3) если совпадают отсортированные варианты, то положить 2-ое слово в группу к первому слову,                         |->   group.append(other_word)
#      Потом следующее, следующее и т.д. до конца списка.
#   4) затем удалить 1-ое проверенное слово из оригинального списка, чтобы таким образом уменьшить список и
#      перейти к следующему за 1-ым словом.
#   5) т.к. перебраны и проверены все слова с одинаковым набором букв, то в списке после удаления остались только те,
#      буквы из которых на встречаются одновременно в одном слове.
#   6) снова создается группа, которая начинается с другого слова и производится поиск по пп. 1)-4).
#   7) все группы, где больше 1 слова, формируются в список анаграмм.

# def anagrams(words):
#     anagram_groups = []
#     for w in words:
#         group = []
#         sorted_word = ''.join(sorted(w))
#         for other_word in words[:]:
#             other_word_sorted = ''.join(sorted(other_word))
#             if other_word_sorted == sorted_word:
#                 group.append(other_word)
#                 words.remove(other_word)
#             group = list(set(group))
#         if len(group) > 1:
#             anagram_groups.append(group)
#     return anagram_groups
#
# words = ['cat', 'cta', 'dog', 'tac', 'god', 'act', 'cta', 'cta', 'xyz', 'zxy', 'yzx']
# anagram_groups = anagrams(words)
# print(f'\nАнаграммы: ', anagram_groups)
# ----------------------------------------------------------

# words = ['cat', 'cta', 'dog', 'tac', 'god', 'act', 'cta', 'cta', 'xyz', 'zxy', 'yzx']
# print(len(words), words[0:1])
# w_0 = words[0]; w_1 = words[1]; w_2 = words[2]; w_10 = words[10]
# print('-' * 40)

# --------------------------- для двух первых слов
# group = [w_0]
# new_w = []
# for l in w_0:
#     if l in w_1:
#         new_w.append(l)
#         ''.join(new_w)
# print(''.join(new_w))
# if ''.join(new_w) == w_0:
#     group.append(w_1)
#     print(group)
# else:
#     f'No matches found.'
# ---------------------------

# group = []
# i = 1
# new_w = []
# while i <= len(words) - 1:
#     for l in words[i-1]:                # Берем буквы из 1-го слова и...
#         if l in words[i]:               # проверяем их наличие во 2-м.
#             new_w.append(l)             # Если есть совпадение, составляем снова 1-е слово.
#     if ''.join(new_w) == words[i-1]:
#         group.append(words[i])
#     i += 1
# print(group)



# _____________________________________    Task 2    _____________________________________
# Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет, является ли set1
# подмножеством set2. Функция должна возвращать True, если все элементы из set1 содержатся в set2, и
# False в противном случае. Функция должна быть реализована без использования встроенных методов issubset или <=.
# # Пример множеств
# # {1, 2, 3}
# # {1, 2, 3, 4, 5}
# # Пример вывода:
# # True
#
# def is_subset(set1, set2):
#     if set1.issubset(set2) is True:
#         return True
#     else:
#         return False
#
# s1 = {1, 2, 3}
# s2 = {1, 2, 3, 4, 5}
# print(is_subset(s1, s2))

