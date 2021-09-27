import random 

print("Welcome to GUESS THE NUMBER GAME! \nYour job is guess a number from 0 to 10000, good luck!")

def guess(x):
    secret_number = random.randint(0,x)
    guess = 0
    while guess != secret_number:
        guess = int(input(f"Guess a number from 1 and 10000: "))
        if guess > secret_number:
            print("\nYour guess is too high! Try Again\n")
        elif guess < secret_number:
            print("\nYour guess is too low! Try Again\n")
        else:
            print(f"\nCONGRATULATION, YOU'VE MADE IT\nYou guessed the number {secret_number} corretly!\n")

guess(10000)