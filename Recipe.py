

class Recipe:
    """An option in the coffee machine"""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def toString(self):
        print(self.name & ": " & str(self.price))

    