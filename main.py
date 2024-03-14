# Operator overloading
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)


num1 = ComplexNumber(1, 2)
num2 = ComplexNumber(3, 4)
result = num1 + num2
print(result)
