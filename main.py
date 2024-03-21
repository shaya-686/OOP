# Human
import math


class Human:
    human_count = 0

    def __init__(self, name, birthday, phone, city, country, address):
        self.__name = name
        self.__birthday = birthday
        self.__phone = phone
        self.__city = city
        self.__country = country
        self.__address = address
        Human.human_count += 1

    @staticmethod
    def get_human_count():
        return Human.human_count


first_human = Human("Bob", "20000212", "38011111111", "Roma", "Italy", "First human address")
second_human = Human("Alice", "20000312", "38022222222", "Roma", "Italy", "Second human address")

print(f"Number of human: {Human.get_human_count()}")


# geometric shapes
class GeometricShapes:
    count = 0

    @staticmethod
    def triangle_area_herons_formula(a, b, c):
        p = (a + b + c) / 2
        GeometricShapes.counter()
        return round(pow(p * (p - a) * (p - b) * (p - c), 0.5), 2)

    @staticmethod
    def triangle_area_coordinates_formula(x1, y1, x2, y2, x3, y3):
        GeometricShapes.counter()
        return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    @staticmethod
    def rectangle_area_formula(a, b):
        GeometricShapes.counter()
        return a * b

    @staticmethod
    def square_area_formula(a):
        GeometricShapes.counter()
        return a ** 2

    @staticmethod
    def diamond_area_formula(d1, d2):
        GeometricShapes.counter()
        return d1 * d2 / 2

    @staticmethod
    def counter():
        GeometricShapes.count += 1

    @staticmethod
    def get_count():
        return GeometricShapes.count


print(f"{GeometricShapes.triangle_area_herons_formula(4, 5, 6)=}")
print(f"{GeometricShapes.triangle_area_coordinates_formula(1,3,5,9,7,3)=}")
print(f"{GeometricShapes.rectangle_area_formula(4,5)=}")
print(f"{GeometricShapes.square_area_formula(4)=}")
print(f"{GeometricShapes.diamond_area_formula(4, 8)=}")
print(GeometricShapes.get_count())


# MathOperations

class MathOperations:

    @staticmethod
    def maximum(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def minimum(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def average(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(num):
        return math.factorial(num)


print(f"{MathOperations.maximum(5,6,7,8)=}")
print(f"{MathOperations.minimum(5,6,7,8)=}")
print(f"{MathOperations.average(5,6,7,8)=}")
print(f"{MathOperations.factorial(4)=}")
