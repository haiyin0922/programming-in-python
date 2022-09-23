import random
seed_value = int(input())
random.seed(seed_value)
while True:
    player = input('rock, paper, scissors?\n')
    if player == 'quit':
        print('bye!')
        break
    elif player == 'rock':# ... YOUR CODE to handle other conditions
        computer = random.choice(['rock', 'paper', 'scissors'])
        if(computer == 'rock'):
            print("I'm rock, tied!")
        if(computer == 'paper'):
            print("I'm paper, you lose!")
        if(computer == 'scissors'):
            print("I'm scissors, you win!')
    elif player == 'paper':

    elif player == 'scissors':
