''' The game Maexchen. '''

import random
import time

__author__ = "7147252, Lüttig, 7251869, Ullmann"
__credits__ = ""
__email__ = "s2244177@stud.uni-franfurt.de, s1343080@stud.uni-frankfurt.de"


# global variables
points = []
history = []
names = []
last_throw = 0
Maexchen_value = 21
Hamburger_value = 42
start = 10
minus = 1
order = 0
special_values = [11, 22, 33, 44, 55, 66,
                  Maexchen_value, Hamburger_value]


def throw():
    ''' Returns a dice roll '''
    return random.randint(1, 6)


def check_throw(i):
    ''' Checks if the throw is legitimate. '''
    # Number between 11 and 66 is possible with two dices.
    # If it is a wrong input the return is False.
    cheats = [666, 420, 69]
    if i in cheats:
        return True

    if i <= 66 and i >= 11:
        digits = str(i)
        if not order:
            # First digit need to be larger than the second
            if digits[0] >= digits[1]:
                # Gives i a bigger value if it is a special number.
                if i in special_values:
                    i = int(check_value(i))
                    # Return true if the number is larger than the number in the last round.
                    if i > last_throw:
                        return True
                # Return true if the number is larger than the number in the last round.
                elif i > last_throw:
                    return True
        else:
            if i in special_values:
                i = int(check_value(i))
                # Return true if the number is larger than the number in the last round.
                if i > last_throw:
                    return True
                # Return true if the number is larger than the number in the last round.
            elif i > last_throw:
                return True

    return False


def check_choice(s):
    ''' Checks what the player chose. '''
    return s in ['g', 'n']


def check_choice_gamestart(s):
    ''' Checks wether to start the game or call function for options. '''
    return s in ['S', 'O']


def update_points(player_number, real_throw, alleged_throw, real_result):
    ''' Updates the points of a player if the result is doubted. '''
    global points, last_throw, names, points
    decrease = 0
    # god mode
    if points[player_number] != "god":
        # Condition 1: player who didn't believe result is wrong.
        if alleged_throw <= real_throw:
            # This 3 if structures check how much points are subtracted.
            # If the roll was a Hamburger (default=42) or a Maexchen (default=21) the order of the players is reversed.
            if real_throw == 74:
                # multiplicator for special value
                decrease = 3 * minus
                names.sort(reverse=True)
                points.sort(reverse=True)
                print("Hamburger! Reihenfolge wird geändert: ", ', '.join(names))
            elif real_throw == 73:
                # multiplicator for special value
                decrease = 2 * minus
                names.sort(reverse=True)
                points.sort(reverse=True)
                print("Maexchen! Reihenfolge wird geändert: ", ', '.join(names))
            else:
                decrease = minus
            # Takes the first player of the sequence if the player who rolled the dice was the last in the sequence
            # and subtracts the points from the player who was wrong.
            if player_number == (len(names)-1):
                print("Die Zahl war:", real_result)
                # points can not go below 0
                if points[0] - decrease < 0:
                    points[0] = 0
                else:
                    points[0] -= decrease
                print("Spieler", names[0], "hat jetzt", points[0], "Punkte.")
            # Takes the next player in the sequence and decreases his points.
            elif player_number != (len(names)-1):
                print("Die Zahl war:", real_result)
                # points can not go below 0
                if points[0] - decrease < 0:
                    points[0] = 0
                else:
                    points[player_number+1] -= decrease
                print("Spieler", names[player_number+1],
                      "hat jetzt", points[player_number+1], "Punkte.")
        # Condition 2: player who rolled the dice lied.
        elif alleged_throw > real_throw:
            # This 3 if structures check how much points are subtracted.
            if alleged_throw == 74:
                decrease = 3
            elif alleged_throw == 73:
                decrease = 2
            else:
                decrease = 1
            print("Die Zahl war:", real_result)
            points[player_number] -= decrease
            print("Spieler", names[player_number],
                  "hat jetzt", points[player_number], "Punkte.")
    else:
        print("da ist was schief gelaufen ;)")
    last_throw = 0


def clear_screen():
    ''' clean the terminal output
    source: https://stackoverflow.com/questions/2084508/clear-terminal-in-python '''
    print(chr(27) + "[2J" + chr(27)+"[H")


