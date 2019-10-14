#!/usr/bin/python3

# Peter Normington
# 2019-10-13

from LEDBoard import *

class TrafficLights:
    def __init__(self):
        # Set up the board configuration
        tl_pin_colour = {
            "Green":17,
            "Amber":18,
            "Red":19,
        }
        
        self.tlboard = LEDBoard(tl_pin_colour)

    def activate(self):
        self.tlboard.light_led("Red")
        sleep(4)
        self.tlboard.light_led("Amber")
        sleep(2)
        self.tlboard.extinguish_led("Red")
        self.tlboard.extinguish_led("Amber")
        self.tlboard.light_led("Green")
        sleep(4)
        self.tlboard.extinguish_led("Green")
        self.tlboard.light_led("Amber")
        sleep(2)
        self.tlboard.extinguish_led("Amber")


if __name__ == '__main__':
    tl = TrafficLights()
    # Run until stopped by keyboard interrupt (Ctrl+C)
    try:
        while True:            
            tl.activate()
    except (KeyboardInterrupt):
        print("\nTraffic lights stopped")

