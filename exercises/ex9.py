class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

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
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            new_account = BankAccount(account_number, initial_balance)
            self.accounts[account_number] = new_account
            print(f"Account {account_number} created.")
        else:
            print("Account already exists.")

    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            sender = self.accounts[from_account]
            receiver = self.accounts[to_account]
            if sender.get_balance() >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print("Transfer successful.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Invalid account numbers.")

    def calculate_total_balance(self):
        total_balance = sum(account.get_balance()
                            for account in self.accounts.values())
        return total_balance


# Test the Bank class
bank = Bank()

bank.create_account("12345", 1000)
bank.create_account("67890", 500)

bank.transfer("12345", "67890", 200)

print("Total bank balance:", bank.calculate_total_balance())
