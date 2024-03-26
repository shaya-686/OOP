# inheritance

class Animal:
    def sound(self):
        print("Hrrr")

    def make_noise(self):
        self.sound()
        self.sound()
        self.sound()


class Dog(Animal):
    def run(self):
        print("Running")

    def sound(self):
        print("Hav")


class Cat(Animal):
    def sound(self):
        super().sound()
        print("Meow")

    def get_super(self):
        print(super())


# obj = Dog()
# obj.sound()
# obj.make_noise()
# obj = Cat()
# obj.sound()
# obj.get_super()

class Figure:
    def __init__(self, area):
        self._area = area
        print("Init from Figure")

    def _method(self):
        print("Hello")


class Circle(Figure):
    def __init__(self, area, radius):
        super().__init__(area)
        self.__radius = radius
        print("Init circle")

    def print_info(self):
        print(f"{self._area=}")
        print(f"{self.__radius=}")
        super()._method()


# obj = Circle(20, 3)
# obj.print_info()


# School
class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def get_name(self):
        return self._name


class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self._student_id = student_id

    def get_id(self):
        return self._student_id

    def set_id(self, new_id):
        self._student_id = new_id

    def get_info(self, objects):
        print(f"Student {self._name} objects:")
        for i, object in enumerate(objects):
            print(f"{i + 1}.{object}")


class Teacher(Person):
    def __init__(self, name, age, gender, employee_id):
        super().__init__(name, age, gender)
        self._employee_id = employee_id
        self._students = []

    def get_id(self):
        return self._employee_id

    def set_id(self, new_id):
        self._employee_id = new_id

    def get_info(self, objects):
        print(f"Employee {self._name} objects:")
        for i, object in enumerate(objects):
            print(f"{i + 1}.{object}")

    def add_student(self, student: Student):
        self._students.append(student)

    def add_grade(self, grade):
        for student in self._students:
            print(f"{student.get_name()} get {grade}")


student1 = Student("John", 27, "male", "0001233")
student2 = Student("Mike", 27, "male", "0001233")
student1.get_info(["Math", "Python", "C++"])

teacher = Teacher("Anna", 35, "female", "9991234")
teacher.add_student(student1)
teacher.add_student(student2)
teacher.add_grade(12)


# MusicShop
class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity



class CD(Product):
    def __init__(self, name, price, quantity, singer, song_quantity):
        super().__init__(name, price, quantity)
        self._singer = singer
        self._song_quantity = song_quantity

    def get_singer(self):
        return self._singer

    def set_singer(self, new_singer):
        self._singer = new_singer

    def get_song_quantity(self):
        return self._song_quantity

    def set_song_quantity(self, new_song_quantity):
        self._song_quantity = new_song_quantity



class MusicalInstrument(Product):
    def __init__(self, name, price, quantity, instrument_type, material):
        super().__init__(name, price, quantity)
        self._instrument_type = instrument_type
        self._material = material

    def get_instrument_type(self):
        return self._instrument_type

    def set_instrument_type(self, new_instrument_type):
        self._instrument_type = new_instrument_type

    def get_material(self):
        return self._material

    def set_material(self, new_material):
        self._material = new_material


cd = CD("cd_name", 200, 1, "Ocean Elsa", 10)
print(cd.get_singer())

