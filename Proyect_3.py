'''
Game_Show.py
This code plays the game of the three doors.
Where the user would chose a door and then one door would open and with the new information
the user would decided if he wants to stick with his decision or change it.
Keegan Sand 
15/11/2022
Code Review: Karson Chrispens @ 4:50 PM on 11/28
'''

import random
# Global variables
change_win = 0
NOchange_win = 0
change_loss = 0
NOchange_loss = 0
lose = 0
won = 0

# FORMAT
def doors():
    print("                                                                                     ")
    print("    |---------------|          |---------------|          |---------------|          ")
    print("    |               |          |               |          |               |          ")
    print("    |               |          |               |          |               |          ")
    print("    |       1       |          |       2       |          |       3       |          ")
    print("    |               |          |               |          |               |          ")
    print("    |               |          |               |          |               |          ")
    print("    |               |          |               |          |               |          ")
    print("    |           --- |          |           --- |          |           --- |          ")
    print("    |               |          |               |          |               |          ")
    print("    |               |          |               |          |               |          ")
    print("    |               |          |               |          |               |          ")
    print("    |               |          |               |          |               |          ")
    print("    |---------------|          |---------------|          |---------------|          ")
    print("                                                                                     ")
def door_open(value):
    if value == 1:
        print("                                                                                     ")
        print("    |---------------|          |---------------|          |---------------|          ")
        print("    | \\             |          |               |          |               |          ")
        print("    |  |            |          |               |          |               |          ")
        print("    |  |            |          |       2       |          |       3       |          ")
        print("    |  |            |          |               |          |               |          ")
        print("    |  |            |          |               |          |               |          ")
        print("    |  |            |          |               |          |               |          ")
        print("    | -|   |||      |          |           --- |          |           --- |          ")
        print("    |  |  /   \\     |          |               |          |               |          ")
        print("    |  |  |   |     |          |               |          |               |          ")
        print("    |  |  |   |     |          |               |          |               |          ")
        print("    |  |  -----     |          |               |          |               |          ")
        print("    |---------------|          |---------------|          |---------------|          ")
        print("                                                                                     ")
    elif value == 2:
        print("                                                                                     ")
        print("    |---------------|          |---------------|          |---------------|          ")
        print("    |               |          | \\             |          |               |          ")
        print("    |               |          |  |            |          |               |          ")
        print("    |       1       |          |  |            |          |       3       |          ")
        print("    |               |          |  |            |          |               |          ")
        print("    |               |          |  |            |          |               |          ")
        print("    |               |          |  |            |          |               |          ")
        print("    |           --- |          | -|    |||     |          |           --- |          ")
        print("    |               |          |  |   /   \\    |          |               |          ")
        print("    |               |          |  |   |   |    |          |               |          ")
        print("    |               |          |  |   |   |    |          |               |          ")
        print("    |               |          |  |   -----    |          |               |          ")
        print("    |---------------|          |---------------|          |---------------|          ")
        print("                                                                                     ")
    elif value == 3:
        print("                                                                                     ")
        print("    |---------------|          |---------------|          |---------------|          ")
        print("    |               |          |               |          | \\             |          ")
        print("    |               |          |               |          |  |            |          ")
        print("    |       1       |          |       2       |          |  |            |          ")
        print("    |               |          |               |          |  |            |          ")
        print("    |               |          |               |          |  |            |          ")
        print("    |               |          |               |          |  |            |          ")
        print("    |           --- |          |           --- |          | -|    |||     |          ")
        print("    |               |          |               |          |  |   /   \\    |          ")
        print("    |               |          |               |          |  |   |   |    |          ")
        print("    |               |          |               |          |  |   |   |    |          ")
        print("    |               |          |               |          |  |   -----    |          ")
        print("    |---------------|          |---------------|          |---------------|          ")
        print("                                                                                     ")
