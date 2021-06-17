''' The game Schiffeversenken. '''
import random, time
import numpy as np
import curses

__author__ = "1359831, Ruschmaritsch, 1357985, Ullmann, x, Lotte"
__credits__ = ""
__email__ = "david.ruschmaritsch@stud.fra-uas.de, marc.ullmann@stud.fra-uas.de, x"


class Ship:
    ''' Blueprint for the ship objects '''
    def __init__(self, size):
        self.size = size
        self.rotation = "hori"
        self.position_x = 0
        self.position_y = 0
    

def create_matchfield(ySize, xSize, screen):
    matchfield = np.zeros((ySize, xSize))
    set_ships(0,0,matchfield,1,ySize,xSize,screen)


def update_matchfield(yPos, xPos, matchfield, screen):
    matchfield_visual = str(matchfield)
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


def set_ships(yPos, xPos, matchfield, player, yGameSize, xGameSize, screen):
    curinput = ""
    rotation = "hori"
    counter = 0
    ship_pos_x = 0
    ship_pos_y = 0
    game_y_pos = 10
    game_x_pos = 0
    ship_5 = Ship(5)
    ship_4 = Ship(4)
    ship_3 = Ship(3)
    ship_2 = Ship(2)
    ship_1 = Ship(2)
    ship_list = [ship_5, ship_4, ship_3, ship_2, ship_1]
    ship_list_placed = []
    
    screen.keypad(1)
    curses.mousemask(-1)
        
    for i in ship_list:
    # Places all necessary ships
        size = i.size
        if counter == len(ship_list)-1:
            counter = counter
        else:
            counter += 1
        next_ship = ship_list[counter]
        last_ship = ship_list[counter-1]


        if rotation == 'hori':
        # Draws ship on horizontal axis
            matchfield[yPos, xPos:xPos+size] = 1
        else: 
        # Draws ship on vertical axis
            matchfield[yPos:yPos+size, xPos] = 1
        update_matchfield(game_y_pos, game_x_pos, matchfield, screen)

        while curinput != ord('q'):
        # Position of ship
            for y in ship_list_placed:
            # Draw placed ships
                if y.rotation == 'hori':
                # Checks if current ship object is horizontal
                    matchfield[y.position_y, y.position_x:y.position_x+y.size] = 1
                else:
                # Checks if current ship object is vertical
                    matchfield[y.position_y:y.position_y+y.size, y.position_x] = 1
                update_matchfield(game_y_pos, game_x_pos, matchfield, screen)

            matchfield[yPos, xPos:xPos+size] = 0
            matchfield[yPos:yPos+size, xPos] = 0

            curinput = userinput(screen)

            if curinput == 'right':
            # Checks if userinput is right
                if rotation == 'hori':
                # Checks if ship rotation is horizontal
                    if xPos + size >= xGameSize:
                    # Doesn't move ship if it exceeds the matchfield to the right
                        matchfield[yPos, xPos:xPos+size] = 1    
                    else:                
                        xPos += 1
                        matchfield[yPos, xPos:xPos+size] = 1
                else:
                    if xPos + 1 >= xGameSize:
                    # Doesn't move ship if it exceeds the matchfield to the right
                        matchfield[yPos:yPos+size, xPos] = 1
                    else:
                        xPos += 1
                        matchfield[yPos:yPos+size, xPos] = 1

            elif curinput == 'down':
            # Checks if userinput is down
                if rotation == 'hori':
                # Checks if ship rotation is horizontal
                    if yPos + 1 >= yGameSize:
                    # Doesn't move ship if it exceeds the matchfield at the bottom
                        matchfield[yPos, xPos:xPos+size] = 1
                    else:
                        yPos += 1
                        matchfield[yPos, xPos:xPos+size] = 1
                else:
                    if yPos + size >= yGameSize:
                    # Doesn't move ship if it exceeds the matchfield at the bottom
                        matchfield[yPos:yPos+size, xPos] = 1
                    else:
                        yPos += 1
                        matchfield[yPos:yPos+size, xPos] = 1

            elif curinput == 'left':
            # Checks if userinput is left
                if rotation == 'hori':
                # Checks if ship rotation is horizontal
                    if xPos - 1 < 0:
                        # Doesn't move ship if it exceeds the matchfield to the left
                        matchfield[yPos, xPos:xPos+size] = 1
                    else:
                        xPos -= 1
                        matchfield[yPos, xPos:xPos+size] = 1
                else:
                    if xPos - 1 < 0:
                    # Doesn't move ship if it exceeds the matchfield to the left                   
                        matchfield[yPos:yPos+size, xPos] = 1
                    else:
                        xPos -= 1
                        matchfield[yPos:yPos+size, xPos] = 1

            elif curinput == 'up':
            # Checks if userinput is up
                if rotation == 'hori':
                # Checks if ship rotation is horizontal
                    if yPos - 1 < 0:
                        # Doesn't move ship if it exceeds the matchfield at the top
                        matchfield[yPos, xPos:xPos+size] = 1
                    else:
                        yPos -= 1
                        matchfield[yPos, xPos:xPos+size] = 1
                else:
                    if yPos - 1 < 0:
                    # Doesn't move ship if it exceeds the matchfield at the top
                        matchfield[yPos:yPos+size, xPos] = 1    
                    else:
                        yPos -= 1
                        matchfield[yPos:yPos+size, xPos] = 1

            elif curinput == 'r':
            # Checks if userinput is r for rotation
                if rotation == 'hori':
                # Checks if ship rotation is horizontal
                    if yPos + size > yGameSize:
                    # Doesn't rotate ship if it exceeds the matchfield to the right
                        matchfield[yPos, xPos:xPos+size] = 1
                    else:
                        rotation = "verti"
                        matchfield[yPos:yPos+size, xPos] = 1
                else:
                    if xPos + size > xGameSize:
                    # Doesn't move ship if it exceeds the matchfield at the bottom
                        matchfield[yPos, xPos:xPos+size]
                    else:
                        rotation = "hori"
                        matchfield[yPos, xPos:xPos+size] = 1

            elif curinput == 'enter':
            # Checks if userinput is enter
                iteration = 0
                iteration_placed_ship = 0
                ship_placement = False
                loop = True
                xPosCur = xPos
                yPosCur = yPos

                if not ship_list_placed:
                # First ship doesn't need to check overlap -> directly placed
                    ship_placement = True
                else: 
                    for cur_ship in ship_list_placed:
                        iteration = 0
                        iteration_placed_ship = 0
                        # Checks if ships overlap
                        if rotation == 'hori' and cur_ship.rotation == 'hori':
                        # Checks if ship rotation is horizontal
                            if yPos == cur_ship.position_y:
                            # Checks if ships lie in the same y coordinates
                                while iteration <= size:
                                # Runs until the size of the current ship is reached
                                    while loop == True or iteration >= cur_ship.size:
                                    # Stops if ships overlap or the size is reached
                                        if xPos + iteration == cur_ship.position_x + iteration_placed_ship:
                                        # Checks if current x coordinate overlaps with the current selected ship
                                            screen.addstr(10,0,"Schiffe überschneiden sich")
                                            loop = False
                                        else:
                                            iteration +=1
                                    iteration += 1
                                    iteration_placed_ship += 1
                                if loop == True:
                                # Ships don't overlap; ready for placing ship
                                    ship_placement = True
                            else:
                                ship_placement = True

                        elif rotation == 'hori' and cur_ship.rotation == 'verti':
                        # Checks if ship rotation is horizontal
                            while iteration_placed_ship <= cur_ship.size:
                            # Runs until the size of the current ship is reached
                                iteration = 0
                                while iteration <= size:
                                # Stops if ships overlap or the size is reached
                                    if (xPos + iteration == cur_ship.position_x 
                                    and yPos == cur_ship.position_y + iteration_placed_ship):
                                    # Checks if current x coordinate overlaps with the current selected ship
                                        screen.addstr(10,0,"Schiffe überschneiden sich")
                                        loop = False
                                        iteration += 1
                                    else:
                                        iteration +=1
                                iteration_placed_ship += 1
                            if loop == True:
                            # Ships don't overlap; ready for placing ship
                                ship_placement = True
                            else:
                                ship_placement = False
                        
                        elif rotation == 'verti' and cur_ship.rotation == 'hori':
                        # Checks if ship rotation is horizontal
                            while iteration_placed_ship <= cur_ship.size:
                            # Runs until the size of the current ship is reached
                                iteration = 0
                                while iteration <= size:
                                # Stops if ships overlap or the size is reached
                                    if (xPos == cur_ship.position_x + iteration_placed_ship and
                                    yPos + iteration == cur_ship.position_y):
                                    # Checks if current x coordinate overlaps with the current selected ship
                                        screen.addstr(10,0,"Schiffe überschneiden sich")
                                        loop = False
                                        iteration +=1
                                    else:
                                        iteration +=1
                                iteration_placed_ship += 1
                            if loop == True:
                            # Ships don't overlap; ready for placing ship
                                ship_placement = True
                            else:
                                ship_placement = False
                            
                        elif rotation == 'verti' and cur_ship.rotation == 'verti':
                        # Checks if ship rotation is horizontal
                            if xPos == cur_ship.position_x:
                            # Checks if ships lie in the same x coordinates
                                while iteration <= size:
                                # Runs until the size of the current ship is reached
                                    while loop == True or iteration >= cur_ship.size:
                                    # Stops if ships overlap or the size is reached
                                        if yPos + iteration == cur_ship.position_y + iteration_placed_ship:
                                        # Checks if current y coordinate overlaps with the current selected ship
                                            screen.addstr(10,0,"Schiffe überschneiden sich")
                                            loop = False
                                        else:
                                            iteration +=1
                                    iteration += 1
                                    iteration_placed_ship += 1
                                if loop == True:
                                # Ships don't overlap; ready for placing ship
                                    ship_placement = True
                            else:
                                ship_placement = True
                        
                if ship_placement == True:
                    i.position_x = xPosCur 
                    i.position_y = yPosCur
                    if rotation == 'hori':
                    # Sets ship (current object) rotation and moves current location
                        i.rotation = "hori"
                        yPos += 1
                        matchfield[yPos, xPos:xPos+next_ship.size] = 1
                    else:            
                        i.rotation = "verti"
                        xPos += 1
                        matchfield[yPos:yPos+next_ship.size, xPos] = 1
                    ship_list_placed.append(i)
                    update_matchfield(game_y_pos, game_x_pos, matchfield, screen)
                    break

            update_matchfield(game_y_pos, game_x_pos, matchfield, screen)
        options()
                    


                
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