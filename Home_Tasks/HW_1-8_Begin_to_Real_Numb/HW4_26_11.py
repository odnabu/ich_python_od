# Home Tasks 4, 26.11.24
# ___ Logical Operations ___

# ___ Task 1 ___ Даны формулы:
#   ¬((A ∨ B) ∧ (C ∨ D))      (Eq.A) и
#    ((¬A ∧ ¬B) ∨ (¬C ∧ ¬D))  (Eq.B).
# Используя закон Де Моргана, докажите, что эти формулы эквивалентны.
# Закон де Моргана:
#   ¬(A ∧ B) = ¬A ∨ ¬B  (Eq.1)
# not (A and B) == not A or not B
#  ¬(A ∨ B) = ¬A ∧ ¬B (Eq.2)
# not (A or B) == not A and not B

# __ Доказательство __
# Подставим (Eq.1) в (Eq.A), получим:
#   ¬((A ∨ B) ∧ (C ∨ D)) = [-(A ∨ B) ∨ -(C ∨ D)].
# Теперь в полученный результат подставим (Eq.2):
#   [-(A ∨ B) ∨ -(C ∨ D)] = [(-A ∧ -B) ∨ (-C ∧ -D)] |=>
#   [(-A ∧ -B) ∨ (-C ∧ -D)] = ((¬A ∧ ¬B) ∨ (¬C ∧ ¬D)) Q.E.D. (quod erat demonstrandum)


# Далее проверим утверждение на примере.
# Будем исходить из утверждения, что формулы эквивалентны.
# Тогда обе формулы должны выполняться для любых булевых A, B, C, D.
# Положим для начала следующие значения для булевых величин:
print(f'\n___ Task 1 ___')
import random
a = random.choice([True, False])
b = random.choice([True, False])
c = random.choice([True, False])
d = random.choice([True, False])
print(f'\nСлучайным образом зададим булевые значения для:\n  a = {a}, b = {b}, c = {c}, d = {d}')

# Далее проверим для первой формулы (Eq.A):
# 1)  (A ∨ B) == (A or B):
condition_1_1 = a | b
print(f'\nДалее пошагово выполним проверку для первой формулы ¬((A ∨ B) ∧ (C ∨ D)):'
      f'\n1)  (A ∨ B) is {condition_1_1}. Type is "{bool(condition_1_1)}"') # Result is 15 (TRUE)
# 2)  (C ∨ D) == (C or D):
condition_1_2 = c | d
print(f'2)  (C ∨ D) is {condition_1_2}. Type is "{bool(condition_1_2)}"') # Result is 7 (TRUE)
# 3)  (A ∨ B) ∧ (C ∨ D) == (A or B) and (C or D):
condition_1_3 = condition_1_1 & condition_1_2
print(f'3)  (A ∨ B) ∧ (C ∨ D) is {condition_1_3}. Type is "{bool(condition_1_3)}"') # Result is 7 (TRUE)
# 4)  ¬(A ∨ B) ∧ (C ∨ D) == not (A or B) and (C or D):
condition_1_4 = not condition_1_3
print(f'4)  ¬(A ∨ B) ∧ (C ∨ D) is {condition_1_4}. Type is "{bool(condition_1_4)}"') # Result is 7 (TRUE)

# Теперь проверим для второй формулы (Eq.B):
# 1)  (-A ∧ -B) == (-A and -B):
condition_2_1 = (not a) & (not b)
print(f'\nТеперь выполним проверку для 2-ой формулы (¬A ∧ ¬B) ∨ (¬C ∧ ¬D):'
      f'\n1)  (-A ∧ -B) is {condition_2_1}. Type is "{bool(condition_2_1)}"') # Result is 15 (TRUE)
# 2)  (-C ∧ -D) == (-C and -D):
condition_2_2 = (not c) & (not d)
print(f'2)  (-C ∧ -D) is {condition_2_2}. Type is "{bool(condition_2_2)}"') # Result is 7 (TRUE)
# 3)  (-A ∧ -B) ∨ (-C ∧ -D) == (-A and -B) or (-C and -D):
condition_2_3 = condition_2_1 | condition_2_2
print(f'3)  (-A ∧ -B) ∨ (-C ∧ -D) is {condition_2_3}. Type is "{bool(condition_2_3)}"') # Result is 7 (TRUE)

print(f'\n{condition_1_4} == {condition_2_3}. \nКак видно, равенство всегда выполняется.'
      f'\nQ.E.D.\n')

# ___ Task 2 ___
# Напишите программу, которая запрашивает у пользователя два логических значения (True или False)
# и выводит результаты следующих логических операций:
# 1) Логическое И (and) между двумя значениями.
# 2) Логическое ИЛИ (or) между двумя значениями.
# 3) Логическое НЕ (not) для каждого значения.
# 4) Результат сравнения двух значений на равенство.
# 5) Результат сравнения двух значений на неравенство.

print(f'___ Task 2 ___\n')
# ОШИБКА !!!!
log_val_1 = bool(input('Enter the first logical value (True or False): '))
log_val_2 = bool(input('Enter the second logical value (True or False): '))
print(f'\nResult of logical AND: {log_val_1 & log_val_2}.')
print(f'Result of logical OR: {log_val_1 | log_val_2}.')
print(f'Result of logical NOT for 1-st: {not log_val_1}.')
print(f'Result of logical NOT for 2-st: {not log_val_2}.')
print(f'The result of comparing two values for equality: {log_val_1 == log_val_2}.')
print(f'The result of comparing two values for inequality: {log_val_1 != log_val_2}.')
