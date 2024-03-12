# Створіть клас Circle з атрибутом radius та методом
# area, який поверне площу кола з вказаним радіусом.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = round(3.14 * self.radius, 2)
        return circle_area


circle1 = Circle(20)
print(f"Circle area: {circle1.area()}")
