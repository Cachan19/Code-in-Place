from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    Place missing beepers back in the columns.
    """
    for i in range(4):
        fix_tower()
        if front_is_clear():
            move_to_next()

def fix_tower():
    turn_left()
    while front_is_clear():
        place_missing_beeper()
        move()
    place_missing_beeper()
    turn_around()
    return_to_bottom()

def place_missing_beeper():
    if no_beepers_present():
        put_beeper()

def return_to_bottom():
    while front_is_clear():
        move()
    turn_left()

def move_to_next():
    for i in range(4):
        move()

def turn_around():
    for i in range(2):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()