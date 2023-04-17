user_year = '1928'                          # str, '1928'
mktrf_list = [0.43, 0.14, 0.71]             # list, [0.43, 0.14, 0.71]

max_value = max(mktrf_list)                 # float, 0.71
min_value = min(mktrf_list)                 # float, 0.14

avg = round(sum(mktrf_list)/len(mktrf_list), 2)                                 # float, 0.43
sorted_mktrf_list = sorted(mktrf_list)                                          # list, [0.14, 0.43, 0.71]
middle = round(len(mktrf_list)/2)                                               # int, 2

if len(mktrf_list) % 2 == 1:                                                    # bool, True
    median = sorted_mktrf_list[middle - 1]                                      # float, 0.43
else:                                                                           # bool, False
    median = 0.5*sorted_mktrf_list[middle] + 0.5*sorted_mktrf_list[middle-1]    # float, 0.57

print(f'{user_year} (Mkt-RF), {len(mktrf_list)} values, max {max_value}, min {min_value}, avg {avg}, median {median}')
