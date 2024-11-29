import random

user_wins = 0
computer_wins = 0

game_options = ['rock', 'paper', 'scissor']

while True:
    user_input = input('Please enter Rock/Paper/Scissor or type Q to quit:  '). lower()
    if user_input == 'q':
        break

    if user_input not in game_options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = game_options[random_number]
    print ('computer has picked', computer_pick + ".")

    if user_input == 'Rock' and computer_pick == 'Scissor':
        print('you win')
        user_wins += 1

    elif user_input == 'Scissor' and computer_pick == 'Paper':
        print('you win')
        user_wins += 1

    elif user_input == 'Paper' and computer_pick == 'Rock':
      print('you win')
      user_wins += 1

    else:
      print('You lost')
      computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("byebye!")





