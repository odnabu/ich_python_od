# Tatiana Kletsovka
# \033[0;__;__m \033[m   or   \033[1;__;__m \033[m
# print('#' * 115)      # Для разделения блоков на листе с кодом:
""" ################################################################################################################
 04.04.25
 Python 67: Regular Expressions - SUMMARY 17.
 ################################################################################################################### """

# Video Lesson 67: ------------.
# Video Practice __: wasn't.
# links:
#   - Presentation: Python_34_M.pptx-Regular_Expressions.pdf
#   - Python RegEx: практическое применение регулярок: https://tproger.ru/translations/regular-expression-python.
#   - Регулярные выражения в Python от простого к сложному: https://habr.com/ru/articles/349860/.
#
# def input_numb_list():
#     numb_list = [int(x) for x in input('Enter a list of numbers separated by space: ').split()]
#     return numb_list
# ------------------------ SHORTCUTS ------------------------
# Ctrl + W - выделить текущий блок. если нажимать это сочетание дальше, то будут выделяться родительские блоки.
# Ctrl+Y - Удаление всей строки. Кстати, команда копирования Ctrl+C без выделения также работает для всей строки.
# Ctrl+Akt+L / Alt+Enter - Привести код к принятым стандартам (для Python - PEP8).
# Ctrl+R — Изменить название класса/функции и т. п. по всему проекту.
# Ctrl+Shift + F - Найти по всем файлам.
# Shift + F6 - заменить имя элемента во всех частях во всех файлах.
# -----------------------------------------------------------

print('.' * 120)

""" ___________________________________  Review of previously covered material  ___________________________________ """

# Video 67,

""" \\\\__ NB! __   isinstance(<object>, <type of data>)  -->  ПРОВЕРКА типа данных перед выполнением операций!!! """
num = 3
if isinstance(num, int):
    print(num + 2)


""" ______  Task 1  ______________________________________________________________________________________________ """
# ### Задача: Система обработки заказов:
# Ты разрабатываешь систему обработки заказов для интернет-магазина.
# В магазине продаются разные типы товаров: цифровые, физические и подписки. У каждого типа товара свои правила обработки заказа.
    # #### Условия:
    # 1. Все товары имеют:
    # - название;
    # - цену;
    # 2. При покупке:
    # - **Физический товар** должен быть отправлен по адресу (печать наклейки, доставка).
    # - **Цифровой товар** высылается по email (и даётся скидка в 10% на следующий заказ).
    # - **Подписка** активирует подписку на сервис и присылает уведомление.

# +++++++++++++++++++++++++++++++++++++
from abc import ABC, abstractmethod
# +++++++++++++++++++++++++++++++++++++

class Goods(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def sell(self):
        pass


class PhysicalGoods(Goods):
    def sell(self):
        pass

class DigitalGoods(Goods):
    def sell(self):
        pass

class Subscription(Goods):

    def __init__(self, name, price, duration):
        super().__init__(name, price)
        self.duration = duration

    def sell(self):
        pass


