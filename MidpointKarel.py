from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Find the midpoint of the first row in any world.
    """
    place_beepers()
    clear_wall()
    collect_edge_beepers()
    put_beeper()

# pre: facing east in beginning
# post: facing west at end
def place_beepers():
    while front_is_clear():
        put_beeper()
        move()
    turn_around()

def clear_wall():
    while front_is_clear():
        move()
    if beepers_present():
        pick_beeper()
    turn_around()
    if front_is_clear():
        move()

def collect_edge_beepers():
    while beepers_present():
        pick_beeper()
        move_to_next_edge()

def move_to_next_edge():
    move()
    while beepers_present():
        move()
    turn_around()
    move()

def turn_around():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
