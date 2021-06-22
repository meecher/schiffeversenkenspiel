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
    matchfield_visual_p1, matchfield_ships_p1 = create_matchfield(yGameSize,xGameSize,"p1",screen) 
    matchfield_visual_p2, matchfield_ships_p2 = create_matchfield(yGameSize,xGameSize,"p2",screen) 
    matchfield_visual_hits_p1, matchfield_temp_hits_p1, matchfield_logic_hits_p1 = create_matchfield_hits(10,10, "p1", screen)
    matchfield_visual_hits_p2, matchfield_temp_hits_p2, matchfield_logic_hits_p2 = create_matchfield_hits(10,10, "p2", screen)
    
    shoot(matchfield_visual_hits_p1, matchfield_temp_hits_p1, matchfield_logic_hits_p1, matchfield_ships_p2, yGameSize, xGameSize, "p1", screen)

def singleplayer(screen):
    ''' Creates a matchfield for the player and the computer'''
    yGameSize = 10
    xGameSize = 10
    matchfield_visual_p1, matchfield_ships_p1 = create_matchfield(yGameSize,xGameSize,"comp",screen) 
    matchfield_visual_p2, matchfield_ships_p2 = create_matchfield(yGameSize,xGameSize,"comp",screen) 
    matchfield_visual_hits_p1, matchfield_temp_hits_p1, matchfield_logic_hits_p1 = create_matchfield_hits(10,10, "p1", screen)
    matchfield_visual_hits_p2, matchfield_temp_hits_p2, matchfield_logic_hits_p2 = create_matchfield_hits(10,10, "p2", screen)
    
    shoot(matchfield_visual_hits_p1, matchfield_temp_hits_p1, matchfield_logic_hits_p1, matchfield_ships_p2, yGameSize, xGameSize, "p1", screen)

    #matchfield_visual_p1, matchfield_ships_p1 = create_matchfield(10,10,"p1",screen) 
    #matchfield_visual_p2, matchfield_ships_p2 = create_matchfield(10,10,"comp",screen)


def create_matchfield_hits(ySize, xSize, player, screen):
    ''' Creates matchfields '''
    matchfield_visual = np.chararray((ySize, xSize))
    matchfield_visual[:] = "O"
    matchfield_temp = np.zeros((ySize, xSize))
    matchfield_logic = np.zeros((ySize, xSize))
    return matchfield_visual, matchfield_temp, matchfield_logic

def create_matchfield(ySize, xSize, player, screen):
    ''' Creates matchfields '''
    matchfield_visual = np.chararray((ySize, xSize))
    matchfield_visual[:] = "O"
    matchfield_temp = np.zeros((ySize, xSize))
    matchfield_logic = np.zeros((ySize, xSize))
    matchfield_ship_pos = np.zeros((ySize, xSize))

    if player == 'p1' or player == 'p2':
        matchfield_visual, matchfield_ship_pos = set_ships(2,2,matchfield_visual,matchfield_temp,matchfield_logic,matchfield_ship_pos,ySize,xSize,player,screen)
    else:
        matchfield_visual, matchfield_ship_pos = set_ships_comp(2,2,matchfield_visual,matchfield_temp,matchfield_logic,matchfield_ship_pos,ySize,xSize,player,screen)
    return matchfield_visual, matchfield_ship_pos

def update_matchfield(yGameSize, xGameSize, yPos, xPos, matchfield_visual, matchfield_temp, player, screen):
    ''' Translates temporary matchfield to visual one and displays visuals '''
    i = yPos
    counter = 2
    str_counter = 1
    eingabe = yGameSize

    if player == 'p1':
        currentplayer = "Spieler 1"
        screen.addstr(0,0, currentplayer)
    else:
        currentplayer = "Spieler 2"
        screen.addstr(0,0, currentplayer)

    for x in range(xGameSize):
    # Increases x until gamesize is reached
        for y in range(yGameSize):
         # Increases y until gamesize is reached
            if matchfield_temp[y,x] == 1:
            # Places a x if temporal matchfield has a 1
                matchfield_visual[y,x] = "X"
            else:
                matchfield_visual[y,x] = "O"

    for x in range(eingabe):
    # Creates the coordinate systems of the entered size
        converted_counter = str(str_counter)
        screen.addstr(1,2+x*2, converted_counter+" ")
        screen.addstr(counter,0, chr(65+x))
        counter+=1
        str_counter+=1

    for row in matchfield_visual.astype(str):
    # Converts matchfield in string and displays it
        string_conv = [str(int) for  int in row]
        current_str = ' '.join(string_conv)
        screen.addstr(i,xPos,current_str)
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

