class BankAccount:
    def __init__(self, id, balance): # accountnumber = id
        self.id = id
        self.balance = balance

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,id):
        self._id = id

        raise AttributeError("Invalid id")

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        self._balance = balance

    def deposit(self, x):
        saldo = self.balance + x
        self.balance = saldo
        return saldo

    def withdraw(self, x):
        saldo = self.balance - x
        self.balance = saldo
        return saldo

    def __str__(self):
        return f'Account: {self.id}\nBalance: {self.balance}'

client_1 = BankAccount(444,500)
client_2 = BankAccount(321,400)

print(client_1,"\n")
print(client_2,"\n")

print('')
'''
client_1.deposit(15)
print(client_1)
print("")
client_2.withdraw(30)
print(client_2)
'''

print('tentando mudar o id e saldo')
client_1.id = 222
client_1.balance = 10000
print(client_1)