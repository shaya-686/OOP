class Device:
    def __init__(self, name, brand, model, power, weight):
        self._name = name
        self._brand = brand
        self._model = model
        if power <= 0:
            raise ValueError("Weight should be bigger than 0")
        else:
            self._power = power
        if weight <= 0:
            raise ValueError("Weight should be bigger than 0")
        else:
            self._weight = weight

    def get_name(self):
        return self._name

    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def get_power(self):
        return self._power

    def get_weight(self):
        return self._weight

    def set_name(self, name):
        self._name = name

    def set_brand(self, brand):
        self._brand = brand

    def set_model(self, model):
        self._model = model

    def set_power(self, power):
        if power <= 0:
            raise ValueError("Weight should be bigger than 0")
        else:
            self._power = power

    def set_weight(self, weight):
        if weight <= 0:
            raise ValueError("Weight should be bigger than 0")
        else:
            self._weight = weight

    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Brand: {self._brand}")
        print(f"Model: {self._model}")
        print(f"Power: {self._power}")
        print(f"Weight: {self._weight}")


class CoffeeMachine(Device):
    _coffee_types = ["grains", "ground"]

    def __init__(self, name, brand, model, power, weight, coffee_type, water_tank):
        super().__init__(name, brand, model, power, weight)
        if coffee_type in self._coffee_types:
            self._coffee_type = coffee_type
        else:
            raise ValueError(f"Coffee type should be from the list {self._coffee_types}")
        self._water_tank = water_tank

    def get_coffee_type(self):
        return self._coffee_type

    def get_water_tank(self):
        return self._water_tank

    def set_coffee_type(self, coffee_type):
        self._coffee_type = coffee_type

    def set_water_tank(self, water_tank):
        self._water_tank = water_tank

    def display_info(self):
        print("Coffe machine information:")
        super().display_info()
        print(f"Additional characteristics: coffee type - {self._coffee_type}, water tank volume - {self._water_tank}")


try:
    coffee_machine = CoffeeMachine("Kava S30 2.0", "Phillips", "S30", 100, 5, "grains", "2.0")
    coffee_machine.display_info()
    coffee_machine.set_weight(5.3)
    coffee_machine.set_power(100)
except TypeError as e:
    print("Message: ", e)
except ValueError as e:
    print("Message: ", e)
except Exception as e:
    print("Message: ", e)


class Blender(Device):
    def __init__(self, name, brand, model, power, weight, bowl, speeds_number):
        super().__init__(name, brand, model, power, weight)
        if type(bowl) is bool:
            self._bowl = bowl
        else:
            raise TypeError("Possible values for bowl: True, False")
        if type(speeds_number) is int and speeds_number > 0:
            self._speeds_number = speeds_number
        else:
            raise ValueError("Number of speed should be integer and bigger than 0")

    def get_bowl(self):
        return self._bowl

    def get_speeds_number(self):
        return self._speeds_number

    def set_bowl(self, bowl):
        if type(bowl) is bool:
            self._bowl = bowl
        else:
            raise TypeError(f"Possible values for bowl: True, False")

    def set_speeds_number(self, speeds_number):
        self._speeds_number = speeds_number

    def display_info(self):
        print("Blender information:")
        super().display_info()
        print(f"Additional characteristics: bowl included - {self._bowl}, number of speeds - {self._speeds_number}")


try:
    blender = Blender("Blender S30 2.0", "Panasonic", "S30", 220, 1, True, 12)
    blender.display_info()
    blender.set_speeds_number(10)
    blender.set_bowl(False)
except TypeError as e:
    print("Message: ", e)
except ValueError as e:
    print("Message: ", e)
except Exception as e:
    print("Message: ", e)


class MeatGrinder(Device):
    _grinder_types = ["mechanical", "electric"]

    def __init__(self, name, brand, model, power, weight, grinder_type, nozzles_number):
        super().__init__(name, brand, model, power, weight)
        if grinder_type in self._grinder_types:
            self._grinder_type = grinder_type
        else:
            raise TypeError(f"Possible grinder type values: {self._grinder_types}")
        if type(nozzles_number) is int and nozzles_number >= 0:
            self._nozzles_number = nozzles_number
        else:
            raise ValueError("Number of nozzles should be integer and bigger or equal to 0")

    def get_grinder_type(self):
        return self._grinder_type

    def get_nozzles_number(self):
        return self._nozzles_number

    def set_grinder_type(self, grinder_type):
        if grinder_type in self._grinder_types:
            self._grinder_type = grinder_type
        else:
            raise TypeError(f"Possible grinder type values: {self._grinder_types}")

    def set_nozzles_number(self, nozzles_number):
        if type(nozzles_number) is int and nozzles_number >= 0:
            self._nozzles_number = nozzles_number
        else:
            raise ValueError("Number of nozzles should be integer and bigger or equal to 0")

    def display_info(self):
        print("Grinder information:")
        super().display_info()
        print(f"Additional characteristics: grinder type - {self._grinder_type}, number of nozzles - {self._nozzles_number}")


try:
    grinder = MeatGrinder("Grinder S30 2.0", "Panasonic", "S30", 220, 10, "electric", 12)
    grinder.display_info()
    grinder.set_nozzles_number(10)
    grinder.set_grinder_type("mechanical")
except TypeError as e:
    print("Message: ", e)
except ValueError as e:
    print("Message: ", e)
except Exception as e:
    print("Message: ", e)

