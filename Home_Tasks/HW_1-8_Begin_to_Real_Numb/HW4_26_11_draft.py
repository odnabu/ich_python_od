# Home Tasks 4, 26.11.24
# ___ Logical Operations ___

# ___ Task 1 ___ Даны формулы: ¬((A ∨ B) ∧ (C ∨ D)) и ((¬A ∧ ¬B) ∨ (¬C ∧ ¬D)).
# Используя закон Де Моргана, докажите, что эти формулы эквивалентны.
# Закон де Моргана:
#   ¬ (A  ∧  B) =   ¬ A  ∨  ¬ B
# not (A and B) == not A or not B
#  ¬ (A  ∨  B)  =   ¬ A  ∧  ¬ B
# not (A or B) == not A and not B


# __ Формула 1 __
#  ¬   ( (A ∨  B)  ∧  (C ∨  D) )
#  not [ (A or B) and (C or D) ]
# Возможные варианты булевых значений для реализации FALSE:
#  not [  (true)  and  (true)  ] = FALSE
# Что эквивалентно записи:
#  [ not(true)  and  not(true) ] = false
# Или же:
#  [ false  and  false ] = false  (Eq.1)

# Возможные варианты булевых значений для реализации TRUE:
#  not [  (false)  and  (false)  ] = TRUE
#  not [  (true)   and  (false)  ] = TRUE
#  not [  (false)  and   (true)  ] = TRUE

# __ Формула 2 __
#  (  ¬ A  ∧  ¬ B)  ∨  (  ¬ C  ∧   ¬ D)
#  (not A  & not B) or (not C  & not D)
# Возможные варианты булевых значений для реализации FALSE:
#  (false)  or  (false) = FALSE  (Eq.2)

# Возможные варианты булевых значений для реализации TRUE:
#  (true)  or  (true) = TRUE
#  (true)  or  (false) = TRUE
#  (false)  or  (true) = TRUE

# __ Итог для второго уровня __
# Таким образом: false = false ==> (Eq.1) = (Eq.2)
# [ false  and  false ] = (false)  or  (false)
# Или же:
# not [(true)  and  (true)] = ((false)  or  (false))
# ¬[true ∧ true] = (false ∨ false)  (Eq.3)
# Что так же можно проследить по таблицам истинности для AND и OR.

# Далее проанализируем нижний уровень исходя из (Eq.3).
# __ Формула 1 __
# в левой части равенства (Eq.3) (A or B) = true, когда:
# 1) хотя бы 1 из 2-х элементов равен true, или 2) - сразу оба равны true.
# Их одновременная инверсия в случае 1) не меняет результата:
#  (not(true) or not(false)) = true, тогда как во 2) случае
# значение поменяется на противоположное - false. Однако, верхняя операция
#  false = [false and false] = {(not(true) or not(true)) and (not(true) or not(true))}.



# Далее проверим утверждение.
# Будем исходить из утверждения, что формулы эквивалентны.
# Тогда обе формулы должны выполняться для любых булевых A, B, C, D.
# Положим случайным образом следующие значения для булевых величин:
a = True
b = True
c = True
d = True

# Далее проверим

# -1-  (A ∨ B) == (A or B):
condition_1 = a | b
print(f'-1-  (A ∨ B) is {condition_1}. Type is "{bool(condition_1)}"') # Result is 15 (TRUE)
# -2-  (C ∨ D) == (C or D):
condition_2 = c | d
print(f'-2-  (C ∨ D) is {condition_2}. Type is "{bool(condition_2)}"') # Result is 7 (TRUE)
# -3-  (A ∨ B) ∧ (C ∨ D) == (A or B) and (C or D):
condition_3 = condition_1 & condition_2
print(f'-3-  (A ∨ B) ∧ (C ∨ D) is {condition_3}. Type is "{bool(condition_3)}"') # Result is 7 (TRUE)
# -4-  ¬(A ∨ B) ∧ (C ∨ D) == not (A or B) and (C or D):
condition_4 = not condition_3
print(f'-3-  ¬(A ∨ B) ∧ (C ∨ D) is {condition_4}. Type is "{bool(condition_4)}"') # Result is 7 (TRUE)




# a = 10 # 1010 in binary; b = 5 # 0101 in binary
# c = 7 # 0b111 in binary; d = 3 # 0b11 in binary

# В свою очередь not(true) = false, т.е. not(A or B) = false может быть
# только в 3-х случаях: