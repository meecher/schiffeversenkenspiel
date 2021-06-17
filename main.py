''' The game Schiffeversenken. '''
import random, time
import numpy as np
import curses

__author__ = "1359831, Ruschmaritsch, 1357985, Ullmann"
__credits__ = ""
__email__ = "david.ruschmaritsch@stud.fra-uas.de, marc.ullmann@stud.fra-uas.de"


class Ship:
    ''' Blueprint for the ship objects '''
    def __init__(self, size):
        self.size = size
        #postition = self.postition

def create_matchfield(ySize, xSize, screen):
    matchfield = np.zeros((ySize, xSize))
    set_ships(0,0,matchfield,1,screen)


def update_matchfield(yPos, xPos, matchfield, screen):
    matchfield_visual = str(matchfield)
    screen.clear()
    screen.addstr(0,0,matchfield_visual)
    screen.refresh()

# def overlap_check(y,x, rotation, screen):
#     i = x
#     while i <= size:
#         if i == 1:
#             screen.addstr(0,0,"Invalid location")
#             break
#         else:
#             return 1

def userinput(screen):
    input_key = ""
    curinput = ""
    screen.keypad(1)
    curses.mousemask(-1)

    curinput = screen.get_wch()
    
    if curinput == 'd' or curinput == curses.KEY_RIGHT:
        input_key = "right"
    elif curinput == 's' or curinput == curses.KEY_DOWN:
        input_key = "down"
    elif curinput == 'a' or curinput == curses.KEY_LEFT:
        input_key = "left"
    elif curinput == 'w' or curinput == curses.KEY_UP:
        input_key = "up"
    elif curinput == '\n':
        input_key = "enter"
    elif curinput == curses.KEY_MOUSE:
        input_key = "mouse"
    else: 
        input_key = curinput
    return input_key


def set_ships(yPos, xPos, matchfield, player, screen):
    curinput = ""
    rotation = "hori"
    game_y_pos = 10
    game_x_pos = 0
    ship_5 = Ship(5)
    ship_4 = Ship(4)
    ship_3 = Ship(3)
    ship_2 = Ship(2)
    ship_list = [ship_5, ship_4, ship_3, ship_2]
    
    screen.keypad(1)
    curses.mousemask(-1)
    
    #Ship select men
    # height, width = s.getmaxyx()
    # curses.newwin(nlines, ncols, begin_y, begin_x)
    # menu = ["Schlachtschiff(5)", "Kreuzer(4)", "Zerstörer(3)", "U-Boot(2)"]
    
    # for idx, element in enumerate(menu):
    #     y = height // 2 + idx
    #     x = width // 2 - len(element) // 2
    #     s.addstr(y, x, element)
    #     s.refresh()

    # while True:
    #     curinput = userinput(screen)
    #     if curinput == 'down'
    #---------------------------------------------------------------------------------------------------------------------------------
        
    for i in ship_list:
    # Places all necessary ships
        size = i.size
        matchfield[yPos, xPos:xPos+size] = 1
        update_matchfield(game_y_pos, game_x_pos, matchfield, screen)

        while curinput != ord('q'):
        # Position of ship
            curinput = userinput(screen)
            if curinput == 'right':
                matchfield[yPos, xPos:xPos+size] = 0
                matchfield[yPos:yPos+size, xPos] = 0
                if rotation == 'hori':
                    #matchfield[yPos, xPos:xPos+size] = 0
                    xPos += 1
                    matchfield[yPos, xPos:xPos+size] = 1
                else:
                    #matchfield[yPos:yPos+size, xPos] = 0
                    xPos += 1
                    matchfield[yPos:yPos+size, xPos] = 1
                update_matchfield(game_y_pos, game_x_pos, matchfield, screen)
            elif curinput == 'down':
                matchfield[yPos, xPos:xPos+size] = 0
                matchfield[yPos:yPos+size, xPos] = 0
                if rotation == 'hori':
                    #matchfield[yPos, xPos:xPos+size] = 0
                    yPos += 1
                    matchfield[yPos, xPos:xPos+size] = 1
                else:
                    #matchfield[yPos:yPos+size, xPos] = 0
                    yPos += 1
                    matchfield[yPos:yPos+size, xPos] = 1
                update_matchfield(game_y_pos, game_x_pos, matchfield, screen)
            elif curinput == 'left':
                matchfield[yPos, xPos:xPos+size] = 0
                matchfield[yPos:yPos+size, xPos] = 0

                if rotation == 'hori':
                    #matchfield[yPos, xPos:xPos+size] = 0
                    xPos -= 1
                    matchfield[yPos, xPos:xPos+size] = 1
                else:
                    #matchfield[yPos:yPos+size, xPos] = 0
                    xPos -= 1
                    matchfield[yPos:yPos+size, xPos] = 1
                update_matchfield(game_y_pos, game_x_pos, matchfield, screen)
            elif curinput == 'up':
                matchfield[yPos, xPos:xPos+size] = 0
                matchfield[yPos:yPos+size, xPos] = 0
                if rotation == 'hori':
                    #matchfield[yPos, xPos:xPos+size] = 0
                    yPos -= 1
                    matchfield[yPos, xPos:xPos+size] = 1
                else:
                    #matchfield[yPos:yPos+size, xPos] = 0
                    yPos -= 1
                    matchfield[yPos:yPos+size, xPos] = 1
                update_matchfield(game_y_pos, game_x_pos, matchfield, screen)
            elif curinput == 'r':
                matchfield[yPos, xPos:xPos+size] = 0
                matchfield[yPos:yPos+size, xPos] = 0
                if rotation == 'hori':
                    rotation = "verti"
                    matchfield[yPos:yPos+size, xPos] = 1
                else: 
                    rotation = "hori"
                    matchfield[yPos, xPos:xPos+size] = 1
                update_matchfield(game_y_pos, game_x_pos, matchfield, screen)
            # if curinput == 'enter':
            #     for x in range(ship.size):
            #         #display fields
            #         matchfield[yPos, xPos] = 1

            #         curinput = screen.get_wch()
            #     if curinput == 'r':
            #         return 1
                
