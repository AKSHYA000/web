import random
choices = ('Scissor','Paper','Rock')
user_score = 0
bot_score = 0
while True:
    user_choice = int(input('choose one\n1.Scissor\n2.Paper\n3.Rock\n*.Exit\nchoice : '))
    if user_choice not in range(1,4):
        break
    bot_choice = random.choice(choices)
    print('Bot Choice :',bot_choice)
    user_choice = choices[user_choice-1]
    if user_choice == bot_choice:
        print('Draw')
    elif user_choice == choices[0]:
        if bot_choice == choices[1]:
            print('User Wins')
            user_score += 1
        else:
            print('Bot Wins')
            bot_score += 1
    elif user_choice == choices[1]:
        if bot_choice == choices[2]:
            print('User Wins')
            user_score += 1
        else:
            print('Bot Wins')
            bot_score += 1
    elif user_choice == choices[2]:
        if bot_choice == choices[0]:
            print('User Wins')
            user_score += 1
        else:
            print('Bot Wins')
            bot_score += 1
    print('\n\n\n\n')
print('\n\n\nUser Wins :',user_score,'\nBot Wins :',bot_score)