from bank import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bank_account = BankAccount(int_rate=0.02, balance=0)


    def make_deposit(self, amount):	
        self.bank_account.deposit(amount)	

    def make_withdrawal(self, amount):
        self.bank_account.withdraw(amount)
       

    def display_user_balance(self):
            return(f"User: {self.name}, Balance: {self.bank_account.balance}")

    def transfer_money(self, other_user, amount):
        if self.bank_account.balance >= amount:
            self.bank_account.withdraw(amount)
            other_user.bank_account.deposit(amount)
            print(f"{self.name} transferred {amount} to {other_user.name}")
        else:
            print("Insufficient funds")


Glen = User("Glen Caku", 5000)
Rashford = User("Marcus Rashford", 1000)
Sancho = User("Jadon Sancho", 500)

Glen.make_deposit(1000)
Glen.make_deposit(1500)
Glen.make_deposit(2000)
Glen.make_withdrawal(500)

print(Glen.display_user_balance())



Rashford.make_deposit(500)
Rashford.make_deposit(1000)
Rashford.make_withdrawal(200)
Rashford.make_withdrawal(600)

print(Rashford.display_user_balance())

Sancho.make_deposit(1000)
Sancho.make_withdrawal(200)
Sancho.make_withdrawal(300)
Sancho.make_withdrawal(400)

print(Sancho.display_user_balance())

Glen.transfer_money(Sancho, 250)

print(Glen.display_user_balance())
print(Sancho.display_user_balance())