def check_value(number):
    ''' Outputs a value if a special number is inputted (doublets, maexchen, hamburger). '''
    global Maexchen_value, Hamburger_value
    digits = list(str(number))
    value = number
    # These if structures check what type of special number is inputted
    # and output the assigned value.
    if 1 == int(digits[0]) and 1 == int(digits[1]):
        value = 67
    elif 2 == int(digits[0]) and 2 == int(digits[1]):
        value = 68
    elif 3 == int(digits[0]) and 3 == int(digits[1]):
        value = 69
    elif 4 == int(digits[0]) and 4 == int(digits[1]):
        value = 70
    elif 5 == int(digits[0]) and 5 == int(digits[1]):
        value = 71
    elif 6 == int(digits[0]) and 6 == int(digits[1]):
        value = 72
    elif number == Maexchen_value:
        value = 73
    elif number == Hamburger_value:
        value = 74
    return value


def round_num(player_number):
    ''' Selects the current player and leads the round. '''
    global last_throw
    print(names[player_number], "ist an der Reihe")
    first = throw()
    print_dice(first)
    second = throw()
    print_dice(second)
    # decide if order is normal or changed
    if order == 0:
        # Check how the number is generated: First number in the result needs to be bigger than the second.
        if first == second:
            result = int(str(first)+str(second))
        elif first > second:
            result = int(str(first)+str(second))
        else:
            result = int(str(second)+str(first))
    else:
        result = int(str(first)+str(second))
    print("Das ergibt:", result)
    user = 0
    # Repeats until the function outputs True.
    while not check_throw(user):
        user = int(input("Du sagst: "))
    if user == 666:
        user == result
        points[player_number] = "god"
    elif user == 69:
        result, user == Maexchen_value
    elif user == 420:
        result, user == Hamburger_value
    clear_screen()
    print('Ich habe', user, 'gewürfelt')
    # save dice throw
    real_result = result
    # convert dice to ingame values
    result = check_value(result)
    # Looks if user is a special value. Outputs the assigned string to the given value of the function.
    if user in special_values:
        user = check_value(user)
        if user == 67:
            print("Einerpasch")
        elif user == 68:
            print("Zweierpasch")
        elif user == 69:
            print("Dreierpasch")
        elif user == 70:
            print("Viererpasch")
        elif user == 71:
            print("Fuenferpasch")
        elif user == 72:
            print("Sechserpasch")
        elif user == 73:
            print("Maexchen")
        elif user == 74:
            print("Hamburger")
    last_throw = user
    choice = ""
    # Waits for the user to input his choice
    while not check_choice(choice):
        # Checks if the current player is the last in the sequence to select the guessing player which is the first in the sequence.
        if player_number == (len(names)-1):
            player_guessing = names[0]
        # If the current player isn't the last in the sequence
        # the guessing player is the next in the sequence
        else:
            player_guessing = names[player_number+1]
        message = "Spieler", player_guessing, "(g)lauben oder (n)icht glauben\n"
        choice = input(' '.join(message))
    # If the guessing player doesn't believe the value it calls a function to update the points.
    if choice == 'n':
        update_points(player_number, result, user, real_result)
    # Otherwise it checks if the roll was Hamburger (=42; value=74) which causes the rotation to reverse.
    # If it isn't a Hamburger the game goes on
    elif choice == 'g':
        if user == 74:
            last_throw = 0
            print("Hamburger, neue Runde beginnt.")
            names.sort(reverse=True)
            points.sort(reverse=True)
            print("Reihenfolge wird geändert: ", ', '.join(names))
        else:
            pass


def print_dice(num):
    ''' prints the given number as dice
    if the number is not between 1 and 6 nothing i printed'''
    # Outputs a string visually representing the number
    if num == 1:
        dice = "| | | |\n| |o| |\n| | | |\n"
    elif num == 2:
        dice = "|o| | |\n| | | |\n| | |o|\n"
    elif num == 3:
        dice = "|o| | |\n| |o| |\n| | |o|\n"
    elif num == 4:
        dice = "|o| |o|\n| | | |\n|o| |o|\n"
    elif num == 5:
        dice = "|o| |o|\n| |o| |\n|o| |o|\n"
    elif num == 6:
        dice = "|o|o|o|\n| | | |\n|o|o|o|\n"
    else:
        dice = "| | | |\n| |o| |\n| | | |\n"
    print(dice)


