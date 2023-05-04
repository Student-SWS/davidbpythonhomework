file = open('FF_data.txt')                                                          # 'file' object
summer = 0.0                                                                        # float, 0.0
year_dict = {}                                                                      # dict, {}
num_printed = 0                                                                     # int, 0

try:
    num_results = int(input('please enter a number of results:  '))                 # int, 3
except ValueError:
    print('please restart the program and enter an integer')
    quit()

direction = input('please enter a directory (ascending or descending):  ')          # str, 'ascending'

if direction == 'ascending':                                                        # bool, True
    reverse_vari = False                                                            # bool, False
elif direction == 'descending':                                                     # bool, False
    reverse_vari = True                                                             # bool, False
else:
    print('please restart and enter either ascending or descending')
    quit()

for line in file:                                                                   # str, '19260701    0.09   -0.22   -0.30   0.009\n'
    current_year_info = line.split()                                                # list, ['19260701, '0.09', '-0.22', '-0.30', '0.009\n']
    if (current_year_info[0][:4]) not in year_dict:  # bool, True
        year_dict[current_year_info[0][:4]] = float(current_year_info[1])           # dict, {'1926': 0.09}
    else:
        year_dict[current_year_info[0][:4]] += float(current_year_info[1])          # KeyError

for year in sorted(year_dict, key = year_dict.get, reverse = reverse_vari):         # str, '1933'
    if num_printed < num_results:                                                   # bool, True
        print(f'{year}:  {round(float(year_dict[year]), 2)}')
        num_printed += 1                                                            # int, 1
    else:
        break