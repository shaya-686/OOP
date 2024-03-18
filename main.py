class Country:
    def __init__(self, name, continent, population, telephoneCode, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.telephoneCode = telephoneCode
        self.capital = capital
        self.cities = cities

    def create_country(self):
        print("Enter the information about the country: ")
        self.name = input("Enter the country name: ")
        self.continent = input("Enter the country continent: ")
        self.population = input("Enter the country population: ")
        self.telephoneCode = input("Enter the country telephone code: ")
        self.capital = input("Enter the capital of the country: ")
        cities = []
        print("Add the city or press ENTER to break: ")
        while True:
            city = input("Enter the name of the city: ")
            if city == "":
                break
            else:
                cities.append(city)
        self.cities = cities

    def __add__(self, city):
        if city in self.cities:
            print("City is already exist")
        else:
            self.cities.append(city)
            print(f"{city} is added to the {self.name}")
            return self

    def __sub__(self, city):
        if city in self.cities:
            self.cities.remove(city)
            print("City is removed from the list")
            return self
        else:
            print(f"{city} is not found in {self.name}")

    def __eq__(self, other):
        return self.population == other.population

    def __gt__(self, other):
        return self.population > other.population

    def __lt__(self, other):
        return self.population < other.population

    def __str__(self):
        return (f"Information about the country: "
                f"name - {self.name}, "
                f"continent - {self.continent}, "
                f"population - {self.population},"
                f"telephoneCode - {self.telephoneCode},"
                f"capital - {self.capital},"
                f"cities - {self.cities}")


first_country = Country("", "", "", "", "", "")
second_country = Country("", "", "", "", "", "")

first_country.create_country()
second_country.create_country()

print(first_country)
print(second_country)

print(first_country + "Kyiv")
print(first_country - "Kyiv")

if first_country == second_country:
    print("This countries have the same population")
elif first_country > second_country:
    print("First country is bigger than the second one")
elif first_country < second_country:
    print("Second country is bigger than the first one")
