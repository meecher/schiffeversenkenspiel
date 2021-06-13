''' The game Schiffeversenken. '''

import random, time
import numpy as np
import curses

__author__ = "1359831, Ruschmaritsch, 1357985, Ullmann"
__credits__ = ""
__email__ = "david.ruschmaritsch@stud.fra-uas.de, marc.ullmann@stud.fra-uas.de"


class ship:
    ''' Blueprint for the ship objects '''
    def __init__(self, size, rotation, position):
        self.size = size

def create_matchfield(ySize, xSize, screen):
    #global matchfield1
    #matchfield1 = np.zeros((ySize, xSize))
    matchfield1 = np.zeros((ySize, xSize))
    set_ships(0,0,matchfield1,1,screen)
    #atchfield1_visual = str(matchfield1)
    #screen.addstr(0,0,str(matchfield1_visual))
    #print(matchfield1)
    #global matchfield2
    #screen.addstr(0,0,np.zeros((ySize, xSize))
    #matchfield2 = np.zeros((ySize, xSize))

def update_matchfield(yPos, xPos, matchfield, player, screen):
    matchfield_visual = str(matchfield)
    screen.clear()
    screen.addstr(0,0,str(matchfield_visual))
    screen.refresh()
    return 0
    #set_ships(yPos, xPos, matchfield, player, screen)

def set_ships(yPos, xPos, matchfield, player, screen):
   # global matchfield1
    screen.keypad(1)
    curses.mousemask(-1)

    update_matchfield(yPos, xPos, matchfield, player, screen)
    curinput= ""
    while curinput != ord('q'):
        curinput = screen.get_wch()
        if curinput == 'd' or curinput == curses.KEY_RIGHT:
            matchfield[yPos, xPos] = 0
            xPos += 1
            matchfield[yPos, xPos] = 1
            update_matchfield(0, 0, matchfield, player, screen)
        if curinput == 's' or curinput == curses.KEY_DOWN:
            matchfield[yPos, xPos] = 0
            yPos += 1
            matchfield[yPos, xPos] = 1
            update_matchfield(0, 0, matchfield, player, screen)
        if curinput == 'a' or curinput == curses.KEY_LEFT:
            matchfield[yPos, xPos] = 0
            xPos -= 1
            matchfield[yPos, xPos] = 1
            update_matchfield(0, 0, matchfield, player, screen)
        if curinput == 'w' or curinput == curses.KEY_UP:
            matchfield[yPos, xPos] = 0
            yPos -= 1
            matchfield[yPos, xPos] = 1
            update_matchfield(0, 0, matchfield, player, screen)

def options():
    ''' Currently not in use '''
    print("hi")

def init_game(screen, mode):
    ''' Starts selected game mode '''
    #screen.addstr(curses.LINES // 2,
    #curses.COLS // 2 - len(mode) // 2,
    #mode, curses.A_BLINK)
    screen.refresh()
    create_matchfield(10,10,screen)



def beginn_screen(screen): 
    ''' Let's the player select the game mode '''
    screen.keypad(1)
    curses.mousemask(-1)

    comp = "Computer"
    mp = "2 Spieler"
    currselction = "mp"
    pressed = False
    check_press = False
    mouse_press = False
    x, y = 0, 0

    screen.addstr(curses.LINES // 2,
    curses.COLS // 2 - len(mp) // 2 - 10,
    mp, curses.A_REVERSE) 
    screen.addstr(curses.LINES // 2,
    curses.COLS // 2 - len(comp) // 2 + 10,
    comp, curses.A_BLINK)
    screen.refresh()

    while True:
    # Highlights current selected item; waits for input
        curinput = screen.get_wch() 
                 
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
                screen.erase()
                screen.refresh()
                screen.addstr(curses.LINES // 2,
                curses.COLS // 2 - len(comp) // 2 + 10,
                comp, curses.A_BLINK)
                screen.addstr(curses.LINES // 2,
                curses.COLS // 2 - len(mp) // 2 - 10,
                mp, curses.A_REVERSE) 
                screen.refresh()
                currselction = "mp"
                if mouse_press == True:
                # Confirms selection if mouse is pressed       
                    screen.erase()
                    screen.refresh()
                    init_game(screen, currselction)

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
                screen.erase()
                screen.refresh()
                screen.addstr(curses.LINES // 2,
                curses.COLS // 2 - len(comp) // 2 + 10,
                comp, curses.A_REVERSE)
                screen.addstr(curses.LINES // 2,
                curses.COLS // 2 - len(mp) // 2 - 10,
                mp, curses.A_BLINK)
                screen.refresh()
                currselction = "comp"
                if mouse_press == True: 
                # Confirms selection if mouse is pressed      
                    screen.erase()
                    screen.refresh()
                    init_game(screen, currselction) 
            
        if curinput == '\n':    
        # Enter for selection; starts new function with selected gamemode
            screen.erase()
            screen.refresh()
            init_game(screen, currselction) 

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

def c_main(screen): 
    ''' Starts the game '''
    beginning = "Schiffeversenken"
    curses.mousemask(-1)
    curses.mouseinterval(0)
    curses.curs_set(0)
    screen.keypad(True)

    pressed = False
    x, y = 0, 0

    while True: 
    # Waits for input
        screen.addstr(curses.LINES // 2,
        curses.COLS // 2 - len(beginning) // 2,
        beginning, curses.A_REVERSE)

        if pressed:
        # Checks if mouse is pressed
            if y == curses.LINES // 2 and x in range((curses.COLS // 2 - len(beginning) // 2 + 10)-10,(curses.COLS // 2 - len(beginning) // 2 + 10)+7): 
            # Checks if desired coordinates are pressed for the main menu button
                screen.erase()
                screen.refresh()
                beginn_screen(screen)

        curinput = screen.get_wch()
        if curinput == 'q':
        # Quits programm when the key q is pressed
            return 0
        elif curinput == '\n':
        # Starts game if enter is pressed
            screen.erase()
            screen.refresh()
            beginn_screen(screen)
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