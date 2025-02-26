## Лекция 22 - Lambda-функции. Функции высшего порядка

- [Передача функций в качестве аргументов](#Передача-функций-в-качестве-аргументов)
- [Lambda-функции](#Lambda-функции)
- [Функция как ключ в sorted, min, max](#Функция-как-ключ-в-sorted-min-max)


## Передача функций в качестве аргументов

Функции в Python являются объектами, которые можно присваивать переменным, хранить в коллекциях 
и передавать в другие функции. 

При передаче функции в качестве аргумента передаётся **сама ссылка на функцию, а не её результат**.  
Это означает, что функция не выполняется сразу, а только передаётся в другую функцию, где её можно вызвать.

#### **Как это работает?**
Когда функция передаётся в качестве аргумента:
- **Не нужно указывать `()`** при передаче, иначе передастся результат её выполнения.
- Функция может быть вызвана внутри другой функции по переданной ссылке с помощью **`()`**.


#### **Пример 1: Передача функции без вызова**
```python
def square(x):
    return x * x

def cube(x):
    return x * x * x

def apply_function(func, value):
    return func(value)  # Вызываем переданную функцию внутри другой функции

result_square = apply_function(square, 5)   # Передаём функцию square без вызова (без скобок)
result_cube = apply_function(cube, 5)       # Передаём функцию cube без вызова (без скобок)
print(result_square)
print(result_cube)
```

#### **Пример 2: Ошибка при передаче вызванной функции**
```python
def square(x):
    return x * x

def apply_function(func, value):
    return func(value)

# Передается результат вызова функции, а не ссылка на функцию:
result = apply_function(square(5), 5)       # Ошибка!
```

#### **Пример 3: Передача встроенной функции**

```python
def process_data(func, data):
    return func(data)

# Можно передавать не только пользовательские функции, но и встроенные
result = process_data(abs, -10)
print(result)
```


## Lambda-функции

#### Синтаксис:
```python
lambda arguments: expression
```
- **`lambda`** — ключевое слово для создания анонимной функции.
- **`arguments`** — параметры, которые принимает функция.
- **`expression`** — выражение, результат которого возвращается (без `return`).

#### Примеры:

__Lambda-функцию можно присвоить переменной, что на практике не используется.__

1. **Lambda с одним аргументом**
```python
# Функция принимает число x и возвращает его квадрат
square = lambda x: x ** 2
print(square(4))
print(square(5))

# Аналог с def
def square(x):
    return x ** 2
print(square(4))
print(square(5))
```

2. **Lambda с несколькими аргументами**
```python
# Функция принимает два аргумента и возвращает их сумму
add = lambda x, y: x + y
print(add(3, 5))
print(add(8, 9))

# Аналог с def
def add(x, y):
    return x + y
print(add(3, 5))
print(add(8, 9))
```

3. **Lambda как аргументы других функций**: 
`lambda`-функции можно передавать как **аргументы** в другие функции, не создавая отдельные именованные функции.  

```python
def apply_func(func, numbers):
    return [func(num) for num in numbers]

result = apply_func(lambda x: x + 10, [5, 8, 3])
print(result)
```

### **Особенности lambda-функций**
- Lambda-функция всегда **возвращает** результат выражения.
- Lambda может содержать только **одно выражение**.
- Нет многострочных блоков кода (`if`, `for` и т. д.).


## Функция как ключ в sorted, min, max

В Python функции **`sorted()`**, **`min()`** и **`max()`** принимают необязательный параметр **`key`**, который определяет, 
по какому критерию выполнять сортировку или поиск минимального/максимального значения.

__В параметр key можно передавать не только встроенные функции (например, len, abs), но и пользовательские функции, созданные с помощью def или lambda.__


### Параметр key в sorted()

#### Синтаксис:
```python
sorted(iterable, key=function, reverse=False)
```

#### Пример: Встроенная функция
```python
words = ['mango', 'grape', 'apple', 'strawberry', 'banana', 'pineapple', 'kiwi', 'blueberry']
# Сортировка по длине слов
result = sorted(words, key=len)
print(result)
```

#### Пример: Пользовательская функция
```python
def last_char_len(s):
    return s[-1], len

words = ['mango', 'grape', 'apple', 'strawberry', 'banana', 'pineapple', 'kiwi', 'blueberry']
# Сортировка по последнему символу и длине (последовательно)
result = sorted(words, key=last_char_len)
print(result)
```

#### Пример: Анонимная функция lambda 
```python
words = ['mango', 'grape', 'apple', 'Strawberry', 'Banana', 'pineapple', 'kiwi', 'blueberry']
# Сортировка по первому символу (игнорируя регистр) и по последнему символу
result = sorted(words, key=lambda x: (x[0].lower(), x[-1]))
print(result)
```

#### Пример: Сортировка списка кортежей
```python
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
# Сортировка списка кортежей по второму элементу
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
```


### Параметр key в min max()

#### Синтаксис:
```python
min(iterable, key=function)
max(iterable, key=function)
```

#### Пример: Поиск самого длинного слова
```python
words = ["apple", "banana", "kiwi", "grapefruit"]
longest_word = max(words, key=len)
print(longest_word)
```

#### Пример: Поиск города с минимальным населением
```python
cities = [('New York', 8419600), ('Los Angeles', 3980400), ('Chicago', 2716000)]
smallest_city = min(cities, key=lambda x: x[1])
print(smallest_city)
```
