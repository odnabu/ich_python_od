# Home Tasks 5, 02.12.24
# ___ Operators IF, ELIF, ELSE ___

# ___ Task 1 ___
# Три числа в порядке возрастания.
n1 = int(input("Enter the 1-st number: n1 = "))
n2 = int(input("Enter the 2-nd number: n2 = "))
n3 = int(input("Enter the 3-d number: n3 = "))
list_n = [n1, n2, n3]
mx = max(list_n)
mn = min(list_n)
if mn < n1 < mx:
    md = n1
elif mn < n2 < mx:
    md = n2
elif mn < n3 < mx:
    md = n3
print(f'\nNumbers in ascending order: {mx}, {md}, {mn}.')

# ___ Task 2 ___
# Високосный год.
year = int(input(f'\nEnter the year: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:    #  != - сравнение на НЕравенство.
    print(f'\nThe year {year} is a leap year (Gregorian calendar).')
else: print(f'\nThe year {year} is not a leap year (Gregorian calendar).')