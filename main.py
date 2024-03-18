class City:
    def __init__(self, name, region, country, population, zipCode, telephoneCode):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.zipCode = zipCode
        self.telephoneCode = telephoneCode

    def create_city(self):
        print("Enter the information about the city: ")
        self.name = input("Enter the city name: ")
        self.region = input("Enter the city region: ")
        self.country = input("Enter the city country: ")
        while True:
            try:
                self.population = int(input("Enter the city population: "))
                break
            except ValueError as e:
                print("Population should be int")
        self.zipCode = input("Enter the city zipCode: ")
        self.telephoneCode = input("Enter the city telephoneCode: ")

    def __str__(self):
        return (f"Information about the city: "
                f"name - {self.name}, "
                f"region - {self.region}, "
                f"population - {self.population},"
                f"telephoneCode - {self.telephoneCode},"
                f"country - {self.country},"
                f"zipCode - {self.zipCode}")

    def __add__(self, some_population):
        self.population += some_population
        return self

    def __sub__(self, some_population):
        if some_population > self.population:
            print("Population cannot be changed")
        else:
            self.population -= some_population
            return self

    def __eq__(self, other):
        return self.population == other.population

    def __gt__(self, other):
        return self.population > other.population

    def __lt__(self, other):
        return self.population < other.population


first_city = City("", "", "", "", "", "")
second_city = City("", "", "", "", "", "")

first_city.create_city()
second_city.create_city()

print(first_city)
print(second_city)

print(first_city + 1000)
print(second_city - 1000)

if first_city == second_city:
    print("This cities have the same population")
elif first_city > second_city:
    print("First city is bigger than the second one")
elif first_city < second_city:
    print("Second city is bigger than the first one")