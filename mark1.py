# Using button events to operate LEDs and examine threads
# originally "flash_led_with_button.py" from MGB 1/11/21
# This version Peter Normington 2021-11-01

from gpiozero import LED, Button
from signal import pause
import sys
import threading
import pprint

red = LED(16)
grn = LED(20)
yel = LED(21)

btn_ops = Button(19)
btn_stop = Button(26)

pp = pprint.PrettyPrinter(indent=2)

def flash(btn,t_on,t_off,howmany):
    btn.blink(on_time=t_on, off_time=t_off, n=howmany,background=True)

def pressed():
    print("Pressed")
    flash(grn,1,0.5,3)

def released():
    print("Released")
    flash(red,0.5,1,3)

def stop_running():
    print("STOP pressed!")
    print("Number of threads active: ",threading.active_count())
    print("Threads: ")
    pp.pprint(threading.enumerate())
    btn_ops.close()
    sys.exit()

try:
    #while True:
    btn_ops.when_pressed = pressed
    btn_ops.when_released = released
    btn_stop.when_pressed = stop_running
    pause()
except KeyboardInterrupt:
    print("...")
    print("Number of threads active: ",threading.active_count())
    print("Threads: ")
    pp.pprint(threading.enumerate())
    print("Closing the ops button")
    btn_ops.close()
    print("Number of threads active: ",threading.active_count())
    print("Threads: ")
    pp.pprint(threading.enumerate())
    print("Ending program run")
    sys.exit()