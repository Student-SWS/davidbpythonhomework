step_value = int(input("please enter an integer: "))    # int, 4
current_value = 0                                       # int, 0
stop_value = 100                                        # int, 100

print(f"counting from 0 to 100 by {step_value}'s")

while current_value < stop_value:                       # bool, true
    print(current_value)
    current_value += step_value                         # int, 4