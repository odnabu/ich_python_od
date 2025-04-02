# Инкапсуляция

Инкапсуляция в объектно-ориентированном программировании (ООП) означает упаковку данных (полей) и методов, работающих 
с ними, внутри одного объекта и предоставление контроля над доступом к этим данным.
В Python существует три основных типа доступа к членам класса:

## 1. Публичный доступ (public):

Публичные члены класса (атрибуты и методы) доступны извне класса. К ним можно обращаться напрямую без ограничений.

Пример:
```python
class MyClass:
    def __init__(self, name):
        self.name = name  # Публичный атрибут

    def public_method(self):
        return f"Hello, {self.name}!"  # Публичный метод

obj = MyClass("John")
print(obj.name)
print(obj.public_method())
```

## 2. Защищенный доступ (protected):

\Защищенный доступ (члены класса, начинающиеся с одного подчеркивания) в Python используется для того, чтобы 
обозначить, что эти члены не предназначены для использования извне класса, но к ним можно обращаться напрямую.

Пример:
```python
class MyClass:
    def __init__(self, protected_name, name):
        self._protected_variable = protected_name  # Защищенный атрибут
        self.name = name  # Публичный атрибут

    def _protected_method(self):
        return f"Hello, {self._protected_variable}!"  # Защищенный метод

obj = MyClass("Alice")
print(obj._protected_variable)
print(obj._protected_method())
```

Часто защищенные атрибуты и методы используются для внутренних реализаций класса. Это могут быть вспомогательные 
методы или переменные, которые не являются частью общего интерфейса класса.
```python
class Car:
    def __init__(self, make, model):
        self._make = make  # Защищенный атрибут
        self._model = model  # Защищенный атрибут

    def _start_engine(self):
        print(f"Engine of {self._make} {self._model} started")

    def drive(self):
        self._start_engine()
        print(f"{self._make} {self._model} is driving")

my_car = Car("Toyota", "Camry")
my_car.drive()
```


## 3. Приватный доступ:

Приватные члены класса в Python (члены, начинающиеся с двух подчеркиваний) предназначены для ограничения доступа к 
ним извне класса. Однако, следует отметить, что в Python приватность не является строгим ограничителем доступа, а 
скорее предостережением.
```python
class MyClass:
    def __init__(self, name):
        self.__private_variable = name  # Приватный атрибут

    def __private_method(self):
        return f"Hello, {self.__private_variable}!"  # Приватный метод

obj = MyClass("Bob")
# print(obj.__private_variable)      # Это вызовет ошибку
# print(obj.__private_method())       # Это вызовет ошибку
```

Обратите внимание, что в Python существует соглашение об именовании, которое регламентирует, какие члены следует считать публичными, защищенными и приватными. Однако, это всего лишь соглашение, и сам Python не делает строгого разделения на уровни доступа.

На самом деле сокрытие в Python не настоящее и доступ к атрибуту мы получить все же можем. Но для этого надо написать `Класс_или_объект._Класс__атрибут/метод`:
```python
class MyClass:
    def __init__(self, name):
        self.__private_variable = name  # Приватный атрибут

    def __private_method(self):
        return f"Hello, {self.__private_variable}!"  # Приватный метод

obj = MyClass("Bob")
print(obj._MyClass__private_variable)
print(obj._MyClass__private_method())
```

## Создание методов-геттеров и методов-сеттеров

Можно создать методы-геттеры и методы-сеттеры для доступа к приватным атрибутам. Эти методы позволяют читать и изменять значения атрибутов, предоставляя контроль над доступом.

```python
class MyClass:
    def __init__(self):
        self.__private_variable = 42  # Приватный атрибут

    def get_private_variable(self):
        return self.__private_variable

    def set_private_variable(self, value):
        self.__private_variable = value

obj = MyClass()
print(obj.get_private_variable())
obj.set_private_variable(100)
print(obj.get_private_variable())
```


---

## Декоратор `property`

В Python, property - это встроенная функция, которая позволяет создавать управляемые атрибуты (managed attributes) 
в классах. Управляемые атрибуты в классе позволяют использовать методы getter, setter и deleter для работы с атрибутом, 
при этом использование их выглядит как обращение к обычному атрибуту.

