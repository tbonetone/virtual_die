# A simple 6 sided die script

from random import randint


roll_count = 0

one_count = 0
two_count = 0
three_count = 0
four_count = 0
five_count = 0
six_count = 0

def intro():
    print("""
    Welcome to virtual die.
    Hit 'Q' to quit, 'N' to specify a number of rolls,
        or any other key for a normal roll.""")
    response = input("> ")
    if response.upper() == "Q":
        print("Bye!")
        exit()
    elif response.upper() == "N":
        print("How many rolls of the die do you want to be done?")
        how_many = input("> ")
        numb_roll(int(how_many))
    else:
        roll()

def roll():
    number = randint(1, 6)
    print("The die shows {}!".format(number))
    global roll_count
    roll_count += 1
    global one_count, two_count, three_count, four_count, five_count, six_count
    if number == 1:
        one_count += 1
    elif number == 2:
        two_count += 1
    elif number == 3:
        three_count += 1
    elif number == 4:
        four_count += 1
    elif number == 5:
        five_count += 1
    elif number == 6:
        six_count += 1
    print("Roll again?")
    response = input("> ").upper()
    if response == "Y":
        roll()
    else:
        end()

def numb_roll(x):
    for rolls in range(1, x+1):
        number = randint(1, 6)
        global roll_count
        roll_count += 1
        global one_count, two_count, three_count, four_count, five_count, six_count
        if number == 1:
            one_count += 1
        elif number == 2:
            two_count += 1
        elif number == 3:
            three_count += 1
        elif number == 4:
            four_count += 1
        elif number == 5:
            five_count += 1
        elif number == 6:
            six_count += 1
    end()

def end():
    if roll_count == 1:
        print("You rolled the die once.")
    elif roll_count > 1:
        print("You rolled the die {} times.".format(roll_count))
    print("You rolled {} ones, {} twos, {} threes, {} fours, {} fives, and {} sixes".format(one_count, two_count, three_count, four_count, five_count, six_count))
    print("Bye!")
    exit()

intro()
