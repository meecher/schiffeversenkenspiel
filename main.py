''' The game Schiffeversenken. '''

import random, time
from cursebox import *
from cursebox.constants import EVENT_BACKSPACE, EVENT_ENTER


__author__ = "1359831, Ruschmaritsch, 1357985, Ullmann"
__credits__ = ""
__email__ = "david.ruschmaritsch@stud.fra-uas.de, marc.ullmann@stud.fra-uas.de"

def options():
    print("hi")

def init_game(playerdefine):
    print("hi")

def beginn_screen(width, height):
    with Cursebox() as cb:  
        comp = "Computer"
        mp = "2 Spieler"
        cb.put(x=(width - len(comp)) / 2,
            y=height / 2, text=comp,
            fg=colors.black, bg=colors.white)
        cb.put(x=(width - len(mp)) / 2,
            y=height / 2, text=mp,
            fg=colors.black, bg=colors.white)

def main(): 
    ''' Starts the game '''
    with Cursebox() as cb:  
        width, height = cb.width, cb.height
        greeting = "Schiffeversenken"
        # Center text on the screen
        cb.put(x=(width - len(greeting)) / 2,
            y=height / 2, text=greeting,
            fg=colors.black, bg=colors.white)
        # Wait for any keypress
        event = cb.poll_event()
        if event == EVENT_ENTER:
            cb.clear()
            beginn_screen(width, height)
    


if __name__ == "__main__":
    main()
    input()