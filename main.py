# fraction

class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def display_fraction(self):
        print(f"{self.nominator}/{self.denominator}")

    def add(self, other_fraction):
        result_nominator = self.nominator * other_fraction.denominator + other_fraction.nominator * self.denominator
        result_denominator = other_fraction.denominator * self.denominator
        return Fraction(result_nominator, result_denominator)

    def subtract(self, other_fraction):
        result_nominator = self.nominator * other_fraction.denominator - other_fraction.nominator * self.denominator
        result_denominator = other_fraction.denominator * self.denominator
        return Fraction(result_nominator, result_denominator)

    def multiply(self, other_fraction):
        result_nominator = self.nominator * other_fraction.nominator
        result_denominator = other_fraction.denominator * self.denominator
        return Fraction(result_nominator, result_denominator)

    def divide(self, other_fraction):
        result_nominator = self.nominator * other_fraction.denominator
        result_denominator = other_fraction.nominator * self.denominator
        return Fraction(result_nominator, result_denominator)


first_fraction = Fraction(10, 20)
new_fraction = Fraction(5, 20)

first_fraction.display_fraction()
new_fraction.display_fraction()

result_addition = first_fraction.add(new_fraction)
result_addition.display_fraction()

result_subtraction = first_fraction.subtract(new_fraction)
result_subtraction.display_fraction()

result_multiplication = first_fraction.multiply(new_fraction)
result_multiplication.display_fraction()

result_division = first_fraction.divide(new_fraction)
result_division.display_fraction()