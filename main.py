''' The game Schiffeversenken. '''
import random, time
import Ship
import numpy as np
import curses

__author__ = "1359831, Ruschmaritsch, 1357985, Ullmann, x, Lotte"
__credits__ = ""
__email__ = "david.ruschmaritsch@stud.fra-uas.de, marc.ullmann@stud.fra-uas.de, x"
    

def mulitplayer(screen):
    create_matchfield(10,10,screen) 

def singleplayer(screen):
    create_matchfield(10,10,screen)

def create_matchfield(ySize, xSize, screen):
    matchfield_visual = [[0]*xSize]*ySize
    matchfield_temp = np.zeros((ySize, xSize))
    matchfield_logic = np.zeros((ySize, xSize))
    set_ships(0,0,matchfield_visual,matchfield_temp,matchfield_logic,1,ySize,xSize,screen)

def update_matchfield(yPos, xPos, matchfield_temp, screen):
    matchfield_temp = str(matchfield_temp)
    #screen.addstr(0,0,matchfield_temp)
    #screen.refresh()

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

def draw_visual(matchfield_visual,screen):
    i = 0
    for row in matchfield_visual:
        string_ints = [str(int) for  int in row]
        stringli = ' '.join(string_ints)
        screen.addstr(i,0,stringli)
        screen.refresh()
        i += 1
    screen.refresh()

def update_visual(rotation,yStart,yStop,xStart,xStop,matchfield_visual,screen):
    i = xStart
    y = yStart
    if rotation == 'hori':
        while i < xStop:
            matchfield_visual[i][yStart] = 1
    else:
        while y < yStop:
            matchfield_visual[xStart][y] = 1
    i = 0
    for row in matchfield_visual:
        string_ints = [str(int) for  int in row]
        stringli = ' '.join(string_ints)
        screen.addstr(i,0,stringli)
        screen.refresh()
        i += 1
    screen.refresh()

