#!/usr/bin/python3
# interrupt-21-3.py
# Peter Normington
# 2021-10-12

# Object-oriented version of interrupt script

from gpiozero import Button 
from subprocess import check_call
from signal import pause
import sys

def actionw():
    print("Hello, white!\n")
  
def actionb():
    print("Hello, black!\n")

def stop_running():
    print("STOP (Red) pressed!\n")
    sys.exit()

<<<<<<< HEAD
white_btn = Button(16, bounce_time=0.05)
black_btn = Button(20, bounce_time=0.05)
red_btn = Button(21, hold_time = 2)
=======
white_btn = Button(16, bounce_time=0.5)
#black_btn = Button(20)
exit_btn = Button(20)
#red_btn = Button(21)
>>>>>>> d085d09e87adbbe5c7cd42fd13f65c71d5288b9f

try:
    while True:
        white_btn.when_pressed = actionw
        black_btn.when_pressed = actionb
        red_btn.when_held = stop_running
        #white_btn.when_released = action2
except KeyboardInterrupt:
    print("\nEnding program run\n")
  