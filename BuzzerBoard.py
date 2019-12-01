#!/usr/bin/python3

# Peter Normington
# 2019-12-01
                                                                                                                                                           
from gpiozero import Buzzer
from time import sleep          

class BuzzerBoard:
    def __init__(self,pin_buzzer):

        self.pin_buzzer = pin_buzzer
        
        # buzzers are keyed by name
        self.buzzer = {}
        for name,pin in self.pin_buzzer.items():
            self.buzzer[name]=Buzzer(pin)
    
    def test_buzzer(self,name):
        self.buzzer[name].on()
        sleep(1)
        self.buzzer[name].off()

    def test_all_buzzers(self):
        for name in self.buzzer.keys():
            self.test_buzzer(name)

# Test the class
if __name__ == '__main__':
    print("Buzzer test program")
    # Set up the board configuration
 
    peters_pin_buzzer = {                                                                                                                                                                                                                                                                                                                                                                                                                                                             
            "Buzzer1":20,
        }

    petersboard = BuzzerBoard(peters_pin_buzzer)
    # Run the test
    print("Testing the buzzer...")
    petersboard.test_buzzer("Buzzer1")
    print("All done!")
