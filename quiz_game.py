import random

actual_number = random.randrange(0, 15)
guesses = 0
while True:
    guesses += 1
    guess_game = input("Make a guess: ")
    if guess_game.isdigit():
        guess_game = int(guess_game)
    else:
        print('Please type a number next time.')
        continue
    if guess_game == actual_number:
        print('U got it!')
        break
    elif guess_game> actual_number:
        print('You have guessed a high number. Try again')
    else:
        print('You have guessed a low number. Try again')
print('You got it in', guesses, 'guesses')