def all_open(value):
    if value == 1:
        print("                                                                                     ")
        print("    |---------------|          |---------------|          |---------------|          ")
        print("    | \\             |          | \\             |          | \\             |          ")
        print("    |  |            |          |  |            |          |  |            |          ")
        print("    |  |     $      |          |  |            |          |  |            |          ")
        print("    |  |   $$$$$$   |          |  |            |          |  |            |          ")
        print("    |  |  $  $      |          |  |            |          |  |            |          ")
        print("    |  |  $  $      |          |  |            |          |  |            |          ")
        print("    | -|   $$$$$    |          | -|    |||     |          | -|    |||     |          ")
        print("    |  |     $  $   |          |  |   /   \\    |          |  |   /   \\    |          ")
        print("    |  |     $  $   |          |  |   |   |    |          |  |   |   |    |          ")
        print("    |  |  $$$$$$    |          |  |   |   |    |          |  |   |   |    |          ")
        print("    |  |     $      |          |  |   -----    |          |  |   -----    |          ")
        print("    |---------------|          |---------------|          |---------------|          ")
        print("                                                                                     ")
    elif value == 2:
        print("                                                                                     ")
        print("    |---------------|          |---------------|          |---------------|          ")
        print("    | \\             |          | \\             |          | \\             |          ")
        print("    |  |            |          |  |            |          |  |            |          ")
        print("    |  |            |          |  |     $      |          |  |            |          ")
        print("    |  |            |          |  |   $$$$$$   |          |  |            |          ")
        print("    |  |            |          |  |  $  $      |          |  |            |          ")
        print("    |  |            |          |  |  $  $      |          |  |            |          ")
        print("    | -|    |||     |          | -|   $$$$$    |          | -|    |||     |          ")
        print("    |  |   /   \\    |          |  |     $  $   |          |  |   /   \\    |          ")
        print("    |  |   |   |    |          |  |     $  $   |          |  |   |   |    |          ")
        print("    |  |   |   |    |          |  |  $$$$$$    |          |  |   |   |    |          ")
        print("    |  |   -----    |          |  |     $      |          |  |   -----    |          ")
        print("    |---------------|          |---------------|          |---------------|          ")
        print("                                                                                     ")
    elif value == 3:
        print("                                                                                     ")
        print("    |---------------|          |---------------|          |---------------|          ")
        print("    | \\             |          | \\             |          | \\             |          ")
        print("    |  |            |          |  |            |          |  |            |          ")
        print("    |  |            |          |  |            |          |  |     $      |          ")
        print("    |  |            |          |  |            |          |  |   $$$$$$   |          ")
        print("    |  |            |          |  |            |          |  |  $  $      |          ")
        print("    |  |            |          |  |            |          |  |  $  $      |          ")
        print("    | -|    |||     |          | -|    |||     |          | -|   $$$$$    |          ")
        print("    |  |   /   \\    |          |  |   /   \\    |          |  |     $  $   |          ")
        print("    |  |   |   |    |          |  |   |   |    |          |  |     $  $   |          ")
        print("    |  |   |   |    |          |  |   |   |    |          |  |  $$$$$$    |          ")
        print("    |  |   -----    |          |  |   -----    |          |  |     $      |          ")
        print("    |---------------|          |---------------|          |---------------|          ")
        print("                                                                                     ")

# CHECKINGS

#cheks for strings and floats
def number(value):
    flag = True
    while flag:
        try:
            int(value)
            flag = False
        except ValueError:
            print("Please try again using integers only.")
            value = input("Let's try again: ")
    return int(value)

#checks for an input
def something(value):
    flag = True
    while flag:
        if len(value) == 0:
            value = input()
        else:
            flag= False
    return value

# door opening
def otherDoorFrom(Udoor, Mdoor):
    num = [1,2,3]
    if Udoor == Mdoor:
        num.remove(Udoor)
        num.remove(num[random.randint(0,1)])
        return num[0]
    else:
        num.remove(Udoor)
        num.remove(Mdoor)
        return num[0]

