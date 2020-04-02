#!/usr/bin/python3
# interrupt-OO-3.py
# Peter Normington
# 2020-04-02

# Object-oriented version of interrupt script

from gpiozero import Button 

def action1():
    print("Hello, world!\n")
  
def action2():
    print("Goodbye, universe!\n")


btn = Button(17)
btn.when_pressed = action1
btn.when_released = action2