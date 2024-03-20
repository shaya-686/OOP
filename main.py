class Taxi:
    carTypes = {"Economy": 100, "Standard": 200, "Comfort": 300}

    def __init__(self):
        self.__client = None
        self.__carType = None
        self.__address = None
        self.__cost = None

    def get_client(self):
        return self.__client

    def get_car_type(self):
        return self.__carType

    def get_address(self):
        return self.__address

    def get_cost(self):
        return self.__cost

    def set_car_type(self, new_car_type):
        if str(new_car_type).capitalize() not in Taxi.carTypes.keys():
            print(f"You should choose the carType type from the list: {Taxi.carTypes}")
        else:
            self.__carType = new_car_type.capitalize()
            self.__cost = Taxi.carTypes[self.__carType]

    def set_address(self, new_address):
        self.__address = new_address

    def __str__(self):
        return f"Client: {self.__client}, car type: {self.__carType}, address: {self.__address}, cost: {self.__cost}"

    def add_taxi(self):
        while True:
            try:
                self.__client = input("Enter the client name: ").capitalize()
                if len(self.__client) == 0:
                    raise ValueError(f"The number of symbols for client name should be bigger than 0")
                else:
                    break
            except ValueError as e:
                print("Message: ", e)

        while True:
            try:
                self.__carType = input("Enter the car type: ").capitalize()
                if self.__carType not in Taxi.carTypes.keys():
                    raise ValueError(f"Choose car type from the existing values {Taxi.carTypes.keys()}")
                else:
                    break
            except ValueError as e:
                print("Message: ", e)
        while True:
            try:
                self.__address = input("Enter the client address: ")
                if len(self.__address) == 0:
                    raise ValueError(f"The number of symbols for client address should be bigger than 0")
                else:
                    break
            except ValueError as e:
                print("Message: ", e)
        self.__cost = Taxi.carTypes[self.__carType]

    def __del__(self):
        print("Taxi deleted!")
        del self


taxi = Taxi()
print(taxi)
taxi.add_taxi()

print(f"{taxi.get_client()=}")
print(f"{taxi.get_car_type()=}")
print(f"{taxi.get_address()=}")
print(f"{taxi.get_cost()=}")

taxi.set_car_type("Standard")
print(taxi)

taxi.set_address("New address")
print(taxi)

del taxi
