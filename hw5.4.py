file = open('states.csv')                                   # 'file' object
state_dictionary = {}                                       # dict, {}

for line in file:                                           # str, 'AL,4908621,52420,Alabama\n'
    state_info = line.split(',')                            # list, ['AL', '4908621', '52420', 'Alabama\n']
    state_dictionary[state_info[3][:-1]] = state_info[0]    # dict, {'Alabama': 'AL'}

user_input = input("""there are 50 pairs in the lookup dict
please enter a state name: """)                             # str, 'New York'

try:
    print(state_dictionary[user_input])
except KeyError:
    print(f'no state found with name "{user_input}"')
