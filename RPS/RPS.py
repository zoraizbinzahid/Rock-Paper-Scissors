import random

while True:
    my_answer = input('Choose: rock, paper, or scissors: ')
    my_answer = my_answer.lower()

  

    if my_answer != 'rock' and my_answer != 'paper' and my_answer != 'scissors':
        print('invalid')
        continue

    computer_answer = random.choice(['rock', 'paper', 'scissors'])
    print(f'Computer chose: {computer_answer}')

    if my_answer == computer_answer:
        print('its a tie!') 
    elif my_answer == 'rock' and computer_answer == 'scissors' or my_answer == 'paper' and computer_answer == 'rock' or my_answer == 'scissors' and computer_answer == 'paper':
        print('you Win!')
        break
    else:
        print('you lose, try again!')   