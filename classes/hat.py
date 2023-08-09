import random


class Hat:
    def __init__(self):
        self.homes = ["Cabuçu", "Vila isabel", "Rio de Janeiro"]

    def sort(self, name):
        home = random.choice(self.homes)
        print(name, "is in", home)


hat = Hat()
# There is no other Hat just one. And that way we could create multiple objects
# hat_2 = Hat()
# hat_3 = Hat()
hat.sort("Vitin")

# Adding a new decorator called classmethods


class Hat:
    homes = ["Cabuçu", "Vila isabel", "Rio de Janeiro"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.homes))


Hat.sort("Vitin")
