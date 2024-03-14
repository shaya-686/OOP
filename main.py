# До вже реалізованого класу «Автомобіль» додайте
# необхідні перевантажені методи та оператори.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return (f"Car information: "
                f"brand - {self.brand}, "
                f"model - {self.model},"
                f"year - {self.year}")

    def __eq__(self, other):
        return self.year == other.year

    def __gt__(self, other):
        return self.year > other.year

    def __lt__(self, other):
        return self.year < other.year


car1 = Car("AUDI", "A6", "2022")
car2 = Car("AUDI", "A6", "2020")
print(car1)

if car1 == car2:
    print("The years of this cars is the same")
elif car1 > car2:
    print("First car is newer then the second car")
elif car1 < car2:
    print("First car is older then the second car")
else:
    print("Year of this cars is not equal")
