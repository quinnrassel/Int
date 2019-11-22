# __author__ Quinn RASSEL
# this is a text based game with the goal of getting enough numbers to hit 20


def get_one():
    """ a way to check for a initial error or value error

    :return:
    """
    n = 0
    while n != 1:
        try:
            n = int(input("Enter number 1: "))
        except ValueError:
            print("Enter a whole numeric number: ")


def get_two():
    """ a way to check for a initial error or value error

        :return:
        """
    n = 0
    while n != (1, 2):
        try:
            n = int(input("Enter number 1: "))
        except ValueError:
            print("Enter a whole numeric number: ")


def get_three():
    """ a way to check for a initial error or value error

        :return:
        """
    n = 0
    while n != (1, 2, 3):
        try:
            n = int(input("Enter number 1: "))
        except ValueError:
            print("Enter a whole numeric number: ")


def get_four():
    """ a way to check for a initial error or value error

        :return:
        """
    n = 0
    while n != (1, 2, 3, 4):
        try:
            n = int(input("Enter number 1: "))
        except ValueError:
            print("Enter a whole numeric number: ")


def winnersGame():
    """
This is the game played after the player has won, it shows the winnings
    """
    print("WINNERS GAME")
    total = 0
    for x in range(5):
        num = int(input("Enter a number 1-5: "))
        total += num
    print("The total is:", total)
    n = total
    if n == 5:
        print("Your winnings are 1")
        w = 1
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 6:
        print("Your winnings are 9")
        w = 9
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 7:
        print("Your winnings are 3")
        w = 3
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 8:
        print("Your winnings are 12")
        w = 12
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 9:
        print("Your winnings are 4")
        w = 4
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 10:
        print("Your winnings are 2")
        w = 2
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 11:
        print("Your winnings are 23")
        w = 23
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 12:
        print("Your winnings are 12")
        w = 12
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 13:
        print("Your winnings are 45")
        w = 45
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 14:
        print("Your winnings are 17")
        w = 17
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 15:
        print("Your winnings are 6")
        w = 6
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 16:
        print("Your winnings are 8")
        w = 8
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 17:
        print("Your winnings are 0")
        w = 0
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 18:
        print("Your winnings are 19")
        w = 19
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 19:
        print("Your winnings are 5")
        w = 5
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 20:
        print("Your winnings are 30")
        w = 30
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 21:
        print("Your winnings are 0")
        w = 0
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 22:
        print("Your winnings are 0")
        w = 0
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 23:
        print("Your winnings are 2")
        w = 2
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 24:
        print("Your winnings are 24")
        w = 24
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    elif n == 25:
        print("Your winnings are 1")
        w = 1
        if w >= 40:
            print("You got a ton out of this")
        elif w >= 30:
            print("You got a lot out of this")
        elif w >= 20:
            print("You got a good amount out of this")
        elif w >= 10:
            print("You got something out of this")
        elif w >= 1:
            print("You got a little out of this")
        else:
            print("You got nothing out of this")
    else:
        print("Invalid input")


