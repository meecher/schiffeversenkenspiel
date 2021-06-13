import numpy as np
import curses
import curses.panel
matchfield1 = 0
matchfield2 = 0

screen = curses.initscr()
curses.noecho()
screen.keypad(1)
dims = screen.getmaxyx()

def create_matchfield(ySize, xSize):
    global matchfield1
    matchfield1 = np.zeros((ySize, xSize))
    print(matchfield1)
    global matchfield2
    matchfield2 = np.zeros((ySize, xSize))

def set_ships(yPos, xPos, player):
    global matchfield1

    key = ''
    while key != ord('q'):
        key = screen.getch()
        print(key)
        if key == curses.KEY_RIGHT:
            print("right")
            matchfield1[yPos, xPos] = 0
            xPos += 1
            matchfield1[yPos, xPos] = 1
        screen.addstr(0, 0, str(matchfield1))
        screen.refresh()
        if key == curses.KEY_DOWN:
            print("down")
            matchfield1[yPos, xPos] = 0
            yPos += 1
            matchfield1[yPos, xPos] = 1
        screen.refresh()
        if key == curses.KEY_LEFT:
            print("left")
            matchfield1[yPos, xPos] = 0
            xPos -= 1
            matchfield1[yPos, xPos] = 1
        screen.refresh()
        if key == curses.KEY_UP:
            print("up")
            matchfield1[yPos, xPos] = 0
            yPos -= 1
            matchfield1[yPos, xPos] = 1
        screen.refresh()