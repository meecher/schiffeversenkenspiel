''' The game Schiffeversenken. '''

import random, time
from cursebox import *
from cursebox.constants import EVENT_BACKSPACE, EVENT_ENTER, EVENT_ESC, EVENT_LEFT, EVENT_UP


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
        cb.refresh()
        cb.poll_event()
        #cb.put(x=(width - len(mp)) / 2,
        #    y=height / 2, text=mp,
        #    fg=colors.black, bg=colors.white)

def main(): 
    ''' Starts the game '''
    with Cursebox() as cb:  
        width, height = cb.width, cb.height
        greeting = "Schiffeversenken"
        test = "lkafnoknsskgnpesgn"
        #cb.set_cursor(10,10)
        # Center text on the screen
        cb.put(x=(width - len(greeting)) / 2,
            y=height / 2, text=greeting,
            fg=colors.black, bg=colors.white)
        # Wait for any keypress
        cb.poll_event()
        cb.clear()
        beginn_screen(width, height)
        #cb.put_arrow(10,10,0,colors.black,colors.white)
        #cb.clear()
        #äif event == EVENT_UP:
            #cb.clear
            #beginn_screen(width, height)
            #cb.put(x=(width - len(test)) / 2,
            #    y=height / 2, text=test,
            #    fg=colors.black, bg=colors.white)
            #cb.refresh()
    


if __name__ == "__main__":
    main()
    input()