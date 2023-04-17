user_input = input('please enter a 4-digit year: ')         # str, 2012

if len(user_input) == 4 and user_input.isdigit():           # bool, True
    print(f'input validated:  {user_input}')

else:                                                       # bool, False
    print('sorry, must be 4 digits')
    exit()