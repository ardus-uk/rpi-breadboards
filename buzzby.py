#!/usr/bin/python3

# Peter Normington
# 2019-12-03

from BuzzerBoard import *

buzzer_setup = {
    "Whistle":20,
}

my_bb = BuzzerBoard(buzzer_setup)
for i in range(1,5):
    my_bb.buzz("Whistle",i/10)


