
class Animals:
    def breath(self):
        print("Breathing")

    def move(self):
        print("Moving")

    def eat_food(self):
        print("Eating")


class Dogs(Animals):
    pass


class Cat(Animals):
    pass


my_dog = Dogs()
my_dog.breath()
my_dog.move()
my_dog.eat_food()
