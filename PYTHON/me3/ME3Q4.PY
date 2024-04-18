"""
Write a python program to implement Math Quiz: Present players with 
random math questions (addition, subtraction, multiplication, division) and 
keep track of their score.
"""
import random
operators_available = ('**','*','/','+','-')
game_difficulty = 3
userScore = 0

def generate_question():
    operators = random.sample(operators_available,random.randint(1,game_difficulty))
    answer = 0
    question = ''
    for i in range(len(operators)):
        question += f'{random.randint(1,50)}{operators[i]}'
    question += f'{random.randint(1,50)}'
    answer = eval(question)
    return (question,round(answer,2))
while True:
    data = generate_question()
    print(data[0])
    result = float(input('Answer = '))
    if result == data[1]:
        print('Congratulation Correct Answer')
        userScore += 1
    else:
        print('GameOver')
        print('Your Score =',userScore)
        break