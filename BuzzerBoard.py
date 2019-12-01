#!/usr/bin/python3

# Peter Normington
# 2019-12-01
                                                                                                                                                           
from gpiozero import Buzzer
from time import sleep          

class buzzerBoard:
    def __init__(self,pin_buzzer):

        self.pin_buzzer = pin_buzzer
        
        # buzzers are keyed by name
        self.buzzer = {}
        for name,pin in self.pin_buzzer.items():
            self.buzzer[name]=buzzer(pin)
    
    def test_buzzer(self,name):
        self.buzzer[name].on()
        time.sleep(1)
        self.buzzer[name].off()

    def test_all_buzzers(self):
        for name in self.pin_buzzer.keys():
            self.test_buzzer(name)

# Test the class
if __name__ == '__main__':
    print("buzzer test program")
    # Set up the board configuration
 
    peters_buzzer = {                                                                                                                                                                                                                                                                                                                                                                                                                                                             
            "Buzzer1":20,
        }
    petersboard = buzzerBoard(peters_buzzer)
    # Run the test
    print("Testing the buzzer...")
    petersboard.test_buzzer("Buzzer1")
    print("All done!")
