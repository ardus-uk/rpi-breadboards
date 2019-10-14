#!/usr/bin/python3

# Peter Normington
# 2019-10-11
                                                                                                                                                           
from gpiozero import LED
from time import sleep          

class LEDBoard:
    def __init__(self,pin_colour):

        self.pin_colour = pin_colour

        # LEDs are keyed by colour
        self.led = {}
        for colour,pin in self.pin_colour.items():
            self.led[colour] = LED(pin)
  
    def light_led(self,colour):
        self.led[colour].on()
    
    def extinguish_led(self,colour):
        self.led[colour].off()
    
    def test_led(self,colour,duration):
        self.led[colour].on()
        sleep(duration)
        self.led[colour].off()

    def test_all_leds(self,duration,rest_interval):
        for colour in self.pin_colour.keys():
            print ("Colour: ",colour,"\nDuration: ", duration,"\nRest Interval:",rest_interval)
            self.test_led(colour,duration)
            sleep(rest_interval)

# Test the class
if __name__ == '__main__':
    print("LED test program")
    # Set up the board configuration
    peters_pin_colour = {
            "Green":17,
            "Yellow":18,
            "Red":19,
            "Blue":20,
        }
    petersboard = LEDBoard(peters_pin_colour)
    # Run the tests
    print("Testing the Green LED")
    petersboard.test_led("Green",3)
    sleep(3)
    print("Testing the Yellow LED")
    petersboard.test_led("Yellow",3)
    sleep(3)
    print("Testing the Red LED")
    petersboard.test_led("Red",3)
    sleep(3)
    print("Testing all LEDs by colour")
    petersboard.test_all_leds(2,1)
    print("All done!")
