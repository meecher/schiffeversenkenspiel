''' The game Schiffeversenken. '''
import random, time
import Ship
import numpy as np
import curses

__author__ = "1359831, Ruschmaritsch, 1357985, Ullmann, 135x, Lotte"
__credits__ = ""
__email__ = "david.ruschmaritsch@stud.fra-uas.de, marc.ullmann@stud.fra-uas.de, x@stud.fra-uas.de"
    

def multiplayer(screen):
    ''' Creates to matchfields '''
    yGameSize = 10
    xGameSize = 10
    game_y_pos = 3
    game_x_pos = 2
    game_end = True
    matchfield_ships_p1, ship_list_placed_p1, matchfield_visual_2 = create_matchfield(yGameSize,xGameSize,game_y_pos,game_x_pos,"comp",screen) 
    matchfield_ships_p2, ship_list_placed_p2, matchfield_visual_2_p2 = create_matchfield(yGameSize,xGameSize,game_y_pos,game_x_pos,"comp",screen) 
    matchfield_visual_hits_p1, matchfield_temp_hits_p1, matchfield_logic_hits_p1 = create_matchfield_hits(yGameSize,xGameSize, "p1", screen)
    matchfield_visual_hits_p2, matchfield_temp_hits_p2, matchfield_logic_hits_p2 = create_matchfield_hits(yGameSize,xGameSize, "p2", screen)
    
    yPos_p1 = 0
    xPos_p1 = 0
    yPos_p2 = 0
    xPos_p2 = 0

    while game_end:
        if len(ship_list_placed_p1) == 0:
            screen.clear()
            win_msg = "P2 Gewonnen"
            screen.addstr(curses.LINES // 2, curses.COLS // 2 - len(win_msg) // 2 - 10,win_msg, curses.A_REVERSE)
            game_end = False
            screen.refresh()
            time.sleep(10)
            break
        elif len(ship_list_placed_p2) == 0:
            screen.clear()
            win_msg = "P1 Gewonnen"
            screen.addstr(curses.LINES // 2, curses.COLS // 2 - len(win_msg) // 2 - 10,win_msg, curses.A_REVERSE)
            game_end = False
            screen.refresh()
            time.sleep(10)
            break
        yPos_p1, xPos_p1, matchfield_ships_p2, matchfield_logic_hits_p1, ship_list_placed_p2 = shoot(game_y_pos,game_x_pos, yPos_p1, xPos_p1, 
        matchfield_ships_p1, ship_list_placed_p1, matchfield_visual_2, matchfield_visual_hits_p1, matchfield_temp_hits_p1, matchfield_logic_hits_p1, 
        matchfield_ships_p2, ship_list_placed_p2, yGameSize, xGameSize, "p1", screen)

        yPos_p2, xPos_p2, matchfield_ships_p1, matchfield_logic_hits_p2, ship_list_placed_p1 = shoot(game_y_pos,game_x_pos,yPos_p2, xPos_p2, 
        matchfield_ships_p2, ship_list_placed_p2, matchfield_visual_2_p2, matchfield_visual_hits_p2, matchfield_temp_hits_p2, matchfield_logic_hits_p2,
        matchfield_ships_p1, ship_list_placed_p1, yGameSize, xGameSize, "p2", screen)


def singleplayer(screen):
    ''' Creates a matchfield for the player and the computer'''
    ''' Creates two matchfields '''
    yGameSize = 10
    xGameSize = 10
    game_y_pos = 3
    game_x_pos = 2
    game_end = True
    matchfield_ships_p1, ship_list_placed_p1, matchfield_visual_2 = create_matchfield(yGameSize,xGameSize,game_y_pos,game_x_pos,"comp",screen) 
    matchfield_ships_p2, ship_list_placed_p2, matchfield_visual_2_p2 = create_matchfield(yGameSize,xGameSize,game_y_pos,game_x_pos,"comp",screen) 
    matchfield_visual_hits_p1, matchfield_temp_hits_p1, matchfield_logic_hits_p1 = create_matchfield_hits(yGameSize,xGameSize, "p1", screen)
    matchfield_visual_hits_p2, matchfield_temp_hits_p2, matchfield_logic_hits_p2 = create_matchfield_hits(yGameSize,xGameSize, "comp", screen)
    
    yPos_p1 = 0
    xPos_p1 = 0
    yPos_p2 = 0
    xPos_p2 = 0

    already_hit = True
    direction = "" 
    hit = False
    last_hit = ()
    y_neg = True
    y_positive = True
    x_neg = True
    x_positive = True
    not_hit_two = False
    ship_hit = False
    

    while game_end:
        if len(ship_list_placed_p1) == 0:
            screen.clear()
            win_msg = "Computer hat gewonnen"
            screen.addstr(curses.LINES // 2, curses.COLS // 2 - len(win_msg) // 2 - 10,win_msg, curses.A_REVERSE)
            game_end = False
            screen.refresh()
            time.sleep(10)
            break
        elif len(ship_list_placed_p2) == 0:
            screen.clear()
            win_msg = "P1 Gewonnen"
            screen.addstr(curses.LINES // 2, curses.COLS // 2 - len(win_msg) // 2 - 10,win_msg, curses.A_REVERSE)
            game_end = False
            screen.refresh()
            time.sleep(10)
            break
        yPos_p1, xPos_p1, matchfield_ships_p1, matchfield_logic_hits_p1, ship_list_placed_p2 = shoot(game_y_pos,game_x_pos,yPos_p1, xPos_p1, matchfield_ships_p1, ship_list_placed_p1, matchfield_visual_2, 
        matchfield_visual_hits_p1, matchfield_temp_hits_p1, matchfield_logic_hits_p1, matchfield_ships_p2, 
        ship_list_placed_p2, yGameSize, xGameSize, "p1", screen)

        (ship_hit, not_hit_two, y_neg, y_positive, x_neg, x_positive, already_hit, direction, hit, last_hit, yPos_p2, xPos_p2, matchfield_ships_p1, 
        matchfield_logic_hits_p2, ship_list_placed_p1) = random_shot(game_y_pos, game_x_pos, ship_hit, not_hit_two, y_neg, y_positive, x_neg, x_positive, already_hit, direction, 
        hit, last_hit, yPos_p2, xPos_p2, matchfield_visual_2_p2, matchfield_ships_p2, ship_list_placed_p1, matchfield_visual_hits_p2, matchfield_logic_hits_p2, matchfield_ships_p1, 
        ship_list_placed_p1, yGameSize, xGameSize, "comp", screen)

def continue_game(game_y_pos, game_x_pos, yGameSize, xGameSize, screen):
    curinput = ""
    screen.addstr(game_y_pos+yGameSize+3,15,"Druecke Enter zum fortfahren.",curses.A_REVERSE)   

    while curinput != 'enter':
        curinput = userinput(screen)
       
    screen.addstr(game_y_pos+yGameSize+3,15,"                              ")

def create_matchfield_hits(ySize, xSize, player, screen):
    ''' Creates matchfields '''
    matchfield_visual = np.chararray((ySize, xSize))
    matchfield_visual[:] = "O"
    matchfield_temp = np.zeros((ySize, xSize))
    matchfield_logic = np.zeros((ySize, xSize))
    return matchfield_visual, matchfield_temp, matchfield_logic

def create_matchfield(ySize, xSize, game_y_pos, game_x_pos, player, screen):
    ''' Creates matchfields '''
    matchfield_visual = np.chararray((ySize, xSize))
    matchfield_visual_2 = np.chararray((ySize, xSize))
    matchfield_visual[:] = "O"
    matchfield_temp = np.zeros((ySize, xSize))
    matchfield_logic = np.zeros((ySize, xSize))
    matchfield_ship_pos = np.zeros((ySize, xSize))

    if player == 'p1' or player == 'p2':
        matchfield_visual, matchfield_ship_pos, ship_list_placed = set_ships(game_y_pos,game_x_pos,matchfield_visual,matchfield_temp,matchfield_logic,matchfield_ship_pos,ySize,xSize,player,screen)
    else:
        matchfield_visual, matchfield_ship_pos, ship_list_placed = set_ships_comp(game_y_pos,game_x_pos,matchfield_visual,matchfield_temp,matchfield_logic,matchfield_ship_pos,ySize,xSize,player,screen)
    return matchfield_ship_pos, ship_list_placed, matchfield_visual_2

def update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos, matchfield_visual, matchfield_temp, player, mode, screen):
    ''' Translates temporary matchfield to visual one and displays visuals '''
    i = game_y_pos
    counter = game_y_pos
    str_counter = 1
    screen.addstr(0,0,"           ")
    screen.addstr(game_y_pos+yGameSize+1,0,"        ")

    if player == 'p1':
        currentplayer = "Spieler 1:"
        screen.addstr(game_y_pos-3,0, currentplayer, curses.A_REVERSE)
    elif player == 'p2':
        currentplayer = "Spieler 2:"
        screen.addstr(game_y_pos-3,0, currentplayer, curses.A_REVERSE)
    else:
        currentplayer = "Computer:"
        screen.addstr(game_y_pos-3,0, currentplayer, curses.A_REVERSE)
    screen.addstr(game_y_pos+yGameSize+2,0, "Gegner: ")

    for x in range(xGameSize):
    # Increases x until gamesize is reached
        for y in range(yGameSize):
         # Increases y until gamesize is reached
            if matchfield_temp[y,x] == 1:
            # Places a x if temporal matchfield has a 1
                if player == "comp":
                    if mode == "secondary":
                        matchfield_visual[y,x] = "?"
                else:
                    matchfield_visual[y,x] = "X" 
            elif matchfield_temp[y,x] == 2:
                matchfield_visual[y,x] = "*" 
            elif matchfield_temp[y,x] == 3:
                matchfield_visual[y,x] = "%"  
            else:
                if player == "comp":
                    if mode == "secondary":
                        matchfield_visual[y,x] = "?" 
                else:
                    matchfield_visual[y,x] = "O" 

    for x in range(yGameSize):
    # Creates the coordinate systems of the entered size
        converted_counter = str(str_counter)
        screen.addstr(game_y_pos-2, game_x_pos+x*2, converted_counter+" ")
        screen.addstr(counter,game_x_pos-2, chr(65+x))

        screen.addstr(game_y_pos-1, game_x_pos+x, "_")
        screen.addstr(game_y_pos-1, game_x_pos+xGameSize+x, "_")
        screen.addstr(game_y_pos+yGameSize, game_x_pos+x, "_")
        screen.addstr(game_y_pos+yGameSize, game_x_pos+xGameSize+x, "_")
        screen.addstr(counter,game_x_pos-1, "|")
        screen.addstr(game_y_pos+yGameSize,game_x_pos-1, "|")
        screen.addstr(counter,game_x_pos+xGameSize+10, "|")
        screen.addstr(game_y_pos+yGameSize,game_x_pos+xGameSize+10, "|")

        counter+=1
        str_counter+=1

    for row in matchfield_visual.astype(str):
    # Converts matchfield in string and displays it
        string_conv = [str(int) for  int in row]
        current_str = ' '.join(string_conv)
        screen.addstr(i,game_x_pos,current_str)
        i+=1
    screen.refresh()

def userinput(screen):
    ''' Checks user input '''
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

def random_shot(game_y_pos, game_x_pos, ship_hit, not_hit_two, y_neg, y_positive, x_neg, x_positive, already_hit, direction, hit, last_hit, yPos, xPos, 
matchfield_visual_2, matchfield_own_ships, ship_list_placed_own, matchfield_visual, matchfield_logic, matchfield_ship_pos, ship_list_placed, yGameSize, xGameSize, player, screen):

    current_ships(game_y_pos,game_x_pos,xGameSize,yGameSize,ship_list_placed_own,ship_list_placed,screen)

    update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos,matchfield_visual, matchfield_logic, player, "primary", screen)
    update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos+30, matchfield_visual_2, matchfield_own_ships, player, "secondary", screen)
    while already_hit == True:
        yPos = random.randint(0, xGameSize-1)
        xPos = random.randint(0, yGameSize-1)
        # First ship doesn't need to check overlap -> directly placed
        current_ship = 0
        already_hit = False
        
        if matchfield_logic[yPos,xPos] == 2 or matchfield_logic[yPos,xPos] == 3:
        # Checks if field is already hit
            already_hit = True

    if already_hit == False:
        not_hit_two = True
        while not_hit_two == True:
            if ship_hit == True:
                if yPos + 1 >= yGameSize:
                    y_positive = False
                elif yPos - 1 < 0:
                    y_neg = False
                elif xPos + 1 > xGameSize:
                    x_positive = False
                elif xPos - 1 < 0:
                    x_neg = False
                
                if y_neg == True:
                    yPos -= 1
                    y_neg = True
                    direction = "y_neg"
                elif y_positive == True:
                    yPos += 1
                    y_positive = True
                    direction = "y_positive"
                if y_neg == False and y_positive == False:
                    if x_neg == True:
                        xPos -= 1
                        x_neg = True
                        direction = "x_neg"
                    elif x_positive == True:
                        xPos += 1
                        x_positive = True
                        direction = "x_positive"

            if matchfield_logic[yPos,xPos] == 3:
                # Checks if field is already hit
                    not_hit_two = True
                    if direction == 'y_neg':
                        y_neg = False
                        yPos += 1
                    if direction == 'y_positive':
                        y_positive = False
                        yPos -= 1
                    if direction == 'x_neg':
                        x_neg = False
                        xPos += 1
                    if direction == 'x_positive':
                        x_positive = False
                        xPos -= 1

            elif matchfield_logic[yPos,xPos] == 2:
                if direction == 'y_neg':
                    yPos -= 1
                if direction == 'y_positive':
                    yPos += 1
                if direction == 'x_neg':
                    xPos -= 1
                if direction == 'x_positive':
                    xPos += 1

            elif matchfield_logic[yPos,xPos] == 0:
                not_hit_two = False
    

    if already_hit == False:
        current_ship = 0
    # Checks if current field was already hit
        if matchfield_ship_pos[yPos,xPos] == 1:
        # Checks if a ship is placed on current field
            ship_hit = True
            matchfield_logic[yPos,xPos] = 2
            last_hit = (yPos,xPos)
            yPos = last_hit[0]
            xPos = last_hit[1]
            hit = True
            coordinates = (yPos, xPos)
            screen.addstr(game_y_pos+yGameSize+1,0,"Schiff getroffen.")
            screen.refresh()
            time.sleep(1)
            screen.addstr(game_y_pos+yGameSize+1,0,"                                        ")
            screen.refresh()
            for i in ship_list_placed:
            # Checks which ship gets hit
                counter = 0
                for y in i.cords:
                # Goes through the coordinates of the currently selected ship
                    if coordinates == i.cords[counter]:
                    # Deletes ships coordinates if it is hit
                        i.cords.pop(counter)
                    else:
                        counter += 1
                if not i.cords:
                # Deletes ship if all coordinates are hit
                    del i
                    last_hit = ()
                    ship_hit = False
                    hit = False
                    if ship_hit == False:
                        already_hit = True
                    y_neg = True
                    x_neg = True
                    y_positive = True
                    x_positive = True
                    ship_list_placed.pop(current_ship)
                    screen.addstr(game_y_pos+yGameSize+1,0,"*****Schiff zerstört.*****", curses.A_REVERSE)
                    screen.refresh()
                    time.sleep(1)
                    screen.addstr(game_y_pos+yGameSize+1,0,"                                        ")
                    screen.refresh()
                current_ship += 1
        elif matchfield_ship_pos[yPos,xPos] == 0:
        # Checks if field is empty
            matchfield_logic[yPos,xPos] = 3

            if ship_hit == True:
                if direction == 'y_neg':
                    y_neg = False
                    yPos += 1
                if direction == 'y_positive':
                    y_positive = False
                    yPos -= 1
                if direction == 'x_neg':
                    x_neg = False
                    xPos += 1
                if direction == 'x_positive':
                    x_positive = False
                    xPos -= 1

            if ship_hit == False:
                already_hit = True

            screen.addstr(game_y_pos+yGameSize+1,0,"Kein Schiff bei dieser Position")
            screen.refresh()
            hit = False
            time.sleep(1)
            screen.addstr(game_y_pos+yGameSize+1,0,"                                        ")
            screen.refresh()
        
    update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos,matchfield_visual, matchfield_logic, player, "primary", screen)
    continue_game(game_y_pos,game_x_pos,yGameSize,xGameSize,screen)
    return ship_hit, not_hit_two, y_neg, y_positive, x_neg, x_positive, already_hit, direction, hit, last_hit, yPos, xPos, matchfield_ship_pos, matchfield_logic, ship_list_placed

