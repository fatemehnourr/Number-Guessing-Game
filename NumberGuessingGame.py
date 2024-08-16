import random

#Get input
while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            raise ValueError
        break
    except (ValueError):
        print("Please enter a positive integer.")

#Generate random number within range
num = random.randint(1, level)

#Guessing loop
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            raise ValueError
    except (ValueError):
        print("Please enter a positive integer.")
    else:
        if num == guess:
                print("Just Right!")
                break
        elif num > guess:
            print("Too small!")
        else:   # if num < guess
            print("Too large!")




