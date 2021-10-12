#!/usr/bin/python3

# Peter Normington
# 2020-03-24


from ButtonBoard import *

five_buttons_layout = {                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            "Green":27,
            "Red":22,
            "White":23,
            "Blue":24,
            "Yellow":25,
            }

five_buttons_board = ButtonBoard(five_buttons_layout)
five_buttons_board.test_all_buttons()
five_buttons_board.test_button("Green")