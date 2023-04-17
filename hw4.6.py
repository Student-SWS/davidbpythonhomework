user_input = input('please enter a 4-digit year: ')         # str, 1926

if len(user_input) == 4 and user_input.isdigit():           # bool, True
    print(f'input validated:  {user_input}')

else:                                                       # bool, False
    print('sorry, must be 4 digits')
    exit()

mktrf_list = []                                             # list, []
file = open('FF_data.txt', 'r')                             # 'file' object

for line in file:                                           # str, '19260701    0.09   -0.22   -0.30   0.009'
    if line[:4] == user_input:                              # bool, False
        mktrf_list.append(float(line.split()[1]))           # list, [0.09]
    elif int(line[:4]) > int(user_input):                   # bool, False
        break

if mktrf_list == []:                                        # bool, False
    print(f'no values found for year {user_input}')
    exit()

max_value = max(mktrf_list)                                 # float, 1.48
min_value = min(mktrf_list)                                 # float, -1.69

avg = round(sum(mktrf_list)/len(mktrf_list), 2)             # float, 0.43
sorted_mktrf_list = sorted(mktrf_list)                      # list, [-1.69, -1.38, -1.38, -1.2, -1.08, -1.07, -1.04, -0.99, ...]
middle = round(len(mktrf_list)/2)                           # int, 2

if len(mktrf_list) % 2 == 1:                                                    # bool, True
    median = sorted_mktrf_list[middle - 1]                                      # float, 0.43
else:                                                                           # bool, False
   median = 0.5*sorted_mktrf_list[middle] + 0.5*sorted_mktrf_list[middle-1]     # float, 0.57

print(f'{user_input} (Mkt-RF), {len(mktrf_list)} values, max {max_value}, min {min_value}, avg {avg}, median {median}')

