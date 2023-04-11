print ('* Prime Numbers *')
user_input = int(input('Please enter a max integer: '))             # int, 12
num_in_list = 2                                                     # int, 2
current_num_prime = True                                            # bool, True

print('')

while num_in_list <= user_input:                                    # bool, True
    for factor in range(2, round(num_in_list/2)+1):                 # int, 2
        if num_in_list % factor == 0:                               # bool, True
            current_num_prime = False                               # bool, False
    if current_num_prime:                                           # bool, True
        print(num_in_list)

    num_in_list += 1                                                # int, 3
    current_num_prime = True                                        # bool, True