def set_ships_comp(game_y_pos,game_x_pos, matchfield_visual, matchfield_temp, matchfield_logic, matchfield_ship_pos, yGameSize, xGameSize, player, screen):
    ''' Creates and sets all ships in order from biggest to smallest '''
    rotation = "hori"
    yPos = 0
    xPos = 0
    rotation_choice = ["hori", "verti"]
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
    ship_list = [ship_5, ship_4a, ship_4b, ship_3a, ship_3b, ship_3c, ship_2a, ship_2b, ship_2c, ship_2d]
    ship_list_placed = []
        
    for i in ship_list:
    # Places all necessary ships
        yStatic = False
        choice = ["y", "x"]
        ship_placed = False
        yPos_rand = yPos
        xPos_rand = xPos
        size = i.size
        counter_rot = 0
        counter_pos = 0

        rotation = random.choice(rotation_choice)

        if rotation == 'hori':
            if random.choice(choice) == "y":
            # Returns random choice; defines that y is increased everytime x reaches the gamesize
            # Chooses y and x according to the size of the ship and the gamesize
                yPos_rand = random.randrange(0,yGameSize-1)
                yStatic = True
                xPos_rand = 0
            else:
                xPos_rand = random.randrange(0,xGameSize-size)
                yPos_rand = 0
        else: 
            if random.choice(choice) == "y":
            # Returns random choice; defines that y is increased everytime x reaches the gamesize;
            # Chooses y and x according to the size of the ship and the gamesize
                yPos_rand = random.randrange(0,yGameSize-size)
                yStatic = True
                xPos_rand = 0
            else:
                xPos_rand = random.randrange(0,xGameSize-1)
                yPos_rand = 0

        while ship_placed == False:
        # Selects coordinates for the ship
            changed = False
            if counter_rot >= 99:
            # Changes rotation after 99 tries
                if rotation == 'hori':
                # Changes rotation
                    rotation = "verti"
                else:
                    rotation = "hori"
                counter_rot = 0


            matchfield_temp[yPos_rand, xPos_rand:yPos_rand+size] = 0
            matchfield_temp[yPos_rand:yPos_rand+size, xPos_rand] = 0  

            
            if rotation == 'hori':
            # Checks if ship rotation is horizontal
                if yStatic == True:
                # Increases y and resets x after gamesize is reached
                    if yPos_rand + 1 > yGameSize - 1:
                    # Resets y and x if the gamesize is reached
                        yPos_rand = 0
                        xPos_rand = 0
                    elif xPos_rand == xGameSize - 1:
                    # Resets x if it reaches the gamesize and increases y
                        yPos_rand += 1
                        xPos_rand = 0
                else:
                    if xPos_rand + 1 + size > xGameSize - 1:
                    # Resets x and y if the gamesize is reached
                        xPos_rand = 0
                        yPos_rand = 0
                    elif yPos_rand == yGameSize - 1:
                    # Resets y if it reaches the gamesize increases y
                        xPos_rand += 1
                        yPos_rand = 0
                #counter_pos = 0
                if xPos_rand + size > xGameSize - 1:
                # Doesn't move ship if it exceeds the matchfield
                    matchfield_temp[yPos, xPos:xPos+size] = 1 
                else:                
                    matchfield_temp[yPos_rand, xPos_rand:xPos_rand+size] = 1
                    changed = True
            else:
                if yStatic == True:
                # Increases y and resets x after gamesize is reached
                    if yPos_rand + 1 + size > yGameSize - 1:
                    # Resets y and x if the gamesize is reached
                        yPos_rand = 0
                        xPos_rand = 0
                    elif xPos_rand == xGameSize - 1:
                    # Resets x if it reaches the gamesize and increases y
                        yPos_rand += 1
                        xPos_rand = 0
                else:
                    if xPos_rand + 1 > xGameSize - 1:
                    # Resets x and y if the gamesize is reached
                        xPos_rand = 0
                        yPos_rand = 0
                    elif yPos_rand == yGameSize - 1:
                    # Resets y if it reaches the gamesize increases y
                        xPos_rand += 1
                        yPos_rand = 0
                #counter_pos = 0
                if yPos_rand + size >= yGameSize - 1:
                # Doesn't move ship if it exceeds the matchfield
                    matchfield_temp[yPos:yPos+size, xPos] = 1
                else:
                    matchfield_temp[yPos_rand:yPos_rand+size, xPos_rand] = 1
                    changed = True
            
            if changed == True:
            # Cheks if coordinates have changed
                used = False
                if not ship_list_placed:
                # First ship doesn't need to check overlap -> directly placed
                    used = False
                elif rotation == 'hori':
                # Sets ship (current object) rotation and moves current location
                    for j in range(size):
                    # Loop for the current ship size
                        if matchfield_logic[yPos_rand,xPos_rand+j] == 1:
                        # Checks if any field of the horizontal ship is already used
                            used = True
                            matchfield_temp[yPos, xPos:xPos+size] = 1
                            break
                else:
                    for j in range(size):
                    # Loop for the current ship size
                        if matchfield_logic[yPos_rand+j,xPos_rand] == 1:
                        # Checks if any field of the vertical ship is already used
                            used = True
                            matchfield_temp[yPos:yPos+size, xPos] = 1
                            break

                if used == False:
                # If the space is free the ship can be placed
                    i.rotation = rotation
                    i.position_x = xPos_rand
                    i.position_y = yPos_rand
                    i.ship_cords()
                    ship_list_placed.append(i)
                    ship_placed = True

                    if rotation == 'hori':
                    #Reserves spaces for the ship within the logical matchfield for horizontal ships
                        matchfield_logic[yPos_rand, xPos_rand:xPos_rand+size] = 1
                        matchfield_ship_pos[yPos_rand, xPos_rand:xPos_rand+size] = 1
                        # Below checks the spaces around the ship and reserves the place
                        if (yPos_rand-1 >= 0):
                            matchfield_logic[yPos_rand-1, xPos_rand:xPos_rand+size] = 1
                        if (xPos_rand+size+1 <= xGameSize):
                            matchfield_logic[yPos_rand, xPos_rand+size] = 1
                        if (xPos_rand-1 >= 0):
                            matchfield_logic[yPos_rand, xPos_rand-1] = 1
                        if (yPos_rand+1 < yGameSize):
                            matchfield_logic[yPos_rand+1, xPos_rand:xPos_rand+size] = 1
                            yPos += 1
                    else:
                    #Reserves spaces for the ship within the logical matchfield for vertical ships
                        matchfield_logic[yPos_rand:yPos_rand+size, xPos_rand] = 1
                        matchfield_ship_pos[yPos_rand:yPos_rand+size, xPos_rand] = 1
                        # Below checks the spaces around the ship and reserves the place
                        if (xPos_rand-1 >= 0):
                            matchfield_logic[yPos_rand:yPos_rand+size, xPos_rand-1] = 1
                        if (yPos_rand+size+1 <= yGameSize):
                            matchfield_logic[yPos_rand+size, xPos_rand] = 1
                        if (yPos_rand-1 >= 0):
                            matchfield_logic[yPos_rand-1, xPos_rand] = 1
                        if (xPos_rand+1 < xGameSize):
                            matchfield_logic[yPos_rand:yPos_rand+size, xPos_rand+1] = 1
                            xPos += 1

            if yStatic == True:
            # Increases x or y according to leading coordinate
                xPos_rand += 1
            else:
                yPos_rand += 1  
            counter_pos += 1      
            counter_rot += 1
        #update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos,matchfield_visual, matchfield_logic, player, "primary", screen)
    return matchfield_visual, matchfield_ship_pos, ship_list_placed

