#Problem 5: Number Guessing Game
#• Create a number guessing game, where the computer selects a random number, and the player tries to guess it
#• You can use any user interface that you like, but the user must be able to continuously play the game
#• Make sure that you attempt to handle all/some error cases

import random

while(True):
    
    number = random.randint(1,100)

    guess = int(input("guess a number between 1 and 100! "))
    
    if guess == number:
        print('You guessed it!')
        
    else:
        print('Try again!')



