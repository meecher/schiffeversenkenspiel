''' The game Schiffeversenken. '''

import random, time
import curses

__author__ = "1359831, Ruschmaritsch, 1357985, Ullmann"
__credits__ = ""
__email__ = "david.ruschmaritsch@stud.fra-uas.de, marc.ullmann@stud.fra-uas.de"


class ship:
    ''' Blueprint for the ship objects '''
    def __init__(self, size, rotation, position):
        self.size = size


def options():
    print("hi")

def init_game(stdscr, mode):
    ''' Starts selected game mode '''
    stdscr.addstr(curses.LINES // 2,
    curses.COLS // 2 - len(mode) // 2,
    mode, curses.A_BLINK)
    stdscr.refresh()
    curinput = stdscr.get_wch() 


def beginn_screen(stdscr): 
    ''' Let's the player select the game mode '''
    stdscr.keypad(1)
    curses.mousemask(-1)

    comp = "Computer"
    mp = "2 Spieler"
    currselction = "mp"
    pressed = False
    check_press = False
    mouse_press = False
    x, y = 0, 0

    stdscr.addstr(curses.LINES // 2,
    curses.COLS // 2 - len(mp) // 2 - 10,
    mp, curses.A_REVERSE) 
    stdscr.addstr(curses.LINES // 2,
    curses.COLS // 2 - len(comp) // 2 + 10,
    comp, curses.A_BLINK)
    stdscr.refresh()

    while True:
    # Highlights current selected item; waits for input
        curinput = stdscr.get_wch() 
                 
        if curinput == 'a' or curinput == curses.KEY_LEFT or pressed:    
        # Checks for key or mouse press on the left side (multiplayer)
            if y == curses.LINES // 2 and x in range((curses.COLS // 2 - len(mp) // 2)-len(mp),(curses.COLS // 2 - len(mp) // 2)):
            # Checks if mouse coordinates align with the left button
                check_press = True
                mouse_press = True 
            else:
                check_press = False
                mouse_press = False   
            if curinput == 'a' or curinput == curses.KEY_LEFT:
            # Sets the check true if desired key is pressed 
                check_press = True  
            if check_press == True:
            # Draws updated text
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
                if mouse_press == True:
                # Confirms selection if mouse is pressed       
                    stdscr.erase()
                    stdscr.refresh()
                    init_game(stdscr, currselction)

        if curinput == 'd' or curinput == curses.KEY_RIGHT or pressed:
        # Checks for key or mouse press on the right side (singleplayer)
            if y == curses.LINES // 2 and x in range((curses.COLS // 2 - len(comp) // 2 + 10),(curses.COLS // 2 - len(comp) // 2)+18):
            # Checks if mouse coordinates align with the right button
                check_press = True
                mouse_press = True 
            else:
                check_press = False
                mouse_press = False
            if curinput == 'd' or curinput == curses.KEY_RIGHT:
            # Sets the check true if desired key is pressed 
                check_press = True
            if check_press == True:
            # Draws updated text   
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
                if mouse_press == True: 
                # Confirms selection if mouse is pressed      
                    stdscr.erase()
                    stdscr.refresh()
                    init_game(stdscr, currselction) 
            
        elif curinput == '\n':    
        # Enter for selection; starts new function with selected gamemode
            stdscr.erase()
            stdscr.refresh()
            init_game(stdscr, currselction) 

        if curinput == curses.KEY_MOUSE:
        # Handles mouse input
            x, y, bstate = mouse_state()
            if bstate & curses.BUTTON1_PRESSED:
            # Handles mouse pressed state
                pressed = True
            elif bstate & curses.BUTTON1_RELEASED:
            # Handles mouse released state
                pressed = False

def mouse_state():
    ''' Catches current mouse state '''
    _, x, y, _, bstate = curses.getmouse()
    return x, y, bstate

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
    # Waits for input
        stdscr.addstr(curses.LINES // 2,
        curses.COLS // 2 - len(beginning) // 2,
        beginning, curses.A_REVERSE)

        if pressed:
        # Checks if mouse is pressed
            if y == curses.LINES // 2 and x in range((curses.COLS // 2 - len(beginning) // 2 + 10)-10,(curses.COLS // 2 - len(beginning) // 2 + 10)+7): 
            # Checks if desired coordinates are pressed for the main menu button
                stdscr.erase()
                stdscr.refresh()
                beginn_screen(stdscr)

        curinput = stdscr.get_wch()
        if curinput == 'q':
        # Quits programm when the key q is pressed
            return 0
        elif curinput == '\n':
        # Starts game if enter is pressed
            stdscr.erase()
            stdscr.refresh()
            beginn_screen(stdscr)
        elif curinput == curses.KEY_MOUSE:
        # Handles mouse input
            x, y, bstate = mouse_state()
            if bstate & curses.BUTTON1_PRESSED:
            # Handles mouse pressed state
                pressed = True
            elif bstate & curses.BUTTON1_RELEASED:
            # Handles mouse released state
                pressed = False
        else:  
            raise AssertionError(curinput)
 

def main():
    ''' Starts the game '''
    return curses.wrapper(c_main)    

if __name__ == "__main__":
    main()
    input()