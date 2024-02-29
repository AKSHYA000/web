import random

def roll_dice():
    return random.randint(1, 6)

def main():
    total_score = 0
    while total_score < 100:
        input("Press Enter to roll the dice...")
        dice_roll = roll_dice()
        print("You rolled a", dice_roll)
        total_score += dice_roll
        print("Your total score is now", total_score)
    
    print("Congratulations! You've reached 100 points!")

if __name__ == "__main__":
    main()

