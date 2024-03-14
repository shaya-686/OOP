# Static and dynamic polymorphism

# Static polymorphism
def add(x, y):
    return x + y


result1 = add(1, 4)
result2 = add("Hello", "world")

print(result1, result2)


# Dynamic polymorphism
class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Bark!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


def animal_speak(animal):
    return animal.make_sound()


dog, cat = Dog(), Cat()
result1 = animal_speak(dog)
result2 = animal_speak(cat)
print(result1, result2)