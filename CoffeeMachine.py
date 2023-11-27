import Recipe
    
class CoffeeMachine:
    """Coffee Machine like the ones in Metaforum"""

    def __init__(self, catalogue):
        self.catalogue = catalogue

    def start(self):
        print ("Welcome to the coffee machine vendor")
        self.readCatalogue()
        return 

    def readCatalogue(self):
        for r in self.catalogue:
            r.toString()

    def prepareOrder(self, order):
        return

    def initiatePayment(self, order):
        return


def main():
    coffeeMachine = CoffeeMachine([])
    coffeeMachine.start()
    print("Thank you. Bye!")

if __name__ == "__main__":
    main()
