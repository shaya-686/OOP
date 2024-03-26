class Animal:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def display_info(self):
        print(f"Name: {self._name}")


class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def display_info(self):
        super().display_info()
        print(f"Age: {self._age}")


class Crocodile(Animal):
    def __init__(self, name, length):
        super().__init__(name)
        self._length = length

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length

    def display_info(self):
        super().display_info()
        print(f"Length: {self._length} meters")


class Kangaroo(Animal):
    def __init__(self, name, pouch_capacity):
        super().__init__(name)
        self._pouch_capacity = pouch_capacity

    def get_capacity(self):
        return self._pouch_capacity

    def set_capacity(self, capacity):
        self._pouch_capacity = capacity

    def display_info(self):
        super().display_info()
        print(f"Pouch Capacity: {self._pouch_capacity} units")


tiger = Tiger("Mike", 5)
tiger.display_info()

crocodile = Crocodile("Emmie", 3.5)
crocodile.display_info()


kangaroo = Kangaroo("Jack", 2)
kangaroo.display_info()
