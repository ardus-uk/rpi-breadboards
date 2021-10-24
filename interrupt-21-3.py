#!/usr/bin/python3
# interrupt-21-3.py
# Peter Normington
# 2021-10-12

# Object-oriented version of interrupt script

from gpiozero import Button 
from subprocess import check_call
from signal import pause
import sys
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
jcf = os.path.join(script_dir,"config.json")

pin = {}
pin['red'] = 26
pin['black'] = 19
pin['white'] = 13
pin['green'] = 6
pin['yellow'] = 5
pin['blue'] = 22
pin['grey'] = 27

btn = {}
for colour in pin.keys:
    btn[colour] = Button(pin[colour], bounce_time=0.05)


def actionw():
    with open(jcf) as json_cred_file:
        cred = json.load(json_cred_file)
    print("Hello,",cred['name'],"on White\n")
    if (cred['name']=="Ruth"): print("EXTRA\n")
  
def actionb():
    print("Hello, black!\n")
    data = {}
    data['name']="Peter"
    with open(jcf,'w') as json_cred_file:
        json.dump(data,json_cred_file)

def stop_running():
    print("STOP (Red) pressed!\n")
    sys.exit()

# red_btn = Button(26, bounce_time=0.05)
#black_btn = Button(19, bounce_time=0.05)
#white_btn = Button(13, bounce_time=0.05)
#green_btn = Button(6, bounce_time=0.05)
#yellow_btn = Button(5, bounce_time=0.05)
#blue_btn = Button(22, bounce_time=0.05)
#grey_btn = Button(27, bounce_time=0.05)

try:
    while True:
        btn['white'].when_pressed = actionw
        btn['black'].when_pressed = actionb
        btn['red'].when_pressed = stop_running
       # red_btn.when_pressed = stop_running
        #white_btn.when_released = action2
except KeyboardInterrupt:
    print("\nEnding program run\n")
  