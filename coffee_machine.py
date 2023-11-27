from recipe import Recipe
from order import Order
import PySimpleGUI as sg 

    
class CoffeeMachine:
    """Coffee Machine like the ones in Metaforum"""

    def __init__(self, catalogue):
        self.catalogue = catalogue
        self.terminated = False

    def init_sale(self):
        self.order = None
        self.selection_valid = False
    
    def start_screen(self):
        self.init_sale()
        ### Create welcoming GUI
        sg.theme('Purple')
        layout = [ [sg.Text("Welcome to the coffe vending machine at Metaforum, floor 6")],
                  [sg.Text("Here are the available options for your coffe: ")]
        ]
        for o in self.catalogue.values():
            layout.append([sg.Text(o)])
            
        layout.append([sg.Text("Enter something on Row 2"), sg.InputText()])
        layout.append([sg.Button("Order"), sg.Button("Exit")])

        startWindow = sg.Window("MetaCoffee", layout, disable_close=True)
        
        ### Manage GUI interactions
        while not self.selection_valid: 
            event, values = startWindow.read()
            if event == "Exit":
                startWindow.close()
                self.terminated = True
                break
            if event == "Order":
                self.select_order(values[0])
        startWindow.close()
        

    def read_catalogue(self):
        for r in self.catalogue.values():
            print(r)

    def select_order(self, selection):
        if selection in self.catalogue.keys():
            self.order = Order(self.catalogue[selection])
            self.selection_valid = True
        if not self.selection_valid:
            sg.popup("Your selection was not valid, please enter the name of one of our offers.")


    def prepare_order(self):
        if self.terminated:
            return
        layout = [[sg.T("This is your order: " + self.order.to_string() + ". Please, proceed to payment now.")],
                  [sg.Button("Pay"), sg.Button("Cancel")]
        ]
        payWindow = sg.Window("Payment protocol", layout, disable_close=True, modal=True)
        while True:
            events, values = payWindow.read()
            if events == "Pay":
                self.pay_order()
            break
        if not payWindow.is_closed():
            payWindow.close()
            
        return
    
    def pay_order(self):
        self.order.is_paid(True)
        
    def exit_screen(self):
        if self.terminated:
            return
        if self.order.is_paid():
            sg.popup("Do not forget your coffe. Until next time!")
        
    def sell_coffee(self):
        self.start_screen()
        self.prepare_order()
        self.exit_screen()


def main():
    catalogue = createCatalogue()
    coffeeMachine = CoffeeMachine(catalogue)
    while not coffeeMachine.terminated:
        coffeeMachine.sell_coffee()

def createCatalogue():
    catalogue = dict()
    offers = []
    offers.append(Recipe("Capuccino", 0.65))
    offers.append(Recipe("Hot chocolate", 0.50))
    for r in offers:
        catalogue[r.name] = r.to_string()
    return catalogue
    

if __name__ == "__main__":
    main()
