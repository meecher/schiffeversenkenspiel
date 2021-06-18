import curses
import time

def c_main(screen): 
    matchfield_visual = [[0]*10 for i in range (10)]
    i = 0
    for row in matchfield_visual:
        string_ints = [str(int) for  int in row]
        stringli = ' '.join(string_ints)
        screen.addstr(i,0,stringli)
        screen.refresh()
        i += 1
    #stringli = '\n'.join(' '.join(sublist) for sublist in matchfield_visual)
    #for row in matchfield_visual:
    #screen.addstr(0,0,stringli)
    screen.refresh()


def main():
    ''' Starts the game '''
    return curses.wrapper(c_main)    

if __name__ == "__main__":
    main()
    input()

