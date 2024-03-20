class Order:
    roomTypes = {"Economy": 100, "Standard": 200, "Vip": 300}
    minDays = 1
    maxDays = 14

    def __init__(self):
        self.__client = None
        self.__room = None
        self.__days = None
        self.__cost = None

    def get_client(self):
        return self.__client

    def get_room(self):
        return self.__room

    def get_days(self):
        return self.__days

    def get_cost(self):
        return self.__cost

    def set_room(self, new_room):
        if str(new_room).capitalize() not in Order.roomTypes.keys():
            print(f"You should choose the room type from the list: {Order.roomTypes}")
        else:
            self.__room = new_room.capitalize()
            self.__cost = self.calculate_cost()

    def set_days(self, new_days):
        if new_days in range(Order.minDays, Order.maxDays + 1):
            self.__days = new_days
            self.__cost = self.calculate_cost()
        else:
            print("Choose the correct days number from 1 to 14")

    def __str__(self):
        return f"Client: {self.__client}, room type: {self.__room}, days: {self.__days}, cost: {self.__cost}"

    def add_order(self):
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
                self.__room = input("Enter the room type: ").capitalize()
                if self.__room not in Order.roomTypes.keys():
                    raise ValueError(f"Choose room type from the existing values {Order.roomTypes.keys()}")
                else:
                    break
            except ValueError as e:
                print("Message: ", e)
        while True:
            try:
                self.__days = int(input("Enter the number of days: "))
                if self.__days not in range(Order.minDays, Order.maxDays + 1):
                    raise ValueError(f"Choose the correct number of days from {Order.minDays} to {Order.maxDays}")
                else:
                    break
            except ValueError as e:
                print("Message: ", e)
        self.__cost = self.calculate_cost()

    def calculate_cost(self):
        return Order.roomTypes[self.__room] * self.__days

    def __del__(self):
        print("Order deleted!")
        del self


order = Order()
print(order)
order.add_order()

print(f"{order.get_client()=}")
print(f"{order.get_room()=}")
print(f"{order.get_days()=}")
print(f"{order.get_cost()=}")

order.set_room("Standard")
print(order)

order.set_days(7)
print(order)

del order


