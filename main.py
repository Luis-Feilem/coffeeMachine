from coffee_machine import CoffeeMachine
from recipe import Recipe

def main():
    catalogue = createCatalogue()
    coffeeMachine = CoffeeMachine(catalogue)
    coffeeMachine.sell_coffee()

def createCatalogue():
    co_strength = ("Coffee",(1,5), 3)
    co_milk = ("Milk", (0,5), 0)
    co_sugar = ("Sugar", (0,5), 0)
    catalogue = []
    catalogue.append(Recipe("Capuccino", 0.65, [co_strength, co_milk, co_sugar]))
    catalogue.append(Recipe("Hot chocolate", 0.50, [co_milk, co_sugar]))
    catalogue.append(Recipe("Hot water for tea", 0.25))
    return catalogue

if __name__ == "__main__":
    main()