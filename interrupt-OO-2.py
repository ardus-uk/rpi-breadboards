#!/usr/bin/python3
# interrupt-OO.py
# Peter Normington
# 2020-04-02

# Object-oriented version of interrupt script
# With grateful acknowledgement to 
# https://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3

import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)

class UpInput:

# Set up as inputs, pulled up to avoid false detection.  
# Wired to connect to GND on button press, 
# so detect falling edge on each.

    def __init__(self, pin_button, action_function):
        self.pin_button = pin_button
        self.action_function = action_function
        GPIO.setup(self.pin_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # threaded callback functions will run in another thread when events are detected 
    def call_back(self,channel):
        print ("\nFalling edge detected on " + str(self.pin_button))
        print ("Channel = " + str(channel))
        self.action_function()

    def add_event_detector(self, bounce_time):
        GPIO.add_event_detect(self.pin_button, GPIO.FALLING, callback=self.call_back, bouncetime=bounce_time) 

class DownInput:

# Set up as inputs, pulled down initially.  
# Wired to connect to 3V3 on button press, 
# so detect rising edge.

    def __init__(self, pin_button):
        self.pin_button = pin_button
        GPIO.setup(self.pin_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def edge_waiter(self):
        GPIO.wait_for_edge(self.pin_button, GPIO.RISING) 

# Test the class
if __name__ == '__main__':

    def action1():
        print("Hello, world!\n")
  
    def action2():
        print("Hello, universe!\n")

    print ("INSTRUCTIONS")
    print ("------------\n")
    print ("Make sure you have a button connected so that when pressed")
    print ("it will connect GPIO port 23 (pin 16) to GND (pin 6)\n")
    print ("You will also need a second button connected so that when pressed") 
    print ("it will connect GPIO port 17 (pin 11) to GND (pin 14)\n")
    print ("Finally, you will need a third button connected so that when pressed")     
    print ("it will connect GPIO port 24 (pin 18) to 3V3 (pin 1)\n") 
    input("Press Enter when ready\n>")  

    red = DownInput(24)  
    
    black = UpInput(17, action1)
    white = UpInput(23, action2)
    black.add_event_detector(300)
    white.add_event_detector(300)
    
    try:  
        print ("\nWaiting for rising edge on port 24")  
        red.edge_waiter()  
        print ("\nRising edge detected on port 24\n\n--- END OF PROGRAM ---\n.")   
    except KeyboardInterrupt:
        # clean up GPIO on CTRL+C exit
        GPIO.cleanup()
    # clean up GPIO on normal exit
    GPIO.cleanup()             