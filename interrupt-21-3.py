#!/usr/bin/python3
# interrupt-21-3.py
# Peter Normington
# 2021-10-12

# Object-oriented version of interrupt script

from gpiozero import Button 
#import RPi.GPIO as GPIO  

def action1():
    print("Hello, world!\n")
  
def action2():
    print("Goodbye, universe!\n")


btn = Button(16)

try:
    while True:
        btn.when_pressed = action1
        btn.when_released = action2
except KeyboardInterrupt:
    print("\nEnding program run\n")
  