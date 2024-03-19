class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        """
        Add some amount on balance
        :param amount: (int, float) - addition amount of money
        :return: None
        """
        self.__balance += amount

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
        else:
            print("Not enough balance")


account = BankAccount(100)
print(account.get_balance())

account.deposit(55)
print(account.get_balance())

account.withdraw(60)
print(account.get_balance())

account.withdraw(200)
print(account.get_balance())

account.__balance