# choice
def Choice(user, open, choice): 
    success = True
    while success:     

        if choice[0] == "Y" or choice[0] == "y":
            num = [1,2,3]
            num.remove(open)
            if user != open:
                num.remove(user)
            else:
                num.remove(num[random.randint(0,1)]) 
            return num[0], "y"
        elif choice[0] == "N" or choice[0] == "n":
            return user, "n"
        else:
            print("Please answer the question with yes or no.")
            choice = something(input("Would you like to change doors? "))

#   result saving
def results(y_n,user,winner):
    if y_n == "y":
        change = 1
        if user == winner:
            win = 1
        else:
            win = 0
    else:
        change = 0
        if user == winner:
            win = 1
        else:
            win = 0
    return change, win

# USER PLAYED
def Uplayed():
    door = random.randint(1,3)
    doors()
    user = number(input("select one of the three doors: "))
    flag = True
    while flag:
        if not(1 <= user <= 3):
            user = number(input("Please choose from the options (1-3): "))
        else:
            flag = False

    open = otherDoorFrom(user, door)
    door_open(open)
    print("Door {} has detergent".format(open))
    choice = something(input("Would you like to change doors? ")) 
    user, y_n = Choice(user,open,choice)
    all_open(door)
    return results(y_n,user,door)

# checks if winner for user played
def winner(value):
    if value == 1:
        print("Congratulations you WON!!!\n")
    else:
        print("You got detergent!!!\n")

# MACHINE DRIVEN
def Mplayed():
    door = random.randint(1,3)
    user = random.randint(1,3)

    open = otherDoorFrom(user, door)
    choice = ["y","n"]
    user, y_n = Choice(user, open,choice[random.randint(0,1)])
    
    return results(y_n,user,door)

# Results
def counter(change, win):
    global change_win, NOchange_win, change_loss, NOchange_loss, lose, won
    if change == win:
        if change == 1:
            won += 1
            change_win += 1
        else:
            NOchange_loss += 1
            lose += 1 
    elif change != win:
        if change == 1:
            lose += 1
            change_loss += 1
        else:
            NOchange_win += 1
            won += 1

def calculator(lose,won,times,change_win=0,change_loss=0,NOchange_win=0,NOchange_loss=0):
    change = change_win + change_loss
    nochange = NOchange_loss + NOchange_win
    if change != 0:
        change_win_porcentage = (change_win / change) *100 
    else:
        change_win_porcentage= (change_win / (times+1)) *100 # quick fix for 0 times played
    if nochange != 0:
        NOchange_win_porcentage = (NOchange_win / nochange) *100
    else:
        NOchange_win_porcentage = (NOchange_win / (times+1)) *100  # quick fix for 0 times played
    return change_win_porcentage, NOchange_win_porcentage


#main
def main():
    # seed for random
    random.seed(number(input("Enter a seed: ")))

    manual = something(input("would you like to play or simulate? "))
    success = True
    while success:
        if manual[0] == "p" or manual[0] == "P":
            success = False
            again = "y"
            times = 0
            while again[0] == "y" or again == "Y":
                a, b = Uplayed()
                winner(b)
                times += 1
                counter(a,b)
                again = something(input("Would you like to play again? (y for yes) "))

        elif manual[0] == "s" or manual[0] == "S":
            success = False
            times = number(input("how many times would you like to simulate? "))

            for _ in range(times):
                a,b = Mplayed()
                counter(a,b)
        
        else:
            print("Please answer with \"play\" or \"simulate\"")
            manual = something(input("would you like to play or simulate? "))

    print("\nYou played a total of {} times, won a total of {} games, you changed doors a total of {} times.".format(times, won, change_win+change_loss))
    print("{:.0f}% of the times you changed your door you won.".format(
        calculator(lose,won,times,change_win,change_loss,NOchange_win,NOchange_loss)[0]))
    print("{:.0f}% of the times you decided to stay with your option you won.\n".format(
        calculator(lose,won,times,change_win,change_loss,NOchange_win,NOchange_loss)[1]))

main()
