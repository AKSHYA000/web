import random

def roll_dice():
    return random.randint(1, 6)

def player_turn(player):
    input(f"{player}, press Enter to roll the dice...")
    dice_roll = roll_dice()
    print(f"{player} rolled a", dice_roll)
    return dice_roll

def computer_turn(player):
    input("Press Enter for Computer's turn...")
    dice_roll = roll_dice()
    print("Computer rolled a", dice_roll)
    return dice_roll

def main():
    opponent = input("Do you want to play against another player or against the computer? (player/computer): ")
    if opponent.lower() == "player":
        players = ['Player 1', 'Player 2']
    else:
        players = ['Player', 'Computer']
    scores = {player: 0 for player in players}
    while all(score < 100 for score in scores.values()):
        for player in players:
            if player == 'Computer' and opponent.lower() == 'computer':
                dice_roll = computer_turn(player)
                scores[player] += dice_roll
                print("Computer's total score is now", scores[player])
            else:
                dice_roll = player_turn(player)
                scores[player] += dice_roll
                print(f"{player}'s total score is now", scores[player])
            if scores[player] >= 100:
                print(f"Congratulations, {player}! You've reached 100 points!")
                break

if __name__ == "__main__":
    main()
