class Customer:
    def __init__(self, account):
        self.account = account

class Account:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self, customer):
        self.customer = customer

    def get_customer_balance(self):
        return self.customer.account.get_balance()

# Використання
bank = Bank(Customer(Account(500)))
balance = bank.get_customer_balance()
print(f"The balance is: {balance}")