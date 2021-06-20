import curses
import time
import numpy as np

def c_main(screen): 
    ''' Translates temporary matchfield to visual one and displays visuals '''
    ySize = 10
    xSize = 10
    yGameSize = 10
    xGameSize = 10
    player = "p1"
    matchfield_visual = np.chararray((ySize, xSize))
    matchfield_visual[:] = "O"
    matchfield_temp = np.zeros((ySize, xSize))
    matchfield_logic = np.zeros((ySize, xSize))
    matchfield_ship_pos = np.zeros((ySize, xSize))

    matchfield_temp[9,5] = 1

    i = 0
    xPos = 0
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
    time.sleep(10)


def main():
    ''' Starts the game '''
    return curses.wrapper(c_main)    

if __name__ == "__main__":
    main()
    input()

