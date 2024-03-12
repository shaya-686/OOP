
class Animals:
    def breath(self):
        print("Breathing")

    def move(self):
        print("Moving")

    def eat_food(self):
        print("Eating")


class Dogs(Animals):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


class Cat(Animals):
    pass


# my_dog = Dogs()
# my_dog.breath()
# my_dog.move()
# my_dog.eat_food()
my_dog = Dogs("Bob", 5, "labrador")
my_dog_2 = Dogs("Em", 6, "labrador")
print(my_dog.name)
print(my_dog.age)
print(my_dog.breed)