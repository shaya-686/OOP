# Реалізуйте клас «Стадіон». Збережіть у класі: назву
# стадіону, дату відкриття, країну, місто, місткість. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій. До вже реалізованого класу «Стадіон» додайте
# необхідні перевантажені методи та оператори.


class Stadium:
    def __init__(self, name, date_opening, country, city, capacity):
        self.name = name
        self.date_opening = date_opening
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return (f"Stadium information: "
                f"name - {self.name}, "
                f"date of opening - {self.date_opening},"
                f"country - {self.country},"
                f"city - {self.city},"
                f"capacity - {self.capacity}")

    def __add__(self, cap):
        self.capacity += cap

    def __sub__(self, cap):
        if self.capacity < cap:
            print("Stadium capacity is less then capacity that you provide")
        else:
            self.capacity -= cap
            return self

    def __eq__(self, other):
        if self.capacity == other.capacity:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.capacity > other.capacity:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.capacity < other.capacity:
            return True
        else:
            return False


stadium = Stadium("Olymp", "15.02.2000", "Ukraine", "Kyiv", 100000)
stadium2 = Stadium("Olympus", "15.02.2000", "Ukraine", "Kyiv", 99800)
print(stadium)

stadium_with_increase_capacity = stadium + 100
stadium_with_reduced_capacity = stadium - 500
print(stadium_with_increase_capacity, stadium_with_reduced_capacity)
if stadium == stadium2:
    print("Capacity of this stadiums is the same")
elif stadium > stadium2:
    print("First stadium is bigger then the second stadium")
elif stadium < stadium2:
    print("First stadium is less then the second stadium")
else:
    print("Capacity of this stadiums is not equal")
