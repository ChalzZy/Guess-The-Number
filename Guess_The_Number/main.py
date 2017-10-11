# Guess The Number Program - Charles Joseph Monaghan 11/10/2017

# Useful module for selecting random numbers
import random

# Return to this point when user guesses the correct number
restart = 1

while (restart < 10):
    # Variable that chooses a random number
    Random_Number = (random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    # Loop back to this point
    loop = 1

    # Checks if users number is correct or not
    while (loop < 10):

        personStr = input("Guess the random number from 1 - 10?: ")
        person = int(personStr)

        if person == Random_Number:
            print ("You are correct!, the number is", Random_Number)
            print ("Try to guess the new number!")
            restart = restart + 1
            break

        elif Random_Number < person:
            print ("Your number is smaller than your selected number, try again!")
            loop = loop + 1

        else:
            print ("Your number is larger than your selected number, try again!")
            loop = loop + 1
