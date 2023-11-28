from recipe import Recipe
from order import Order
import PySimpleGUI as sg 

    
class CoffeeMachine:
    """Coffee Machine like the ones in Metaforum"""
    init_state = 0
    wait_state = 1
    confirm_state = 2
    prepare_state = 3
    deliver_state = 4
    exit_state = -1

    def __init__(self, catalogue):
        self.catalogue = catalogue
        self.state = self.init_state

    def init_sell(self):
        self.order = None
        self.selection_valid = False
        self.state = self.wait_state
    
    def start_screen(self):
        ### Create welcoming GUI
        sg.theme('Purple')
        layout = [ [sg.Text("Welcome to the coffe vending machine at Metaforum, floor 6")],
                  [sg.Text("Here are the available options for your coffe: ")]
        ]
        for o in self.catalogue.values():
            layout.append([sg.Text(o)])
            
        layout.append([sg.Text("Enter something on Row 2"), sg.InputText()])
        layout.append([sg.Button("Order"), sg.Button("Exit")])

        startWindow = sg.Window("MetaCoffee", layout)
        
        ### Manage GUI interactions
        while self.state == self.wait_state: 
            event, values = startWindow.read()
            if event == "Exit":
                startWindow.close()
                self.state = self.exit_state
                break
            if event == sg.WIN_CLOSED:
                self.state = self.exit_state
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
            self.state = self.confirm_state
        if not self.selection_valid:
            sg.popup("Your selection was not valid, please enter the name of one of our offers.")


    def confirm_and_pay_order(self):
        layout = [[sg.T("This is your order: " + self.order.to_string() + ". Please, proceed to payment now.")],
                  [sg.Button("Pay"), sg.Button("Cancel")]
        ]
        payWindow = sg.Window("Payment protocol", layout,modal=True)
        while self.state == self.confirm_state:
            events, values = payWindow.read()
            if events == "Pay":
                self.pay_order()
                self.state = self.prepare_state
            else:
                self.state = self.wait_state
        if not payWindow.is_closed():
            payWindow.close()
            
        return
    
    def pay_order(self):
        self.order.is_paid(True)
        
    def prepare_order(self):
        self.state = self.deliver_state
        
    def deliver_coffee(self):
        sg.popup("Here is your coffee. Thank you for using our services.")
        self.state = self.init_state
        
    def sell_coffee(self):
        while self.state != self.exit_state:
            match self.state:
                case self.init_state:
                    self.init_sell()
                case self.wait_state:
                    self.start_screen()
                case self.confirm_state:
                    self.confirm_and_pay_order()
                case self.prepare_state:
                    self.prepare_order()
                case self.deliver_state:
                    self.deliver_coffee()


def main():
    catalogue = createCatalogue()
    coffeeMachine = CoffeeMachine(catalogue)
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
