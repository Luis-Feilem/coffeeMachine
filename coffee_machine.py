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
                  [sg.Text("This is our menu today: ")]
        ]
        for k,v in self.catalogue.items():
            layout.append([sg.Button(k),sg.Text(v.price)])
            
        layout.append([sg.Button("Exit")])

        startWindow = sg.Window("MetaCoffee", layout)
        
        ### Manage GUI interactions
        out_state = self.wait_state
        while out_state == self.wait_state: 
            event, values = startWindow.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                out_state = self.exit_state
            else:
                out_state = self.select_order(event)
        startWindow.close()
        return out_state

    def read_order(self):
        return self.order.to_string()

    def select_order(self, selection):
        if selection in self.catalogue.keys():
            self.order = Order(self.catalogue[selection])
            if self.order.is_customizable():
                return self.customize_order()
            else:
                return self.confirm_state
        else:
            sg.popup("Your selection was not valid, please enter the name of one of our offers.")
            return self.wait_state

    def customize_order(self):
        # TODO
        layout = []
        for k,v in self.order.recipe.custom_options.items():
            layout.append([sg.Text("Select how much " + k + " you would like ?"), sg.Slider(self.order.recipe.custom_options[k][0],self.order.recipe.custom_options[k][1], 
                                                                                            key=k, resolution=1, tick_interval=1, orientation="horizontal")])
        layout.append([sg.Button("Confirm"), sg.Button("Cancel")])
        
        customWindow = sg.Window("Customize values", layout,modal=True)
        out_state = self.wait_state
        while out_state == self.wait_state:
            event, values = customWindow.read()
            if event == "Cancel" or event == sg.WIN_CLOSED:
                break
            if event == "Confirm":
                for k in self.order.recipe.custom_options.keys():
                    self.order.customize_option(k, values[k])
                out_state = self.confirm_state
        customWindow.close()
        del values, customWindow
        return out_state

    def confirm_and_pay_order(self):
        layout = [[sg.T("You ordered: " + self.read_order() + ". Please, proceed to payment now.")],
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
        
    def deliver_order(self):
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
                    self.state = self.deliver_order()



