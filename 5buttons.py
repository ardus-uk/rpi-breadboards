#!/usr/bin/python3

# Peter Normington
# 2020-03-24


from ButtonBoard import *

5buttons_layout = {                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            "Green":27,
            "Red":22,
            "White":23,
            "Blue":24,
            "Yellow":25,
        }

5buttons_board = ButtonBoard(5buttons_layout)
5buttons_board.test_all_buttons()