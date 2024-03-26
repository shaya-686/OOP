class Passport:
    def __init__(self, name, number, country):
        self._name = name
        self._number = number
        self._country = country

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_number(self):
        return self._number

    def set_number(self, number):
        self._number = number

    def get_info(self):
        print(f"Person name: {self._name}, passport number: {self._number}, country: {self._country}")


class ForeignPassport(Passport):
    def __init__(self, name, number, country, foreign_number):
        super().__init__(name, number, country)
        self._visa = []
        self._foreign_number = foreign_number

    def get_visa(self):
        return self._visa

    def add_visa(self, visa):
        if visa in self._visa:
            print("Visa has already exist")
        else:
            self._visa.append(visa)

    def get_foreign_number(self):
        return self._foreign_number

    def set_foreign_number(self, new_number):
        self._foreign_number = new_number


passport = Passport("Alice", "CD121353", "Ukraine")
passport.set_name("Bob")
print(f"{passport.get_name()=}")
passport.set_number("CF5145")
print(f"{passport.get_number()=}")
passport.get_info()


foreign_passport = ForeignPassport("Alice", "CD121353", "Ukraine", "JKB51665165")
foreign_passport.add_visa("Canada")
print(f"{foreign_passport.get_visa()=}")
foreign_passport.set_name("Bob")
foreign_passport.set_foreign_number("CF514545")
print(f"{foreign_passport.get_foreign_number()=}")
foreign_passport.get_info()

