import math
import os

#FUNCTIONS

class Player:
    def __init__(self, name, local):
        self.name = name
        self.local = local
        self.chameleon = False

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def setName(self, name):
        self.name = name
    
    def setAsChameleon(self):
        self.chameleon = True

def MainMenu():
    ClearTerminal()
    print(" MENU ".center(50, "-"))
    print("1. Enter New Player")
    print("2. Edit Player")
    print("3. Begin Round")
    print("")

    choice = int(input("Please Choose: "))

    if choice == 1:
        EnterNewPlayer()
    if choice == 2:
        EditPlayer()
    if choice == 3:
        BeginRound()

def EnterNewPlayer():
    ClearTerminal()
    print(" ENTER PLAYER ".center(50, "-"))
    print("")

    name = input("Please Enter Name: " )
    local = YOrNToBoolean(input("Are They Playing On This Computer? (Y or N) "))
    players.append(Player(name,local))
    players.sort()

    MainMenu()

def EditPlayer():
    ClearTerminal()
    print(" EDIT PLAYER ".center(50, "-"))
    print("")

    index = 1
    for player in players:
        print(str(index) + "." + " " + player.name)
        index = index + 1

    print("")
    choice = int(input("Please Choose: "))

    ClearTerminal()
    title = " " + "EDIT" + " " + players[choice - 1].name.upper() + " "
    print(title.center(50, "-"))
    print("")

    name = input("Please Enter Name: " )
    local = YOrNToBoolean(input("Are They Playing On This Computer? (Y or N) "))
    
    players[choice - 1].name = name
    players[choice - 1].local = local
    players.sort()

    MainMenu()

def BeginRound():
    ClearTerminal()
    print(" EDIT GAME PHRASE ".center(50, "-"))
    print("")

    global gamePhrase
    gamePhrase = input("Please Enter Game Phrase: " )
    AssignChameleon()
    AssignTermIndex()
    RoundMenu()

def RoundMenu():
    ClearTerminal()
    print(" ROUND MENU ".center(50, "-"))
    print("1. View Identity Cards")
    print("2. New Term")
    print("3. End Round")
    print("")

    choice = int(input("Please Choose: "))

    if choice == 1:
        ViewIdentityCards()
    if choice == 2:
        AssignTermIndex()
        RoundMenu()
    if choice == 3:
        EndRound()

def ViewIdentityCards():
    ClearTerminal()
    print(" VIEW IDENTITY CARDS ".center(50, "-"))

    index = 1
    for player in players:
        if player.local == True:
            print(str(index) + "." + " " + player.name)
            index = index + 1

    print("")
    choice = int(input("Please Choose: "))

    ClearTerminal()
    title = " " + players[choice - 1].name.upper() + "'S IDENTITY CARD "
    print(title.center(50, "-"))
    print("")

    if players[choice - 1].chameleon == True:
        print(" You are the chameleon.")
    else:
        print("You are not the chameleon. The term is #" + str(termIndex) + ".")
    
    print("")
    input("Press any key to continue ... ")

    RoundMenu()

def EndRound():
    for player in players:
        player.chameleon = False

    MainMenu()


def YOrNToBoolean(input):
    if input == "Y":
        return True
    if input == "N":
        return False

def GamePhraseToIndex():
    chars = list(gamePhrase.lower())
    number = 1

    for char in chars:
        number = number * ord(char)

    number = int(math.pow(number, 0.5))

    index = number % len(players)

    return(index)

def AssignTermIndex():
    global attemptIndex
    attemptIndex = attemptIndex + 1

    chars = list(gamePhrase.lower())
    number = 1

    for char in chars:
        number = number * ord(char)

    number = int(math.pow(number, (attemptIndex / 2.5)))

    index = number % termCount + 1

    global termIndex
    termIndex = index

def AssignChameleon():
    index = GamePhraseToIndex()

    players[index].setAsChameleon()

def ClearTerminal():
    os.system('cls' if os.name=='nt' else 'clear')

# VARIABLES
players = []
gamePhrase = ""
attemptIndex = 1
termCount = 16
termIndex = 0

MainMenu()