from recipe import Recipe

class Order:
    """A recipe that has to be prepared and paid for."""

    def __init__(self, recipe: Recipe):
        self.recipe = recipe
        self.paid = False

    def is_paid(self, *arg):
        if len(arg)>0:
            self.paid = arg[0]
        return self.paid
    
    def to_string(self):
        return self.recipe