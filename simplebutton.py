#!/usr/bin/python3
import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
ButtonPin=17
GPIO.setup(ButtonPin, GPIO.IN)
print(GPIO.input(ButtonPin))
try:
    while True:            
        if GPIO.input(ButtonPin)==False:
            print("Button Pressed")
            print(GPIO.input(ButtonPin))
            time.sleep(1)
        else:
            os.system('clear')
            print("Waiting for a button press...Ctrl C to end")
            print(GPIO.input(ButtonPin))   
        time.sleep(0.5)
except (KeyboardInterrupt):
    print("\nTest stopped")
