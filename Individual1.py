#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Triangle для представления треугольника. Поля данных должны включать
# углы и стороны. Требуется реализовать операции: получения и изменения полей данных,
# вычисления площади, вычисления периметра, вычисления высот, а также определения
# вида треугольника (равносторонний, равнобедренный или прямоугольный).

import math


class Triangle:

    def __init__(self):

        self.__a = 0
        self.__b = 0
        self.__c = 0

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(',')))

        for part in parts:
            if part == 0:
                raise ValueError()

            self.__a = float(parts[0])
            self.__b = float(parts[1])
            self.__c = float(parts[2])

    def set_sides(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_sides(self):
        return self.__a, self.__b, self.__c

    def __per(self):
        return self.__a + self.__b + self.__c

    def __square(self):
        p = self.__per() * 0.5
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

    def __H(self):
        return 2*self.__square()/self.__a, 2*self.__square()/self.__b, 2*self.__square()/self.__c

    def __type(self):

        alpha = math.degrees(math.acos((self.__b ** 2 + self.__c ** 2 - self.__a ** 2) / (2 * self.__c * self.__b)))
        beta = math.degrees(math.acos((self.__a ** 2 + self.__c ** 2 - self.__b ** 2) / (2 * self.__a * self.__c)))
        gamma = math.degrees(math.acos((self.__a ** 2 + self.__b ** 2 - self.__c ** 2) / (2 * self.__a * self.__b)))

        if alpha == 90 or beta == 90 or gamma == 90:
            type1 = "прямоугольный"
        elif self.__a == self.__b == self.__c:
            type1 = "равносторонний"
        elif self.__a == self.__b or self.__b == self.__c or self.__c == self.__a:
            type1 = "равнобедренный"
        else:
            type1 = "разносторонний"
        return type1

    def dispaly(self):
        print("Искомые величины: "
              "Площадь S={}; "
              "Периметр p={}; "
              "Высоты (h1, h2, h3) сотвественно равны {}; "
              "Тип треугольника - {}.".format(self.__per(), self.__square(),  self.__H(), self.__type())
              )


if __name__ == '__main__':
    # Проверка работы класса
    T1 = Triangle()
    T1.read("Введите стороны трегольника ")
    T1.dispaly()

    # Изменение сторон и их получение
    T1.set_sides(5, 5, 5)
    print(T1.get_sides())
    T1.dispaly()
