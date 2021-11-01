# Using button events to operate LEDs
# originally "flash_led_with_button.py" from MGB 1/11/21
#
# C&C Buttons
#

from gpiozero import LED, Button
from signal import pause
import sys
import threading

red = LED(16)
grn = LED(20)
yel = LED(21)

btn_ops = Button(19)
btn_stop = Button(26)

def flash(btn,t_on,t_off,howmany):
    btn.blink(on_time=t_on, off_time=t_off, n=howmany,background=True)

def pressed():
    print("Pressed")
    flash(grn,1,0.5,3)

def released():
    print("Released")
    flash(red,0.5,1,3)

def stop_running():
    print("STOP pressed!\n")
    btn_ops.close()
    sys.exit()

try:
    while True:
        btn_ops.when_pressed = pressed
        btn_ops.when_released = released
        btn_stop.when_pressed = stop_running()
except KeyboardInterrupt:
    print("Number of threads active: ",threading.active_count(),"\n")
    print("Ending program run\n")
    btn_ops.close()
    sys.exit()