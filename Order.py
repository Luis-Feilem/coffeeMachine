class Order:
    """A recipe that has to be prepared and paid for."""

    def __init__(self, recipe):
        self.recipe = recipe
        self.paid = False

    def isPaid(self, *arg):
        if len(arg)>0:
            self.paid = arg[0]
        return self.paid