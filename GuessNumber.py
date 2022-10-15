# Guess Number

import random
number = random.randrange(1,20)
guess = int(input("Guess a number between 1 to 20: "))

while guess != number:
    if guess < number:
        guess = int(input(f"Try higher than {guess}: "))
    else:
        guess = int(input(f"Try lower than {guess}: "))
print(f"\nCongratulations!You guessed the correct number {guess}.\nGood Day!")