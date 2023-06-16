#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Парой называется класс с двумя полями, которые обычно имеют имена first и second. Требуется
реализовать тип данных с помощью такого класса. Во всех заданиях обязательно должны
присутствовать:
метод инициализации __init__ ; метод должен контролировать значения аргументов на
корректность;
ввод с клавиатуры read ;
вывод на экран display .
Реализовать внешнюю функцию с именем make_тип() , где тип — тип реализуемой структуры.
Функция должна получать в качестве аргументов значения для полей структуры и возвращать
структуру требуемого типа. При передаче ошибочных параметров следует выводить сообщение
и заканчивать работу.
Номер варианта необходимо уточнить у преподавателя. В раздел программы, начинающийся
после инструкции if __name__ = '__main__': добавить код, демонстрирующий возможности
разработанного класса.

Поле first — целое положительное число, часы; поле second — целое положительное
число, минуты. Реализовать метод minutes() — приведение времени в минуты.
"""

def is_number(s):
    try:
        int(s)
    except ValueError:
        return False
    return True


def make_conversion(first, second):
    if is_number(first) and is_number(second) and first > 0 and second > 0:
        conversion = Conversion(first, second)
        return conversion
    else:
        raise ValueError


class Conversion:
    def __init__(self, first=0, second=0):
        if is_number(first) and is_number(second):
            if first > 0 and second > 0:
                self.__first = first
                self.__second = second
            else:
                raise ValueError
        else:
            raise ValueError

    def read(self):
        self.__first = int(input("Enter the first value: "))
        self.__second = int(input("Enter the second value: "))

    def display(self):
        print(f"First value: {self.__first}")
        print(f"Second value: {self.__second}")

    def cost(self):
        return 60 * self.__first + self.__second


if __name__ == '__main__':
    p1 = make_conversion(3, 45)
    p1.display()
    print(f"Time in minutes: {p1.cost()}")
    p1.read()
    print(f"Time in minutes: {p1.cost()}")
    p2 = make_conversion("fhhfhf", 4)
    p2.display()
    p2.cost()
