# fraction

class Fraction:
    __count = 0

    def __init__(self, nominator, denominator):
        self.__nominator = nominator
        self.__denominator = denominator
        Fraction.__count += 1

    @staticmethod
    def get_count():
        return Fraction.__count

    def display_fraction(self):
        print(f"{self.__nominator}/{self.__denominator}")

    def add(self, other_fraction):
        result_nominator = self.__nominator * other_fraction.__denominator + other_fraction.__nominator * self.__denominator
        result_denominator = other_fraction.__denominator * self.__denominator
        return Fraction(result_nominator, result_denominator)

    def subtract(self, other_fraction):
        result_nominator = self.__nominator * other_fraction.__denominator - other_fraction.__nominator * self.__denominator
        result_denominator = other_fraction.__denominator * self.__denominator
        return Fraction(result_nominator, result_denominator)

    def multiply(self, other_fraction):
        result_nominator = self.__nominator * other_fraction.__nominator
        result_denominator = other_fraction.__denominator * self.__denominator
        return Fraction(result_nominator, result_denominator)

    def divide(self, other_fraction):
        result_nominator = self.__nominator * other_fraction.__denominator
        result_denominator = other_fraction.__nominator * self.__denominator
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

print(f"{Fraction.get_count()=}")


# Temperature
class TemperatureConverter:
    __count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius_temp):
        try:
            fahrenheit_temp = celsius_temp * 9 / 5 + 32
            TemperatureConverter.__count += 1
            return round(fahrenheit_temp, 2)
        except TypeError as e:
            print("Message: ", e)
            return -1

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit_temp):
        try:
            celsius_temp = (fahrenheit_temp - 32) * 5 / 9
            TemperatureConverter.__count += 1
            return round(celsius_temp, 2)
        except TypeError as e:
            print("Message: ", e)
            return -1

    @staticmethod
    def get_count():
        return TemperatureConverter.__count


print(f"{TemperatureConverter.celsius_to_fahrenheit(10)=}")
print(f"{TemperatureConverter.fahrenheit_to_celsius(100)=}")
print(f"{TemperatureConverter.celsius_to_fahrenheit(15)=}")
print(f"{TemperatureConverter.fahrenheit_to_celsius(210)=}")
print(f"{TemperatureConverter.get_count()=}")


# Converter
class Converter:
    @staticmethod
    def check_value(value):
        try:
            if type(value) in (float, int):
                if value >= 0:
                    return True
                else:
                    raise ValueError("Value should be bigger than 0")
            else:
                raise TypeError("Value should be int or float")
        except TypeError as e:
            print("Message: ", e)
            return False
        except ValueError as e:
            print("Message: ", e)
            return False
        except Exception as e:
            print("Message: ", e)
            return False

    @staticmethod
    def meters_to_feet(meters):
        if Converter.check_value(meters):
            feet = meters * 3.28084
            return feet
        else:
            return -1

    @staticmethod
    def feet_to_meters(feet):
        if Converter.check_value(feet):
            meters = feet / 3.28084
            return meters
        else:
            return -1

    @staticmethod
    def kilometers_to_miles(kilometers):
        if Converter.check_value(kilometers):
            miles = kilometers / 1.60934
            return miles
        else:
            return -1

    @staticmethod
    def miles_to_kilometers(miles):
        if Converter.check_value(miles):
            kilometers = miles * 1.60934
            return kilometers
        else:
            return -1

    @staticmethod
    def kilograms_to_pounds(kilograms):
        if Converter.check_value(kilograms):
            pounds = kilograms * 2.20462
            return pounds
        else:
            return -1

    @staticmethod
    def pounds_to_kilograms(pounds):
        if Converter.check_value(pounds):
            kilograms = pounds / 2.20462
            return kilograms
        else:
            return -1


print(f"{Converter.meters_to_feet(10)=}")
print(f"{Converter.feet_to_meters(100)=}")
print(f"{Converter.kilometers_to_miles(10)=}")
print(f"{Converter.miles_to_kilometers(20)=}")

print(f"{Converter.kilograms_to_pounds(10)=}")
print(f"{Converter.pounds_to_kilograms(22)=}")


# information system
class InformationSystem:
    __data = {}

    @classmethod
    def add_user(cls, user):
        try:
            if user in cls.__data:
                raise KeyError(f"{user} has already exist")
            else:
                cls.__data[user] = []
        except KeyError as e:
            print("Message: ", e)
        except Exception as e:
            print("Message: ", e)

    @classmethod
    def add_contact(cls, user, contact):
        try:
            if user in cls.__data:
                if contact not in cls.__data[user]:
                    cls.__data[user].append(contact)
                else:
                    raise ValueError(f"{contact} has already exist")
            else:
                raise KeyError(f"User {user} is not found")
        except KeyError as e:
            print("Message: ", e)
        except ValueError as e:
            print("Message: ", e)
        except Exception as e:
            print("Message: ", e)

    @classmethod
    def system_info(cls):
        print(f"{cls.__data}")


InformationSystem.add_user("Bob")
InformationSystem.add_user("Bob")
InformationSystem.add_user("Mike")

InformationSystem.add_contact("Bob", "Marie: 3805555555555")
InformationSystem.add_contact("Bob", "Marie: 3805555555555")
InformationSystem.add_contact("Bob", "Jack: 3805555555555")
InformationSystem.add_contact("Mike", "Bob: 3805555555555")

InformationSystem.system_info()