def options():
    ''' Currently not in use '''
    print("hi")

def init_game(screen, mode):
    ''' Starts selected game mode '''
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
        curinput = userinput(screen)
                 
        if curinput == 'left' or curinput == 'mouse':    
        # Checks for key or mouse press on the left side (multiplayer)
            x,y = mouse_pos()
            if y == curses.LINES // 2 and x in range((curses.COLS // 2 - len(mp) // 2)-len(mp),(curses.COLS // 2 - len(mp) // 2)):
            # Checks if mouse coordinates align with the left button
                check_press = True
                mouse_press = True 
            else:
                check_press = False
                mouse_press = False   
            if curinput == 'left':
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

        if curinput == 'right' or curinput == 'mouse': 
        # Checks for key or mouse press on the right side (singleplayer)
            x,y = mouse_pos()
            if y == curses.LINES // 2 and x in range((curses.COLS // 2 - len(comp) // 2 + 10),(curses.COLS // 2 - len(comp) // 2)+18):
            # Checks if mouse coordinates align with the right button
                check_press = True
                mouse_press = True 
            else:
                check_press = False
                mouse_press = False
            if curinput == 'right':
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
            
        if curinput == "enter":    
        # Enter for selection; starts new function with selected gamemode
            screen.clear()
            screen.refresh()
            init_game(screen, currselction) 

def mouse_pos():
    ''' Catches current mouse state '''
    _, x, y, _, _ = curses.getmouse()
    return x, y

def c_main(screen): 
    ''' Starts the game '''
    beginning = "Schiffeversenken"
    curses.mousemask(-1)
    curses.mouseinterval(0)
    curses.curs_set(0)
    screen.keypad(True)

    pressed = False
    x, y = 0, 0

    screen.addstr(curses.LINES // 2,
    curses.COLS // 2 - len(beginning) // 2,
    beginning, curses.A_REVERSE)

    while True: 
    # Waits for input
        curinput = userinput(screen)

        if curinput == "mouse":
        # Checks if mouse is pressed
            x,y = mouse_pos()
            if y == curses.LINES // 2 and x in range((curses.COLS // 2 - len(beginning) // 2 + 10)-10,(curses.COLS // 2 - len(beginning) // 2 + 10)+7): 
            # Checks if desired coordinates are pressed for the main menu button
                screen.erase()
                screen.refresh()
                beginn_screen(screen)
        elif curinput == "enter":
        # Starts game if enter is pressed
            screen.erase()
            screen.refresh()
            beginn_screen(screen)
        #if curinput == "q":
        # Quits programm when the key q is pressed
        #else:  
        #    raise AssertionError(curinput)
 
def userinput(screen):
    input_key = ""
    curinput = ""
    screen.keypad(1)
    curses.mousemask(-1)

    curinput = screen.get_wch()
    
    if curinput == 'd' or curinput == curses.KEY_RIGHT:
        input_key = "right"
    elif curinput == 's' or curinput == curses.KEY_DOWN:
        input_key = "down"
    elif curinput == 'a' or curinput == curses.KEY_LEFT:
        input_key = "left"
    elif curinput == 'w' or curinput == curses.KEY_UP:
        input_key = "up"
    elif curinput == '\n':
        input_key = "enter"
    elif curinput == curses.KEY_MOUSE:
        input_key = "mouse"
    else: 
        input_key = curinput
    return input_key 

def main():
    ''' Starts the game '''
    return curses.wrapper(c_main)    

if __name__ == "__main__":
    main()
    input()