import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val,max_val)

    return roll

while True:
    players = input("Enter total number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Invalid number of players, please select numbers in the range (2-4)")