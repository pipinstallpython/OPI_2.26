#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Составить программу с использованием классов и объектов для решения задачи. Во всех
заданиях, помимо указанных в задании операций, обязательно должны быть реализованы
следующие методы:
метод инициализации __init__ ;
ввод с клавиатуры read ;
вывод на экран display .
Номер варианта необходимо уточнить у преподавателя. В раздел программы, начинающийся
после инструкции if __name__ = '__main__': добавить код, демонстрирующий возможности
разработанного класса.

Реализовать класс Account, представляющий собой банковский счет. В классе должны быть
четыре поля: фамилия владельца, номер счета, процент начисления и сумма в рублях.
Открытие нового счета выполняется операцией инициализации. Необходимо выполнять
следующие операции: сменить владельца счета, снять некоторую сумму денег со счета,
положить деньги на счет, начислить проценты, перевести сумму в доллары, перевести
сумму в евро, получить сумму прописью (преобразовать в числительное).
"""

class Account:
    def __init__(self, owner, number, interest_rate, balance):
        self.owner = owner
        self.number = number
        self.interest_rate = interest_rate
        self.balance = balance

    def read(self):
        self.owner = input("Введите фамилию владельца счета: ")
        self.number = input("Введите номер счета: ")
        self.interest_rate = float(input("Введите процент начисления: "))
        self.balance = float(input("Введите сумму в рублях: "))

    def display(self):
        print("Фамилия владельца: ", self.owner)
        print("Номер счета: ", self.number)
        print("Процент начисления: ", self.interest_rate)
        print("Сумма в рублях: ", self.balance)

    # Смена владельца счета
    def change_owner(self, new_owner):
        self.owner = new_owner

    # Снятие некоторой суммы со счета
    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Снято", amount, "рублей")
        else:
            print("Недостаточно средств на счете")

    # Положить деньги на счет
    def crediting_money(self, amount):
        self.balance += amount
        print("Положено", amount, "рублей")

    # Начислить проценты
    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print("Начислены проценты:", interest, "рублей")

    # Перевести сумму в доллары
    def convert_to_dollars(self, exchange_rate):
        dollars = self.balance / exchange_rate
        print("Сумма в долларах:", dollars)

    # Перевести сумму в евро
    def convert_to_euros(self, exchange_rate):
        euros = self.balance / exchange_rate
        print("Сумма в евро:", euros)

    # Получить сумму прописью (преобразовать в числительное)
    def get_amount_in_words(self):
        ones = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть',
                'семь', 'восемь', 'девять']
        teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать',
                 'четырнадцать', 'пятнадцать', 'шестнадцать',
                 'семнадцать', 'восемнадцать', 'девятнадцать']
        tens = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
                'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
        hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот',
                    'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
        thousands = {
            0: '',
            1: 'одна тысяча',
            2: 'две тысячи',
            3: 'три тысячи',
            4: 'четыре тысячи',
            5: 'пять тысяч',
            6: 'шесть тысяч',
            7: 'семь тысяч',
            8: 'восемь тысяч',
            9: 'девять тысяч'
        }

        amount = int(self.balance)

        thousands_part = amount // 1000
        hundreds_part = (amount // 100) % 10
        tens_part = (amount // 10) % 10
        ones_part = amount % 10

        words = []

        if thousands_part > 0:
            words.append(thousands.get(thousands_part))

        if hundreds_part > 0:
            words.append(hundreds[hundreds_part])

        if tens_part == 1:
            words.append(teens[ones_part])
        else:
            if tens_part > 0:
                words.append(tens[tens_part])

            if ones_part > 0:
                words.append(ones[ones_part])

        amount_in_words = ' '.join(words)
        print("Сумма прописью:", amount_in_words)


if __name__ == '__main__':
    account = Account("", "", 0.0, 0.0)
    account.read()
    account.display()

    account.change_owner("Новый владелец")
    account.withdrawal(500)
    account.crediting_money(1000)
    account.add_interest()
    account.convert_to_dollars(80)
    account.convert_to_euros(86)
    account.get_amount_in_words()
    account.display()