def random_shot(screen, xGamesize, yGamesize, matchfield_logic):
    ''' Random shot function for the AI ''' # Wird später in den Code eingebaut
    hit = False
    doublehit = False
    newshot = True
    hitcounter = 0
    check_two_sides = 0
    current_player = random.randint(1,2)

    while True:
        if current_player == 1:
            current_player = 2

        elif current_player == 2:
            if newshot == True:
                x = random.randint(0, xGamesize)
                y = random.randint(0, yGamesize)
                directions = []
                yCurrent = y
                xCurrent = x
                xStart = x
                yStart = y
                # Below checks the surrounding squares around the shot: Sets possible directions.
                # Possible directions are when the logical number of the matchfield is 0 or 1 and doesnt touch borders.
                if x > 0 and (matchfield_logic[y,x-1] == 0 or matchfield_logic[y,x-1] == 1): directions.append("Westen")
                if x < xGamesize and (matchfield_logic[y,x+1] == 0 or matchfield_logic[y,x+1] == 1): directions.append("Osten")
                if y > 0 and (matchfield_logic[y-1,x] == 0 or matchfield_logic[y-1,x] == 1): directions.append("Norden")
                if y < yGamesize and (matchfield_logic[y+1,x] == 0 or matchfield_logic[y+1,x] == 1): directions.append("Süden")
                newshot = False

            if hit == False and doublehit == False:
                if matchfield_logic[y,x] == 1: #1 is the logical indication for a ship
                    hit = True
                    screen.addstr(yGamesize,0,"The first AI shot hit")
                    screen.refresh()
                    hitcounter += 1
                    matchfield_logic[y,x] = 2  #2 is the logical indication for a hit
                else: 
                    matchfield_logic[y,x] = 3 #3 is the logical indication for a miss

            # First shot hit. Shoots at the nearby field with a random direction until hit.
            else:
                if doublehit == False:
                    random_direction = random.sample(directions,1)
                    directions.remove(random_direction)
                    if random_direction == "Norden":
                        if matchfield_logic[yCurrent-1,xCurrent] == 1:
                            hitcounter += 1
                            yCurrent -= 1
                            matchfield_logic[yCurrent,xCurrent] = 2
                        else: 
                            hit = False
                            matchfield_logic[yCurrent-1,xCurrent] = 3
                    if random_direction == "Osten":
                        if matchfield_logic[yCurrent,xCurrent+1] == 1:
                            hitcounter += 1
                            xCurrent += 1
                            matchfield_logic[yCurrent,xCurrent] = 2
                        else: 
                            hit = False
                            matchfield_logic[yCurrent,xCurrent+1] = 3
                    if random_direction == "Süden":
                        if matchfield_logic[yCurrent+1,xCurrent] == 1:
                            hitcounter += 1
                            yCurrent += 1
                            matchfield_logic[yCurrent,xCurrent] = 2
                        else: 
                            hit = False
                            matchfield_logic[yCurrent+1,xCurrent] = 3
                    if random_direction == "Westen":
                        if matchfield_logic[yCurrent,xCurrent-1] == 1:
                            hitcounter += 1
                            xCurrent -= 1
                            matchfield_logic[yCurrent,xCurrent] = 2
                        else: 
                            hit = False
                            matchfield_logic[yCurrent,xCurrent-1] = 3

                    if hit == True: 
                        screen.addstr(yGamesize,0,"The AI shot hit again")
                        screen.refresh()
                        doublehit = True

                    else: 
                        screen.addstr(yGamesize,0,"The AI shot missed")
                        screen.refresh()
                # When 2 shots land on one ship doublehit is True and now the ship can only be in 2 directions
                else:
                    #
                    # NORTH
                    #
                    if random_direction == "Norden":
                        if matchfield_logic[yCurrent-1,xCurrent] == 1:
                            hitcounter += 1
                            yCurrent -= 1
                            matchfield_logic[yCurrent,xCurrent] = 2
                        elif matchfield_logic[yCurrent-1,xCurrent] == 3:
                        # If the next field shot at would be a field already shot at, it changes to opposite direction and checks the next field form the starting x,y point.
                            yCurrent = yStart
                            xCurrent = xStart
                            random_direction = "Süden"
                            check_two_sides += 1
                            if matchfield_logic[yCurrent+1,xCurrent] == 1:
                                hitcounter += 1
                                yCurrent += 1
                                matchfield_logic[yCurrent,xCurrent] = 2
                            else:
                                hit = False
                                matchfield_logic[yCurrent+1,xCurrent] = 3
                                check_two_sides += 1
                        else:
                            hit = False
                            matchfield_logic[yCurrent-1,xCurrent] = 3
                            check_two_sides += 1
                            random_direction = "Süden"
                    #
                    # EAST
                    #
                    if random_direction == "Osten":
                        if matchfield_logic[yCurrent,xCurrent+1] == 1:
                            hitcounter += 1
                            xCurrent += 1
                            matchfield_logic[yCurrent,xCurrent] = 2
                        elif matchfield_logic[yCurrent,xCurrent+1] == 3:
                        # If the next field shot at would be a field already shot at, it changes to opposite direction and checks the next field form the starting x,y point.
                            yCurrent = yStart
                            xCurrent = xStart
                            random_direction = "Westen"
                            check_two_sides += 1
                            if matchfield_logic[yCurrent,xCurrent-1] == 1:
                                hitcounter += 1
                                xCurrent -= 1
                                matchfield_logic[yCurrent,xCurrent] = 2
                            else: 
                                hit = False
                                matchfield_logic[yCurrent,xCurrent-1] = 3
                                check_two_sides += 1
                        else: 
                            hit = False
                            matchfield_logic[yCurrent,xCurrent+1] = 3
                            check_two_sides += 1
                            random_direction = "Westen"
                    #
                    # SOUTH
                    #
                    if random_direction == "Süden":
                        if matchfield_logic[yCurrent+1,xCurrent] == 1:
                            hitcounter += 1
                            yCurrent += 1
                            matchfield_logic[yCurrent,xCurrent] = 2
                        elif matchfield_logic[yCurrent+1,xCurrent] == 3:
                        # If the next field shot at would be a field already shot at, it changes to opposite direction and checks the next field form the starting x,y point.
                            yCurrent = yStart
                            xCurrent = xStart
                            random_direction = "Norden"
                            check_two_sides += 1
                            if matchfield_logic[yCurrent-1,xCurrent] == 1:
                                hitcounter += 1
                                yCurrent -= 1
                                matchfield_logic[yCurrent,xCurrent] = 2
                            else:
                                hit = False
                                matchfield_logic[yCurrent-1,xCurrent] = 3
                                check_two_sides += 1
                        else:
                            hit = False
                            matchfield_logic[yCurrent+1,xCurrent] = 3
                            check_two_sides += 1
                            random_direction = "Norden"
                    #
                    # WEST
                    #
                    if random_direction == "Westen":
                        if matchfield_logic[yCurrent,xCurrent-1] == 1:
                            hitcounter += 1
                            xCurrent -= 1
                            matchfield_logic[yCurrent,xCurrent-1] = 2
                        elif matchfield_logic[yCurrent,xCurrent-1] == 3:
                            yCurrent = yStart
                            xCurrent = xStart
                            random_direction = "Osten"
                            check_two_sides += 1
                            if matchfield_logic[yCurrent,xCurrent+1] == 1:
                                hitcounter += 1
                                xCurrent += 1
                                matchfield_logic[yCurrent,xCurrent] = 2
                            else: # HIER ERNEUTE ABFRAGE OB ES AUF EIN BENUTZES FELD STÖSST, DANN WÄRE DAS SCHIFF DIREKT VERSENKT!
                                hit = False
                                matchfield_logic[yCurrent,xCurrent+1] = 3
                                check_two_sides += 1
                        else: 
                            hit = False
                            matchfield_logic[yCurrent,xCurrent-1] = 3
                            check_two_sides += 1
                            random_direction = "Osten"

                    if not hit and check_two_sides == 2: 
                        doublehit = False
                        check_two_sides = 0
                        screen.addstr(yGamesize,0,"Schiff zerstört")
                        screen.refresh()
                        newshot = True
        time.sleep(2)
        current_player = 1


