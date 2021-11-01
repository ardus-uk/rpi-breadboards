from gpiozero import LED
from signal import pause

multicolour = LED(12)
multicolour.blink(on_time=3)

pause()
