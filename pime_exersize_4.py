#random number game 

import random

def play_game():
    secret_number = random.randint(1, 1000)
    num_guesses = 0
    while True:
        num_guesses += 1
        guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Congratulations. You guessed the number!")
            break
        if num_guesses > 10:
            print("You should be able to do better!")
            break
    if num_guesses <= 10:
        print("Either you know the secret or you got lucky!")
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == 'y':
        play_game()

play_game()