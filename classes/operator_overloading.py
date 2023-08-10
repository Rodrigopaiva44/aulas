class _Wallet:
    def __init__(self, btc=0, eth=0, matic=0):
        self.btc = btc
        self.eth = eth
        self.matic = matic

    def __str__(self):
        return f"{self.btc} BTC, {self.eth} ETH, {self.matic} MATIC"


vitin = _Wallet(1, 2, 3)
print(vitin)

rodrigo = _Wallet(3, 2, 1)
print(rodrigo)


btc = vitin.btc + rodrigo.btc
eth = vitin.eth + rodrigo.eth
matic = vitin.matic + rodrigo.matic

total = _Wallet(btc, eth, matic)
print(total)

# What if we try to sum the objects?
# print(vitin + rodrigo) A TypeError because python does not know how to sum


class Wallet:
    def __init__(self, btc=0, eth=0, matic=0):
        self.btc = btc
        self.eth = eth
        self.matic = matic

    def __str__(self):
        return f"{self.btc} BTC, {self.eth} ETH, {self.matic} MATIC"

    def __add__(self, other):
        btc = self.btc + other.btc
        eth = self.eth + other.eth
        matic = self.matic + other.matic
        return Wallet(btc, eth, matic)


vitin = Wallet(1, 2, 3)
rodrigo = Wallet(3, 2, 1)
total = vitin + rodrigo
print(total)
