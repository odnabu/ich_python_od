# Semenov Artem
# 19.12.24
# Python 18: STRINGS --> Methods of working with Collections

# ______ Review of previously covered material ______

# __ Task 1 __
# Для данной строки, напечатать строку, где каждый символ повторяется дважды, например,
# 'The' → 'TThhee', 'AAbb' → 'AAAAbbbb'.
# text = input("Enter a text rom: ")
# double_text = ''
# i = 0
# while i < len(text):
#     double_text += text[i] * 2
#     i += 1
#     print(f'Each depleted symbol: {i} - {double_text}.')
# print(f'All depleted text: {double_text}.')


# __________________ Methods of working with Stings __________________

# NB! __ СТРОКИ - НЕИЗМЕНЯЕМЫЙ тип данных __

# __ 1 - .upper(), .lower() __
# s = 'python'
# # print(type(s))
# # print(type(s.))     # . - чтобы увидеть команды работы со строками.
# print(s.upper())      # CAPS letters
# s1 = s.upper()
# print(f's = {s}')
# print(f's1 = {s1}')
# s2 = s1.lower()
# print(f's2 = {s2}')
# print(f's2.upper() = {s2.upper()}')

# __ 2 - .count(__) __
txt = 'The black cat sat on the mat.'
# print(txt.count('he'))
# print(txt.count('a'))
# print(txt.count('at'))
# print(txt.count('at', 2))            # Поиск со 2-го символа.
# print(txt.count('at', 2, 8))         # Поиск со 2-го до 8-го символа.

# __ 3 - .find(),  __ + НУМЕРАЦИЯ СИМВОЛОВ в ОДНОЙ строке.
# ____________________________________________
# i = 0
# text_in_row = ''
# while i < len(txt):
#     text_in_row = str(i) + ' - ' + str(txt[i])
#     # print(f'{i} - {txt[i]}'))
#     print(f'{text_in_row}   ', end='')
#     i += 1
# print(text_in_row, sep=' | ')
# _____________________________________________
# print(txt.find('at'))                # Ищет L слева - направо.
# print(txt.rfind('at', 1, 6))         # Ищет R справа - налево.
# print(txt.index('at'))

# __ 4 - .replace(),  __
# txt_2 = "Hello World"
# print(txt_2)
# print(txt_2.replace('o', 'a'))
# print(txt_2.replace('o', 'abc'))

# __ 5 - .isalpha(), .isdigit(), .isspace() __
# txt_2 = "Hello World"
# txt_let = "HelloWorld"
# txt_numb = "123456"
# print(txt_2, txt_let, txt_numb)
# print(txt_2.isalpha(), txt_2.isdigit(), txt_2.isspace())
# print(txt_let.isdigit(), txt_let.isdigit(), txt_let.isspace())
# print(txt_numb.isdigit(), txt_numb.isdigit(), txt_numb.isspace())

# __ 6 - .startswith(), .endswith() __
# print(txt_2.startswith("Hel"))
# print(txt_2.endswith("d"))

# __ 7 - .rjust(), .ljust() __ Заполнение до какого-то кол-ва символов.
# d = 'ABC'
# print(d.rjust(5, '*'))
# print(d.rjust(15, '*'))
# print(d.rjust(3, '*'))
# print(d.ljust(5, '*'))

# ___ For PART TITLE ___
# thema = 'ABC'
# left_fill = thema.rjust(10, '_')
# # print(left_fill)
# right_fill = left_fill.ljust(50, '_')
# print(right_fill)

# __ 8 - .split() - Возвращает коллекцию строк, т.е. тип Список
# mm = 'Max Muster Mustermann'.split()
# print(mm)
# mm2 = 'MaxMusterMustermann'.split()
# print(mm2)
# mm3 = 'Max,Muster,Mustermann'.split(',')
# print(mm3)
# mm4 = 'Max,Muster,Mustermann'.split('M')
# print(mm4)

# __ Task 9 - .replace().split()
# digits = '1, 2, 3, 4, 5, 6, 7, 8, 9'.replace(' ', '*').split(',')   # По умолчанию разделитель - ПРОБЕЛ.
# print(digits)
# print('Hello World'.split())
# print(', '.join(digits))
# print(''.join(digits))

# h = 'hello world'
# print(set(h))
# print(list(h))

# __ 9 - .strip(), .rstrip(), .lstrip().        # Удаляет пробелы.
# s1 = '      hello world         .              '.strip()
# s2 = '      hello world         .'.lstrip()
# s3 = '      hello world         .      '.rstrip()
# print(f' {s1},\n {s2},\n {s3}.')