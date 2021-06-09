''' The game Schiffeversenken. '''

import random, time
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
    stdscr.refresh()
    curinput = stdscr.get_wch() 


def beginn_screen(stdscr): 
    ''' Let's the player select the game mode '''
    stdscr.keypad(1)
    comp = "Computer"
    mp = "2 Spieler"
    currselction = "mp"
    pressed = False
    check_press = False
    mouse_press = False
    x, y = 0, 0
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

        if curinput == 'a' or curinput == curses.KEY_LEFT or pressed:    
        # Left side highlight (mulitplayer)
            if y == curses.LINES // 2 and x in range((curses.COLS // 2 - len(comp) // 2 + 10),(curses.COLS // 2 - len(comp) // 2 + 10)+8):
            # Checks if mouse coordinates align with the left button
                check_press = True
                mouse_press = True   
            elif curinput == 'a' or curinput == curses.KEY_LEFT:
                check_press = True   
            if check_press == True:
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
                    stdscr.erase()
                    stdscr.refresh()
                    init_game(stdscr, currselction)

        elif curinput == 'd' or curinput == curses.KEY_RIGHT or pressed:
        #Right side highlight (computer)
            if y == curses.LINES // 2 and x in range((curses.COLS // 2 - len(mp) // 2 - 10),(curses.COLS // 2 - len(mp) // 2 - 10)+8):
            # Checks if mouse coordinates align with the right button
                check_press = True
                check_mousepress = True
            elif curinput == 'd' or curinput == curses.KEY_RIGHT:
                check_press = True
            if check_press == True:
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
                    stdscr.erase()
                    stdscr.refresh()
                    init_game(stdscr, currselction) 
            
        elif curinput == '\n':    
        #Enter for selection; starts new function with selected gamemode
            stdscr.erase()
            stdscr.refresh()
            init_game(stdscr, currselction) 

        if curinput == curses.KEY_MOUSE:
            x,y,bstate = mouse_press()
            # _, x, y, _, bstate = curses.getmouse()
            # if bstate & curses.BUTTON1_PRESSED:
            #     pressed = True
            # elif bstate & curses.BUTTON1_RELEASED:
            #     pressed = False

def mouse_press():
    _, x, y, _, bstate = curses.getmouse()
    if bstate & curses.BUTTON1_PRESSED:
        pressed = True
    elif bstate & curses.BUTTON1_RELEASED:
        pressed = False
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
        stdscr.addstr(curses.LINES // 2,
        curses.COLS // 2 - len(beginning) // 2,
        beginning, curses.A_REVERSE)

        if pressed:
            if y == curses.LINES // 2 and x in range((curses.COLS // 2 - len(beginning) // 2 + 10)-10,(curses.COLS // 2 - len(beginning) // 2 + 10)+7): 
                stdscr.erase()
                stdscr.refresh()
                beginn_screen(stdscr)
            #places x at mouse pos
            #stdscr.addstr(y,x, "x")

        curinput = stdscr.get_wch()
        if curinput == 'q':
            return 0
        elif curinput == '\n':
            stdscr.erase()
            stdscr.refresh()
            beginn_screen(stdscr)
        elif curinput == curses.KEY_MOUSE:
            _, x, y, _, bstate = curses.getmouse()
            if bstate & curses.BUTTON1_PRESSED:
                pressed = True
            elif bstate & curses.BUTTON1_RELEASED:
                pressed = False
        else:  
            raise AssertionError(curinput)
 

def main():
    return curses.wrapper(c_main)    

if __name__ == "__main__":
    main()
    input()