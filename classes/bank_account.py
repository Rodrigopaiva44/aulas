class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance}")

# Main program


def main():
    print("Welcome to the Simple Bank Account System!")

    account1 = BankAccount("123456", "Alice")
    account2 = BankAccount("789012", "Bob", 1000)

    account1.deposit(500)
    account2.withdraw(300)
    account1.check_balance()
    account2.check_balance()


if __name__ == "__main__":
    main()
