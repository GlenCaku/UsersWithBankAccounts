class BankAccount:
    accounts = []

    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            print(f"Account balance: {account.balance}, Interest rate: {account.int_rate}")

account1 = BankAccount().deposit(100).deposit(200).deposit(300).withdraw(150).yield_interest()
account2 = BankAccount().deposit(500).deposit(1000).withdraw(200).withdraw(300).withdraw(400).withdraw(50).yield_interest()

BankAccount.print_all_accounts()
