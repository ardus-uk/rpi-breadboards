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
    sys.exit()

white_btn = Button(16)
black_btn = Button(20)
exit_btn = Button(20, hold_time=3)
#red_btn = Button(21)

try:
    while True:
        white_btn.when_pressed = actionw
        black_btn.when_pressed = actionb
        exit_btn.when_held = stop_running
        #white_btn.when_released = action2
except KeyboardInterrupt:
    print("\nEnding program run\n")
  