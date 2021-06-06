''' The game Schiffeversenken. '''

import random, time
import keyboard
from cursebox import *
from cursebox.constants import EVENT_BACKSPACE, EVENT_DOWN, EVENT_ENTER, EVENT_ESC, EVENT_LEFT, EVENT_RIGHT, EVENT_UP


__author__ = "1359831, Ruschmaritsch, 1357985, Ullmann"
__credits__ = ""
__email__ = "david.ruschmaritsch@stud.fra-uas.de, marc.ullmann@stud.fra-uas.de"

def options():
    print("hi")

def init_game(playerdefine):
    print("hi")

def blink(state):
    activestate = 0
    while state > 0:
        if activestate == 0:
            activestate = 1
        else: 
            activestate = 0
    return activestate


def beginn_screen(width, height):
    with Cursebox() as cb:  
        comp = "Computer"
        mp = "2 Spieler"
        x = 1
        cb.clear()
        cb.put(x=(width - len(comp)) / 2 + 10,
        y=height / 2, text=comp, fg=colors.white, bg=colors.black)
        cb.put(x=(width - len(mp)) / 2 - 10,
        y=height / 2, text=mp, fg=colors.black, bg=colors.white)
    
        cb.refresh()

        while x > 0:
            if keyboard.is_pressed('n'):
                cb.clear()
                cb.put(x=(width - len(comp)) / 2 + 10,
                y=height / 2, text=comp, fg=colors.white, bg=colors.black)
                cb.put(x=(width - len(mp)) / 2 - 10,
                y=height / 2, text=mp, fg=colors.black, bg=colors.white)
                cb.refresh()
            elif keyboard.is_pressed('m'):
                cb.clear()
                cb.put(x=(width - len(comp)) / 2 + 10,
                y=height / 2, text=comp, fg=colors.black, bg=colors.white)
                cb.put(x=(width - len(mp)) / 2 - 10,
                y=height / 2, text=mp, fg=colors.white, bg=colors.black)
                cb.refresh()
          
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
        cb.poll_event()
        beginn_screen(width, height)


if __name__ == "__main__":
    main()
    input()