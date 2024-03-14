# Створіть клас «Дріб». Збережіть у класі чисельник
# та знаменник. Реалізуйте методи класу для введеннявиведення даних. Також створіть методи класу для
# виконання арифметичних операцій (додавання,
# віднімання, множення, ділення і т. д.). До вже
# реалізованого класу «Дріб» додайте необхідні
# перевантажені методи та оператори.


class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"

    def __add__(self, other):
        result_nominator = self.nominator * other.denominator + other.nominator * self.denominator
        result_denominator = other.denominator * self.denominator
        return Fraction(result_nominator, result_denominator)

    def __sub__(self, other):
        result_nominator = self.nominator * other.denominator - other.nominator * self.denominator
        result_denominator = other.denominator * self.denominator
        return Fraction(result_nominator, result_denominator)

    def __mul__(self, other):
        result_nominator = self.nominator * other.nominator
        result_denominator = other.denominator * self.denominator
        return Fraction(result_nominator, result_denominator)

    def __truediv__(self, other):
        result_nominator = self.nominator * other.denominator
        result_denominator = other.nominator * self.denominator
        return Fraction(result_nominator, result_denominator)


first_fraction = Fraction(10, 20)
new_fraction = Fraction(5, 20)
print(first_fraction)
print(new_fraction)


result_addition = first_fraction + new_fraction
print(result_addition)

result_subtraction = first_fraction - new_fraction
print(result_subtraction)

result_multiplication = first_fraction * new_fraction
print(result_multiplication)

result_division = first_fraction/new_fraction
print(result_division)
