#!/usr/bin/python3

# Peter Normington
# 2019-12-03

from BuzzerBoard import *

buzzer_setup = {
    "Whistle":20,
}

my_bb = BuzzerBoard(buzzer_setup)
my_bb.buzz("Whistle",0.5)

