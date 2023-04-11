import random

number_to_guess = random.randint(1,100)                                  # int, 7
num_tries = 0                                                            # int, 0

print("I am thinking of a number from 1 to 100. Try to guess it and I'll give you hints about it.")

while True:                                                              # bool, True
    current_guess = input("Your guess?  (q to quit): ")                  # str, 7
    if current_guess == "q":                                             # bool, False
        quit()

    current_guess = int(current_guess)                                   # int, 32
    num_tries += 1                                                       # int, 1

    if number_to_guess < current_guess:                                  # bool, False
        print("your guess is HIGHER than the number I'm thinking of")
    elif number_to_guess > current_guess:                                # bool, False
        print("your guess is LOWER than the number I'm thinking of.")
    else:                                                                # bool, True
        print(f"you got it!  You guessed it in {num_tries} tries")
        quit()