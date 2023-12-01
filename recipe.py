

class Recipe:
    """An option in the coffee machine"""

    def __init__(self, name, price, co: [(str,range,int)] = []):
        self.name = name
        self.price = price
        self.custom_options = {}
        for (k,r,v) in co:
            self.custom_options[k] = (r,v)

    def to_string(self):
        return self.name + ": " + str(self.price) + "€"

    def get_price(self):
        return self.price