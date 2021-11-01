#!/usr/bin/env python3

from gpiozero import LED
from signal import pause

multicolour = LED(12)
multicolour.blink(on_time=2.5)

pause()
