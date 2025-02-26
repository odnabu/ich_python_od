# Semenov Artem

# ___ Review of previously covered material ___
a = 3.2
b = 18.9
c = 3
# print(a + b)
# print(a - b)
print(a / b)
# print(a // b)
# print(a % b) # % - Остаток от деления. Выводится не дробная часть, а часть от целого.
# print(a * b)
# print(a ** b)
# print(a ** (1/c))
# print(pow(a, (1/c))) # pow = ^ or **
# print(pow(a, c))
# print(abs(-123)) # Absolut (a + abs(a))/2
# print(round(-2.48978, 3))
# m = (a, b, c, -25, -0.1e-3, 1.25)
# print(max(m)) # (a+b)/2 + abs(a-)/2
# print(min(m))
# print(sum(m)) # sum(list or set, opt)
# print(sum((a, b, c, -25, -0.1e-3, 1.25))) # sum((a, b, c, d, ...)), opt)

# ___ Logic ___
# x = 10 # 1010 in binary
# y = 5 # 0101 in binary
# print(x & y) # Побитовое И
# print(x | y) # Побитовое ИЛИ - OR
# print(x ^ y) # Побитовое XOR
# print(x << 1) # Сдвиг влево
# print(x >> 1) # Сдвиг вправо
# a = 5
# b = 20
# print(a << 2) # Сдвиг влево (5 * 2^2) = 20
# print(b >> 2) # Сдвиг вправо (20 // 2^2) = 5
# c = 12
# d = 10
# print(b & 2)

# ___ New Thema: Logical data & comparisons ___
# print(4 > 2)
# print(4 < 2)
# a = 5
# b = 7.8
# print(a > b)
# print(a <= b)
# rez = a < b
# print(rez)
# print(type(rez)) # Bool: True, False
# rez = False
# print(rez)
# print(type(rez))

# ___ Операции сравнения: >, <, <=, >=,
# == - сравнение на равенство
# != - сравнение на НЕравенство
# print(5 == 7 - 2)
# print(8 >= 8)
# # print(6 = 6) # Error, here should be ==
# print(6 == 6)
# print(2 != 4)
# print(2 != 2)

# ___ Деление на 2, 3,... ___
# print(8 % 2 == 0)
# print(7 % 2 == 0)
# print(9 % 3 == 0)
# print(10 % 3 == 0)

# ___ NOT - Инверсия (логич. НЕ),
#     AND - Конъюнкция (логическое И),
#     OR - Дизъюнкция (Логич. ИЛИ) ___
# y = 1.85
# x = 2
# Попадает ли это число в диапазон от -2 до 5:
# print(y >= -2 and y <= 5) # Попадает в диапазон - AND
# print(x >= -2 and x <= 5) # True if both is true
# print(x > -2 and x < 5)
# print(x >= 2 and x < 5)
# print(y < -2 or y < 5) # y - НЕ попадает в диапазон OR. True when one of both is true.
# print(-2 <= y <= 5) # Analog __ AND ___

# Проверка на кратность какому-либо числу
# x = 9
# print(x % 2 == 0 or x % 3 ==0)
# print(x % 2 == 0 and x % 3 ==0)

# ___ Inverting of conditions: NOT ___
# x = 9
# print(x % 2 == 0 or x % 3 ==0)
# print(not(x % 2 == 0 or x % 3 ==0)) # Инвертация условия сравнения
# print(not x % 2 == 0 or x % 3 ==0) # Инвертация условия сравнения БЕЗ СКОБОК.
# __ NB! __ У оператора NOT самый высокий приоритет (1).
#           AND - средний приоритет (2). O
#           R - самый низкий приоритет (3).

# ___ BOOL ___
# print(bool(1)) # Преобразует аргумент в логический тип TRUE or FALSE
# print(bool(-10))
# print(bool(2.5))
# print(bool('Hello'))
# print(bool(0)) # Always FALSE
# print(bool('')) # Always FALSE
# print(bool(" ")) # Here is a space, so that's TRUE.
# print(bool([])) # Always FALSE
# print(bool([1, 2, 3]))  # Here is not empty, so that's TRUE.
# print # Зарезервированное слово, поэтому НЕТ реакции.
# print(5 + 7) # Выполнение функции.

# ___ Импликация --> . Эквивалентность <--> (оба истинны или оба ложны) ___





