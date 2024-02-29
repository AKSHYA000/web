import random
options = ('Goat','Goat','Car')
doors = random.sample(options,3)
user_choice = int(input('choose one door\n1.door1\n2.door2\n3.door3\nchoice : '))
if user_choice not in range(1,4):
    print('error')
else:
    user_choice -= 1
    showing_door = 0
    while True:
        showing_door = random.randint(0,2)
        if showing_door != user_choice and doors[showing_door] == 'Goat':
            break
    print('Doors:-')
    print('1.','?' if showing_door!=0 else 'Goat','\n2.','?' if showing_door!=1 else 'Goat','\n3.','?' if showing_door!=2 else 'Goat')
    print('Your Choice =',user_choice+1,'\nDo You want to stick or switch?\n1.Stick\n2.Switch')
    op = int(input('Choice = '))
    if op not in range(1,3):
        print('error')
    else:
        if op == 1:
            print('You Got',doors[user_choice])
            print('1.',doors[0],'\n2.',doors[1],'\n3.',doors[2])
        else:
            new_user_choice = 0
            while True:
                if new_user_choice!=showing_door and new_user_choice!=user_choice:
                    break
                else:
                    new_user_choice += 1
            print('You Got ',doors[new_user_choice])
            print('1.',doors[0],'\n2.',doors[1],'\n3.',doors[2])