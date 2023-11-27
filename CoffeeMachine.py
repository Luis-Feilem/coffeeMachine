from Recipe import Recipe
from Order import Order
    
class CoffeeMachine:
    """Coffee Machine like the ones in Metaforum"""

    def __init__(self, catalogue):
        self.catalogue = catalogue
        self.order = None

    def start(self):
        print("Welcome to the coffee machine vendor")
        self.readCatalogue()
        self.order = self.selectOrder()
        self.prepareOrder()
        print("Thank you for using our services. See you soon!")

    def readCatalogue(self):
        for r in self.catalogue.values():
            print(r)

    def selectOrder(self):
        valid = False
        while not valid:
            selection = input("Please, enter your selection\n")
            if selection in self.catalogue.keys():
                order = Order(self.catalogue[selection])
                valid = True
        return order


    def prepareOrder(self):
        print("Your order will now be prepared.")
        if not self.order.isPaid():
            print("Please, proceed to payment.")
            self.payOrder()
        print("Payment received. Here is your order.")
        return
    
    def payOrder(self):
        self.order.isPaid(True)
        


def main():
    catalogue = createCatalogue()
    coffeeMachine = CoffeeMachine(catalogue)
    coffeeMachine.start()

def createCatalogue():
    catalogue = dict()
    offers = []
    offers.append(Recipe("Capuccino", 0.65))
    offers.append(Recipe("Hot chocolate", 0.50))
    for r in offers:
        catalogue[r.name] = r.toString()
    return catalogue
    

if __name__ == "__main__":
    main()
