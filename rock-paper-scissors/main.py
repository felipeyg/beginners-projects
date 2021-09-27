import random

def play():
    user = input("'r' for rock, 'p' for paper and 's' for scissors: ")
    list = ['rock', 'paper', 'scissors']
    computer = random.choice(list)
    print(f'Computer choose {computer} so\n')
    if computer == 'rock' and user == 'r':
        print("draw!")
    elif computer == 'rock' and user == 'p':
        print(f'You Won!')   
    elif computer == 'rock' and user == 's':
        print("You Lost!")
    elif computer == 'paper' and user == 'r':
        print("You Lost!")
    elif computer == 'paper' and user == 'p':
        print(f'Draw!')   
    elif computer == 'paper' and user == 's':
        print("You Won!")
    elif computer == 'scissors' and user == 'r':
        print("You Won!")
    elif computer == 'scissors' and user == 'p':
        print(f'You Lost!')   
    elif computer == 'scissors' and user == 's':
        print("Draw!")


play ()