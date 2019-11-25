#!/usr/bin/python3

# Peter Normington
# 2019-11-25

from LEDBoard import *

class SuperLEDBoard(LEDBoard):

    def __init__(self):
        # Set up the board configuration
        slb_pin_colour = {
            "White":13,
            "Orange":16,
            "Green":17,
            "Amber":18,
            "Red":19,
            "Blue":20,
            "Pink":23,
            "Rainbow":26,
        }
        LEDBoard.__init__(self,slb_pin_colour)
        
if __name__ == '__main__':
    peters_slb = SuperLEDBoard()
    # Run until stopped by keyboard interrupt (Ctrl+C)
    try:
        while True:            
            slb.test_all_leds(5,1)
    except (KeyboardInterrupt):
        print("\nTest stopped")

