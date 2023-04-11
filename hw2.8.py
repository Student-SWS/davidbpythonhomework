while True:
    player_location = "east"        # str, "east"
    chicken_location = "east"       # str, "east"
    fox_location = "east"           # str, "east"
    grain_location = "east"         # str, "east"

    print("**THE FOX, THE CHICKEN AND THE GRAIN**")
    print("")

    print(f"""You are on the {player_location} bank of a river.
You must transport a fox, a chicken
and a bag of grain to the west bank.
However, you can only carry one item
at a time.  Good luck!""")
    print("")

    while True:

        if fox_location == chicken_location != player_location:         # bool, False
            print("oops, the fox got the chicken!")
            print("")
            break
        elif chicken_location == grain_location != player_location:     # bool, False
            print("oops, the chicken got the grain!")
            print("")
            break

        print(f"you now are on the {player_location} bank")
        print(f"the chicken is now on the {chicken_location} bank")
        print(f"the fox is now on the {fox_location} bank")
        print(f"the grain is now on the {grain_location} bank")

        current_choice = input("What would you carry in the seat of the boat ([Enter] for nothing, q to quit)?  ")  # str, "chicken"

        print("")

        if current_choice == "q":                           # bool, False
            quit()

        elif current_choice == "fox":                       # bool, False
            if player_location == fox_location:             # bool, True
                if player_location == "east":               # bool, True
                    fox_location = "west"                   # str, "west"
                    player_location = "west"                # str, "west"
                else:                                       # bool, False
                    fox_location = "east"                   # str, "east"
                    player_location = "east"                # str, "east"
            else:                                           # bool, False
                print(f"I'm sorry {current_choice} is not in the same location as the player")
                print("")
                continue
            print(f"...carrying the {current_choice} to the {player_location} bank...")
            print("")

        elif current_choice == "chicken":                   # bool, True
            if player_location == chicken_location:         # bool, True
                if chicken_location == "east":              # bool, True
                    chicken_location = "west"               # str, "west"
                    player_location = "west"                # str, "west"
                else:                                       # bool, False
                    chicken_location = "east"               # str, "east"
                    player_location = "east"                # str, "east"
            else:                                           # bool, False
                print(f"I'm sorry {current_choice} is not in the same location as the player")
                print("")
                continue
            print(f"...carrying the {current_choice} to the {player_location} bank...")
            print("")

        elif current_choice == "grain":                     # bool, True
            if player_location == grain_location:           # bool, True
                if grain_location == "east":                # bool, True
                    grain_location = "west"                 # str, "west"
                    player_location = "west"                # str, "west"
                else:                                       # bool, False
                    grain_location = "east"                 # str, "east"
                    player_location = "east"                # str, "east"
            else:                                           # bool, False
                print(f"I'm sorry {current_choice} is not in the same location as the player")
                print("")
                continue
            print(f"...carrying the {current_choice} to the {player_location} bank...")
            print("")

        elif current_choice == "":                          # bool, False
            if player_location == "east":                   # bool, True
                player_location = "west"                    # str, "west"
            else:                                           # bool, False
                player_location = "east"                    # str, "east"

            print(f"...carrying NOTHING to the {player_location} bank...")
            print("")

        elif current_choice != "":                          # bool, False
            print(f"sorry, I don't recognize '{current_choice}'.  Try again.")
            continue