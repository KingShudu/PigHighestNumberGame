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
    else:
        print("Error encountered")

max_score = 50
player_scores = [0 for _ in range(players)]
while max(player_scores) < max_score:

    for playerIndex in range(players):
        print("\nPlayer number",playerIndex +1 ,"'s turn has started")
        print("Your current score is ", player_scores[playerIndex],"\n")
        current_score=0
        while True:
            should_roll = input("Would you like to roll? (y)")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("Your turn is over you rolled a 1")
                current_score = 0
                break

            else:
                current_score += value
                print("You rolled a ", value)

            print("Your score is: ", current_score)
        player_scores[playerIndex] += current_score
        print("Your total score is: ", player_scores[playerIndex])
maximum_score = max(player_scores)
winningPlayerId = player_scores.index(maximum_score)
print("Player number ", winningPlayerId + 1," has won the game with a score of ", player_scores[winningPlayerId], "points")