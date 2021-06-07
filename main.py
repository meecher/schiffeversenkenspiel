''' The game Schiffeversenken. '''

import random, time
from re import escape
#import keyboard
import curses

__author__ = "1359831, Ruschmaritsch, 1357985, Ullmann"
__credits__ = ""
__email__ = "david.ruschmaritsch@stud.fra-uas.de, marc.ullmann@stud.fra-uas.de"

def options():
    print("hi")

def init_game(stdscr, mode):
    stdscr.addstr(curses.LINES // 2,
    curses.COLS // 2 - len(mode) // 2,
    mode, curses.A_BLINK)

def beginn_screen(stdscr): 
    stdscr.keypad(1)
    comp = "Computer"
    mp = "2 Spieler"
    currselction = "mp"
    stdscr.addstr(curses.LINES // 2,
    curses.COLS // 2 - len(comp) // 2 + 10,
    comp, curses.A_BLINK)
    stdscr.addstr(curses.LINES // 2,
    curses.COLS // 2 - len(mp) // 2 - 10,
    mp, curses.A_REVERSE) 
    stdscr.refresh()

    while True:
    #Highlights current selected item
        curinput = stdscr.get_wch()
        if curinput == 'a' or curinput == curses.KEY_LEFT:    
        #Left side highlight (mulitplayer)
            stdscr.erase()
            stdscr.refresh()
            stdscr.addstr(curses.LINES // 2,
            curses.COLS // 2 - len(comp) // 2 + 10,
            comp, curses.A_BLINK)
            stdscr.addstr(curses.LINES // 2,
            curses.COLS // 2 - len(mp) // 2 - 10,
            mp, curses.A_REVERSE) 
            stdscr.refresh()
            currselction = "mp"
        elif curinput == 'd' or curinput == curses.KEY_RIGHT:
        #Right side highlight (computer)
            stdscr.erase()
            stdscr.refresh()
            stdscr.addstr(curses.LINES // 2,
            curses.COLS // 2 - len(comp) // 2 + 10,
            comp, curses.A_REVERSE)
            stdscr.addstr(curses.LINES // 2,
            curses.COLS // 2 - len(mp) // 2 - 10,
            mp, curses.A_BLINK)
            stdscr.refresh()
            currselction = "comp"
        elif curinput == 'o' or curinput == "\n":
            stdscr.erase()
            stdscr.refresh()
            init_game(stdscr, currselction) 

def c_main(stdscr): 
    ''' Starts the game '''
    beginning = "Schiffeversenken"
    curses.mousemask(-1)
    curses.mouseinterval(0)
    curses.curs_set(0)
    stdscr.keypad(True)

    pressed = False
    x, y = 0, 0
    while True: 

        stdscr.addstr(curses.LINES // 2,
        curses.COLS // 2 - len(beginning) // 2,
        beginning, curses.A_REVERSE)
        if pressed:
            stdscr.addstr(y,x, "x")

        c = stdscr.get_wch()
        if c == 'q':
            return 0
        elif c == '\n':
            stdscr.erase()
            stdscr.refresh()
            beginn_screen(stdscr)
        elif c == curses.KEY_MOUSE:
            _, x, y, _, bstate = curses.getmouse()
            if bstate & curses.BUTTON1_PRESSED:
                pressed = True
            elif bstate & curses.BUTTON1_RELEASED:
                pressed = False
            #stdscr.addstr(1, 0, 'mouse')
        else:  
            raise AssertionError(c)
 

def main():
    return curses.wrapper(c_main)    

if __name__ == "__main__":
    main()
    input()