def set_ships_comp(yPos, xPos, matchfield_visual, matchfield_temp, matchfield_logic, matchfield_ship_pos, yGameSize, xGameSize, player, screen):
    ''' Creates and sets all ships in order from biggest to smallest '''
    rotation = "hori"
    game_y_pos = yPos
    game_x_pos = xPos
    yPos = 0
    xPos = 0
    counter = 0
    tries = 0
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

            # screen.clear()
            # screen.addstr(0,0,str(matchfield_logic))
            # screen.addstr(game_y_pos+yGameSize+1,0,"                                                                                            ")
            # cords = "y:" + str(yPos_rand) + " x:" + str(xPos_rand) + " rot:" + rotation + " size:" + str(size) + "count:" + str(counter) + " tries:" + str(tries)
            # screen.addstr(game_y_pos+yGameSize+1,0,cords)
            # screen.refresh()
            # time.sleep(0.01)
        update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos, matchfield_visual, matchfield_ship_pos, player, screen)
    return matchfield_visual, matchfield_ship_pos

def set_ships(yPos, xPos, matchfield_visual, matchfield_temp, matchfield_logic, matchfield_ship_pos, yGameSize, xGameSize, player, screen):
    ''' Creates and sets all ships in order from biggest to smallest '''
    rotation = "hori"
    curinput = ""
    counter = 0
    game_y_pos = yPos
    game_x_pos = xPos
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
        
        update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos,matchfield_visual, matchfield_temp, player, screen)

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

                update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos, matchfield_visual, matchfield_temp, player, screen)

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
                i.position_x = xPos
                i.position_y = yPos
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
                            screen.addstr(game_y_pos+yGameSize,0,"Schiff kann hier nicht platziert werden.")
                            screen.refresh()
                            time.sleep(0.1)
                            screen.addstr(game_y_pos+yGameSize,0,"                                        ")
                            screen.refresh()
                            matchfield_temp[yPos, xPos:xPos+size] = 1

                else:
                    for j in range(size):
                    # Loop for the current ship size
                        if matchfield_logic[yPos+j,xPos] == 1:
                        # Checks if any field of the vertical ship is already used
                            used = True
                            screen.addstr(game_y_pos+yGameSize,0,"Schiff kann hier nicht platziert werden.")
                            screen.refresh()
                            time.sleep(0.1)
                            screen.addstr(game_y_pos+yGameSize,0,"                                        ")
                            screen.refresh()
                            matchfield_temp[yPos:yPos+size, xPos] = 1
                            

                if used == False:
                # If the space is free the ship can be placed
                    i.rotation = rotation
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
                    update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos, matchfield_visual, matchfield_temp, player, screen)
                    break

            update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos, matchfield_visual, matchfield_temp, player, screen)
    return matchfield_visual, matchfield_ship_pos
              
