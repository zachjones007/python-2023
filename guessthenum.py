import random

def playGame(secretNumber, guess, numGuesses):

    while guess != secretNumber:
        guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
        numGuesses += 1
        if guess < secretNumber:
            print("Too low. Try again.")
        elif guess > secretNumber:
            print("Too high. Try again.")

        if numGuesses > 10:
            print("You should be able to do better!")
            break

    if numGuesses <= 10:
        print("Either you know the secret or you got lucky!")
    print("Congratulations. You guessed the number!")

playGame(random.randint(1, 1000), 0, 0)
playAgain = input("Do you want to play again (y/n)? ")

while playAgain == "y":
    playGame(random.randint(1, 1000), 0, 0)
    playAgain = input("Do you want to play again (y/n)? ")