def set_ships(yPos, xPos, matchfield_visual, matchfield_temp, matchfield_logic, player, yGameSize, xGameSize, screen):
    curinput = ""
    rotation = "hori"
    counter = 0
    game_y_pos = 10
    game_x_pos = 0
    ship_5 = Ship.Ship(5)
    ship_4a = Ship.Ship(4)
    ship_4b = Ship.Ship(4)
    ship_3a = Ship.Ship(3)
    ship_3b = Ship.Ship(3)
    ship_3c = Ship.Ship(3)
    ship_2a = Ship.Ship(2)
    ship_2b = Ship.Ship(2)
    ship_2c = Ship.Ship(2)
    ship_2d = Ship.Ship(2)
    ship_fill = Ship.Ship(1)
    ship_list = [ship_5, ship_4a, ship_4b, ship_3a, ship_3b, ship_3c, ship_2a, ship_2b, ship_2c, ship_2d, ship_fill]
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
            matchfield_temp[yPos, xPos:xPos+size] = 1
            #_______________________________________________________________
            update_visual(rotation,yPos,yPos,xPos,(xPos+size-1),matchfield_visual,screen)
        else: 
        # Draws ship on vertical axis
            matchfield_temp[yPos:yPos+size, xPos] = 1
        update_matchfield(game_y_pos, game_x_pos, matchfield_temp, screen)

        while curinput != ord('q'):
        # Position of ship
            for y in ship_list_placed:
            # Draw placed ships
                if y.rotation == 'hori':
                # Checks if current ship object is horizontal
                    matchfield_temp[y.position_y, y.position_x:y.position_x+y.size] = 1
                else:
                # Checks if current ship object is vertical
                    matchfield_temp[y.position_y:y.position_y+y.size, y.position_x] = 1
                update_matchfield(game_y_pos, game_x_pos, matchfield_temp, screen)

            matchfield_temp[yPos, xPos:xPos+size] = 0
            matchfield_temp[yPos:yPos+size, xPos] = 0

            curinput = userinput(screen)

            if curinput == 'right':
            # Checks if userinput is right
                if rotation == 'hori':
                # Checks if ship rotation is horizontal
                    if xPos + size >= xGameSize:
                    # Doesn't move ship if it exceeds the matchfield to the right
                        matchfield_temp[yPos, xPos:xPos+size] = 1    
                    else:                
                        xPos += 1
                        matchfield_temp[yPos, xPos:xPos+size] = 1
                else:
                    if xPos + 1 >= xGameSize:
                    # Doesn't move ship if it exceeds the matchfield to the right
                        matchfield_temp[yPos:yPos+size, xPos] = 1
                    else:
                        xPos += 1
                        matchfield_temp[yPos:yPos+size, xPos] = 1

            elif curinput == 'down':
            # Checks if userinput is down
                if rotation == 'hori':
                # Checks if ship rotation is horizontal
                    if yPos + 1 >= yGameSize:
                    # Doesn't move ship if it exceeds the matchfield at the bottom
                        matchfield_temp[yPos, xPos:xPos+size] = 1
                    else:
                        yPos += 1
                        matchfield_temp[yPos, xPos:xPos+size] = 1
                else:
                    if yPos + size >= yGameSize:
                    # Doesn't move ship if it exceeds the matchfield at the bottom
                        matchfield_temp[yPos:yPos+size, xPos] = 1
                    else:
                        yPos += 1
                        matchfield_temp[yPos:yPos+size, xPos] = 1

            elif curinput == 'left':
            # Checks if userinput is left
                if rotation == 'hori':
                # Checks if ship rotation is horizontal
                    if xPos - 1 < 0:
                        # Doesn't move ship if it exceeds the matchfield to the left
                        matchfield_temp[yPos, xPos:xPos+size] = 1
                    else:
                        xPos -= 1
                        matchfield_temp[yPos, xPos:xPos+size] = 1
                else:
                    if xPos - 1 < 0:
                    # Doesn't move ship if it exceeds the matchfield to the left                   
                        matchfield_temp[yPos:yPos+size, xPos] = 1
                    else:
                        xPos -= 1
                        matchfield_temp[yPos:yPos+size, xPos] = 1

            elif curinput == 'up':
            # Checks if userinput is up
                if rotation == 'hori':
                # Checks if ship rotation is horizontal
                    if yPos - 1 < 0:
                        # Doesn't move ship if it exceeds the matchfield at the top
                        matchfield_temp[yPos, xPos:xPos+size] = 1
                    else:
                        yPos -= 1
                        matchfield_temp[yPos, xPos:xPos+size] = 1
                else:
                    if yPos - 1 < 0:
                    # Doesn't move ship if it exceeds the matchfield at the top
                        matchfield_temp[yPos:yPos+size, xPos] = 1    
                    else:
                        yPos -= 1
                        matchfield_temp[yPos:yPos+size, xPos] = 1

            elif curinput == 'r':
            # Checks if userinput is r for rotation
                if rotation == 'hori':
                # Checks if ship rotation is horizontal
                    if yPos + size > yGameSize:
                    # Doesn't rotate ship if it exceeds the matchfield to the right
                        matchfield_temp[yPos, xPos:xPos+size] = 1
                    else:
                        rotation = "verti"
                        matchfield_temp[yPos:yPos+size, xPos] = 1
                else:
                    if xPos + size > xGameSize:
                    # Doesn't move ship if it exceeds the matchfield at the bottom
                        matchfield_temp[yPos, xPos:xPos+size]
                    else:
                        rotation = "hori"
                        matchfield_temp[yPos, xPos:xPos+size] = 1

            elif curinput == 'enter':
            # Checks if userinput is enter
                # First ship doesn't need to check overlap -> directly placed
                i.position_x = xPos
                i.position_y = yPos
                used = False

                if not ship_list_placed:
                # First ship doesn't need to check overlap -> directly placed
                    used = False
                elif rotation == 'hori':
                # Sets ship (current object) rotation and moves current location
                    for j in range(next_ship.size):
                        screen.addstr(10,0,str(j))
                        screen.refresh()
                        if matchfield_logic[yPos,xPos+j] == 1:
                            used = True

                    if used == False:
                        i.rotation = "hori"
                        matchfield_temp[yPos, xPos:xPos+next_ship.size] = 1

                else:
                    for j in range(next_ship.size):
                        if matchfield_logic[yPos+j,xPos] == 1:
                            used = True
                            
                    if used == False:
                        i.rotation = "verti"
                        matchfield_temp[yPos:yPos+next_ship.size, xPos] = 1

                if used == False:
                    ship_list_placed.append(i)
                    if rotation == 'hori':
                    #Ship gets added to logical matchfield
                        matchfield_logic[yPos, xPos:xPos+size] = 1
                        matchfield_logic[yPos-1, xPos:xPos+size] = 1
                        matchfield_logic[yPos+1, xPos:xPos+size] = 1
                        matchfield_logic[yPos, xPos+size+1] = 1
                        matchfield_logic[yPos, xPos+size-1] = 1
                        yPos += 1
                    else:
                        matchfield_logic[yPos:yPos+size, xPos] = 1
                        matchfield_logic[yPos:yPos+size, xPos+1] = 1
                        matchfield_logic[yPos:yPos+size, xPos-1] = 1
                        matchfield_logic[yPos:yPos+size, xPos] = 1
                        matchfield_logic[yPos:yPos+size, xPos] = 1
                        xPos += 1
                    update_matchfield(game_y_pos, game_x_pos, matchfield_temp, screen)
                    break

            update_matchfield(game_y_pos, game_x_pos, matchfield_temp, screen)
        #return matchfield_visual, matchfield_logic

                    


                
def options():
    ''' Currently not in use '''
    print("hi")

def init_game(screen, mode):
    ''' Starts selected game mode '''
    screen.refresh()
    if mode == 'comp':
        singleplayer(screen)
    else:
        mulitplayer(screen)

    

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