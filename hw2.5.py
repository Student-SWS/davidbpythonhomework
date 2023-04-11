current_value = 1                              # int, 1
current_sum = 0                                # int, 0
max = int(input('please enter an int: '))      # int, 5

while current_value <= max:                    # bool, true
    current_sum += current_value               # int, 1
    current_value += 1                         # int, 2

print(f"sum from 1 to {max} is {current_sum}")