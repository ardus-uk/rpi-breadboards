#!/usr/bin/python3

# Peter Normington
# 2019-12-03

from Buzzerboard import *

buzzer_setup = {
    "Whistle":20,
}

my_bb = Buzzerboard(buzzer_setup)
my_bb.buzz(0.5)

