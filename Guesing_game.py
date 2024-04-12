import random

def gues_the_number(x):
    random_number = random.randint(1, x)
    gues = 0
    while gues != random_number:
        gues = int(input(f"Enter the number between 1 and {x} :"))
        if gues > random_number:
            print(" Hint: Your gues is too high, Try again")

        elif gues < random_number:
            print("Hint: Your gues is too low, Try again")
    print(f"Congratultions, you've guessed correctly, you've won jackpot.")

gues_the_number(100)