def shoot(matchfield_visual, matchfield_temp, matchfield_logic, matchfield_ship_pos, yGameSize, xGameSize, player, screen):
    ''' Creates and sets all ships in order from biggest to smallest '''
    counter = 0
    curinput = ""
    game_y_pos = 2
    game_x_pos = 2
    yPos = 0
    xPos = 0
    
    screen.keypad(1)
    curses.mousemask(-1)

    matchfield_temp[yPos,xPos] = 1        
    update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos,matchfield_visual, matchfield_temp, player, screen)

    while curinput != ord('q'):
    # Position of ship
        update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos, matchfield_visual, matchfield_temp, player, screen)

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
            hit = False
            if matchfield_ship_pos[yPos,xPos] == 0:
            # Sets ship (current object) rotation and moves current location
                screen.addstr(game_y_pos+yGameSize,0,"Kein Schiff bei dieser Position")
                screen.refresh()
                time.sleep(0.1)
                screen.addstr(game_y_pos+yGameSize,0,"                                        ")
                screen.refresh()
                matchfield_temp[yPos, xPos] = 1
            else:
                hit = True
                screen.addstr(game_y_pos+yGameSize,0,"Schiff getroffen.")
                screen.refresh()
                time.sleep(0.1)
                screen.addstr(game_y_pos+yGameSize,0,"                                        ")
                screen.refresh()
                matchfield_temp[yPos, xPos] = 1
                        

            if hit == True:
            # If the space is free the ship can be placed
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
                update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos, matchfield_visual, matchfield_temp, player, screen)
                break

        update_matchfield(yGameSize, xGameSize, game_y_pos, game_x_pos, matchfield_visual, matchfield_temp, player, screen)
    return matchfield_visual, matchfield_ship_pos

def options():
    ''' Currently not in use '''
    print("hi")

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

def main():
    ''' Starts the game '''
    return curses.wrapper(c_main)    

if __name__ == "__main__":
    main()
    input()