from datetime import datetime


class Human:
    def __init__(self, name, birthday, phone, city, country, address):
        self.name = name
        self.birthday = birthday
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def create_human(self):
        print("Enter the information about the human: ")
        self.name = input("Enter the human name: ")
        while True:
            date_format = "%Y/%m/%d"
            date_of_birth = input("Enter the human birthday: ")
            try:
                self.birthday = datetime.strptime(date_of_birth, date_format)
                break
            except ValueError as e:
                print("Date has incorrect type: ", e)
        self.phone = input("Enter the human phone: ")
        self.city = input("Enter the human city: ")
        self.country = input("Enter the human country: ")
        self.address = input("Enter the human address: ")

    def __str__(self):
        return (f"Human information: "
                f"name - {self.name}, "
                f"birthday - {self.birthday},"
                f"phone - {self.phone},"
                f"city - {self.city},"
                f"country - {self.country},"
                f"address - {self.address}")

    def __sub__(self, other):
        if self.birthday < other.birthday:
            self.birthday, other.birthday = other.birthday, self.birthday
        return self.birthday - other.birthday

    def __eq__(self, other):
        return self.birthday == other.birthday

    def __gt__(self, other):
        return self.birthday > other.birthday

    def __lt__(self, other):
        return self.birthday < other.birthday


first_human = Human("", "", "", "", "", "")
second_human = Human("", "", "", "", "", "")

first_human.create_human()
second_human.create_human()

print(first_human)
print(second_human)

print("The difference between dates of birthday: ", first_human - second_human)

if first_human == second_human:
    print("This humans have birthdays in one day!")
elif first_human < second_human:
    print("First human is older than the second one")
elif first_human > second_human:
    print("Second human is older than the first one")