def set_ships(game_y_pos,game_x_pos, matchfield_visual, matchfield_temp, matchfield_logic, matchfield_ship_pos, yGameSize, xGameSize, player, screen):
    ''' Creates and sets all ships in order from biggest to smallest '''
    rotation = "hori"
    curinput = ""
    counter = 0
    yPos = 0
    xPos = 0
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
    ship_list = [ship_5, ship_4a, ship_4b, ship_3a, ship_3b, ship_3c, ship_2a, ship_2b, ship_2c, ship_2d]
    ship_list_placed = []
    
    screen.keypad(1)
    curses.mousemask(-1)
        
    for i in ship_list:
    # Places all necessary ships
        size = i.size
        if counter == len(ship_list)-1:
        # Checks if the last ship is placed
            counter = counter
        else:
            counter += 1

        next_ship = ship_list[counter]
        last_ship = ship_list[counter-1]

        if rotation == 'hori':
        # Draws ship on horizontal axis
            matchfield_temp[yPos, xPos:xPos+size] = 1
        else: 
        # Draws ship on vertical axis
            matchfield_temp[yPos:yPos+size, xPos] = 1
        
        update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos,matchfield_visual, matchfield_temp, player, "primary", screen)

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

                update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos,matchfield_visual, matchfield_temp, player, "primary", screen)

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
                        matchfield_temp[yPos:yPos+size, xPos] = 1
                    else:
                        rotation = "hori"
                        matchfield_temp[yPos, xPos:xPos+size] = 1

            elif curinput == 'enter':
            # Checks if userinput is enter
                # First ship doesn't need to check overlap -> directly placed
                used = False

                if not ship_list_placed:
                # First ship doesn't need to check overlap -> directly placed
                    used = False
                elif rotation == 'hori':
                # Sets ship (current object) rotation and moves current location
                    for j in range(size):
                    # Loop for the current ship size
                        if matchfield_logic[yPos,xPos+j] == 1:
                        # Checks if any field of the horizontal ship is already used
                            used = True
                            screen.addstr(game_y_pos+yGameSize+1,0,"Schiff kann hier nicht platziert werden.")
                            screen.refresh()
                            time.sleep(0.1)
                            screen.addstr(game_y_pos+yGameSize+1,0,"                                        ")
                            screen.refresh()
                            matchfield_temp[yPos, xPos:xPos+size] = 1

                else:
                    for j in range(size):
                    # Loop for the current ship size
                        if matchfield_logic[yPos+j,xPos] == 1:
                        # Checks if any field of the vertical ship is already used
                            used = True
                            screen.addstr(game_y_pos+yGameSize+1,0,"Schiff kann hier nicht platziert werden.")
                            screen.refresh()
                            time.sleep(0.1)
                            screen.addstr(game_y_pos+yGameSize+1,0,"                                        ")
                            screen.refresh()
                            matchfield_temp[yPos:yPos+size, xPos] = 1
                            

                if used == False:
                # If the space is free the ship can be placed
                    i.rotation = rotation
                    i.position_x = xPos
                    i.position_y = yPos
                    i.ship_cords()
                    ship_list_placed.append(i)
                    if rotation == 'hori':
                    #Reserves spaces for the ship within the logical matchfield for horizontal ships
                        matchfield_logic[yPos, xPos:xPos+size] = 1
                        matchfield_ship_pos[yPos, xPos:xPos+size] = 1
                        # Below checks the spaces around the ship and reserves the place
                        if (yPos-1 >= 0):
                            matchfield_logic[yPos-1, xPos:xPos+size] = 1
                        if (xPos+size+1 <= xGameSize):
                            matchfield_logic[yPos, xPos+size] = 1
                        if (xPos-1 >= 0):
                            matchfield_logic[yPos, xPos-1] = 1
                        if (yPos+1 < yGameSize):
                            matchfield_logic[yPos+1, xPos:xPos+size] = 1
                            yPos += 1
                    else:
                    #Reserves spaces for the ship within the logical matchfield for vertical ships
                        matchfield_logic[yPos:yPos+size, xPos] = 1
                        matchfield_ship_pos[yPos:yPos+size, xPos] = 1
                        # Below checks the spaces around the ship and reserves the place
                        if (xPos-1 >= 0):
                            matchfield_logic[yPos:yPos+size, xPos-1] = 1
                        if (yPos+size+1 <= yGameSize):
                            matchfield_logic[yPos+size, xPos] = 1
                        if (yPos-1 >= 0):
                            matchfield_logic[yPos-1, xPos] = 1
                        if (xPos+1 < xGameSize):
                            matchfield_logic[yPos:yPos+size, xPos+1] = 1
                            xPos += 1       
                    update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos,matchfield_visual, matchfield_temp, player, "primary", screen)
                    break

            update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos,matchfield_visual, matchfield_temp, player, "primary", screen)
    continue_game(game_y_pos,game_x_pos,yGameSize,xGameSize,screen)
    return matchfield_visual, matchfield_ship_pos, ship_list_placed

