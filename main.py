''' The game Schiffeversenken. '''

import cursebox as cb
import random
import time

__author__ = "1359831, Ruschmaritsch, 1357985, Ullmann"
__credits__ = ""
__email__ = "david.ruschmaritsch@stud.fra-uas.de, marc.ullmann@stud.fra-uas.de"

def options():
    print("hi")

def init_game(playerdefine):
    print("hi")

def clear_screen():
    ''' clean the terminal output
    source: https://stackoverflow.com/questions/2084508/clear-terminal-in-python '''
    print(chr(27) + "[2J" + chr(27)+"[H")

def main():
    ''' Starts the game '''
    #testwindow
    #width, height = cb.width, cb.height
    #greeting = "Hello, World!"
    # Center text on the screen
    #cb.put(x=(width - len(greeting)) / 2,
    #y=height / 2, text=greeting,
    #fg=colors.black, bg=colors.white)
    # Wait for any keypress
    #cb.poll_event()

    #Oldcode
    num = 0
    playerdefine = ""
    s = ""
    while s != "S":
        s = input(" (S)tart \n (O)ptions \n").upper()
        if s == 'O':
            options()
    playerdefine = input("(Z)weispieler oder (A)lleine?: ")
    # Checks if the input of the player is above 1 otherwise the game doesn't start.
    if(playerdefine > 1):
        init_game(playerdefine)
    # Repeats the rounds until there is only one player left which then wins.
    


if __name__ == "__main__":
    main()
    input()

