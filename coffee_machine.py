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

    def __init__(self, catalogue: [Recipe]):
        self.catalogue = {}
        for r in catalogue:
            self.catalogue[r.name] = r
        self.state = self.init_state

    def init_sell(self):
        self.order = None
        return self.wait_state
    
    def start_screen(self):
        sg.theme('Purple')
        layout = [ [sg.Text("Welcome to the coffe vending machine at Metaforum, floor 6")],
                  [sg.Text("Here are the available options for your coffe: ")]
        ]
        for r in self.catalogue.values():
            layout.append([sg.Text(r.to_string())])
            
        layout.append([sg.Text("Enter the option you would like to have (case sensitive)"), sg.InputText()])
        layout.append([sg.Button("Order"), sg.Button("Exit")])

        startWindow = sg.Window("MetaCoffee", layout)
        
        ### Manage GUI interactions
        out_state = self.wait_state
        while out_state == self.wait_state: 
            event, values = startWindow.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                out_state = self.exit_state
            if event == "Order":
                out_state = self.select_order(values[0])
        startWindow.close()
        return out_state

    def read_recipe(r):
        return r.to_string()

    def select_order(self, selection):
        if selection in self.catalogue.keys():
            self.order = Order(self.catalogue[selection])
            if self.order.is_customizable():
                return self.customize_order()
            else:
                print("not customizable")
                return self.confirm_state
        else:
            sg.popup("Your selection was not valid, please enter the name of one of our offers.")
            return self.wait_state

    def customize_order(self):
        # TODO
        layout = []
        for co in self.order.recipe.custom_options:
            layout.append([sg.Text("Select how much " + co[0] + " you would like ("+ str(co[1])+ ")"), sg.InputText(co[2])])
        layout.append([sg.Button("Confirm"), sg.Button("Cancel")])
        
        customWindow = sg.Window("Customize values", layout,modal=True)
        out_state = self.wait_state
        while out_state == self.wait_state:
            event, values = customWindow.read()
            if event == "Cancel" or event == sg.WIN_CLOSED:
                break
            if event == "Confirm":
                out_state = self.confirm_state
        customWindow.close()
        return out_state

    def confirm_and_pay_order(self):
        layout = [[sg.T("This is your order: " + self.order.to_string() + ". Please, proceed to payment now.")],
                  [sg.Button("Pay"), sg.Button("Cancel")]
        ]
        
        payWindow = sg.Window("Payment protocol", layout,modal=True)
        out_state = self.confirm_state
        while out_state == self.confirm_state:
            events, values = payWindow.read()
            if events == "Pay":
                out_state = self.pay_order()
            else:
                out_state = self.wait_state
        if not payWindow.is_closed():
            payWindow.close()
        return out_state
    
    def pay_order(self):
        # TODO
        self.order.is_paid(True)
        return self.prepare_state
        
    def prepare_order(self):
        # TODO
        # Look at order custom options and prepare accordingly
        
        return self.deliver_state
        
    def deliver_coffee(self):
        # TODO?
        sg.popup("Here is your coffee. Thank you for using our services.")
        return self.init_state
        
    def sell_coffee(self):
        while self.state != self.exit_state:
            match self.state:
                case self.init_state:
                    self.state = self.init_sell()
                case self.wait_state:
                    self.state = self.start_screen()
                case self.confirm_state:
                    self.state = self.confirm_and_pay_order()
                case self.prepare_state:
                    self.state = self.prepare_order()
                case self.deliver_state:
                    self.state = self.deliver_coffee()



