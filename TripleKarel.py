from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    Karel paints the outsides of the different sized buildings
    """
    for i in range(2):
        paint_building()
        turn_corner_right()
    paint_building()


def paint_building():
    for i in range(2):
        color_wall()
        turn_corner_left()
    color_wall()

def color_wall():
    while left_is_blocked():
        put_beeper()
        move()

def turn_corner_left():
    turn_left()
    move()

def turn_corner_right():
    put_beeper()
    turn_right()
    move()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
