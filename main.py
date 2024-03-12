# Створіть клас BankAccount з атрибутами balance
# та owner, а також методами deposit та withdraw для
# здійснення операцій з балансом. Реалізуйте перевірку
# на те, що баланс не може стати від'ємним.


class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"{self.owner}, balance is less then operation amount!")
        else:
            self.balance -= amount
            print(f"Balance: {self.balance}")


bankAccount1 = BankAccount(100, "Oleksandra")
bankAccount1.deposit(200)
bankAccount1.withdraw(50)
bankAccount1.withdraw(300)