Основные компоненты property:
1. Getter:
  Это метод, который возвращает значение управляемого атрибута.
2. Setter:
  Это метод, который устанавливает значение управляемого атрибута.
3. Deleter:
  Это метод, который удаляет управляемый атрибут.

Пример использования property:

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._pi = 3.14

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Width must be greater than zero")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("Height must be greater than zero")

    @property
    def area(self):
        return self._width * self._height

    @property
    def pi(self):
        return self._pi

    @pi.deleter
    def pi(self):
        del self._pi

# Создаем объект класса Rectangle
rectangle = Rectangle(width=10, height=5)

# Используем управляемые атрибуты
print(rectangle.width)
print(rectangle.height)
print(rectangle.area)

# Используем setter для изменения значений
rectangle.width = 12
rectangle.height = 6

print("\nUpdated: ")
print(rectangle.width)
print(rectangle.height)
print(rectangle.area)

print("\nDeleter: ")

print(rectangle.pi)
del rectangle.pi
# print(rectangle.pi)  # этот код вызовет ошибку, т.к. атрибут больше не существует
```



Пример зачем использовать property:
1. Создаем класс пользователя с публичными атрибутами login, password и воспользуемся его атрибутами:
```python
class User:
    def __init__(self, login, password):
        self.login = login  # Публичный атрибут
        self.password = password  # Публичный атрибут


# Создаем объект класса User
user = User(login="John", password="Secure password")

# Используем публичный атрибут
print("Login:", user.login)
print("Password:", user.password)

# Меняем публичный атрибут
user.login = "New login"
user.password = "New password"

# Используем публичный атрибут
print("Login:", user.login)
print("Password:", user.password)
```


2. Далее мы понимаем что сделать атрибуты публичными было ошибкой и делаем их приватными. Но при этом возникает проблема что перестает работать весь код, который где эти атрибуты использовались:

```python
class User:
    def __init__(self, login, password):
        self.__login = login  # Приватный атрибут
        self.__password = password  # Приватный атрибут


# Создаем объект класса User
user = User(login="John", password="Secure password")

# # Используем публичный атрибут
# print("Login:", user.login)
# print("Password:", user.password)

# # Меняем публичный атрибут
# user.login = "New login"
# user.password = "New password"

# # Используем публичный атрибут
# print("Login:", user.login)
# print("Password:", user.password)
```


 3. Добавляем методы геттеров и сеттеров для доступа к атрибутам. Но предыдущий код с использованием атрибутов всё ещё не работает в том не виде, его нужно менять:

```python
class User:
    def __init__(self, login, password):
        self.__login = login  # Приватный атрибут
        self.__password = password  # Приватный атрибут

    def get_login(self):
        return self.__login

    def set_login(self, new_login):
        self.__login = new_login

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

# Создаем объект класса User
user = User(login="John", password="Secure password")

# # Используем публичный атрибут
# print("Login:", user.login)
# print("Password:", user.password)

# # Меняем публичный атрибут
# user.login = "New login"
# user.password = "New password"

# # Используем публичный атрибут
# print("Login:", user.login)
# print("Password:", user.password)


# Используем методы геттеров
print("Login:", user.get_login())
print("Password:", user.get_password())

# Используем методы сеттеров
user.set_login("New login")
user.set_password("New password")

# Используем методы геттеров после изменения значений
print("Login:", user.get_login())
print("Password:", user.get_password())
```


А теперь вместо методов геттеров и сеттеров используем `property`. Обратите внимание что код взаимодействующий с атрибутами находится без изменений:

```python
class User:
    def __init__(self, login, password):
        self.__login = login  # Приватный атрибут
        self.__password = password  # Приватный атрибут

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_login):
        self.__login = new_login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        # TODO: check password
        self.__password = new_password

# Создаем объект класса User
user = User(login="John", password="Secure password")

# Используем публичный атрибут
print("Login:", user.login)
print("Password:", user.password)

# Меняем публичный атрибут
user.login = "New login"
user.password = "New password"

# Используем публичный атрибут
print("Login:", user.login)
print("Password:", user.password)
```


