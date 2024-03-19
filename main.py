class User:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        self.__age = new_age

    def set_email(self, new_email):
        self.__email = new_email

    def __str__(self):
        return f"Name: {self.__name}, date: {self.__age}, desc: {self.__email}"


user = User("Bob", 30, "bob@gmail.com")
print(f"{user.get_name()=}")
print(f"{user.get_age()=}")
print(f"{user.get_email()=}")

user.set_age(10)
user.set_name("Ann")
user.set_email("new@gmail.com")
print(user)


class ShoppingCart:
    def __init__(self):
        self.__products = []

    def get_products(self):
        return self.__products

    def add_product(self, product, price):
        product_exists = False
        for item in self.__products:
            if product == item[0]:
                print("Product already exists")
                product_exists = True
                break
        if not product_exists:
            self.__products.append((product, price))

    def basket_total(self):
        total = 0
        for item in self.__products:
            total += item[1]
        return total

    def __str__(self):
        return f"{self.__products}"


cart = ShoppingCart()
cart.add_product("Milk", 200)
cart.add_product("Coffee", 300)
cart.add_product("Tea", 400)
cart.add_product("Coffee", 300)

print(f"{cart.get_products()=}")

print(f"{cart.basket_total()=}")


class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def top_up(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
        else:
            print("Not enough balance")


wallet = Wallet(50)
print(f"{wallet.get_balance()=}")

wallet.top_up(50)
print(f"{wallet.get_balance()=}")

wallet.withdraw(60)
print(f"{wallet.get_balance()=}")

wallet.withdraw(200)
print(f"{wallet.get_balance()=}")


class Computer:
    def __init__(self, processor, ram, gpu):
        self.__processor = processor
        self.__ram = ram
        self.__gpu = gpu

    def get_processor(self):
        return self.__processor

    def get_ram(self):
        return self.__ram

    def get_gpu(self):
        return self.__gpu

    def set_processor(self, new_processor):
        self.__processor = new_processor

    def set_ram(self, new_ram):
        self.__ram = new_ram

    def set_gpu(self, new_gpu):
        self.__gpu = new_gpu

    def __str__(self):
        return f"Processor: {self.__processor}, ram: {self.__ram}, video card: {self.__gpu}"


computer = Computer("AMD Ryzen 7 4800H (2.9 - 4.2 ГГц)", 8, "nVidia GeForce RTX 3050")
print(f"{computer.get_processor()=}")
print(f"{computer.get_ram()=}")
print(f"{computer.get_gpu()=}")

computer.set_processor("Intel Core i5-10400H (2.6 - 4.6 ГГц)")
print(computer)

computer.set_ram(16)
print(computer)

computer.set_gpu("nVidia GeForce GTX 1650")
print(computer)
