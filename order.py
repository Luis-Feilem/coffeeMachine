from recipe import Recipe

class Order:
    """A recipe that has to be prepared and paid for."""

    def __init__(self, recipe: Recipe, custom_levels: dict[str, int] = {}):
        self.recipe = recipe
        self.paid = False
        self.custom_levels = custom_levels.copy() # otherwise we assign memory address and custom options get corrupted between orders

    def is_paid(self, *arg):
        if len(arg)>0:
            self.paid = arg[0]
        return self.paid
    
    def to_string(self):
        out = ""
        if not self.is_customizable():
            out = self.recipe.to_string()
        else:
            out += self.recipe.name + " ("
            for k,v in self.custom_levels.items():
                out += k + ": " + str(int(v)) + ", "
            out = out[:-2] + "): " + str(self.recipe.price) + "€"
        return out
    
    def is_customizable(self):
        return len(self.recipe.custom_options)!=0
    
    def customize_option(self, option, level):
        self.custom_levels[option] = level