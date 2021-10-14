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

white_btn = Button(16, bounce_time=0.05)
black_btn = Button(20, bounce_time=0.05)
red_btn = Button(21)


try:
    while True:
        white_btn.when_pressed = actionw
        black_btn.when_pressed = actionb
        red_btn.when_pressed = stop_running
        #white_btn.when_released = action2
except KeyboardInterrupt:
    print("\nEnding program run\n")
  