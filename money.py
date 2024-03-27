class Money:
    _currencies = {"Dollar": 100, "Euro": 100, "KWD": 1000, "BHD": 1000}  # currency and number of subunits in main unit

    def __init__(self, currency, main_unit, subunit):
        if currency in self._currencies:
            self._currency = currency
        else:
            raise ValueError("Unknown currency")
        if type(main_unit) is int and type(subunit) is int:
            if main_unit < 0 or subunit < 0:
                raise ValueError("Value should be bigger than 0")
            else:
                self._main_unit = main_unit  # example: Dollar, Euro
                self._subunit = subunit  # example: Cent, Euro cent
        else:
            raise TypeError("Values should be int")

    def get_main_unit(self):
        return self._main_unit

    def get_subunit(self):
        return self._subunit

    def set_main_unit(self, main_unit):
        if main_unit >= 0:
            self._main_unit = main_unit
        else:
            raise ValueError("Main unit value should be bigger than 0")

    def set_subunit(self, subunit):
        if subunit >= 0:
            self._subunit = subunit
        else:
            raise ValueError("Subunit value should be bigger than 0")

    def set_unit(self, amount):
        self._main_unit = amount // self._currencies[self._currency]
        self._subunit = amount % self._currencies[self._currency]

    def subunit_amount(self):
        return self._subunit + self._main_unit * self._currencies[self._currency]

    def main_unit_amount(self):
        return self._main_unit + self._subunit / self._currencies[self._currency]

    def display_amount(self):
        print(f"Money convert to subunits: {self.subunit_amount()}")
        print(f"Money convert to main units: {self.main_unit_amount()}")
        print(f"Main unit int - {self._main_unit}, subunit - {self._subunit}")


class Product:
    def __init__(self, name, price: Money):
        self._name = name
        self._price = price

    def decrease_price(self, delta: Money):
        new_price = self._price.subunit_amount() - delta.subunit_amount()
        self._price.set_unit(new_price)

    def display_product(self):
        print(f"Product name: {self._name}")
        self._price.display_amount()


try:
    product_price = Product("first_product", Money("Dollar", 10, 1025))
    price_change = Money("Dollar", 2, 12)
    product_price.decrease_price(price_change)
    product_price.display_product()
except TypeError as e:
    print("Message: ", e)
except ValueError as e:
    print("Message: ", e)
except Exception as e:
    print("Message: ", e)
