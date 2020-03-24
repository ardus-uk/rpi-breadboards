#!/usr/bin/python3

# Peter Normington
# 2019-10-11
                                                                                                                                                           
from gpiozero import Button
from time import sleep          

class ButtonBoard:
    def __init__(self,pin_button):

        self.pin_button = pin_button
        
        # Buttons are keyed by name
        self.button = {}
        for name,pin in self.pin_button.items():
            self.button[name]=Button(pin)
    
    def test_button(self,name):
        print(name,self.button[name].value)

    def test_all_buttons(self):
        for name in self.pin_button.keys():
            self.test_button(name)

# Test the class
if __name__ == '__main__':
    print("Button test program")
    # Set up the board configuration
 
    peters_pin_button = {                                                                                                                                                                                                                                                                                                                                                                                                                                                             
            "Master":27,
        }
    petersboard = ButtonBoard(peters_pin_button)
    # Run the tests
    print("Testing the button after one second")
    sleep(1)
    petersboard.test_button("Master")
    print("All done!")
