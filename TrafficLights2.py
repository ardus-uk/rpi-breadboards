#!/usr/bin/python3

# Peter Normington
# 2019-10-13

from LEDBoard import *

class TrafficLights2(LEDBoard):
    pass

    def __init__(self):
        # Set up the board configuration
        tl_pin_colour = {
            "Green":17,
            "Amber":18,
            "Red":19,
        }
        LEDBoard.__init__(self,tl_pin_colour)
        
    def activate(self):
        self.light_led("Red")
        sleep(4)
        self.light_led("Amber")
        sleep(2)
        self.extinguish_led("Red")
        self.extinguish_led("Amber")
        self.light_led("Green")
        sleep(4)
        self.extinguish_led("Green")
        self.light_led("Amber")
        sleep(2)
        self.extinguish_led("Amber")


if __name__ == '__main__':
    tl = TrafficLights2()
    # Run until stopped by keyboard interrupt (Ctrl+C)
    try:
        while True:            
            tl.activate()
    except (KeyboardInterrupt):
        print("\nTraffic lights stopped")