def current_ships(game_y_pos, game_x_pos, xGameSize, yGameSize, ship_list_placed_own, ship_list_placed_enemy, screen):
    ships_own = [0,0,0,0]
    ships_enemy = [0,0,0,0]

    for i in ship_list_placed_own:
        if i.size == 5:
            ships_own[0] += 1
        elif i.size == 4:
            ships_own[1] += 1
        elif i.size == 3:
            ships_own[2] += 1
        elif i.size == 2:
            ships_own[3] += 1    
    
    for i in ship_list_placed_enemy:
        if i.size == 5:
            ships_enemy[0] += 1
        elif i.size == 4:
            ships_enemy[1] += 1
        elif i.size == 3:
            ships_enemy[2] += 1
        elif i.size == 2:
            ships_enemy[3] += 1    
    
    ships_own_str = ("Schlachtschiff " + str(ships_own[0]) + "x, Kreuzer " + str(ships_own[1]) + 
    "x, Zerstoerer " + str(ships_own[2]) + "x, U-Boote " + str(ships_own[3]) + "x")
    ships_enemy_str = ("Schlaftschiff " + str(ships_enemy[0]) + "x, Kreuzer " + str(ships_enemy[1]) + 
    "x, Zerstoerer " + str(ships_enemy[2]) + "x, U-Boote " + str(ships_enemy[3]) + "x")

    screen.addstr(0,11,"                                                         ")
    screen.addstr(0,11,ships_own_str)
    screen.addstr(game_y_pos+yGameSize+2,10,"                                                         ")
    screen.addstr(game_y_pos+yGameSize+2,8,ships_enemy_str)
    screen.refresh()
     
