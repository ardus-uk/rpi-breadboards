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
#grn = LED(21)

def say_hello():
    print("Hello!")

def flash_red():
    say_hello()
    red.blink(on_time=1, off_time=0.5, n=3,background=True)

def say_goodbye():
    print("Goodbye!")
    flash_yel()

def flash_yel():
    yel.blink(on_time=0.5, off_time=1, n=3,background=True)

def flash_green():
    pass
    #replace pass with your code

button = Button(26)

button.when_pressed = flash_red
button.when_released = say_goodbye
button.when_held = flash_green

pause()    # This keep the main thread running
button.close() 