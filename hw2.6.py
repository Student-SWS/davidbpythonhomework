max_possible = 100                  # int, 100
min_possible = 0                    # int, 0
user_response = "nothing"           # str, "nothing"
higher_or_lower = "nothing"         # str, "nothing"

print("Think of a number between 100 and 0, and I will try to guess it.")
input("Hit [Enter] to start.")

while True:
    current_guess = round((max_possible + min_possible)/2)             # int, 50
    user_response = input(f"is it {current_guess} (yes/no/quit)?")     # str, "no"

    if user_response == "yes":                                         # bool, False
        print("I knew I could do it!")
        quit()

    elif user_response == "no":                                                     # bool, True
        higher_or_lower = input(f"is it higher or lower than {current_guess}?")     # str, "higher"
        if higher_or_lower == "higher":                                             # bool, True
            min_possible = current_guess                                            # int, 50
        elif higher_or_lower == "lower":                                            # bool, False
            max_possible = current_guess                                            # int, 50

        elif user_response == "quit":                                               # bool, False
            quit()