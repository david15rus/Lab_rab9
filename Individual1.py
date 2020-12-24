#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Triangle для представления треугольника. Поля данных должны включать
# углы и стороны. Требуется реализовать операции: получения и изменения полей данных,
# вычисления площади, вычисления периметра, вычисления высот, а также определения
# вида треугольника (равносторонний, равнобедренный или прямоугольный).

import math
from turtledemo.chaos import h


class Triangle:

    def __init__(self):

        self.a = 0
        self.b = 0
        self.c = 0
        self.S = 0

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(',')))

        if parts == 0:
            raise ValueError()
        self.a = float(parts[0])
        self.b = float(parts[1])
        self.c = float(parts[2])

    def per(self):
        P = self.a + self.b + self.c
        return P

    def square(self):
        p = (self.a + self.b + self.c) * 0.5
        self.S = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return self.S

    def H(self):
        type_h = input("Введите букву строны, для которой нужно вычислить высоту (a, b или с) ")
        if type_h == "a":
            h1 = 2*self.S/self.a
        elif type_h == "b":
            h1 = 2*self.S/self.b
        else:
            h1 = 2*self.S/self.c
        return h1

    def type(self):

        alpha = math.degrees(math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.c * self.b)))
        beta = math.degrees(math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c)))
        gamma = math.degrees(math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b)))

        if alpha == 90 or beta == 90 or gamma == 90:
            type1 = "прямоугольный"
        elif self.a == self.b == self.c:
            type1 = "равносторонний"
        elif self.a == self.b or self.b == self.c or self.c == self.a:
            type1 = "равнобедренный"
        else:
            type1 = "разносторонний"
        return type1

    def dispaly(self):
        print("Искомые величины "
              "Площадь S={} "
              "Периметр p={} "
              "Высота h={} "
              "Тип треугольника - {} ".format(T1.square(), T1.per(), T1.H(), T1.type())
              )


if __name__ == '__main__':
    T1 = Triangle()
    T1.read("Введите стороны трегольника ")
    T1.dispaly()
