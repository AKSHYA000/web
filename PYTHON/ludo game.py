import random

def roll_dice():
    return random.randint(1, 6)

def main():
    players = ['Player 1', 'Player 2']
    scores = {player: 0 for player in players}
    while all(score < 100 for score in scores.values()):
        for player in players:
            input(f"{player}, press Enter to roll the dice...")
            dice_roll = roll_dice()
            print(f"{player} rolled a", dice_roll)
            scores[player] += dice_roll
            print(f"{player}'s total score is now", scores[player])
            if scores[player] >= 100:
                print(f"Congratulations, {player}! You've reached 100 points!")
                break

if __name__ == "__main__":
    main()