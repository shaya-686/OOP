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

    def update_country(self, **kwargs):
        for key, value in kwargs.items():
            if key == "name":
                self.name = value
            elif key == "continent":
                self.continent = value
            elif key == "population":
                self.population = value
            elif key == "telephoneCode":
                self.telephoneCode = value
            elif key == "capital":
                self.capital = value
            else:
                print("Unknown attribute")
        self.display_country()

    def add_city_to_country(self, city):
        if city in self.cities:
            print("City is already exist")
        else:
            self.cities.append(city)
            print(f"{city} is added to the {self.name}")
            self.display_country()

    def delete_city_from_country(self, city):
        if city in self.cities:
            self.cities.remove(city)
            print("City is deleted")
            self.display_country()
        else:
            print(f"{city} is not found in {self.name}")

    def display_country(self):
        print(f"Information about the country: "
              f"name - {self.name}, "
              f"continent - {self.continent}, "
              f"population - {self.population},"
              f"telephoneCode - {self.telephoneCode},"
              f"capital - {self.capital},"
              f"cities - {self.cities}")


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
        self.population = input("Enter the city population: ")
        self.zipCode = input("Enter the city zipCode: ")
        self.telephoneCode = input("Enter the city telephoneCode: ")

    def display_city(self):
        print(f"Information about the city: "
              f"name - {self.name}, "
              f"region - {self.region}, "
              f"population - {self.population},"
              f"telephoneCode - {self.telephoneCode},"
              f"country - {self.country},"
              f"zipCode - {self.zipCode}")


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
        self.birthday = input("Enter the human birthday: ")
        self.phone = input("Enter the human phone: ")
        self.city = input("Enter the human city: ")
        self.country = input("Enter the human country: ")
        self.address = input("Enter the human address: ")

    def display_human(self):
        print(f"Information about the human: "
              f"name - {self.name}, "
              f"birthday - {self.birthday}, "
              f"phone - {self.phone},"
              f"city - {self.city},"
              f"country - {self.country},"
              f"address - {self.address}")


first_country = Country("", "", "", "", "", "")
first_country.create_country()
first_country.display_country()
first_country.update_country(population=111111, telephoneCode=111)
first_country.add_city_to_country("Kyiv")
first_country.delete_city_from_country("Kyiv")

first_city = City("", "", "", "", "", "")
first_city.create_city()
first_city.display_city()

first_human = Human("", "", "", "", "", "")
first_human.create_human()
first_human.display_human()
