class Clock:
    def __init__(self, model, brand, year, price, clockType):
        self.model = model
        self.brand = brand
        self.year = year
        self.price = price
        self.clockType = clockType

    def create_clock(self):
        print("Enter the information about the clock: ")
        self.model = input("Enter the clock model: ")
        self.brand = input("Enter the clock brand: ")
        self.clockType = input("Enter the clockType: ")
        while True:
            try:
                self.year = int(input("Enter the clock year: "))
                break
            except ValueError as e:
                print("Year should be int")
        while True:
            try:
                self.price = float(input("Enter the clock price: "))
                break
            except ValueError as e:
                print("Price should be float")

    def __str__(self):
        return (f"Information about the clock: "
                f"model - {self.model}, "
                f"brand - {self.brand}, "
                f"year - {self.year},"
                f"price - {self.price},"
                f"clockType - {self.clockType}")

    def __add__(self, some_price):
        self.price += some_price
        return self

    def __sub__(self, some_price):
        if some_price > self.price:
            print("Price cannot be changed")
        else:
            self.price -= some_price
            return self

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price


first_clock = Clock("", "", "", "", "")
second_clock = Clock("", "", "", "", "")

first_clock.create_clock()
second_clock.create_clock()

print(first_clock)
print(second_clock)

print(first_clock + 1000)
print(second_clock - 1000)

if first_clock == second_clock:
    print("This clocks have the same price")
elif first_clock > second_clock:
    print("First clock is more expensive than the second one")
elif first_clock < second_clock:
    print("Second clock is more expensive than the first one")
