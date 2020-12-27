#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Triad (тройка чисел); определить методы изменения полей и вычисления
# суммы чисел. Определить производный класс Triangle с полями-сторонами. Определить
# методы вычисления углов и площади треугольника.
import math


class Triad:

    def __init__(self, a=5, b=5, c=5):
        self.a = a
        self.b = b
        self.c = c

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(',')))

        if parts == 0:
            raise ValueError()
        self.a = parts[0]
        self.b = parts[1]
        self.c = parts[2]

    def sum(self):
        return self.a + self.b + self.c


class Triangle(Triad):
    def __init__(self, a, b, c):
        super(Triangle, self).__init__(a, b, c)

    def angles(self):
        self.alpha = int(math.degrees(math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.c * self.b))))
        self.beta = int(math.degrees(math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c))))
        self.gamma = int(math.degrees(math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b))))
        return self.alpha, self.beta, self.gamma

    def square(self):
        p = (self.a + self.b + self.c) * 0.5
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


if __name__ == '__main__':
    T1 = Triangle(5, 5, 5)
    T1.read("Введите стороны треугольника ")
    T1.angles()
    print("Искомые величины "
          "Углы треугольника {} "
          "Сумма сторон {} "
          "Площадь {}".format(T1.angles(), T1.sum(), T1.square()))
