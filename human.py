class Human:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def get_name(self):
        return self._name

    def get_info(self):
        print(f"Person: {self._name}, age: {self._age}, gender: {self._gender}")


class Builder(Human):
    def __init__(self, name, age, gender, licence):
        super().__init__(name, age, gender)
        self._projects = []
        self._licence = licence

    def get_projects(self):
        return self._projects

    def add_project(self, project):
        if project in self._projects:
            print("Project has already exist")
        else:
            self._projects.append(project)

    def get_licence(self):
        return self._licence

    def set_licence(self, new_licence):
        self._licence = new_licence

    def get_info(self):
        print(f"{super().get_info()}. Builder info: {self._projects}, {self._licence}")


class Sailor(Human):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self._sailing_routes = []
        self._qualifications = []

    def get_sailing_routes(self):
        return self._sailing_routes

    def add_sailing_route(self, sailing_route):
        if sailing_route in self._sailing_routes:
            print("Sailing_route has already exist")
        else:
            self._sailing_routes.append(sailing_route)

    def get_qualifications(self):
        return self._qualifications

    def add_qualification(self, qualification):
        if qualification in self._qualifications:
            print("Qualification has already exist")
        else:
            self._qualifications.append(qualification)

    def get_info(self):
        print(f"{super().get_info()}. Builder info: {self._sailing_routes}, {self._qualifications}")


class Pilot(Human):
    def __init__(self, name, age, gender, health):
        super().__init__(name, age, gender)
        self._aircraft_types = []
        self._health = health

    def get_aircraft_types(self):
        return self._aircraft_types

    def add_aircraft_type(self, aircraft_type):
        if aircraft_type in self._aircraft_types:
            print("Aircraft_type has already exist")
        else:
            self._aircraft_types.append(aircraft_type)

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health

    def get_info(self):
        print(f"{super().get_info()}. Builder info: {self._aircraft_types}, {self._health}")


builder = Builder("Bob", 47, "male", "A")
builder.add_project("First")
print(f"{builder.get_projects()=}")
builder.set_licence("B")
print(f"{builder.get_licence()=}")
builder.get_info()


sailor = Sailor("Mike", 28, "male")
sailor.add_sailing_route("Transatlantic Crossing")
print(f"{sailor.get_sailing_routes()=}")
sailor.add_qualification("medical diploma")
print(f"{sailor.get_qualifications()=}")
sailor.get_info()


pilot = Pilot("Kate", 28, "female", "good")
pilot.add_aircraft_type("Helicopter")
print(f"{pilot.get_aircraft_types()=}")
pilot.set_health("normal")
print(f"{pilot.get_health()=}")
pilot.get_info()