def shoot(game_y_pos,game_x_pos, yPos, xPos, matchfield_own_ships, ship_list_placed_own, matchfield_visual_2, matchfield_visual, matchfield_temp, matchfield_logic, matchfield_ship_pos, ship_list_placed, yGameSize, xGameSize, player, screen):
    ''' Creates and sets all ships in order from biggest to smallest '''
    counter = 0
    curinput = ""
    screen.keypad(1)
    curses.mousemask(-1)

    current_ships(game_y_pos,game_x_pos,xGameSize,yGameSize,ship_list_placed_own,ship_list_placed,screen)
    
    matchfield_temp[yPos,xPos] = 1        
    update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos, matchfield_visual, matchfield_temp, player, "primary", screen)
    update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos+30,matchfield_visual_2, matchfield_own_ships, player, "secondary", screen)

    while curinput != ord('q'):
    # Position of ship
        yPos_cur = 0
        xPos_cur = 0
        for i in range(xGameSize):
        # Updates temporal matchfield with hits and misses
            for y in range(yGameSize):
            # Converts logic to temporal matchfield
                if matchfield_logic[yPos_cur,xPos_cur] == 1:
                    matchfield_temp[yPos_cur,xPos_cur] = 1
                elif matchfield_logic[yPos_cur,xPos_cur] == 2:
                    matchfield_temp[yPos_cur,xPos_cur] = 2
                elif matchfield_logic[yPos_cur,xPos_cur] == 3:
                    matchfield_temp[yPos_cur,xPos_cur] = 3
                yPos_cur += 1
            yPos_cur = 0
            xPos_cur += 1
        update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos, matchfield_visual, matchfield_temp, player, "primary", screen)

        matchfield_temp[yPos, xPos] = 0

        curinput = userinput(screen)

        if curinput == 'right':
        # Checks if userinput is right
            if xPos + 1 >= xGameSize:
            # Doesn't move ship if it exceeds the matchfield to the right
                matchfield_temp[yPos, xPos] = 1 
            else:                
                xPos += 1
                matchfield_temp[yPos, xPos] = 1

        elif curinput == 'down':
        # Checks if userinput is down
            # Checks if ship rotation is horizontal
            if yPos + 1 >= yGameSize:
            # Doesn't move ship if it exceeds the matchfield at the bottom
                matchfield_temp[yPos, xPos] = 1
            else:
                yPos += 1
                matchfield_temp[yPos, xPos] = 1
    
        elif curinput == 'left':
        # Checks if userinput is left
            if xPos - 1 < 0:
                # Doesn't move ship if it exceeds the matchfield to the left
                matchfield_temp[yPos, xPos] = 1
            else:
                xPos -= 1
                matchfield_temp[yPos, xPos] = 1

        elif curinput == 'up':
        # Checks if userinput is up
            if yPos - 1 < 0:
                # Doesn't move ship if it exceeds the matchfield at the top
                matchfield_temp[yPos, xPos] = 1
            else:
                yPos -= 1
                matchfield_temp[yPos, xPos] = 1

        elif curinput == 'enter':
        # Checks if userinput is enter
            # First ship doesn't need to check overlap -> directly placed
            current_ship = 0
            already_hit = False

            if matchfield_logic[yPos,xPos] == 2 or matchfield_logic[yPos,xPos] == 3:
            # Checks if field is already hit
                screen.addstr(game_y_pos+yGameSize+1,0,"Dieses Feld wurde schon beschossen.")
                screen.refresh()
                time.sleep(1)
                screen.addstr(game_y_pos+yGameSize+1,0,"                                        ")
                screen.refresh()
                already_hit = True

            if already_hit == False:
            # Checks if current field was already hit
                if matchfield_ship_pos[yPos,xPos] == 1:
                # Checks if a ship is placed on current field
                    matchfield_logic[yPos,xPos] = 2
                    coordinates = (yPos, xPos)
                    screen.addstr(game_y_pos+yGameSize+1,0,"Schiff getroffen.")
                    screen.refresh()
                    time.sleep(1)
                    screen.addstr(game_y_pos+yGameSize+1,0,"                                        ")
                    screen.refresh()

                    if xPos + 1 >= xGameSize:
                    # Changes field's position
                        if yPos + 1 >= yGameSize:
                            matchfield_temp[yPos, xPos] = 1
                        else:
                            yPos += 1
                            matchfield_temp[yPos, xPos] = 1
                    else:
                        xPos += 1
                        matchfield_temp[yPos, xPos] = 1

                    for i in ship_list_placed:
                    # Checks which ship gets hit
                        counter = 0
                        for y in i.cords:
                        # Goes through the coordinates of the currently selected ship
                            if coordinates == i.cords[counter]:
                            # Deletes ships coordinates if it is hit
                                i.cords.pop(counter)
                            else:
                                counter += 1
                        if not i.cords:
                        # Deletes ship if all coordinates are hit
                            del i
                            ship_list_placed.pop(current_ship)
                            screen.addstr(game_y_pos+yGameSize+1,0,"*****Schiff zerstört.*****", curses.A_REVERSE)
                            screen.refresh()
                            time.sleep(1)
                            screen.addstr(game_y_pos+yGameSize+1,0,"                                        ")
                            screen.refresh()
                        current_ship += 1
                    break
                elif matchfield_ship_pos[yPos,xPos] == 0:
                # Checks if field is empty
                    screen.addstr(game_y_pos+yGameSize+1,0,"Kein Schiff bei dieser Position")
                    screen.refresh()
                    time.sleep(1)
                    screen.addstr(game_y_pos+yGameSize+1,0,"                                        ")
                    screen.refresh()
                    matchfield_logic[yPos,xPos] = 3
                    
                    if xPos + 1 >= xGameSize:
                    # Changes field's position
                        if yPos + 1 >= yGameSize:
                            matchfield_temp[yPos, xPos] = 1
                        else:
                            yPos += 1
                            matchfield_temp[yPos, xPos] = 1
                    else:
                        xPos += 1
                        matchfield_temp[yPos, xPos] = 1

                    break
            update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos, matchfield_visual, matchfield_temp, player, "primary", screen)
        update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos, matchfield_visual, matchfield_temp, player, "primary", screen)
    continue_game(game_y_pos,game_x_pos,yGameSize,xGameSize,screen)
    return yPos, xPos, matchfield_ship_pos, matchfield_logic, ship_list_placed

def init_game(screen, mode):
    ''' Starts selected game mode '''
    curses.curs_set(0)
    screen.refresh()
    if mode == 'comp':
        singleplayer(screen)
    else:
        multiplayer(screen)

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
    screen.addstr(curses.LINES//2+5,10,"Wählen sie den Spielmodus aus...")
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
    start_message = ("Willkommen im Spiel Schiffeversenken! Klicken sie in der Mitte auf Schiffeversenken oder drücken sie <Enter>")
    curses.mousemask(-1)
    curses.mouseinterval(0)
    curses.curs_set(0)
    screen.keypad(True)
    curinput = ""

    pressed = False
    x, y = 0, 0
    screen.addstr(curses.LINES // 3,curses.COLS // 2 - len(start_message) //2,start_message)
    screen.addstr(curses.LINES // 2,
    curses.COLS // 2 - len(beginning) // 2,
    beginning, curses.A_REVERSE)

    while curinput != 'q': 
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

def main():
    ''' Starts the game '''
    return curses.wrapper(c_main)    

if __name__ == "__main__":
    main()
    input()