print("Hello World")
n = int(input("Enter number 1:"))
get_one()
if n == 1:
    print("Start Story 1")
    print("Enter 1")
    n = int(input("Enter a number 1:"))
    get_one()
    if n == 1:
        print("Red path")
        n = int(input("Enter number 1:"))
        get_one()
        if n == 1:
            print("You chose car one")
            print("You must make it to 20 to win")
            print("If you hit -20 You Lose")
            print(
                "You have 10 attempts (not including car breakdowns) to get "
                "to 20")
            print("START")
            print("Current number is 0")
            n = int(input("Enter a number 1:"))
            get_one()
            if n == 1:
                print("add 3 to the current number")
                print("Your car has a chance to break down")
                n = int(input("Enter a number 1:"))
                get_one()
                if n == 1:
                    print("Your car breaks down")
                    print("Lose 1")
                    print("You are at 2")
                    n = int(input("Enter number 1:"))
                    get_one()
                    if n == 1:
                        print("You gain 4")
                        print("You are at 6")
                        n = int(input("Enter a number 1:"))
                        get_one()
                        if n == 1:
                            print("You gain 2")
                            print("You are at 8")
                            n = int(input("Enter a number 1-2:"))
                            get_two()
                            if n == 1:
                                print("You gain 5")
                                print("You are at 13")
                                n = int(input("Enter a number 1-2:"))
                                get_two()
                                if n == 1:
                                    print("Your car breaks down")
                                    print("Lose 2")
                                    print("You are at 11")
                                    n = int(input("Enter a number 1-2:"))
                                    get_two()
                                    if n == 1:
                                        print("You lose 4")
                                        print("You are at 7")
                                        n = int(input("Enter a number 1-4:"))
                                        get_four()
                                        if n == 1:
                                            print("You gain 3")
                                            print("You are at 10")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 11")
                                                n = int(input(
                                                    "Enter a number 1-3:"))
                                                get_three()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 13")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final "
                                                                "number is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final"
                                                                " number is "
                                                                "19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final "
                                                                "number is 15")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 14")
                                                        n = int(input(
                                                            "Enter a number"
                                                            " 1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 13")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 15")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 11")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 17")
                                                            print(
                                                                "Almost but"
                                                                " YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 19")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU WIN"
                                                                "!!!")
                                                            winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 12")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 17")
                                                        n = int(input(
                                                            "Enter a number"
                                                            " 1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 13")
                                                        n = int(input(
                                                            "Enter a num"
                                                            "ber 1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 14")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a numbe"
                                                            "r 1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU W"
                                                                "IN!!!")
                                                            winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 19")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                        elif n == 2:
                                            print("You gain 1")
                                            print("You are at 8")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 9")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 11")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number"
                                                            " 1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 12")
                                                        n = int(input(
                                                            "Enter a numb"
                                                            "er 1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 11")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 13")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 9")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 15")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 17")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU WIN!"
                                                                "!!")
                                                            winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 10")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 15")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 11")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 10")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 12")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 8")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 15")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 14")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 15")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number"
                                                            " 1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 19")
                                                            print(
                                                                "Almost but Y"
                                                                "OU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()

                                        elif n == 3:
                                            print("You lose 10")
                                            print("You are at -3")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at -4")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at -2")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 3")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 2")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 4")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 0")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 10")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 13")
                                                            print("YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at -1")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is -2")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 0")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is -4")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 2")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 4")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 3")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print(
                                                                "You gain 17")
                                                            print(
                                                                "!!!YOU"
                                                                " WIN!!!")
                                                            winnersGame()
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 1")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 30")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at -3")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 2")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 1")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 3")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print(
                                                                "You lose 30")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 18")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at -2")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is -3")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is -1")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final nu"
                                                                "mber is -5")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 18")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 3")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 2")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 4")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 0")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 30")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 2")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    if n == 1:
                                                        print("You gain 18")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You lose 22")
                                                        print("YOU LOSE")
                                                    elif n == 3:
                                                        print("You lose 23")
                                                        print("YOU LOSE")
                                        elif n == 4:
                                            print("You gain 1")
                                            print("You are at 8")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 9")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 11")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number"
                                                            " 1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 10")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 12")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 9")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 17")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print(
                                                                "You lose 20")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 10")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 15")
                                                        n = int(input(
                                                            "Enter a number"
                                                            " 1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print(
                                                                "You lose 18")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 11")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 8")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 5")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 15")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 15")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You lose 6")
                                                        print("YOU LOSE")

                                    elif n == 2:
                                        print("You gain 4")
                                        print("You are at 15")
                                        n = int(input("Enter a number 1-4:"))
                                        get_four()
                                        if n == 1:
                                            print("You gain 3")
                                            print("You are at 18")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 19")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                                        elif n == 2:
                                            print("You gain 1")
                                            print("You are at 16")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 17")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 19")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 18")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 19")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                                        elif n == 3:
                                            print("You lose 10")
                                            print("You are at 5")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 6")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 8")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 13")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 12")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 13")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print("YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 9")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 8")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 6")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 14")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 30")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 7")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 12")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 9")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 18")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 8")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 7")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 9")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 5")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 13")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 12")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 8")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You lose 12")
                                                        print("YOU LOSE")
                                                    elif n == 3:
                                                        print("You lose 200")
                                                        print("YOU MEGA LOSE")
                                        elif n == 4:
                                            print("You gain 1")
                                            print("You are at 16")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 17")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 19")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 18")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 19")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                                elif n == 2:
                                    print("Your car doesn't breaks down")
                                    print("You are at 13")
                                    n = int(input("Enter a number 1-2:"))
                                    get_two()
                                    if n == 1:
                                        print("You lose 4")
                                        print("You are at 9")
                                        n = int(input("Enter a number 1-4:"))
                                        get_four()
                                        if n == 1:
                                            print("You gain 3")
                                            print("You are at 12")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 13")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 15")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 14")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 19")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 15")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final "
                                                                "number is 14")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 19")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                        elif n == 2:
                                            print("You gain 1")
                                            print("You are at 10")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 11")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 13")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 12")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 9")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 19")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 12")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 17")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final "
                                                                "number is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 14")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 13")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final "
                                                                "number is 10")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final "
                                                                "number is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 17")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                        elif n == 3:
                                            print("You lose 10")
                                            print("You are at -1")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 0")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 2")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_four()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 7")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 6")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 8")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 4")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 3")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 2")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 4")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 0")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 6")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 8")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 7")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print(
                                                                "You gain 12")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 5")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 12")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 1")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 6")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                ""
                                                                "umber is 5")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 7")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print(
                                                                "You lose 100")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 13")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 2")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 1")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 3")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is -1")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 18")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 7")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 6")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 8")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 4")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 13")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 6")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You lose 33")
                                                        print("YOU LOSE")
                                                    elif n == 2:
                                                        print("You lose 55")
                                                        print("YOU LOSE")
                                                    elif n == 3:
                                                        print("You gain 23")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                        elif n == 4:
                                            print("You gain 1")
                                            print("You are at 10")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 11")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 13")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 10")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 14")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 19")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                        elif n == 3:
                                                            print(
                                                                "You lose 15")
                                                            print(
                                                                "Your final n"
                                                                "umber is 4")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 12")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_four()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 17")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print(
                                                                "You lose 18")
                                                            print(
                                                                "Your final n"
                                                                "umber is 0")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 13")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 5")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 17")
                                                    n = int(input(
                                                        "Enter a number "
                                                        "1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                    elif n == 2:
                                        print("You gain 4")
                                        print("You are at 17")
                                        n = int(input("Enter a number 1-4:"))
                                        get_four()
                                        if n == 1:
                                            print("You gain 3")
                                            print("!!!YOU WIN!!!")
                                            winnersGame()
                                        elif n == 2:
                                            print("You gain 1")
                                            print("You are at 18")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 19")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                                        elif n == 3:
                                            print("You lose 10")
                                            print("You are at 7")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 8")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 10")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 15")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 13")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 11")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 8")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 4")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 9")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 14")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 70")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 10")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 9")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 7")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 15")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 14")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You lose 34")
                                                        print("YOU LOSE")
                                                    elif n == 3:
                                                        print("You lose 66")
                                                        print("YOU LOSE")
                                        elif n == 4:
                                            print("You gain 1")
                                            print("You are at 18")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 19")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                            elif n == 2:
                                print("You gain 3")
                                print("You are at 11")
                                n = int(input("Enter a number 1-2:"))
                                get_two()
                                if n == 1:
                                    print("Your car breaks down")
                                    print("Lose 2")
                                    print("You are at 9")
                                    n = int(input("Enter a number 1-2:"))
                                    get_two()
                                    if n == 1:
                                        print("You lose 4")
                                        print("You are at 5")
                                        n = int(input("Enter a number 1-4:"))
                                        get_four()
                                        if n == 1:
                                            print("You gain 3")
                                            print("You are at 8")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 9")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 11")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number"
                                                            " 1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 12")
                                                        n = int(input(
                                                            "Enter a number"
                                                            " 1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 9")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 17")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 10")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 15")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final "
                                                                "number is 12")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 11")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 8")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 15")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                        elif n == 2:
                                            print("You gain 1")
                                            print("You are at 6")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 7")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 9")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 14")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but Y"
                                                                "OU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 10")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 9")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 7")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 15")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 8")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 13")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 9")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 8")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 6")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 14")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 13")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 14")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()

                                        elif n == 3:
                                            print("You lose 10")
                                            print("You are at -5")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at -4")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You lose 15")
                                                    print("You are at -19")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at -14")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is -15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is -13")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is -17")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 10")
                                                            print(
                                                                "Your final n"
                                                                "umber is -4")
                                                            print("YOU LOST")
                                                    elif n == 2:
                                                        print("You lose 1")
                                                        print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at -13")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is -14")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print(
                                                                "You gain 50")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is -16")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 70")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 2:
                                                    print("You gain 12")
                                                    print("You are at 8")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 13")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print(
                                                                "You lose 40")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 18")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 9")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final "
                                                                "number is 8")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final "
                                                                "number is 10")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 6")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 18")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 12")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 14")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "You gain 30")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 3:
                                                    print("You gain 8")
                                                    print("You are at 4")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 18")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You lose 22")
                                                        print("YOU LOSE")
                                                    elif n == 3:
                                                        print("You lose 23")
                                                        print("YOU LOSE")
                                        elif n == 4:
                                            print("You gain 1")
                                            print("You are at 6")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 7")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 9")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 14")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final nu"
                                                                "mber is 15")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 10")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 9")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 7")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 15")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 8")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 13")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 9")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 8")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 6")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 14")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 13")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 14")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()

                                    elif n == 2:
                                        print("You gain 4")
                                        print("You are at 13")
                                        n = int(input("Enter a number 1-3:"))
                                        get_three()
                                        if n == 1:
                                            print("You gain 3")
                                            print("You are at 16")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 17")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 19")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 18")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 19")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but"
                                                                " YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                                        elif n == 2:
                                            print("You gain 1")
                                            print("You are at 14")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                                winnersGame()
                                            else:
                                                print("You gain 1")
                                                print("You are at 15")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 17")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                ""
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 16")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 17")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                                        elif n == 3:
                                            print("You gain 1")
                                            print("You are at 14")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 15")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 17")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 16")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 17")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                                elif n == 2:
                                    print("Your car doesn't breaks down")
                                    print("You are at 11")
                                    n = int(input("Enter a number 1-2:"))
                                    get_two()
                                    if n == 1:
                                        print("You lose 4")
                                        print("You are at 7")
                                        n = int(input("Enter a number 1-4:"))
                                        get_four()
                                        if n == 1:
                                            print("You gain 3")
                                            print("You are at 10")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 11")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 13")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU"
                                                                " WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 14")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 19")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 12")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 17")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but Y"
                                                                "OU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final "
                                                                "number is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 13")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final "
                                                                "number is 12")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 17")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 18")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                        elif n == 2:
                                            print("You gain 1")
                                            print("You are at 8")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 9")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 11")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final "
                                                                "number is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final "
                                                                "number is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final "
                                                                "number is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 12")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final "
                                                                "number is 11")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 9")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 17")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 10")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 15")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 11")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 8")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 15")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()

                                        elif n == 3:
                                            print("You lose 30")
                                            print("YOU LOSE")
                                        elif n == 4:
                                            print("You gain 1")
                                            print("You are at 8")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                                winnersGame()
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 9")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 11")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 12")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 11")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 9")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 17")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 10")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("You are at 15")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 11")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 10")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 12")
                                                            print("YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 8")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 14")
                                                            print("YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("You are at 15")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 16")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 15")
                                                            print("YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 17")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 13")
                                                            print("YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 19")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()

                                    elif n == 2:
                                        print("You gain 4")
                                        print("You are at 15")
                                        n = int(input("Enter a number 1-3:"))
                                        get_three()
                                        if n == 2:
                                            print("You gain 7")
                                            print("!!!YOU WIN!!!")
                                        elif n == 1:
                                            print("You gain 1")
                                            print("You are at 16")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 17")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 19")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 18")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 19")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
                                        elif n == 3:
                                            print("You gain 1")
                                            print("You are at 16")
                                            n = int(input("Enter a number:"))
                                            if n == 777:
                                                print("!!!YOU WIN!!!")
                                            elif n == 23:
                                                print("!!!YOU LOSE!!!")
                                            else:
                                                print("You gain 1")
                                                print("You are at 17")
                                                n = int(input(
                                                    "Enter a number 1-4:"))
                                                get_four()
                                                if n == 1:
                                                    print("You gain 2")
                                                    print("You are at 19")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 2:
                                                    print("You gain 1")
                                                    print("You are at 18")
                                                    n = int(input(
                                                        "Enter a number 1-3:"))
                                                    get_three()
                                                    if n == 1:
                                                        print("You gain 5")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                    elif n == 2:
                                                        print("You gain 1")
                                                        print("You are at 19")
                                                        n = int(input(
                                                            "Enter a number "
                                                            "1-4:"))
                                                        get_four()
                                                        if n == 1:
                                                            print("You lose 1")
                                                            print(
                                                                "Your final n"
                                                                "umber is 18")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 2:
                                                            print("You gain 1")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                        elif n == 3:
                                                            print("You lose 3")
                                                            print(
                                                                "Your final n"
                                                                "umber is 16")
                                                            print(
                                                                "Almost but "
                                                                "YOU LOST")
                                                        elif n == 4:
                                                            print("You gain 3")
                                                            print(
                                                                "!!!YOU "
                                                                "WIN!!!")
                                                            winnersGame()
                                                    elif n == 3:
                                                        print("You gain 6")
                                                        print("!!!YOU WIN!!!")
                                                        winnersGame()
                                                elif n == 3:
                                                    print("You gain 6")
                                                    print("!!!YOU WIN!!!")
                                                    winnersGame()
