"""William Carter Dog Game, 11/11/22 V3.10.5"""
import random as r
import time
v = 1 # Sets up first turn move so player goes
loop = True
while loop:
    menu = input("\n Play game(1) \n Quit(2): \n")
    if menu == "1":                         # If player decides to play
        loop = False
        Startgame = True
    elif menu == "2":                       # If player chooses to quit
        loop = False
        print("Thank you for playing")
        time.sleep(4)
        quit()
    else:
        print("Invalid Answer, Please try again:")

while Startgame == True:
    try:
        deck = int(input("What size deck would you like to play with?"))            # Asks player how many cards they want to play with
        if deck < 4 or deck > 30 or deck % 2 != 0:                              
            print("Invalid deck size, it must be between 4 and 30 and not be an odd number \n")
        else:
            Startgame = False
            Cards_each = int(deck / 2)          # Finds out how many cards will be in each deck
    except:
        print("An error occurred, try again")

def setup(Cards_each, deck):
    text = open("dogs.txt", "r", encoding="utf-8-sig")
    dogs = []

    for i in range(30):
        lines = text.readline()
        name = lines
        exercise = r.randint(1, 5)
        intelligence = r.randint(1, 100)
        friendliness = r.randint(1, 10)
        drool = r.randint(1, 10)
        dog = {                                 # Reads dogs line by line and creates a dictionary with their name and randomly assigned stats
            "name": name,
            "exercise": exercise,
            "intelligence": intelligence,
            "friendliness": friendliness,
            "drool": drool
        }
        dogs.append(dog)                        # Puts Stats and name of dog into an array to be pulled out of for cards

    player_cards = []

    for i in range(Cards_each):             # Pulls dictionaries out of array randomly and puts it into one player's deck
        dog = r.choice(dogs)
        dogs.remove(dog)
        player_cards.append(dog)
    comp_cards = []

    for i in range(Cards_each):
        dog = r.choice(dogs)
        dogs.remove(dog)
        comp_cards.append(dog)
    return player_cards, comp_cards


def main_game(player_cards, comp_cards, victory):
    print("\nYou have", len(player_cards))
    print("\nComputer has", len(comp_cards))
    current_card = player_cards[0]                  # Pulls first card out of each player's deck and removes it from the deck for the time being
    current_comp_card = comp_cards[0]
    player_cards.pop(0)
    comp_cards.pop(0)
    if victory == 1:
        print("\nname:", current_card["name"] + "exercise:", current_card["exercise"], "\nintelligence",        # Shows dictionary of stats for player to decide
              current_card["intelligence"], "\nfriendliness:", current_card["friendliness"], "\ndrool:",
              current_card["drool"])
        choice = 0
        while choice < 1 or choice > 4:                 # Making sure inputs are allowed
            try:
                choice = int(input("\nWould you like to play exercise (1), Intelligence(2), Friendliness(3) or Drool(4)\n"))
            except:
                print("An error occurred, try again")
    elif victory == 0:
        print("\nname:", current_card["name"] + "exercise:", current_card["exercise"], "\nintelligence",
              current_card["intelligence"], "\nfriendliness:", current_card["friendliness"], "\ndrool:",
              current_card["drool"])
        time.sleep(2)
        choice = r.randint(1,4)                         # Letting computer randomly choose a stat if it won last round
        if choice == 1:
            print("Computer chose Exercise")
            time.sleep(2)

        if choice == 2:
            print("Computer chose Intelligence")
            time.sleep(2)

        if choice == 3:
            print("Computer chose Friendliness")
            time.sleep(2)

        if choice == 4:
            print("Computer chose Drool")
            time.sleep(2)


    if choice == 1:                                                 # Sets what stat is being compared to what choice the player/computer chose
        player_stat = current_card["exercise"]
        comp_stat = current_comp_card["exercise"]
    elif choice == 2:
        player_stat = current_card["intelligence"]
        comp_stat = current_comp_card["intelligence"]
    elif choice == 3:
        player_stat = current_card["friendliness"]
        comp_stat = current_comp_card["friendliness"]
    elif choice == 4:
        player_stat = current_card["drool"]
        comp_stat = current_comp_card["drool"]

    return player_stat, comp_stat, current_card, current_comp_card, comp_cards, player_cards, choice


def compare_cards(player_stat, comp_stat, current_card, current_comp_card, player_cards, comp_cards):   # Compares any stats given except drool

    if player_stat >= comp_stat:                    # Checks if stat is higher to computers
        print("You won")
        player_cards.append(current_comp_card)      # Gives both cards to players deck
        player_cards.append(current_card)
        victory = 1                                 # Tells program player won last round

    elif comp_stat > player_stat:                   # Checks if stat is lower than computers
        print("You lose")
        comp_cards.append(current_card)             # Gives both cards to computers deck
        comp_cards.append(current_comp_card)
        victory = 0                                 # Tells program computer won last round


    return player_cards, comp_cards, victory


def drool_compare(player_stat, comp_stat, current_card, current_comp_card, player_cards, comp_cards):   # Compares the drool stats as they are different to other 3

    if player_stat <= comp_stat:                # Checks if stat is lower than computers
        print("You won")
        player_cards.append(current_comp_card)  # Gives both cards to players deck
        player_cards.append(current_card)
        victory = 1                             # Tells program player won last round

    elif comp_stat < player_stat:                      # Checks if stat is higher than computers
        print("You lose")
        comp_cards.append(current_card)                # Gives both cards to computers deck
        comp_cards.append(current_comp_card)
        victory = 0                                    # Tells program computer won last round

    return player_cards, comp_cards, victory


sp_c, sc_c = setup(Cards_each, deck)

repeat = True
while repeat:
    p_s, c_s, current_c, c_current_c, c_c, p_c, chosen_stat = main_game(sp_c, sc_c, v)   # Starts game to get cards and ask for stats

    if chosen_stat == 4:         # Checking if stat is drool, which is handled differently
        sp_c, sc_c, v = drool_compare(p_s, c_s, current_c, c_current_c, p_c, c_c)
    else:
        sp_c, sc_c, v = compare_cards(p_s, c_s, current_c, c_current_c, p_c, c_c)

    if len(sp_c) == 0:                     # Checking if Player has won or lost yet
        print("Game over, you lost")
        repeat = False
    elif len(sc_c) == 0:
        print("Well done, you won")
        repeat = False