def options():
    ''' Let's the user select different options for the game. '''
    choices = ["1", "2", "3", "4", "5"]
    print("(1) Mäxchen konfigurieren\n\
    (2) Hamburger konfigurieren\n\
    (3) Stellen konfigurieren\n\
    (4) Abzug konfigurieren\n\
    (5) Start Punkte konfigurieren\n")
    choice = 0
    while choice not in choices:
        choice = input(": ")
        if choice == "1":
            update_max()
        elif choice == "2":
            update_ham()
        elif choice == "3":
            update_order()
        elif choice == "4":
            update_minus()
        elif choice == "5":
            update_start()


def update_max():
    ''' updates maexchen value '''
    global Maexchen_value
    new_max = 0
    # Waits for the user to input a new correct value for Maexchen.
    while not check_throw(new_max):
        new_max = int(input("Der Wert von Maexchen (normal 21):"))
    Maexchen_value = new_max
    print("Der Wert von Maexchen ist jetzt:", Maexchen_value)


def update_ham():
    ''' updates hamburger value '''
    global Hamburger_value
    new_ham = 0
    # Waits for the user to input a new correct value for Hamburger.
    while not check_throw(new_ham):
        new_ham = int(input("Der Wert von Hamburger (normal 42):"))
    Hamburger_value = new_ham
    print("Der Wert von Hamburger ist jetzt:", Maexchen_value)


def update_order():
    ''' updates order '''
    global order
    new_order = ""
    # Waits for the user to choose the method for ordering the numbers.
    while new_order not in ["0", "1"]:
        new_order = input(
            "Reihenfolge nach Wert(0)\nReichenfolge nach 'Reihenfolge' (1)")
    order = new_order


def update_minus():
    ''' Changes the value for the subtracted points. '''
    global minus
    new_minus = 0
    # Waits for the user to input a new correct value for Maexchen.
    while new_minus <= 0:
       # check if convertion to int is possible
        try:
            new_minus = int(input("Der Wert zum abziehn (normal 1)"))
        except:
            new_minus = 0
    minus = new_minus


def update_start():
    ''' Changes the start points of the player. '''
    global start
    new_start = 0
    # Waits for the user to input a new correct value for Maexchen.
    while new_start <= 0:
       # check if convertion to int is possible
        try:
            new_start = int(input("Der Startwert (normal 10)"))
        except:
            new_start = 0
    start = new_start


def init_game(number_of_players):
    ''' Initializes the game by creating player lists '''
    global points, names
    # Creates a list with points for each player.
    for i in range(0, number_of_players):
        points.append(start)
    # Creates a list with the name of each player.
    for i in range(1, number_of_players+1):
        names.append(input(str(i)+'. Spieler: '))
    random.shuffle(names)
    print("Die Reihenfolge ist:", ', '.join(names))


def print_history():
    round = 1
    for points in history:
        print(str(round) + ": " + str(points))
        round += 1


def main():
    ''' Starts the game '''
    num = 0
    s = ""
    while s != "S":
        s = input(" (S)tart \n (O)ptions \n").upper()
        if s == 'O':
            options()
    players = int(input("Wie viele Spieler:"))
    # Checks if the input of the player is above 1 otherwise the game doesn't start.
    if(players > 1):
        init_game(players)
    else:
        print("Alleine will keiner Spielen!")
        input()
        exit()
    # Repeats the rounds until there is only one player left which then wins.
    while len(names) > 1:
        counter = 0
        round_num(num)
        history.append(points.copy())
        # After every round it checks if a player is out of the game (<=0 points)
        # and deletes him out of the game if it's true
        for i in points:
            if i <= 0:
                print(names[points.index(0)], "ist raus.")
                points.pop(counter)
                names.pop(counter)
                print("Neue Reihenfolge: ", ', '.join(names))
            else:
                counter += 1
        # If it is the last player in the sequence it goes back to the first player.
        # Otherwise it goes over to then next.
        if num == (len(names)-1):
            num = 0
        else:
            num += 1
    print(names[0], "hat gewonnen!")
    print_history()


if __name__ == "__main__":
    main()
    input()
