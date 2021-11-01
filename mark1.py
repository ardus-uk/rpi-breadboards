# Using different button events to flash different LEDs
# originally "flash_led_with_button.py"
# MGB 1/11/21
#
# C&C Buttons
#

#grn.blink(on_time=my_on_time, off_time=my_off_time, n=my_flashes,background=True)

from gpiozero import LED
from gpiozero import Button
from signal import pause

red = LED(16)
yel = LED(20)
grn = LED(21)

def flash(btn,t_on,t_off,howmany):
    btn.blink(on_time=t_on, off_time=t_off, n=howmany,background=True)

def say_hello():
    print("Hello!")
    flash(green,1,0.5,3)

def say_goodbye():
    print("Goodbye!")
    flash(red,0.5,1,3)

button = Button(26)

button.when_pressed = say_hello
button.when_released = say_goodbye
#button.when_held = flash_green

pause()    # This keep the main thread running
button.close() 